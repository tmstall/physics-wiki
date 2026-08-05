---
source: claude_export
conversation_uuid: 69f8581e-95c1-4b13-8b28-417ec1948cae
title: "The Droplet That Rewrites the Ring:"
created_at: 2026-06-26T15:30:06.939784Z
updated_at: 2026-06-26T15:33:05.283141Z
tier: A
score: 268
n_messages: 2
---

# The Droplet That Rewrites the Ring:

## Human

Analyze paper

## Assistant

Now let me retrieve the full paper from the journal or a preprint source. The abstract is available but the full paper is paywalled on ACS. Let me search for a preprint.

I now have enough material to proceed — the key mechanistic detail (OH• radical attack → ring expansion to 7-membered lactone → CO extrusion → contraction to pyridine) is confirmed from the Chemistry World report. Let me now fetch the supporting info table of contents to see what additional mechanistic data was provided.

I now have a comprehensive picture of the paper and its field context. The key mechanistic detail — OH• attack → 7-membered lactone intermediate → CO extrusion → ring contraction to pyridine — is confirmed. Let me now deliver the full analysis.

---

**Access Status**
Full paper: not publicly accessible (ACS paywalled, no arXiv preprint found)
Abstract: retrieved from ACS DOI page
Supplementary material: table of contents visible (47 figures, extensive mechanistic data)
Secondary sources: Chemistry World news coverage (confirmed mechanism details), Phys.org report, GKToday summary
Analysis basis: abstract + secondary sources with confirmed mechanistic details; full SI not retrieved

---

## 1. Punchy Title & One-Sentence Hook

**The Droplet That Rewrites the Ring: How a Mist of Water Turns Aniline into Pyridine Without a Single Added Reagent**

A 4-micrometer water droplet accomplishes in a millisecond what industrial chemistry requires heavy-metal catalysts, strong oxidants, and harsh conditions to do at all — swapping a carbon atom in a benzene ring for a nitrogen atom and handing you back a pyridine.

---

## 2. Big-Picture Context

This is an experimental synthetic chemistry paper reporting a new reaction enabled by a new medium: the air-water interface of aerosolized microdroplets. The stakes are both fundamental (what makes a microdroplet chemically different from bulk water?) and applied (can you make pharmaceutically critical pyridine rings without catalysts, oxidants, or waste streams?).

Pyridine and its derivatives are not just chemical curiosities — they're load-bearing scaffolds in an enormous fraction of pharmaceuticals. Niacin (vitamin B3), nicotinamide (NAD+ precursor, skincare ingredient), isoniazid (TB antibiotic), and hundreds of drug candidates contain pyridine rings. The conversion of aniline (benzene ring with an NH₂ group) into pyridine (6-membered ring where one CH has been replaced by an N) is a *skeletal* transformation — you're not changing what's attached to the ring, you're changing what the ring *is*. That's enormously harder than peripheral functionalization. Conventional routes require multi-step sequences, palladium or other transition-metal catalysts, strong oxidants, and/or harsh temperatures.

The field context is the rapidly growing area of microdroplet chemistry, which has demonstrated over the past decade that reactions at air-water interfaces can proceed by pathways simply unavailable in bulk solution. Richard Zare's group at Stanford (where PI Banerjee did his postdoc) pioneered much of this, showing that hydrogen peroxide forms spontaneously in sprayed water, that sugars convert to platform chemicals, and that even C–F bonds — famously the strongest single bonds in organic chemistry — cleave without catalysts in microdroplets. Each new result has pushed harder against the intuition that "water is water." The Banerjee group has been one of the most active labs extending this frontier, and this paper represents their most dramatic result yet: not just acceleration of a known reaction, or enabling of a previously sluggish one, but accomplishing a skeletal rearrangement that has no known precedent under ambient conditions.

**Paper Type & Stakes:** This is an experimental mechanistic paper reporting a novel reaction with green-chemistry implications. The stakes are high on both axes: if the mechanism holds up and scales, it opens a reagent-free route to pyridine scaffolds; and the result places a substantial new constraint on any theory of what makes microdroplet interfaces chemically special.

**Prior Belief Check:** This result will surprise experts. Skeletal editing — swapping atoms within an aromatic ring — is considered one of the harder problems in organic synthesis precisely because it requires breaking aromatic stabilization, reorganizing bonds within a resonance-stabilized system, and then re-closing. The expert expectation prior to this work was that microdroplets could accelerate conventional reactions or occasionally open new reaction channels for *peripheral* functionalization, but not that they could accomplish core-atom swaps unaided. The claim of ~80% conversion in milliseconds at room temperature with no reagents is genuinely surprising to the synthetic chemistry community. It is not incremental — it represents a qualitative new capability claim for microdroplet chemistry.

