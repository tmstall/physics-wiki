<#
.SYNOPSIS
  Paper-queue worker. Run by the scheduled task 'PhysicsWiki-PaperQueue' (at logon, on wake from
  sleep, every 30 min) or by hand. Holds queue\worker.lock while running, so only one worker runs.

  Each run:
    1. retries a failed git push and any Drive copies that failed earlier;
    2. imports job files dropped into G:\My Drive\Technical Papers\Queue\ (moved to Queue\_picked\);
    3. resets orphaned *.running jobs to pending;
    4. processes pending jobs one at a time (oldest first). A usage limit stops the run and
       parks the job as *.limit until the reset time; later runs retry it.
#>
param([int]$MaxJobs = 10, [switch]$NoDriveInbox)
$ErrorActionPreference = 'Continue'
. (Join-Path $PSScriptRoot 'pipeline-lib.ps1')
Initialize-PipelineEnv
New-Item -ItemType Directory -Path $QueueDir -Force | Out-Null
$wlog = Join-Path $QueueDir 'worker.log'
$lockPath = Join-Path $QueueDir 'worker.lock'

# --- single-instance lock: an exclusively-held handle (released by the OS if we crash) ---
try { $lock = [IO.File]::Open($lockPath, 'OpenOrCreate', 'ReadWrite', 'None') }
catch { Write-Log 'Another worker holds the lock; exiting.' $wlog; exit 0 }
try {
    $lock.SetLength(0); $b = [Text.Encoding]::ASCII.GetBytes("pid $PID started $(Get-Date -Format s)"); $lock.Write($b, 0, $b.Length); $lock.Flush()

    function Set-JobStatus([string]$Path, [string]$Status, $Job) {
        $new = ($Path -replace '\.(pending|running|done|failed|limit)\.json$', ".$Status.json")
        Write-Utf8File $Path ($Job | ConvertTo-Json -Depth 8)
        if ($new -ne $Path) { Move-Item -LiteralPath $Path -Destination $new -Force }
        return $new
    }
    function Read-Job([string]$Path) { return ([IO.File]::ReadAllText($Path) | ConvertFrom-Json) }
    function Set-Field($Obj, [string]$Name, $Value) { $Obj | Add-Member -NotePropertyName $Name -NotePropertyValue $Value -Force }

    # 1a. retry a pending git push
    $sb = (Invoke-Git $RepoRoot @('status', '-sb')).out -split "`n" | Select-Object -First 1
    if ($sb -match '\[ahead \d+') {
        $p = Invoke-Git $RepoRoot @('push', 'origin', 'HEAD')
        Write-Log "Retry git push ($sb): exit $($p.code)" $wlog
    }
    # 1b. retry Drive copies that failed while G: was unavailable
    $retry = Join-Path $QueueDir 'drive-retry.txt'
    if ((Test-Path $retry) -and (Wait-DriveMount $DriveAnalyses 60)) {
        $left = @()
        foreach ($l in (Get-Content $retry -Encoding UTF8)) {
            if (-not $l.Trim()) { continue }
            $src, $dst = $l -split "`t"
            try { $n = Copy-Verified $src (Join-Path $dst (Split-Path $src -Leaf)); Write-Log "Drive retry ok: $src ($n bytes)" $wlog }
            catch { $left += $l; Write-Log "Drive retry failed: $l - $($_.Exception.Message)" $wlog }
        }
        if ($left.Count) { Set-Content $retry $left -Encoding UTF8 } else { Remove-Item $retry -Force }
    }

    # 2. Drive inbox
    if (-not $NoDriveInbox -and (Test-Path $DriveQueue)) {
        $picked = Join-Path $DriveQueue '_picked'; $rejected = Join-Path $DriveQueue '_rejected'
        New-Item -ItemType Directory -Path $picked, $rejected -Force | Out-Null
        $cut = (Get-Date).AddSeconds(-15)
        foreach ($f in (Get-ChildItem $DriveQueue -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -in '.txt', '.json' -and $_.Name -notmatch '^[~.]' -and $_.LastWriteTime -lt $cut })) {
            $stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
            try {
                $s = Read-JobSpecFile $f.FullName
                $jp = New-QueueJob -Paper $s.paper -Title $s.title -Type $(if ($s.type) { $s.type } else { 'analyze' }) -Question $s.question -Append:([bool]$s.append) -DryRun:([bool]$s.dryRun) -Force:([bool]$s.force) -Source ('drive:' + $f.Name)
                Move-Item -LiteralPath $f.FullName -Destination (Join-Path $picked ($stamp + '_' + $f.Name)) -Force
                Write-Log "Imported Drive job $($f.Name) -> $jp" $wlog
            } catch {
                Move-Item -LiteralPath $f.FullName -Destination (Join-Path $rejected ($stamp + '_' + $f.Name)) -Force
                Write-Log "Rejected Drive job $($f.Name): $($_.Exception.Message)" $wlog
            }
        }
    }

    # 3. orphaned running jobs (we hold the lock, so nothing else is running them)
    foreach ($f in (Get-ChildItem $QueueDir -Filter '*.running.json' -File)) {
        $j = Read-Job $f.FullName
        if ([int]$j.attempts -ge 3) { Set-Field $j 'finished' (Get-Date).ToString('s'); Set-JobStatus $f.FullName 'failed' $j | Out-Null; Write-Log "Orphaned job failed after 3 attempts: $($f.Name)" $wlog }
        else { Set-JobStatus $f.FullName 'pending' $j | Out-Null; Write-Log "Reset orphaned job to pending: $($f.Name)" $wlog }
    }

    # 4. process
    $done = 0
    while ($done -lt $MaxJobs) {
        $now = Get-Date
        $limits = @(Get-ChildItem $QueueDir -Filter '*.limit.json' -File | Sort-Object Name)
        $hold = $null
        foreach ($f in $limits) { $j = Read-Job $f.FullName; if ($j.retryAfter -and ([datetime]$j.retryAfter) -gt $now) { $hold = $j.retryAfter } }
        if ($hold) { Write-Log "Usage limit active until $hold; not starting jobs." $wlog; break }
        $next = @($limits) + @(Get-ChildItem $QueueDir -Filter '*.pending.json' -File | Sort-Object Name) | Select-Object -First 1
        if (-not $next) { break }

        $job = Read-Job $next.FullName
        Set-Field $job 'attempts' ([int]$job.attempts + 1); Set-Field $job 'started' (Get-Date).ToString('s')
        $runPath = Set-JobStatus $next.FullName 'running' $job
        Write-Log "Job start: $(Split-Path $runPath -Leaf) ($($job.type) $($job.paper)$(if ($job.dryRun) { ', dry run' }))" $wlog
        $resFile = [IO.Path]::ChangeExtension($runPath, '.result.tmp')
        if (Test-Path $resFile) { Remove-Item $resFile -Force }
        $ps = Join-Path $PSHOME 'powershell.exe'
        $clean = { param($s) if ($s) { ([string]$s).Replace('"', "'") } else { $null } }
        if ($job.type -eq 'deepdive') {
            $a = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', (Join-Path $AutoDir 'deep-dive.ps1'), '-Paper', (& $clean $job.paper), '-Question', (& $clean $job.question), '-ResultFile', $resFile)
            if ($job.append) { $a += '-Append' }
            if ($job.dryRun) { $a += '-DryRun' }
        } else {
            $a = @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', (Join-Path $AutoDir 'analyze-paper.ps1'), '-Paper', (& $clean $job.paper), '-ResultFile', $resFile, '-JobId', (Split-Path $runPath -Leaf))
            if ($job.title) { $a += @('-Title', (& $clean $job.title)) }
            if ($job.dryRun) { $a += '-DryRun' }
            if ($job.force) { $a += '-Force' }
        }
        & $ps @a 2>&1 | ForEach-Object { "$_" } | Out-File (Join-Path $QueueDir 'last-job-console.log') -Encoding utf8
        $code = $LASTEXITCODE
        $res = $null; if (Test-Path $resFile) { try { $res = [IO.File]::ReadAllText($resFile) | ConvertFrom-Json } catch { }; Remove-Item $resFile -Force -ErrorAction SilentlyContinue }
        Set-Field $job 'result' $res; Set-Field $job 'exitCode' $code
        switch ($code) {
            0 { $st = 'done' }
            2 { $st = 'done' }    # duplicate: nothing to do (result.status = duplicate)
            3 { $st = 'limit' }
            default { $st = 'failed' }
        }
        if ($st -eq 'limit') {
            $ra = (Get-Date).AddHours(1)
            if ($res -and $res.resetsAt) { try { $ra = [DateTimeOffset]::FromUnixTimeSeconds([int64]$res.resetsAt).LocalDateTime.AddMinutes(2) } catch { } }
            Set-Field $job 'retryAfter' $ra.ToString('s')
        } else { Set-Field $job 'finished' (Get-Date).ToString('s') }
        $final = Set-JobStatus $runPath $st $job
        Write-Log "Job end: $(Split-Path $final -Leaf) exit $code status $st$(if ($res) { ' (' + $res.status + ')' })" $wlog
        $done++
        if ($st -eq 'limit') { Write-Log 'Stopping the queue: usage limit (extra usage is disabled).' $wlog; break }
    }
}
finally { $lock.Close() }
