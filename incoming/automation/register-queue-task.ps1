<#
.SYNOPSIS
  Registers (or re-registers) the user-level scheduled task 'PhysicsWiki-PaperQueue' that runs the
  queue worker at logon, on wake from sleep (System log, Power-Troubleshooter event 1) and every
  30 minutes. Runs only while the user is logged on (no password stored, no admin needed).
  .\register-queue-task.ps1            # register / update
  .\register-queue-task.ps1 -Remove    # unregister
#>
param([switch]$Remove)
$ErrorActionPreference = 'Stop'
$name = 'PhysicsWiki-PaperQueue'
if ($Remove) { schtasks.exe /Delete /TN $name /F; exit $LASTEXITCODE }
$user = "$env:USERDOMAIN\$env:USERNAME"
$vbs = Join-Path $PSScriptRoot 'run-hidden.vbs'
$start = (Get-Date).AddMinutes(5).ToString('yyyy-MM-ddTHH:mm:00')
$sub = "&lt;QueryList&gt;&lt;Query Id='0' Path='System'&gt;&lt;Select Path='System'&gt;*[System[Provider[@Name='Microsoft-Windows-Power-Troubleshooter'] and EventID=1]]&lt;/Select&gt;&lt;/Query&gt;&lt;/QueryList&gt;"
$xml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Author>$user</Author>
    <Description>Physics-Wiki paper queue worker (incoming\automation\queue-worker.ps1): processes queued paper analyses one at a time.</Description>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger><Enabled>true</Enabled><UserId>$user</UserId><Delay>PT2M</Delay></LogonTrigger>
    <EventTrigger><Enabled>true</Enabled><Subscription>$sub</Subscription><Delay>PT3M</Delay></EventTrigger>
    <TimeTrigger><Enabled>true</Enabled><StartBoundary>$start</StartBoundary><Repetition><Interval>PT30M</Interval><StopAtDurationEnd>false</StopAtDurationEnd></Repetition></TimeTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author"><UserId>$user</UserId><LogonType>InteractiveToken</LogonType><RunLevel>LeastPrivilege</RunLevel></Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>true</RunOnlyIfNetworkAvailable>
    <IdleSettings><StopOnIdleEnd>false</StopOnIdleEnd><RestartOnIdle>false</RestartOnIdle></IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT6H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec><Command>wscript.exe</Command><Arguments>"$vbs"</Arguments><WorkingDirectory>$PSScriptRoot</WorkingDirectory></Exec>
  </Actions>
</Task>
"@
$tmp = Join-Path $env:TEMP 'PhysicsWiki-PaperQueue.xml'
[IO.File]::WriteAllText($tmp, $xml, [Text.Encoding]::Unicode)
schtasks.exe /Create /TN $name /XML $tmp /F
$code = $LASTEXITCODE
Remove-Item $tmp -Force
exit $code