**Replication & Convergence Note:** This result comes from a single group (Banerjee lab, IISER Tirupati) with no independent replication yet reported. The Chemistry World account notes that the team themselves initially suspected contamination, and repeated experiments at a different site to rule that out — which is a useful internal replication, but not independent group replication. What independent confirmation would look like: another lab in a different country reproducing the aniline-to-pyridine conversion using their own spray setup and confirming the product identity by mass spectrometry and GC-MS. Until that happens, the ~80% conversion figure and the proposed mechanism should be treated as compelling but not settled.

---

## 3. Background Crash-Course

**What is aromatic stabilization, and why does it make skeletal editing hard?**

Benzene — and aniline, which is just benzene with an NH₂ group attached — has its six electrons delocalized around the ring in a way that makes the ring unusually stable. Think of it as a resonating circuit board where current flows continuously around the loop: disrupting the loop costs real energy that you immediately have to pay back. Peripheral reactions (adding or modifying groups *attached to* the ring) are routine because they don't interrupt the circuit. Skeletal editing does interrupt it — you have to open the ring, insert or remove an atom, and re-close it in a new configuration.

Breaks when: the "circuit" metaphor implies the ring is purely electronic with no geometric structure. In reality benzene is also a rigid hexagon — ring opening and closing involve real conformational changes and strained intermediates, not just electronic redistribution. The analogy is good for explaining *why it costs energy* but misleads if you start asking about the geometry of the transition state.

**What is a microdroplet interface, and why is it different from bulk water?**

When you spray an aqueous solution into air, you create droplets a few micrometers across. The surface-to-volume ratio is enormous — for a 4-μm droplet, roughly 10⁶ times larger than a macroscopic container. At that interface, water molecules don't have their full network of hydrogen-bond partners on one side, so they're more "stressed," with different polarity and reactivity than interior molecules. Think of it like the surface layer of a crowd at a concert: the people at the edge are oriented outward, more available for contact, not hemmed in on all sides. Meanwhile, as the droplet evaporates, the solute concentration at the surface rises rapidly, and evaporation itself creates a local charge separation — surface layers tend to accumulate protons (H⁺), making the microdroplet interface anomalously acidic. Add to this that charged droplets carry electric fields that can polarize and activate bonds.

Breaks when: pushed to imply the interface has a single well-defined chemistry. In fact, there is active debate in the field about how H₂O₂ forms in sprayed water (internal electric fields? partial dehydration of surface ions? corona discharge?), and different reaction classes may be driven by different aspects of the interface. The analogy also doesn't capture the millisecond timescale: these aren't equilibrium surfaces, they're rapidly evolving as evaporation shrinks the droplet.

**What is skeletal editing in the broader synthetic context?**

Skeletal editing is the emerging synthetic strategy of modifying a molecule's *core scaffold* — inserting, deleting, or swapping atoms within a ring — rather than just decorating the periphery. Analogy: think of it as editing the CPU architecture of a chip rather than adding more memory. The CPU change alters every downstream circuit's behavior in a way that adding peripheral components can't. In drug discovery, swapping a carbon for a nitrogen in a phenyl ring (making benzene into pyridine) changes the molecule's polarity, hydrogen-bonding capacity, and metabolic stability simultaneously — all highly desirable for improving drug-likeness. Until recently this required multi-step sequences; Levin's group and others have pioneered reagent-based skeletal editing, but those routes still require specific reagents and catalysts.

Breaks when: the CPU analogy implies precise, engineered control. Current skeletal editing — including this paper — still has questions about regioselectivity (which carbon gets swapped?). In drug discovery, you often need to place the nitrogen at a specific position, and the microdroplet method does not yet demonstrate that level of control.

**Central analogy for this paper:** a stressed crowd edge that catalyzes reactions no concert hall interior could.

---

## 4. Core Technical Explanation

**The experimental setup**

The team dissolves aniline in water and nebulizes it with pressurized nitrogen gas, creating a fine mist of microdroplets roughly 4 μm in diameter — about 1/20th the width of a human hair. These droplets travel through air for microseconds to milliseconds before being collected for analysis. In some experiments they apply +5 kV to charge the droplets; in others the droplets are left uncharged. They then vary droplet size (by adjusting nebulizer pressure and orifice geometry), charge, pH, and UV irradiation. Product identification uses high-resolution mass spectrometry (HRMS) and gas chromatography-mass spectrometry (GC-MS) with isotope labeling and radical trapping to probe mechanism.

