---
source: claude_export
conversation_uuid: 4bccfd68-6176-428b-8ff5-1d8b215ddbc2
title: "Patent analysis"
created_at: 2026-07-08T16:24:37.745757Z
updated_at: 2026-07-08T16:28:55.397243Z
tier: A
score: 246
n_messages: 2
---

# Patent analysis

## Human

Analyze this patent

## Assistant

Analyzing | Framework v3.7.1 | patent, not a peer-reviewed paper — I pulled and analyzed the primary filing directly rather than working from the uploaded essay

**Access Status**
- **Primary document** (US 2024/0378175 A1, "Multi-Chip Systolic Arrays"): retrieved in full from Google Patents — complete specification, all 42 claims, figure list, citation list, and legal-event history.
- **Uploaded document**: a secondary journalistic analysis (SETI Park's thread). I treated it as a pointer and commentary, then cross-checked its factual claims against the primary filing. It holds up well; corrections are minor and flagged in §6.
- **Supplementary**: examiner citation list (8 references) and USPTO legal events retrieved. The TechCrunch valuation figures, the "LVI" power pillar, and the companion granted patents (US 12,361,091 etc.) come from the essay/press and are *not* independently re-verified here.
- **Analysis basis**: full primary patent text; essay as secondary context.

Two framing notes before the analysis, per the not-a-paper check in your framework. First, this isn't a scientific paper — it's a *patent application*, a legal-technical instrument. So two of your honesty checkpoints get remapped: "Replication & Convergence" becomes "has the office granted this / does silicon exist," and "Prior Belief Check" becomes "is this architecturally surprising vs. incremental." Second, what you uploaded is an essay *about* the patent, not the patent — so I went to the source. Everything below is grounded in the filing itself.

---

## 1. Punchy Title & One-Sentence Hook

**"The Array That Pretends To Be One Chip, and the Wire Where Everyone Else Puts a Switch."**

Etched's founding filing asks to build one enormous AI matrix engine out of many identical small chips wired edge-to-edge — and, in its sharpest claim, to feed that engine by *hardwiring* memory straight into the compute columns, deleting the routing switch the whole industry treats as mandatory.

---

## 2. Big-Picture Context

**Paper Type & Stakes.** This is a foundational architecture patent — a broad "here is our machine" filing (42 claims, four independent) staking out territory for a fixed-function transformer accelerator. What's at stake isn't a scientific truth but *ownership*: whether Etched holds an exclusive right to the memory-and-array design it now markets, or merely a dated, signed description of it. As of the record, the answer is "neither yet" — the application sits under a final rejection.

The problem this addresses is concrete and mid-2023-current: single-die systolic arrays hit a ceiling. The filing states it plainly — most chips cap out around a 128×128 floating-point array (~16K multiply-accumulate units), and it's "unreasonable to expect a single chip to interface with 100s of GB of memory" for large-model weights. A systolic array's efficiency scales beautifully with size (an N×N array does on the order of 2N² operations per clock while ingesting only ~2N inputs per clock — throughput grows as area, bandwidth demand only as edge length), so being stuck at 128×128 leaves enormous efficiency on the table.

The landscape before this: everyone knew tiling and chiplets were the escape hatch. Google's TPU ran matrix units at 128×128 for generations; Cerebras went wafer-scale; the accelerator literature was thick with multi-node and tiled designs. Etched's move is to compose small *identical* arrays into one array that the host, over PCIe, cannot distinguish from a single monolithic device — and to specialize the whole thing for one workload family (transformers) so hard that it "does not take instructions at runtime, and only executes instructions in a preset loop."

That fixed-function conviction is the strategic center of gravity. This is the paper trail behind Etched's public thesis (the Sohu chip): bet the entire architecture on transformers staying dominant, and trade all generality for density and efficiency.

**Prior Belief Check.** To an accelerator architect in 2023, almost nothing here is *surprising*. Multi-chip systolic composition, weight-stationary dataflow, HBM-at-the-top weight streaming, an attention sidecar — these are competent, aggressive engineering choices, not field-overturning insights. The one genuinely distinctive move is the no-switch memory hardwiring (claim 39), and even that reads as a clever exploitation of weight-stationarity rather than a new principle. The correct calibration is: *incremental-to-clever architecture, strategically coherent, not a conceptual breakthrough.* The essay's own verdict — "the founders wrote it down early; the office decides whether early also meant original" — is the right frame.

**Replication & Convergence Note (adapted).** This is a single-applicant filing with no independent validation of either kind that matters. Legally: the USPTO has *not* granted it — a non-final action, a response, a second non-final action, another response, then a **final rejection mailed 23 October 2025** against **eight prior-art references** (Intel ×2, IBM, Rambus, Salesforce, ETRI, Alibaba, TSMC). Physically: nothing in the patent record shows working silicon embodying these claims; the "shipping racks" are the company's own PR, invisible to the docket. "Independent confirmation" here would mean *claims surviving examination substantially intact* and/or *third-party teardown of real hardware practicing them* — neither exists today.

---

## 3. Necessary Background Crash-Course

**Systolic array.** A grid of tiny multiply-accumulate units that pass data to their right and lower neighbors every clock tick. Weights flow in from the top, the input tensor flows in from the left, each cell multiplies-and-adds and hands the operands along, and matrix products fall out with no register spilling to memory.

*Analogy:* a bucket brigade in two dimensions — water (data) moves cell-to-cell on every beat, and each person adds their bit as it passes, so the line stays full and nobody idles.
*Breaks when:* you imagine the brigade can reroute freely. A systolic array is rigid — data only moves in fixed directions on a fixed schedule. That rigidity is the whole point (it's why it's efficient) and also why anything needing random access (like attention's history) has to leave the array.

**Weight-stationary.** The model weights are loaded and held in place; the data streams past them. Because a transformer's weights are constant at inference, the same weights parked in a column get reused for every token and every row below.

*Analogy:* a stamping press. You mount the die (weights) once, then run sheet after sheet of metal (tokens) through it. Re-cutting the die per sheet would be absurd; you cut once, stamp forever.
*Breaks when:* the weights change — training, fine-tuning, or a model swap. Then "stationary" becomes a liability, and this design leans hard on the assumption that they never change at runtime.

**Chip-to-chip composition (the multi-chip trick).** Wire the edges of small local arrays together so results flow across die boundaries as if the seam weren't there. The filing names UCIe (Universal Chiplet Interconnect Express, ~32 GT/s, 16–64 lanes) as one option, over an interposer or as a vertical stack via microbumps.

*Analogy:* Intel-era territory for you — this is NUMA sockets stitched into one coherence domain, except here the "coherence" illusion is dead simple because the dataflow is one-directional and pre-scheduled. The host sees one array the way an OS sees one flat address space over a multi-socket board.
*Breaks when:* you push the NUMA analogy toward cache coherence or arbitrary remote access. There's none of that — the seams only carry the fixed systolic dataflow (right, down, and a bursty right-to-left feedback path), not general memory traffic.

**HBM channels + the switch.** High-Bandwidth Memory delivers capacity through independent channels that can't talk to each other. To let any compute unit reach any address, designers insert a crossbar switch. That switch is the thing claim 39 deletes.

*Analogy:* a mail sorting hub (crossbar) that lets any letter reach any P.O. box. Etched's move: if every box always gets mail from exactly one sender, skip the hub — run a dedicated wire from each sender to its box.
*Breaks when:* a sender ever needs to reach a different box. Then there's no hub to route through, and you're stuck. The design accepts this because weights are constant and always land in the same columns.

**Central analogy for this patent: a stamping press wired straight to its own reel of steel — no sorting hub.**

---

## 4. Core Technical Explanation

The filing builds outward in six moves.

**(1) One logical array from many identical dies (FIG. 1–2, claims 1, 26).** Each IC holds a local array (the spec allows anywhere from ~100×100 up to 10,000×10,000 DPUs). Horizontal connections between dies are *bidirectional* — mostly a fat left-to-right pipe (hundreds of GB/s) with a thin, bursty right-to-left return path (tens of GB/s) used to feed rightmost results back to the leftmost inputs. Vertical connections are *unidirectional*, top-to-bottom only. Four 100×100 dies in a row make a 100×400 array; stacked as a column, a 400×100. "In one embodiment, the ICs are all identical" — one mask set, manufactured many times.

**(2) Weights at the top, reused all the way down (FIG. 3, claim 15).** Memory chips (HBMs) sit only on the top row. Weights stream down through the vertical connections and get *reused across every row* — so adding a fourth or fifth row of compute dies adds FLOPs without adding a single memory chip. That's the scaling economics: compute scales on the vertical axis, memory cost doesn't follow. Ganging multiple HBMs per top die pushes >1 TB/s into each top IC.

**(3) The no-switch memory hardwiring (FIG. 5, claims 7, 19, 32, 39).** For constant weights, each HBM channel is hardwired to one specific column (which can run through *all* the dies in that column, top to bottom). Column A can read channel A and nothing else. The payoff, stated plainly: no switching element to build, which "can save space and power." Claim 39 is the crisp legal ask — an IC with a systolic array plus a memory device whose channels are "hardwired to respective one or more columns... without any switching element." Critically, **claim 39 is independent and does not require the multi-chip package at all.** The memory idea is claimed as its own invention.

**(4) The attention sidecar (FIG. 6, claims 11–13).** Most transformer work treats tokens in isolation — perfect for the array. Self-attention is the exception: it "use[s] data computed from previous tokens" (your KV-cache). So each die gets *auxiliary circuitry* beside its array tile, with its own private local memory, handling attention. Claim 13 states a hard negative rule: "the local systolic arrays do not communicate with the local memory chips." Math-that-forgets and math-that-remembers are physically walled apart.

**(5) Fixed-function identity ([0027]).** "The systolic array does not take instructions at runtime, and only executes instructions in a preset loop." This is the ASIC bet in one sentence — no instruction fetch, no branch prediction, one job forever. Note: this lives in the *description*, not in any claim.

**(6) Keeping it busy (FIG. 7).** Overlap operations — feed the next batch's inputs before the previous computation drains. Elementwise post-processing (GeLU, residual, scale/bias) happens on the fly. The one unavoidable stall is **layer normalization**, which needs the full row's mean and variance before it can proceed, costing roughly one row-length of clocks. Even with that, the spec claims **≥98% utilization.** Also description-only, not claimed.

### Assumption Audit

**Watch:** A reader assumes the "no-switch memory" is the payoff of the giant-array invention. **The patent actually** decouples them — claim 39 needs only *one* IC and *one* memory device. The two halves (multi-chip composition, no-switch memory) are claimed separately and can be granted, rejected, or owned independently. That separation is the essay's sharpest correct observation.

**Watch:** A reader assumes hardwiring channels to columns is a *bandwidth/speed* optimization. **The patent actually** motivates it by *area and power* ("save space and power"), not throughput — and it *costs* capability: a column can read only its own channel, so you trade all random access for a wire. It's constraint-exploitation, not acceleration.

**Watch:** A reader assumes the most impressive numbers — 98% utilization, the fixed-function loop, the pipelining schedule — are the protected invention. **The patent actually** confines all of those to the description and figures (FIG. 7, [0027]); *no claim covers them.* They're enablement narrative, showing the machine works, not intellectual property. The IP is the structural stuff: arrays wired together, memory hardwired to columns, the attention sidecar.

---

## 5. What's Genuinely New or Clever

Two things stand out, and it's worth being precise about *new-to-whom*.

**The no-switch hardwiring (claim 39)** is the cleverest specific move — and the most differentiated from the crowd. It's a genuine insight that *weight-stationarity dissolves the need for a memory crossbar*: if the mapping from channel to consumer never changes, the switch is pure overhead. New to the field? Arguably, as a claimed limitation. Clever regardless.

**The clean split of attention into a memory-owning sidecar walled off from the array (claim 13's negative limitation)** is the second. It's an honest architectural admission — "our beautiful dataflow engine can't do attention, so we bolt on separate hardware that can" — encoded as a specific, non-obvious floorplan rule. That negative limitation ("arrays do *not* communicate with the local memory chips") is the kind of concrete constraint that survives examination better than broad structural claims.

What is *not* new: multi-chip/tiled/wafer-scale systolic composition, weight-stationary dataflow, and HBM-at-the-top streaming were all well-established by 2023. Claim 1 reads on more or less any multi-chip systolic package — which is exactly why it's the first casualty.

---

## 6. Limitations & Open Questions

**Claim 1 (and its siblings 15, 26) is almost certainly too broad to grant as written.** *(A) Consensus* — the examiner has rejected the application over eight references spanning exactly this space (Intel, IBM, Rambus, ETRI's bidirectional PE array, Alibaba's floorplan matrix extension, TSMC's reconfigurable PEs); broad structural claims like this are the standard first casualty of examination. *(application docket + examiner citations + broader literature)*

**Even claim 39's no-switch limitation may be judged obvious for weight-stationary designs.** *(B) Contested* — reasonable practitioners could argue either way: hardwiring constant data paths is an intuitive optimization once you commit to weight-stationarity, yet the specific "no switching element" limitation is crisp and may hold. *(analyst inference + broader literature)*

**The record cannot show whether shipping silicon embodies any of this.** *(A) Consensus* — patents never prove reduction to practice; whether Etched's racks actually practice claim 39 is invisible from the docket, by the nature of the instrument. *(analyst inference)*

**The attention-sidecar's hard memory wall may not reflect what gets built.** *(C) Speculative* — the spec itself hedges ("in other examples, the local systolic arrays may also have access to the memory chips... as scratchpad"), and real KV-handling evolves fast; the clean wall may be a drafting convenience more than a shipped constraint. *(paper [0051] + analyst inference)*

**Thin family: US-only, no PCT, no continuation.** *(B) Contested significance* — the granted trio in Etched's stack reportedly got international and continuation treatment; this one didn't, which *could* signal lower strategic priority or simply timing. The record doesn't say, and a continuation can still be filed while the parent is alive. *(analyst inference; the "granted trio" grant numbers come from the essay, unverified here)*

**One correction to the essay's docket reading:** the essay states a "request for continued examination docketed 24 April 2026." The legal-event history I can see ends at the **23–24 October 2025 final rejection** and does not show a 2026 RCE. The essay may be reading a fresher USPTO docket than Google Patents mirrors; I can confirm *post-final-rejection, still pending*, but not the specific April 2026 RCE date. Treat that one detail as unverified.

**12–24 month watch items:** whether an RCE/appeal narrows claim 39 to something ornamental or preserves the no-switch limitation; whether continuations appear to rebuild the family; and whether any third-party teardown ever confirms the architecture in silicon.

---

## 7. Detailed Summary & Explanation

*Structural adaptation note (per framework): I materially adapted this analysis because the subject is a patent, not an empirical paper, and because the actual upload was a secondary essay — I retrieved and analyzed the primary filing instead. The "Replication" and "Prior Belief" checkpoints were remapped to patent-appropriate questions (grant status, silicon existence, architectural novelty). No honesty checkpoint was skipped.*

The filing describes a machine that turns many small, identical AI chips into one giant matrix-multiply engine. Each chip carries a modest systolic array; wiring their edges together — fat pipes rightward and downward, a thin feedback path leftward — makes them behave, from the host's point of view over PCIe, like a single enormous array. The motivation is a real 2023 ceiling: individual chips top out near a 128×128 array and can't reasonably hold hundreds of gigabytes of model weights, so you compose instead of enlarge.

The design is relentlessly weight-stationary. Weights load once at the top row of chips and stream downward, reused across every row — meaning you can add compute (more rows) without adding memory. Its sharpest idea follows from that: since the weights feeding each column never change, you can run a dedicated wire from each memory channel straight into its column and throw away the routing switch the industry normally requires, saving area and power at the cost of any flexibility to read memory randomly. That "no switch" idea is claimed on its own (claim 39), independent of the multi-chip machine — which is why the memory story can be owned separately from the array story.

The architecture also honestly carves out what it *can't* do well. A systolic array is great at the token-by-token matrix math of a transformer but bad at self-attention, which needs the history of previous tokens. So each chip gets a separate "sidecar" processor with its own private memory for attention, deliberately walled off from the main array. And the whole device is fixed-function by design — no runtime instructions, just a preset loop — which is the architectural embodiment of Etched's transformer-only bet.

The interpretive choice worth flagging: the *impressive engineering* (98% utilization, the pipelining schedule, the fixed-function loop) is narrative, not claimed IP, while the *owned* material is the plumbing (arrays wired together, memory hardwired to columns, the attention sidecar). Reading this as a technical paper would celebrate the former; reading it as a patent means watching the latter, because that's what converts — or doesn't — into an asset. Right now it's converted into nothing: a final rejection stands over a crowded field, and the collateral value the company has twice pledged rests on claims the office hasn't blessed.

*Where I'm least confident in this analysis:* the live prosecution status — specifically whether the essay's April 2026 RCE detail is current — since the docket I could retrieve ends at the October 2025 final rejection, and patent examination status shifts month to month. I'm also relying on the essay (not primary verification) for the companion granted patents, the TriplePoint reel/frame numbers, and the valuation/PR figures.

---

## 8. Three Crystallized Takeaways

1. **Etched's whole pitch is "the best layer is no layer" — and the patent shows it's literally a wire where everyone else puts a switch, justified entirely by the fact that AI weights, once loaded, never move.**

2. **The impressive parts aren't the owned parts.** The 98%-utilization pipelining and the fixed-function design are just the filing showing its work; the actual intellectual property is boring plumbing — chips wired edge-to-edge and memory soldered straight to compute columns.

3. **This is a dated signature, not a deed.** Three years in, the flagship claim sits under a final rejection in a field crowded with Intel, IBM, and Rambus prior art. Etched can prove it *wrote the idea down first*; it cannot yet prove it *owns* it.

---

## 9. Shorter Summary

Etched's founding patent (filed May 2023, inventors Uberti and Zhu) describes a fixed-function AI accelerator built by wiring many small, identical chips into one giant matrix-multiply engine that a host computer sees as a single device. It targets a real limit of the time: individual chips cap out near a 128×128 compute array and can't hold a large model's weights, so the design composes small arrays rather than trying to build one huge one.

The architecture is aggressively "weight-stationary" — model weights load once and get reused as data streams past — and its cleverest move follows directly from that. Because the weights feeding each compute column never change, the filing proposes hardwiring each memory channel straight into its column and deleting the routing switch that normally lets any compute unit reach any memory. That saves chip area and power, at the cost of all flexibility. This "no-switch" idea is claimed independently, so it can be owned separately from the multi-chip machine. It's the sharpest, most distinctive part of the document, and the basis of Etched's public "the best layer is no layer" pitch.

The design also honestly separates what a systolic array does well (the token-by-token math of transformers) from what it doesn't (self-attention, which needs earlier tokens), handing attention to a separate sidecar processor with its own walled-off memory. The whole machine runs a preset loop with no runtime instructions — the purest form of Etched's bet that transformers stay dominant.

The catch is legal, not technical. As of the record, the application sits under a final rejection (October 2025) against eight prior-art references from Intel, IBM, Rambus and others — because multi-chip systolic arrays are a well-trodden field, and the broadest claims read on almost any tiled accelerator. The patent proves authorship and a dated architecture; it does not yet prove ownership, and it cannot show whether real hardware embodies the claims. Etched has twice pledged its patent stack as loan collateral, which makes the outcome of this examination genuinely consequential: if the no-switch claim survives intact, the pitch becomes property; if it narrows or dies, the document stays the earliest signed record of a bet, with the office's answer stapled to it.

---

Want me to go deeper on any thread — the claim-by-claim survivability analysis (which of the 42 are likely to hold), how this maps onto what's publicly known about the Sohu silicon, or the specific prior-art references the examiner is leaning on?
