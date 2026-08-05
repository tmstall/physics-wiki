---
source: claude_export
conversation_uuid: a175fb0e-9415-4141-8025-0714e636f5c5
title: "Magneto-optical trapping of metal hydride molecules"
created_at: 2026-06-26T15:35:52.427513Z
updated_at: 2026-06-26T15:37:59.840565Z
tier: A
score: 16
n_messages: 4
---

# Magneto-optical trapping of metal hydride molecules

## Human

Analyze paper.
This website utilizes technologies such as cookies to enable essential site functionality, as well as for analytics, personalization, and targeted advertising. Privacy Policy
Accept
Deny non-essential
Manage preferences

Magneto-Optical Trapping of a Metal Hydride Molecule
Jinyu Dai
1,*, Benjamin Riley
1, Qi Sun
1, Debayan Mitra
1,2, and Tanya Zelevinsky

Phys. Rev. Lett. 136, 233403 – Published 10 June, 2026

DOI: https://doi.org/10.1103/xy6y-kyhc

Abstract
We demonstrate a three-dimensional magneto-optical trap (MOT) of a metal hydride molecule, CaH. We are able to scatter ∼104 photons with vibrational loss covered up to vibrational quantum number 𝜈 =2. This allows us to laser slow the molecular beam near zero velocity with a “white-light” technique and subsequently load it into a radio-frequency MOT. The MOT contains 230(40) molecules, limited by beam source characteristics and predissociative loss of CaH. The temperature of the MOT is below one millikelvin. The predissociative loss mechanism could, in turn, facilitate controlled dissociation of the molecule, offering a possible route to optical trapping of hydrogen atoms for precision spectroscopy.

Physics Subject Headings (PhySH)
Cold and ultracold molecules
Molecule trapping & guiding
Physics logo purple small
synopsis

Trapping a Precursor to Ultracold Hydrogen
Published 10 June, 2026
Researchers have used laser cooling and trapping to isolate calcium monohydride, a key step toward producing ultracold atomic hydrogen.

See more in Physics

Authorization Required
We need you to provide your credentials before accessing this content.
Log in via your institution
If your institution provides access using Shibboleth/OpenAthens log in.

Log in via APS Member Subscription
If you have a personal subscription through your APS membership please log in.
Starting August 1, 2019 APS member subscribers will need to log in using your member credentials instead of your APS Journal Account.
APS Member Log In
Other Options
Buy Article »
Log in with APS Journals Account
Log in with username/password provided by your institution
Get access through a U.S. public or high school
Supplemental Material (Subscription Required)
References (Subscription Required)
Outline
Information
Abstract
Physics News and Commentary
Article Text
Purpose Led Publishing - Science is our shareholder
APS Logo

Authors

Reviewers

Librarians

Students

Connect
ISSN 1079-7114 (online), 0031-9007 (print).
©2026 American Physical Society. All rights reserved.
Physical Review Letters™ is a trademark of the American Physical Society, registered in the United States, Canada, European Union, and Japan. The APS Physics logo and Physics logo are trademarks of the American Physical Society. Information about registration may be found here. Use of the American Physical Society websites and journals implies that the user has read and agrees to our Terms and Conditions and any applicable Subscription Agreement.

## Assistant

**Access Status**
Full paper: not publicly accessible (PRL paywalled; abstract retrieved from journal page)
Abstract: retrieved from PRL landing page
Supplementary material: press release/news coverage retrieved from Phys.org
Analysis basis: abstract + supplementary sources (Phys.org news article, PRL abstract, PRL synopsis)

Proceeding to retrieve arXiv preprint per Master Retrieval Protocol.

Good — the arXiv HTML page is accessible. Let me fetch the full paper body.

Full paper retrieved. Updating access status.

**Access Status** (updated)
Full paper: retrieved from arXiv (arXiv:2512.22350v2, including Supplemental Material)
Abstract: retrieved from PRL landing page
Supplementary material: Supplemental Material retrieved in full (laser configuration table, EOM details)
Analysis basis: full text

This is a short PRL Letter (~4 pages, single narrow result). Brief pre-read: CaH MOT is the one result; background and methods sections are dense but the physics arc is clean. This reads as a strong lite candidate — a focused experimental Letter with one primary demonstration, limited theoretical content, and a clear but narrow contribution. **Lite or full?**

---

*(Noting this while I wait for your call: if you want full, I'll proceed immediately. The paper is short enough that full won't be wasteful, and the predissociation physics and white-light slowing are both genuinely interesting mechanisms worth the crash-course treatment.)*

## Human

Lite

## Assistant

| lite mode

---

## 1. Punchy Title & One-Sentence Hook

**Catching Hydrogen's Precursor: The First Laser Trap of a Metal Hydride Molecule**