**The result: aniline → pyridine at ~80% conversion**

Within the millisecond lifetime of airborne microdroplets, aniline undergoes rapid skeletal reorganization, achieving up to ~80% conversion to pyridine. This is the headline claim. The transformation involves replacing one CH unit in the benzene ring with an N atom — a net loss of one carbon and gain of one nitrogen in the ring, with the exocyclic NH₂ group serving as the nitrogen source.

The reaction is promoted by smaller droplet size, interfacial acidity, strong electric fields, and reactive oxygen species, and is accelerated by UV light and droplet charging. Each of these knobs tunes the same underlying chemistry: they all increase either the concentration of hydroxyl radicals (•OH) or protons at the droplet surface.

**The proposed mechanism: expand, eject, contract**

The mechanistic picture, supported by isotopic labeling and radical trapping, has three stages:

*Stage 1 — Radical initiation:* An interfacial hydroxyl radical (•OH) attacks the aniline ring. The •OH is generated spontaneously at the air-water interface — the same process responsible for H₂O₂ formation in sprayed water, now well-established by the broader microdroplet literature. Surface-bound electron transfer between OH⁻ and H⁺ ions concentrated at the droplet surface generates •OH radicals.

*Stage 2 — Ring expansion to a 7-membered lactone:* Following an initial attack by a hydroxyl radical, the aniline substrate undergoes a ring expansion to form a seven-membered lactone intermediate. This is the structural crux. The 6-membered benzene ring transiently expands to a 7-membered ring containing an oxygen (a lactone = a cyclic ester). Think of this as briefly unhinging one wall of the hexagon, inserting an oxygen-containing "wedge," and forming a 7-membered structure that still keeps the nitrogen from the amine group in play.

*Stage 3 — CO extrusion and ring contraction:* Elimination of carbon monoxide then contracts this ring back down to six atoms. The 7-membered lactone ejects a CO unit (this is the key bond-breaking step that removes one ring carbon), and the remaining atoms close back into a 6-membered ring — but now with nitrogen in the ring rather than in an exocyclic position. The result is pyridine.

This sequence — expand/insert, then eject/contract — is a known class of reaction in organic chemistry called *Wolff rearrangement* territory or more broadly a *ring expansion / CO extrusion* cascade. It's been seen in photochemistry and in some metal-catalyzed reactions, but executing it this cleanly under ambient conditions with no added reagents, using only the interfacial chemistry of a water droplet, is what's unprecedented.

**Protons and radicals cooperate**

The mechanism requires *both* the interfacial acidic environment (protons) and the •OH radicals. Protons facilitate protonation steps that stabilize intermediates; •OH radicals provide the oxidative kick to initiate ring opening and/or drive subsequent steps. This explains why acidic pH and charged (proton-enriched) droplets enhance yield, why UV light (which generates more ROS) helps, and why smaller droplets (higher surface-area-to-volume ratio, more interfacial chemistry per molecule) outperform larger ones.

**Demonstration substrates**

The team extends the reaction to substituted anilines and demonstrates synthesis of three real drugs: niacin (nicotinic acid, vitamin B3), nicotinamide, and isoniazid (the TB antibiotic). This confirms the reaction isn't a one-substrate curiosity.

**Assumption Audit**

Watch: readers may assume "80% conversion" means 80% isolated yield. The paper actually reports up to ~80% conversion as measured directly (by mass spectrometry on the airborne products), while Chemistry World confirms the isolated yield is substantially lower — meaning collection efficiency is a separate bottleneck not captured by the headline number.

Watch: readers from physics/physical chemistry may assume "air-water interface" means a single well-characterized surface with a known mechanism. The paper actually works within a *contested* mechanistic landscape: the community is still actively debating exactly how •OH and H₂O₂ form in microdroplets (internal electric fields? partial dehydration? corona discharge?), and the proposed mechanism here is consistent with but does not definitively settle that broader debate. The mechanism is proposed, not fully proven.

Watch: readers may assume this reaction is equivalent to the Levin-group-type skeletal editing (which involves controlled reagents and defined selectivity). The paper's reaction is mechanistically distinct — it runs through a radical-mediated cascade rather than a designed organometallic mechanism — and crucially has not yet demonstrated regioselective control over *which* ring position gets the nitrogen when multiple positions are chemically distinct.

---

## 5. What's Genuinely New or Clever

**1. The first reagent-free ambient skeletal swap between a benzene and a pyridine ring.**

