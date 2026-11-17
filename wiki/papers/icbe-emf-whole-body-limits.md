---
tags: [papers, emf, radiofrequency, risk-assessment, ntp]
last_updated: 2026-11-15
status: analysis-ingest
related_papers: [hrv-resonance-baroreflex]
source_analysis: "raw/analyses/2026-11-13_doi-10.1186-s12940-026-01288-6_icbe-emf-whole-body-emf-limits-ntp.md"
---

# Whole-Body RF Limits and Animal Cancer Counts

**One-line summary:** Melnick and Moskowitz run a benchmark-dose calculation on two radiofrequency rat bioassays and get a protective level tens to hundreds of times below the 80 mW/kg whole-body limit; almost all of that factor is a straight-line extrapolation, the cited replications are null and unmentioned, and the comparison is to the limit rather than to measured exposures. *Environmental Health* (2026).

## Key claims and results

- **Paper:** Ronald L. Melnick and Joel M. Moskowitz, for ICBE-EMF. *Environmental Health* **25**, 42 (2026). DOI [10.1186/s12940-026-01288-6](https://doi.org/10.1186/s12940-026-01288-6). Published 14 March 2026. The analysis merged two same-day passes. The supplement with the paper’s own poly-3 rates was not retrieved. Tumour counts were taken from NTP TR-595 and the Ramazzini record.
- The public whole-body specific absorption rate limit, 80 mW/kg, is a heating limit: behavioural disruption in eight rats and six monkeys, then a factor of fifty. It was not derived from cancer data.
- The paper fits the NTP and Ramazzini tumour counts, takes a lower confidence bound on a small effect, and divides by about a thousand to reach one extra cancer per hundred thousand under a linear no-threshold line. Across five dataset–endpoint pairs the ratio to the existing limit runs from about 15 to about 900, near 200 at eight hours a day for the combined NTP set. A fertility slope gives a factor of about 8–24. The analysis reproduced the ratio table and put the paper’s benchmark dose inside a reconstruction from the public counts. The arithmetic is not the failure.
- The factor of a thousand is the linear extrapolation below every tested dose. A mildly curved response cuts the headline from about two hundred to about six. A threshold removes it. The 6 W/kg group that drives the NTP slope sits above the 4 W/kg level the guidelines treat as thermal. Japan–Korea validation studies reported no carcinogenic effect at 4 W/kg and are not discussed. The fertility input’s own corrigendum reports no significant dose trend.
- The comparison is limit versus proposed limit. Survey whole-body exposures are nearer 0.01 mW/kg, below even the paper’s strictest number. The paper does not estimate excess cancers at actual exposures, and it does not treat local handset SAR.

## Physical intuition

A cooling spec answers how hot a chip gets. It does not answer the bit-error rate. The RF whole-body number answers “when does this field warm an animal enough to change its behaviour?” The paper asks a different question, in regulatory units used for chemical carcinogens, and gets a much smaller number. That smaller number stands only if risk is linear all the way down and if these two bioassays are the right inputs. Neither premise is settled by the arithmetic.

## Limitations and assumptions

- Linearity at untested doses is unverifiable at these risk levels. ICNIRP treats heating as the mechanism, which is why those bodies do not apply the carcinogen default.
- Male rats only, and the most sensitive endpoint, with uncertainty factors stacked on top.
- Reporting a benchmark dose to four figures from counts of a handful of tumours overstates the resolution. Forty table cells rest on five slopes and one model choice.
- This page is the paper’s argument and the analysis’s checks. It is not a finding that everyday exposures cause cancer.

## Connections

- Unrelated physiology shelf (autonomic rhythms): [[hrv-resonance-baroreflex]]. Do not merge the two questions.
- Islands. No concept page for radiofrequency limits.

## Open questions

- Does a multi-dose bioassay with a typical control rate reproduce a monotonic tumour increase below the thermal SAR?
- What excess incidence do these potencies imply at measured population exposures?

## Source

- `raw/analyses/2026-11-13_doi-10.1186-s12940-026-01288-6_icbe-emf-whole-body-emf-limits-ntp.md`