Calcium monohydride — a molecule that self-destructs when you shine light on it — has been laser-cooled and trapped for the first time, opening a backdoor route to ultracold hydrogen that direct laser cooling of hydrogen itself cannot provide.

---

## 2. Big-Picture Context

**Paper Type & Stakes:** This is an experimental milestone Letter — a single clean demonstration result from the Zelevinsky group at Columbia, establishing CaH as the first metal hydride molecule to be magneto-optically trapped. The stakes are two-layered: immediate (a new molecular species joins the small club of laser-cooled diatomics), and downstream (a credible path toward optically trapped ultracold hydrogen for precision fundamental physics).

Hydrogen is the simplest atom in the universe and for that reason one of the most powerful testbeds for QED. The 1S–2S transition has been measured to kilohertz precision, and a whole family of transitions — Lamb shift, 2S–4P, 1S–3S — have been pushed to extraordinary accuracy to pin down the proton charge radius. The limiting factor for further improvement is Doppler broadening: the hydrogen atoms in these experiments are in a beam, so they're moving, and moving atoms see a smeared-out laser frequency. The obvious fix is to trap and cool the hydrogen atoms. The problem is that hydrogen is essentially impossible to laser-cool directly — it lacks the closed optical cycling transitions that make atoms like rubidium or cesium amenable to laser cooling.

The workaround the field has converged on: cool a molecule that *contains* hydrogen, trap it, and then photodissociate it near threshold so the hydrogen atom inherits the molecule's low temperature. Metal hydrides — diatomic molecules with a heavy metal atom bonded to a hydrogen — are the natural candidates, because the electronic structure of the metal end provides the nearly-closed transitions needed for laser cooling while the molecule still carries a hydrogen payload. The fluoride molecules (CaF, SrF, BaF) that have dominated the laser-cooled molecule field for the past decade can't do this job. Metal hydrides can, but they come with a nasty complication: predissociation, where the molecule falls apart spontaneously when it absorbs a photon via certain excited states. That complication is precisely what this paper had to solve.

**Prior Belief Check:** The result is not surprising in the sense that it was theoretically anticipated and the Zelevinsky group had already demonstrated direct laser cooling of CaH in 1D in earlier work (2022). What's notable to experts is that the predissociation problem was severe enough that success was genuinely uncertain — the photon budget (how many photons you can scatter before losing the molecule) is roughly an order of magnitude tighter than for fluoride molecules, and scattering ~7,000 photons for slowing while losing ~0.4% per photon to predissociation means barely half the initial population survives to be trapped. Demonstrating that this works at all in 3D is a meaningful result, not just an incremental checkbox. The 230-molecule number is modest by molecular MOT standards, and the field will regard it as a proof-of-concept rather than a production platform in its current form.

**Replication & Convergence Note:** Single-group result with no independent confirmation to date. Independent confirmation would look like a second group trapping CaH or another metal hydride in a MOT; given that the same group's 2022 laser cooling paper preceded this by three years, replication timelines in this subfield are on the order of years.

---

## 5. What's Genuinely New or Clever

**1. Routing around predissociation by choosing the right excited states.**
The core cleverness is surgical: CaH has multiple electronically excited states, and some of them predissociate rapidly while others are stable. The team threads the needle by driving the main cycling transition through the A²Π state (which is stable enough) and using the B²Σ⁺ state only for the vibrational repump of the ν=1 level — accepting that the B-state predissociation eats into the photon budget but managing the loss rate carefully. They then measure the predissociation probability directly from the MOT lifetime and photon scattering rate, getting 0.37% per photon, which is in better agreement with theory than their own earlier measurement. The predissociation that seemed like a fatal flaw turns out to be a manageable tax — and eventually, the paper points out, it becomes an *asset*: near-threshold dissociation is exactly the mechanism they'll use to release ultracold hydrogen atoms from the trap.

**2. White-light slowing with EOM-based spectral broadening.**
Molecular beams have a spread of velocities, and a narrow-linewidth slowing laser only decelerates molecules in a narrow velocity slice. The solution here is to broaden the slowing laser's frequency spectrum using strongly driven electro-optic modulators at ~4.3 MHz, producing ~400 MHz of broadening. This keeps molecules resonant across a wide velocity range simultaneously, dramatically increasing the fraction of the beam that gets slowed to MOT-capture velocity. This "white-light" technique isn't new to the field, but its implementation here is tailored to CaH's specific hyperfine and spin-rotation structure (a 1.9 GHz spin-rotation splitting plus ~50–100 MHz hyperfine splittings), requiring a carefully layered EOM scheme that covers all the relevant sub-levels without gaps.

---

## 6. Limitations & Open Questions