Every prior aniline→pyridine route required multiple steps and/or metal catalysts or strong oxidants. The insight here isn't just "microdroplets are reactive" — that was established. It's that the specific cooperative action of interfacial protons + •OH radicals can traverse the ring expansion/CO-extrusion cascade fast enough (in milliseconds) to compete with droplet evaporation and fragmentation. The cleverness is recognizing that the microdroplet interface provides *both* the radical oxidant *and* the acid catalyst simultaneously, without any reagent, essentially running what would be a multi-step reaction as a concerted interfacial event.

**2. The accidental discovery and rigorous verification.**

Banerjee's group discovered the reaction fortuitously while using aniline as a nucleophile in other microdroplet reactions, and initially suspected the pyridine signal was a contaminant. They repeated experiments with different materials, equipment, and even at a different site before concluding the microdroplets had genuinely induced the rearrangement. This trajectory — serendipitous observation → rigorous elimination of artifacts → mechanistic investigation — is how genuine surprises get properly established, and it adds credibility to the result. The paper's 47-figure SI (!) reflects the depth of verification performed.

---

## 6. Limitations & Open Questions

**The mechanism is proposed, not definitively established.** The radical trapping and isotopic labeling experiments are consistent with the OH•-initiated ring expansion / CO extrusion pathway, but HRMS in a millisecond-timescale reaction cannot directly observe the 7-membered lactone intermediate — it's inferred from the logic of the product distribution and labeling pattern. (B) Contested — mechanistic assignments from mass spectrometry in fast spray reactions are standard practice in the field, and experts generally accept this level of mechanistic evidence as sufficient for a proposed mechanism, but it falls short of direct spectroscopic observation of intermediates. (paper — the mechanism is labeled a "proposal" in the abstract and by the authors)

**Isolated yield is substantially lower than measured conversion.** The team's isolated yields were substantially lower than those measured directly during the reaction, and developing a procedure to efficiently generate and collect larger quantities of product will be a crucial next step. If the collection efficiency problem isn't solved, the 80% conversion figure is kinetically impressive but practically limited. (A) Consensus — this is a known challenge in all microdroplet synthetic chemistry, not unique to this paper. (broader literature)

**No regioselectivity control demonstrated.** For substituted anilines, the ring swap must place the nitrogen at a specific position to be useful in drug synthesis. The paper demonstrates the reaction works on substituted anilines (and makes three drugs), but doesn't establish whether the nitrogen insertion is positionally selective or whether it gives a mixture that happens to include the desired isomer. This is a major gap for medicinal chemistry applications. (A) Consensus — regioselectivity is the central challenge in all skeletal editing, universally acknowledged. (analyst inference from field context, though almost certainly acknowledged in paper)

**The fundamental physics of the microdroplet interface remains contested.** The paper's mechanism relies on •OH being available at the interface, which it attributes to the standard microdroplet chemistry. But there is active debate about whether reaction accelerations in microdroplets are caused by internal electric fields, partial dehydration raising the free energy of surface ions, or simply higher encounter frequencies — and the claimed mechanism for H₂O₂ formation (which underpins •OH availability) is disputed in the literature. This doesn't invalidate the observed reaction, but it means the mechanistic explanation rides on contested terrain. (B) Contested — the reaction is clearly happening; what exactly drives it is argued. (broader literature)

**Scalability is unproven.** Nebulization is an established technique but producing gram-to-kilogram quantities of pyridine derivatives via aerosolized microdroplets requires engineering solutions that don't currently exist. The focus going forward is on making the transformation both practical and scalable. (A) Consensus — acknowledged by authors explicitly. (paper)

---

## 7. Detailed Summary & Explanation

Nandy et al. report that aqueous aniline, when nebulized into airborne microdroplets a few micrometers across, spontaneously converts to pyridine at the air-water interface under completely ambient conditions — room temperature, atmospheric pressure, no catalysts, no oxidants, no reagents beyond water. Up to ~80% conversion is measured by mass spectrometry within the millisecond lifetime of the droplets. This is the first demonstration of a reagent-free skeletal swap between a benzene-type ring (aniline) and a pyridine ring.

The driving force is the uniquely hostile chemistry of the microdroplet surface. When water is sprayed, the interface becomes proton-enriched (anomalously acidic), carries residual electric fields from charge separation, and spontaneously generates hydroxyl radicals (•OH) — the same ROS implicated in atmospheric oxidation chemistry. Inside the droplet in bulk water, these conditions don't prevail; at the surface, they converge. Smaller droplets have more surface per unit volume, so more molecules encounter the active zone — which is why smaller drops give better yield. Charging the droplets and UV irradiation both boost •OH availability and further improve conversion.

