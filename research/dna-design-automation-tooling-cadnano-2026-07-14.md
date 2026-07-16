# DNA Design-Automation Tooling (caDNAno / scaffold-routing) — supported memo
<!-- memo-schema: 0.4 -->

> Captured 2026-07-14. Source: Claude Code `/research` → intake-by-hand. Slug: dna-design-automation-tooling-cadnano-2026-07-14.
> Program: dna-nanotech-foglet-research, bottleneck dig #2 of 4. Audit floor 5/5; mapping floor; banned-phrase (0 hits); cite-token (0).
> **All rows medium** — every quote is WebSearch-summary provenance (PNAS primary 403'd); verify verbatim against primaries before high-confidence use. These are qualitative *tool-capability* claims (a landscape), not numeric thresholds.

## Research Context
- **Problem:** DNA design-automation tooling (caDNAno/scaffold-routing) — SOTA + gaps.
- **Schema:** memo-schema 0.4

## The landscape (the answer)
The field moved from **manual visualization** (caDNAno, Tiamat — expert routes every base) → **geometry-driven automation** (Bathe-lab suite: **DAEDALUS**/TALOS for 3D, **PERDIX**/METIS for 2D, DX vs 6HB edges; **ATHENA** = the unifying open-source GUI, mesh→scaffold+staples) → the **ML/inverse-design frontier** (Nature Materials 2024 graph-neural-net that predicts shape *and* inverse-designs for a target in ~real time). caDNAno remains the interop hub: automated tools export caDNAno files so experts can still hand-edit. The newest folding-accuracy work (**PNAS 2024, Douglas lab/UCSF**) reduces staple routing to weighted-graph shortest-path + thermodynamic scoring.

## Audit table (supported rows — medium)

| Tool / claim | Source | Year | URL | Excerpt (≤25 w) | Conf |
|---|---|---|---|---|---|
| caDNAno/Tiamat = manual scaffold routing + staple design (expert-only baseline) | Bathe (NAR) | 2021 | https://academic.oup.com/nar/article/49/18/10265/6368527 | "scaffold routing and staple sequence design…performed manually…software such as caDNAno or Tiamat" | med |
| DAEDALUS — automated 3D polyhedral scaffold routing + staples (DX edges) | Veneziano/Bathe | 2016 | https://www.science.org/doi/10.1126/sciadv.aav0655 | "DAEDALUS solves the scaffold routing and staple design problem fully automatically for any 3D polyhedral surface" | med |
| PERDIX — automated 2D free-form routing (graph theory) + caDNAno output | Bathe | 2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6314877/ | "optimized scaffold routing based on graph theory…A caDNAno file is also generated as output" | med |
| TALOS/METIS — stiffer 6HB-edge automated variants | Bathe (NAR) | 2021 | https://academic.oup.com/nar/article/49/18/10265/6368527 | "6HB edge-based 2D and 3D assemblies showed significantly enhanced mechanical stiffness" | med |
| ATHENA — open-source GUI, mesh→scaffold+staples for any wireframe (DX/6HB) | Bathe (NAR) | 2021 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8501967/ | "ATHENA has a graphical user interface that automatically renders…scaffold routing and staple strand sequences" | med |
| ATHENA integrates caDNAno editing + oxDNA/atomistic simulation | Bathe (NAR) | 2021 | https://academic.oup.com/nar/article/49/18/10265/6368527 | "ATHENA also enables external editing of sequences using caDNAno…atomic-level models…oxDNA" | med |
| PNAS 2024 — folding accuracy via weighted-graph shortest-path + thermodynamic scoring | Aksel/Navarro/Fong/Douglas (UCSF) | 2024 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10983894/ | "reducing the problem of DNA strand routing to the known problem of shortest-path finding in a weighted graph" | med |
| Nature Materials 2024 — GNN predicts shape + automated inverse design (~real time) | Nat Mater | 2024 | https://www.nature.com/articles/s41563-024-01846-8 | "enables an automated inverse design of DNA origami structures for given target shapes…real-time virtual prototyping" | med |
| Science 2024 — inverse-designed pyrochlore lattice; field lacks a general high-yield design framework | Science | 2024 | https://www.science.org/doi/10.1126/science.adl5549 | "hindered by the lack of a general framework for discovering designs that self-assemble with high yield" | med |
| Limit — DAEDALUS can't render fully arbitrary 3D (non-discrete edges, arbitrary vertices) | Bathe (NAR) | 2021 | https://academic.oup.com/nar/article/49/18/10265/6368527 | "DAEDALUS remains incapable of rendering…completely arbitrary 3D polyhedra composed of non-discrete edge-lengths" | med |

## Source-Locator Coverage
- Rows submitted: 10 · supported: 10 · unsupported: 0 · survival 100% (all medium — provenance-capped).

## Decisions for Human Confirmation (cap 5)

| Claim | Source URL | Candidate use / Verification needed | Conf |
|---|---|---|---|
| ATHENA is the modern entry GUI (mesh→scaffold+staples, any wireframe, exports caDNAno) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8501967/ | **Use:** treat ATHENA as the default automated design tool + caDNAno for manual refinement. **Verify:** current ATHENA maintenance/version + whether it now handles arbitrary 3D. | med |
| PNAS 2024 (Douglas/UCSF) folding-accuracy design principles (graph shortest-path + thermodynamics) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10983894/ | **Use:** apply on top of caDNAno designs to raise folding yield. **Verify:** the specific fold-improvement magnitude (the "6–30×" figure was NOT verifiable this pass — PNAS 403'd). | med |
| ML inverse design (Nature Materials 2024 GNN) is the emerging frontier | https://www.nature.com/articles/s41563-024-01846-8 | **Use:** watch as the path to target-shape→design automation. **Verify:** reproducibility + maturity beyond the paper; DNA-data-scarcity impact. | med |
| The real tooling gap = no general high-yield self-assembly design framework (Science 2024) + arbitrary-3D limit | https://www.science.org/doi/10.1126/science.adl5549 | **Use:** frame the open research problem for the program. **Verify:** monitor for a general solver. | med |
| Coverage gap — scadnano / Adenita / MagicDNA / oxView not covered | — | **Use:** none yet. **Verify:** run a follow-up dig on these tools before claiming a complete landscape. | — |

## Verification trace (Mission Control L1)
Run `2026-07-14-1534-research-dna-design-automation`. Audit floor 10/10 · mapping 10/10 · banned 0 · cite-token 0 · source-identity: 10 provenance-flag (websearch-summary, all capped medium). Sub-task "Intake validation": PASS (10 supported / 0 unsupported).

## Promotion Gate reminder
Input to the 4-step Promotion Gate, not approval. Every row is provenance-capped medium — verify verbatim against the primary papers (esp. the PNAS 2024 fold-improvement number) before any uplift.
