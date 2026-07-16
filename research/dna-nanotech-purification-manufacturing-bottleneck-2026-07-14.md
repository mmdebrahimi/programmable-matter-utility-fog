# DNA Nanotech — Purification & Manufacturing Scale-Up Bottleneck (memo)
<!-- memo-schema: 0.4 -->

> Captured 2026-07-14. Source: Claude Code `/research` (focused, single-session web pass). Slug: dna-nanotech-purification-manufacturing-bottleneck-2026-07-14.
> Program: dna-nanotech-foglet-research (bottleneck dig #1 of 4). Tests **H2** (the gating bottleneck to real programmable matter is manufacturing/purification, not the science of the units).

## Research Context
- **Problem:** resolve whether DNA-nanostructure purification/manufacturing scales — the deep-dive named it the dominant bottleneck.
- **Schema:** memo-schema 0.4

## The verdict (H2 → CONFIRMED, with a sharp refinement)
**Making the discrete units at scale is essentially SOLVED; the real barriers are cost and therapeutic-grade purity, not assembly.** Bulk production of both the long scaffold *and* the short staples has been demonstrated at **gram scale** in standard bioreactors. What still gates real-world/therapeutic deployment is (a) raw-material **cost**, (b) **GMP-grade purification** beyond research gels, and (c) scaling the *whole process chain* to m³. So H2 is right in direction but should be stated precisely: **the bottleneck is manufacturing ECONOMICS + GMP purity, not "can we build the units."**

## Findings

| # | Finding | Value | Source | Confidence |
|---|---|---|---|---|
| 1 | Biotechnological mass production upgraded DNA origami from milligram → **gram scale** via self-excising DNAzyme "cassettes" (bacteriophage ssDNA precursor + Zn²⁺-dependent DNA-cleaving enzymes) that mass-produce arbitrary staple + scaffold strands in ONE bioreactor process | mg → g scale | Praetorius/Kick/Dietz et al., *Nature* 552:84-87 (2017), [nature24650](https://www.nature.com/articles/nature24650) | high |
| 2 | Scaffold ssDNA (M13) bioreactor production: phage titers up to **1.6×10¹⁴ pfu/mL**, **up to 410 mg ssDNA per liter**, ~50× titer gain, 2 orders-of-magnitude efficiency vs shake-flask (was ~4 mg/L) | 410 mg/L | Nano Letters 2015 (phage scaffolds), [PMC4532261](https://pmc.ncbi.nlm.nih.gov/articles/PMC4532261/) | high |
| 3 | Cost is the standing barrier: scaffold ~**$200/µg** (M13 phage DNA); staples ~**$1200 per 10 mg** of origami filament — "prohibitive" for large-scale/therapeutic manufacturing | $200/µg | secondary analysis; flagged for primary re-verify | medium |
| 4 | Sustainable/recycling manufacturing: recover excess staples post-assembly + refold with recycled strands (recycled structures match pristine geometry) — cuts cost + waste for scale-up | qualitative | Nano Letters 2024, [10.1021/acs.nanolett.4c02695](https://pubs.acs.org/doi/10.1021/acs.nanolett.4c02695) | high |
| 5 | Research-scale purification = agarose-gel electrophoresis / Freeze-N-Squeeze / PEG precipitation; these reveal **structural heterogeneity**. Therapeutic grade needs **HPLC + chromatography (AEX/HIC/SEC) + AFM sorting** | qualitative | TUM scale-up project + reviews | medium |
| 6 | GMP path requires validated **endotoxin removal (<0.25 EU/mg)**, structure-preserving sterile filtration, stability-indicating assays; **no FDA-specific guidelines** yet for DNA nanomedicines; oncology clinical trials projected **~3–5 yr** | <0.25 EU/mg | [TUM biovt scale-up](https://www.epe.ed.tum.de/en/biovt/research/fermentation/scale-up-of-the-microbial-production-of-dna-nanoobjects/) + secondary | medium |
| 7 | Cross-contamination-free contract manufacturing enabled by phagemid+helper design (phagemid can't self-replicate without helper) — any CDMO can produce the ssDNA | qualitative | Praetorius/Dietz 2017 | high |
| 8 | Adjacent GMP DNA infrastructure already exists: 4basebio (7 GMP cleanrooms, **50 mg–10 g** batch sizes); Touchlight dbDNA (FDA IND cleared 2023, 3 therapies in clinic) — a manufacturing base DNA-nano can leverage | 50 mg–10 g | BioPharm International / vendor | medium |

## The remaining scale-up gap (what's actually unsolved)
- **Cost** at therapeutic scale (scaffold $/µg dominates).
- **GMP purity**: current gel purification leaves heterogeneity + endotoxin; chromatography/HPLC at scale is immature for these large, delicate objects.
- **Whole-chain m³ scaling**: fermentation → ssDNA isolation → autocatalytic self-assembly → purification, all validated end-to-end, is the open engineering program (TUM biovt).

## Sourcing caveat (honesty rail)
The specific cost figures (#3) and some GMP/timeline numbers (#6) came via a secondary web overview, not primary papers — flagged **medium** confidence; verify against the original ACS Nano / Cell / Nature papers before quoting. The gram-scale mass-production milestone (#1, #2) and recycling (#4) are primary-sourced and **high** confidence.

## Bottom line for the program
H2 confirmed with refinement: **the unit-fabrication problem is solved to gram scale; DNA nanotech's path to real deployment is gated by manufacturing cost + GMP purification, and there's already an adjacent GMP-DNA industry to leverage.** This *raises* confidence that DNA nanotech is the promising foglet path — the bottleneck is an economics/process-engineering problem with active solutions, not a physics wall.