The proposed mechanism has three steps: (i) •OH attacks the aniline ring, initiating ring opening; (ii) the ring expands to a 7-membered lactone intermediate — a transient, unstable structure containing oxygen in the ring; (iii) the lactone ejects a CO molecule, the ring contracts back to 6 members, and re-aromatizes — now with the amine nitrogen in the ring position rather than exocyclic. The net result is one ring carbon has been removed and replaced by the nitrogen from the original NH₂ group. Isotopic labeling (using ¹⁸O-labeled water and ¹⁵N-labeled aniline) and radical trapping experiments support this pathway, though the 7-membered intermediate is inferred rather than directly observed.

The authors extend the chemistry to substituted anilines and demonstrate direct synthesis of niacin (vitamin B3), nicotinamide, and isoniazid — all pharmaceutically relevant pyridine derivatives.

**Why the summary is framed this way:** I've centered the explanation on the mechanism rather than just the yield claim, because the mechanism is both what makes this scientifically interesting and where the uncertainty lives. The 80% conversion is the headline number but the collected yield caveat is load-bearing for anyone thinking about applications. The microdroplet interface background is necessary because the paper's claims are only intelligible against the contested but rapidly advancing understanding of what those interfaces actually do.

**Genuine Uncertainty Disclosure:** Where I'm least confident in this analysis: the mechanistic section, specifically the 7-membered lactone intermediate and CO extrusion pathway. This detail is confirmed by Chemistry World's reporting of the paper, but without access to the full paper's SI (47 figures including isotopic labeling data and radical trapping experiments), I cannot assess how tightly the labeling data actually constrains this pathway versus alternatives. A reader with full paper access should examine the ¹⁵N and ¹⁸O labeling results directly.

---

## 8. Three Crystallized Takeaways

1. **Water, sprayed into a mist, can perform skeletal surgery on molecules that bulk water leaves untouched.** The air-water interface of a 4-micrometer droplet concentrates protons, radicals, and electric fields into a zone so reactive it can swap a ring atom in milliseconds — no metal catalyst required.

2. **The mechanism is a "expand-eject-contract" cascade:** hydroxyl radical opens the benzene ring, an oxygen inserts to form a transient 7-membered lactone, then CO is expelled and the ring re-closes as pyridine — an entirely ambient version of chemistry that normally requires photochemical or organometallic conditions.

3. **The gap between measured conversion (80%) and isolated yield is the central practical problem:** the chemistry works beautifully inside the droplet, but catching the product efficiently enough to be useful at scale is an unsolved engineering challenge that will determine whether this ever leaves the lab.

---

## 9. Shorter Summary

Water microdroplets — tiny airborne spheres a few millionths of a meter across — can transform aniline (a benzene ring with an amino group) directly into pyridine (a 6-membered ring containing a nitrogen atom) in milliseconds, at room temperature and atmospheric pressure, with no added catalysts, oxidants, or reagents. Up to 80% of the aniline converts to pyridine during the brief airborne lifetime of the droplets. The Banerjee group at IISER Tirupati discovered this reaction accidentally and, after rigorous verification including experiments at a separate facility, published it in the Journal of the American Chemical Society in June 2026.

The key to the transformation lies at the air-water interface of each droplet. When water is nebulized, its surface becomes enriched in protons (anomalously acidic) and spontaneously generates hydroxyl radicals — aggressive oxidizing species normally associated with atmospheric chemistry. The combination of intense surface electric fields, radical availability, and extreme acidity creates a reaction zone that doesn't exist inside bulk water. Smaller droplets work better precisely because more of their volume is surface.

The proposed mechanism proceeds in three stages: a hydroxyl radical attacks the aniline ring; the ring expands temporarily to a 7-membered structure containing oxygen (a lactone); then a carbon monoxide molecule is expelled, the ring snaps back to 6 members, and re-aromatizes — this time with the nitrogen from the original amino group sitting inside the ring. The net result is a carbon-for-nitrogen swap within the aromatic core, achieved with isotopic labeling and radical trapping experiments supporting the pathway.

The chemistry was extended to make three real pharmaceutical compounds — niacin (vitamin B3), nicotinamide, and isoniazid (a TB antibiotic) — confirming the reaction is general enough to be useful, not just a single-substrate curiosity. The main outstanding challenge is that the measured conversion (80%) reflects what happens inside the droplet; the actually isolated (collected) yield is substantially lower, and making this approach practically scalable will require new engineering to efficiently capture products from an aerosolized mist. The proposed mechanism, while well-supported, also relies on a 7-membered intermediate that is inferred rather than directly observed, and the broader field still debates the exact physical origin of microdroplet reactivity.
