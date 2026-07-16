# DNA Nanotech — In-Vivo Immunogenicity & Clinical Threshold (memo)
<!-- memo-schema: 0.4 -->

> Captured 2026-07-14. Source: Claude Code `/research` → intake-by-hand. Slug: dna-nanotech-immunogenicity-clinical-threshold-2026-07-14.
> Program: dna-nanotech-foglet-research, bottleneck dig #3 of 4. Tests the deep-dive open question "what is the consensus immunogenicity threshold for clinical translation."
> **All rows medium** — quotes are WebSearch-summary provenance (Nature/Wiley/ACS fetches gated); verify verbatim vs primaries before high-confidence use.

## Research Context
- **Problem:** in-vivo immunogenicity clinical threshold for DNA nanostructures.
- **Schema:** memo-schema 0.4

## The answer (good news for the program): immunogenicity is TUNABLE-BY-DESIGN, not a hard wall
There is **no single "immunogenicity threshold" number** — instead the immune response is a **designable knob**:
- **Bare** wireframe DNA origami induce **minimal TLR9 activation** despite internal CpG dinucleotides; only **displayed multivalent unmethylated CpG** drives robust TLR9/interferon activation. So a *delivery* vehicle can be made near-stealthy by minimizing displayed CpG, while a *vaccine* deliberately maximizes it.
- DNA origami is **non-toxic up to high doses in vivo** and its immune response is **dose- and shape-dependent** and **distinct** from a plain TLR9 foreign-DNA response.
- The practical clinical-translation recipe: **PEGylated-oligolysine coating (K10-PEG5k)** for nuclease/salt stability (**up to ~1,000× nuclease protection**) + endotoxin control (**<0.25 EU/mg**, from the purification memo) + minimized displayed CpG for delivery. There is already a **clinical-track cancer-vaccine platform (DoriVac)** that *uses* immunogenicity productively.

## Findings

| # | Finding | Value | Source | Conf |
|---|---|---|---|---|
| 1 | DNA origami elicits **dose-dependent** immunogenicity, **non-toxic up to high doses in vivo**; response is **shape-dependent** + distinct from a TLR9 foreign-DNA response | qualitative | Lucas et al., *Small* 2022, [10.1002/smll.202108063](https://onlinelibrary.wiley.com/doi/full/10.1002/smll.202108063) ([PMC9250639](https://pmc.ncbi.nlm.nih.gov/articles/PMC9250639/)) | med |
| 2 | **Bare** 3D wireframe origami → **minimal TLR9 activation** despite internal CpG; **displayed multivalent CpG** → robust TLR9 + Type I/III IFN. Immunogenicity is designable | qualitative | ACS Nano 2022, [10.1021/acsnano.2c06275](https://pubs.acs.org/doi/abs/10.1021/acsnano.2c06275) | med |
| 3 | CpG **nanoscale spacing** controls activation: 7 nm spacing enhances macrophage activation (CD83/CD40/IL-6); rigidity required (flexible linkers abolish the effect) | 7 | nm | Comberlato et al. | med |
| 4 | Oligolysine coating (0.5:1 N:P) → **~10× more DNase I resistance**; **oligolysine-PEG copolymer → up to ~1,000× protection** against serum nucleases + modest in-vivo PK gain (mouse) | ~1,000× | Ponnuswamy et al., *Nat. Commun.* 2017, [ncomms15654](https://www.nature.com/articles/ncomms15654) | med |
| 5 | **DoriVac** cancer-vaccine platform: square-block origami, CpG at **3.5 nm** → Th1 polarization; synergizes with anti-PD-L1 (melanoma/lymphoma); long-term T-cell memory; uses **K10-PEG5k** coating | 3.5 | nm | DoriVac (Shih lab lineage) | med |
| 6 | **PLASTIQ** (proximity ligation assay) enables in-vivo structural-integrity tracking from **1 µl blood, 0.01 fM** detection; quantifies degradation + PEGylation effectiveness; UV crosslinking as an alternative stabilizer | 0.01 fM | Nat. Nanotechnol. 2025-26, [s41565-025-02091-z](https://www.nature.com/articles/s41565-025-02091-z) | med |

## Bottom line for the program
**⚠️ Correction (2026-07-14 review):** "no single threshold" was over-read below as "largely solved" — the *absence of a standardized regulatory threshold should LOWER confidence, not raise it*, and "tunable by design" ≠ "clinically manageable across construct classes" (all rows here are medium-confidence). Read the paragraph below as *"immunogenicity is a designable variable with promising mitigations,"* NOT "solved."

The immunogenicity "bottleneck" the deep-dive flagged is **a designable variable with promising mitigations** (originally over-stated as "largely a solved design problem"): bare structures are near-stealthy, immune activation is a tunable function of displayed CpG (copy number + ~3.5–7 nm spacing + rigidity), stability is handled by PEGylated-oligolysine coating (~1,000× nuclease protection), toxicity is low to high doses, and in-vivo integrity is now trackable (PLASTIQ). Net: **another "engineering knob, not a wall"** — reinforcing that DNA nanotech's barriers are process/economics, not biology-forbidding. The one genuinely open item is a *standardized regulatory* immunogenicity spec (no FDA-specific DNA-nanomedicine guideline yet).

## Decisions for Human Confirmation (cap 5)
| Claim | Source URL | Candidate use / Verification needed | Conf |
|---|---|---|---|
| Immunogenicity is tunable-by-design (bare = stealthy; displayed CpG = adjuvant) | https://pubs.acs.org/doi/abs/10.1021/acsnano.2c06275 | **Use:** minimize displayed CpG for delivery, maximize for vaccines. **Verify:** confirm bare-vs-displayed TLR9 quant vs primary. | med |
| PEGylated-oligolysine (K10-PEG5k) is the de-facto in-vivo stabilization standard (~1,000× nuclease protection) | https://www.nature.com/articles/ncomms15654 | **Use:** adopt as default coating. **Verify:** the 1,000× figure vs the primary (fetch gated this pass). | med |
| DoriVac = the leading clinical-track translation (CpG 3.5 nm, Th1, anti-PD-L1 synergy) | https://onlinelibrary.wiley.com/doi/full/10.1002/smll.202108063 | **Use:** track as the flagship in-vivo program. **Verify:** current DoriVac trial/IND status. | med |
| PLASTIQ enables in-vivo integrity tracking (0.01 fM, 1 µl blood) — a translation enabler | https://www.nature.com/articles/s41565-025-02091-z | **Use:** the QC/PK tool for in-vivo work. **Verify:** adoption + primary methodology. | med |
| Open item: no FDA-specific DNA-nanomedicine immunogenicity spec yet | — | **Use:** flag as the real regulatory gap. **Verify:** monitor FDA guidance. | — |

## Verification trace (MC L1)
Run `2026-07-14-1547-research-dna-immunogenicity`. Audit 6/6 · mapping 6/6 · banned 0 · cite-token 0 · source-identity: 6 provenance-flag (all medium). Sub-task Intake: PASS (6 supported / 0 unsupported).

## Promotion Gate reminder
Input to the Promotion Gate, not approval. All rows provenance-capped medium — verify vs primaries (esp. the ~1,000× and DoriVac spacing) before uplift.