**Molecule number is very low (230 ± 40) and the photon budget is nearly exhausted by slowing alone.**
The predissociation cuts the available photon budget to ~9,000 total, while slowing alone requires ~7,000. That leaves almost nothing for MOT loading and further cooling. **(A) Consensus** — this is explicitly acknowledged in the paper and is the primary stated limitation; the field broadly understands it as the bottleneck. (paper discussion section)

**The beam source is a second independent bottleneck.**
The cryogenic buffer-gas beam produces CaH at ~300 m/s forward velocity with an order of magnitude lower yield than fluoride beams. Even with improved photon budgets, the starting flux limits what MOT number is achievable. **(A) Consensus** — explicitly stated in the paper. (paper §body)

**No path yet demonstrated to the actual goal: optically trapped ultracold hydrogen.**
The paper establishes the precursor step but the dissociation spectroscopy and hydrogen optical trapping remain future work. The temperature of the CaH MOT (~0.86 mK at lowest) is above what would be ideal for the dissociation-to-hydrogen transfer to work optimally. **(B) Contested** — the paper cites theoretical proposals (Lane 2015; Sun et al. 2023) suggesting the scheme is viable, but the hydrogen transfer efficiency and the resulting hydrogen temperature are undemonstrated. Whether the MOT temperature is actually a problem depends on dissociation kinematics that haven't been experimentally probed. (broader literature + analyst inference)

**The RF MOT configuration may limit achievable phase-space density.**
The radio-frequency MOT technique (switching polarizations and field gradients at 0.9 MHz to remix magnetic dark states) is necessary for CaH's internal structure but is known to introduce heating relative to standard DC MOTs. Reaching the high phase-space densities needed for optical dipole trapping will require sub-Doppler cooling stages that haven't yet been demonstrated for CaH. **(A) Consensus** — standard limitation of RF MOTs for molecules, and the paper itself lists sub-Doppler cooling as a next step. (paper discussion + broader literature)

---

## 8. Three Crystallized Takeaways

1. **Hydrogen is too simple to laser-cool directly, so the trick is to cool a molecule that contains hydrogen, trap it, and then photodissociate it — this paper demonstrates the trapping step for the first time with a metal hydride.**

2. **The very property that makes CaH hard to trap — predissociation, where the molecule falls apart on absorbing certain photons — is the same property that will eventually be exploited to release the ultracold hydrogen atom, turning the liability into the mechanism.**

3. **230 molecules at sub-millikelvin temperatures is a modest number, but it establishes metal hydrides as a viable laser-cooling platform; the path to useful quantities requires either brighter beam sources or chirped slowing to recover the photon budget consumed by predissociation.**

---

## 9. Shorter Summary

Hydrogen's extreme simplicity — the very feature that makes it the gold standard for testing QED and measuring fundamental constants like the proton charge radius — also makes it nearly impossible to laser-cool directly. Without a suitable closed optical cycling transition, you can't use the standard toolkit of laser cooling and trapping that has produced ultracold samples of hundreds of other atomic species. The consequence is that precision hydrogen spectroscopy is stuck battling Doppler broadening from thermal beams, limiting how sharp the transition frequencies can be measured.

The workaround is indirect: laser-cool a molecule that *contains* a hydrogen atom, trap it, and then use a carefully tuned photodissociation step near the bond-breaking threshold to release the hydrogen atom — which inherits the molecule's low temperature and ends up colder than anything achievable by direct means. Metal hydrides are the molecule class built for this job. Their electronic structure, dominated by the heavy metal atom, provides the nearly-closed transitions needed for laser cooling, while the light hydrogen end carries the payload.

The Zelevinsky group at Columbia has now demonstrated the crucial precursor step: trapping calcium monohydride (CaH) in a three-dimensional magneto-optical trap, reaching below one millikelvin with about 230 molecules. The central engineering challenge was predissociation — CaH spontaneously falls apart when it absorbs photons through certain excited states, shrinking the available photon budget to roughly 9,000 total. Since decelerating the molecular beam from ~300 m/s to MOT-capture velocity already consumes ~7,000 of those photons, barely half the initial population survives to be trapped. The team threads this needle by choosing excited states that minimize predissociation during cycling, using spectrally broadened "white-light" slowing lasers to capture a wide velocity slice of the beam simultaneously, and employing a radio-frequency MOT to handle CaH's awkward magnetic dark states.

The result is a proof-of-concept platform. Molecule numbers are modest and limited by both the beam source brightness and the photon budget, but the paper projects that ~1,000 molecules should be reachable with improved slowing. More importantly, the predissociation that costs photon budget during trapping becomes the *mechanism* for releasing ultracold hydrogen afterward — near-threshold photodissociation is precisely how the hydrogen atom will be liberated at low temperature. The path from here to trapped ultracold hydrogen for precision spectroscopy is long but no longer hypothetical.
