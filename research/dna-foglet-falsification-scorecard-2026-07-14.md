# Foglet-Technology Falsification Scorecard — Adversarial Test of H1/H2
<!-- memo-schema: 0.4 -->

> Captured 2026-07-14. Source: Claude Code `/research` (adversarial dig #4). Slug: dna-foglet-falsification-scorecard-2026-07-14.
> Program: dna-nanotech-foglet-research, dig #4. **Purpose: try to BREAK H1 ("DNA nanotech is the most promising foglet tech") and H2, per the 2026-07-14 adversarial review** — replace the "every barrier is an engineering knob" narrative with a testable, weighted scorecard across ALL candidates.

## Method (declared + adjustable — this is the whole point)
"Foglet / utility fog" = **vast numbers of small, discrete, individually-addressable units that reconfigure into arbitrary shapes on command, in open air, with some autonomy.** I score each candidate on 8 foglet-relevant gates, weighted by how load-bearing each is to *that* definition. Scores: **demonstrated=1.0 · partial=0.5 · unknown=0.25 · absent=0.0.** Weighted total /100. **The ranking is rubric-dependent** — a different weighting (favoring molecular precision + scale) flips the result; that dependence is the finding, not a bug.

| Gate | Weight | Why |
|---|---:|---|
| Reversible on-command reconfiguration | 20 | THE core foglet act |
| Operating environment = open air (not sealed wet buffer) | 20 | utility fog works in a room, not a cuvette |
| Discrete addressable units | 15 | "many small units," not bulk material |
| Actuation / motility / speed | 15 | units must move/change fast |
| Autonomy + onboard logic/power | 10 | foglets self-coordinate |
| Scale toward vast unit counts | 10 | "trillions" |
| Cycle lifetime / durability | 5 | reusable |
| Manufacturability / QC at scale | 5 | buildable |

## Gate-status scorecard (adversarial, honest)

| Gate (weight) | DNA nanotech (voxels/SEPP) | Modular/micro robots (magnetic-acoustic) | 4D printing | Smart dust | Drone swarms |
|---|---|---|---|---|---|
| Reversible reconfig (20) | partial 0.5 (voxels flex/rigid; most devices 2-state) | partial 0.5 (field-programmed multi-shape, reversible) | partial 0.5 (shape-memory, limited cycles) | **absent 0.0** | **demonstrated 1.0** |
| Open-air operation (20) | **absent 0.0** (needs aqueous Mg²⁺ buffer) | low 0.25 (⚠️ revised down from 0.5 by the 2026-07-14 micro-robot dig — swarms operate predominantly IN FLUID, not free air) | demonstrated 1.0 | demonstrated 1.0 | demonstrated 1.0 |
| Discrete units (15) | demonstrated 1.0 | demonstrated 1.0 | **absent 0.0** (continuous material) | demonstrated 1.0 | demonstrated 1.0 |
| Actuation/speed (15) | partial 0.5 (slow strand-displacement; ~few Hz only w/ external magnetic levers) | demonstrated 1.0 (fast fields) | partial 0.5 (slow thermal) | absent 0.0 | demonstrated 1.0 |
| Autonomy+power (10) | partial 0.5 (SEPP stores energy+logic; no persistent power) | partial 0.5 (mostly externally field-driven) | absent 0.0 | partial 0.5 | demonstrated 1.0 |
| Scale (10) | **demonstrated 1.0** (10¹²/batch, gram-scale) | unknown 0.25 (dozens–hundreds micro) | partial 0.5 (bulk ≠ units) | partial 0.5 | partial 0.5 (1000s, macro) |
| Cycle lifetime (5) | partial 0.5 (serum degradation; coatings help) | unknown 0.25 | partial 0.5 (fatigue ~10⁴ cyc) | demonstrated 1.0 | demonstrated 1.0 |
| Manufacturability (5) | partial 0.5 (gram bioproduction; GMP open) | partial 0.5 (microfab hard) | demonstrated 1.0 | demonstrated 1.0 | demonstrated 1.0 |
| **WEIGHTED TOTAL /100** | **52.5** | **56.25** (⚠️ revised from 61.25 — open-air 0.5→0.25 per micro-robot dig) | **50.0** | **55.0** | **95.0** |

## The falsification result (H1 as stated: FALSIFIED)
**Under a foglet-faithful rubric, DNA nanotech ranks 4th of 5 (52.5).** Its two lowest gates are the two heaviest: **open-air operation = 0** (it is chemically bound to an aqueous Mg²⁺ buffer — a hard fail for utility fog, which must work in a room), and **reversible reconfiguration + actuation are only partial** (most DNA devices are two-state switches; multi-state needs the very new SEPP coupled arrays; strand-displacement is slow). DNA wins decisively on exactly one gate — **scale** (10¹² units/batch) — plus molecular precision. So:

> **H1 ("DNA nanotech is the most promising *foglet* technology") is FALSIFIED as stated.** DNA is the most promising **molecular self-assembly / nanodevice platform**, not the most promising **foglet/utility-fog** technology. Under the foglet definition, **drone swarms score highest (95) but are macroscopic** (they violate the "tiny, vast-number" spirit — scale gate 0.5); the best *microscale* foglet analogue is **field-driven modular/micro-robots (61.25)** — they operate in air, actuate fast, and reconfigure reversibly, though at low unit counts and low maturity.

## H2 (also corrected)
H2's "engineering not physics" framing survives only weakly. DNA's open-air failure is **physico-chemical** (electrostatic stability needs counter-ions in solution), not merely a cost/process knob — a genuine, non-trivial barrier the earlier digs under-weighted. The honest H2: *the gates are plural AND at least one (operating medium) is a deep material-chemistry constraint, not just cost/GMP.*

## Sensitivity (honest)
If you **re-weight** toward molecular precision + scale + manufacturability (e.g., for a *nanomedicine* goal rather than *utility fog*), **DNA jumps to #1**. That is the correct answer to a *different* question. The ranking is only meaningful once the target application fixes the weights — precisely the brainstorm's point.

## Bottom-line verdict (re-issued, honest + downgraded)
- **No current technology is close to literal utility fog.**
- For the **foglet/utility-fog** goal specifically: **field-driven modular micro-robots are the most promising *microscale* analogue**; drone swarms are the most capable but not "tiny."
- **DNA nanotech is the most promising *molecular programmable-matter* platform** (unmatched scale + precision + biomedical traction) — a real, strong result, just **not** "the most promising foglet tech."
- The earlier "every barrier is an engineering knob" narrative is **retired**: DNA's open-air/actuation limits are partly fundamental material-chemistry, not just cost.

## Update 2026-07-15 — acoustic/field ASSEMBLY scored as its own column
A dedicated deep-dive (`acoustic-field-matter-assembly-2026-07-15.md`) scored **acoustic + field assembly** (levitation/holography/ferrofluid) — distinct from the "magnetic-acoustic micro-robot" column above — on this same rubric: **72.5/100 → ranks #2** (drones 95 > **acoustic/field 72.5** > micro-robots 56.25 > smart-dust 55 > DNA 52.5 > 4D-printing 50). It aces **open-air (1.0)** + discrete-units + speed + lifetime + manufacturability, fails **autonomy (0.0)** + **scale (0.25)**. **Rubric-sensitivity caveat (load-bearing):** the high rank is real but exposes a rubric weakness — the **~25-particle open-air ceiling is a fundamental DOF physics wall** (force ∝ 1/N, *PNAS 2019*), not an engineering knob, and units are fully passive; re-weighting toward the foglet *spirit* (scale+autonomy heavier) **flips it below micro-robots**. Same "ranking is rubric-dependent" finding this scorecard already carries.

## Update 2026-07-15 — MACROSCALE modular self-reconfig robots scored (last branch)
A dedicated deep-dive (`macroscale-modular-self-reconfig-robots-2026-07-15.md`) scored **macroscale modular self-reconfigurable robots** (Kilobot / M-Blocks / claytronics — distinct from the microscale field-robot column above): **87.5/100 → ranks #2** (drones 95 > **modular robots 87.5** > acoustic 72.5 > micro-robots 56.25 > smart-dust 55 > DNA 52.5 > 4D 50). They differ from #1 drones **only on speed** — essentially "drone swarms that fuse into rigid shapes, but slower" — and lead all candidates on **onboard autonomy (1.0)**. **Two load-bearing findings:** (1) the high score exposes a **missing rubric dimension — unit SIZE** (the rubric scores unit *count*, not size, so 1,024 cm-scale robots score like 1,024 µm units; modular robots are ~1,000–10,000× too big for "tiny"), and the physical **3D rigid-reconfig record is only ~24 modules** (M-TRAN III) with **NP-complete planning**. (2) The **autonomy-vs-size wall** — onboard power ∝ L² ⇒ autonomy only fits at mm–cm; sub-mm units must externalize power/control (becoming the field-driven micro-robot, losing autonomy). This **unifies the whole "no candidate is close to utility fog" verdict under one physics law**: you cannot get onboard-autonomous + tiny + vast simultaneously.

## Sources
- [Programmable Modular Acoustic Microrobots (PMC 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11215786/) · [Reversible magnetic microassembly review, Adv. Intell. Syst. 2024](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/aisy.202300471)
- [Real-time magnetic actuation of DNA nanodevices (PMC5899095)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5899095/) · [Magnetically actuated DNA micro/nanorobots review](https://spj.science.org/doi/10.34133/2022/9758460) · [SEPP spring-loaded arrays, Sci. Robotics 2025](https://www.science.org/doi/10.1126/scirobotics.adu3679)
- Prior program memos (deep-dive, purification, tooling, immunogenicity) for DNA gate evidence.
> Provenance note: cross-candidate gate scores are analyst judgments grounded in the cited threads + prior program memos (mostly medium confidence); the scores + weights are explicitly adjustable, not oracle values.
