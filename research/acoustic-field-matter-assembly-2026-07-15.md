# Acoustic / Field-Driven Matter Assembly — foglet tech-ranking deep-dive
<!-- memo-schema: 0.4 -->

> Captured 2026-07-15. Source: Claude Code (`/soraya` conversational-executor) → 3-way parallel `/research`-by-hand sweep + scored synthesis. Slug: acoustic-field-matter-assembly-2026-07-15.
> Program: foglet/programmable-matter tech-ranking. Scores on the **same 8-gate weighted rubric** as `dna-foglet-falsification-scorecard-2026-07-14.md` (DNA 52.5 · micro-robots 56.25 · 4D-printing 50 · smart-dust 55 · drone-swarms 95). Complements the existing "magnetic-acoustic micro-robot" column by scoring **acoustic + field ASSEMBLY** (levitation/holography/ferrofluid) as its own mechanism.
> **All findings primary-pointered** (Nature/Science/PNAS/Nat Commun); cross-candidate gate scores are analyst judgments, explicitly adjustable (same honesty rail as the parent scorecard).

## What this branch is (three sub-mechanisms, different profiles)
| Sub-mechanism | Medium | Units | Scale | Persistent solid? |
|---|---|---|---|---|
| **Acoustic levitation / holographic tweezers (HAT)** | **open AIR** | passive mm beads, individually positioned | **~25 (2D) / 12 (3D)** hard ceiling | no (acoustic collapse) |
| **Acoustic assembly / holography in FLUID** | liquid (required) | passive cells/beads, bulk field-patterned | **thousands** | **yes — via separate gel/UV cure** |
| **Magnetic / electric field assembly** (ferrofluid, colloid, DEP, mag cubes) | mostly liquid; mag-cubes dry | passive, bulk (global field) | millions bulk / ~20 dry cubes | ferrofluid persists soft; mag-cubes latch rigid |

## Findings (primary-sourced)
| # | Finding | Value | Source | Conf |
|---|---|---|---|---|
| 1 | HAT manipulates discrete particles **individually + simultaneously in mid-AIR** | **25 (2D) / 12 (3D icosahedron)**; ~27 projected max | Marzo & Drinkwater, *PNAS* 116:84 (2019), [1813047115](https://www.pnas.org/doi/10.1073/pnas.1813047115) | high |
| 2 | The ceiling is a **fundamental degrees-of-freedom wall**: independent traps ≤ transducer-element budget, per-trap force **∝ ~1/N** → adding traps dilutes stiffness until they can't hold against gravity | force ∝ 1/N | *PNAS* 2019 (authors' own analysis) | high |
| 3 | Single-bead speed is very high (POV volumetric display) | **8.75 m/s** vertical | MATD, Hirayama et al., *Nature* 575:320 (2019), [s41586-019-1739-5](https://www.nature.com/articles/s41586-019-1739-5) | high |
| 4 | Levitated units are **passive EPS beads** — no onboard power/logic/addressing; all control external | zero onboard | *PNAS* 2019 / MRS Bulletin | high |
| 5 | Acoustic **holography in FLUID** patterns **thousands** of cells/beads into an arbitrary 2D/3D shape in one shot | thousands, seconds | Melde/Fischer, *Nature* 537:518 (2016) [nature19755]; *Sci Adv* 9:eadf6182 (2023) | high |
| 6 | Fluid pattern becomes a **real transferable solid** via a **separate cure** (collagen gelation / ~90 s UV of GelMA) — acoustics only patterns; cure solidifies | ~90 s cure | Ma/Fischer *Adv Mater* 32:1904181 (2020); Biofabrication 2025 [add49e](https://iopscience.iop.org/article/10.1088/1758-5090/add49e) | high |
| 7 | Monolithic 3D-printed hologram = **one plate → one fixed pattern** (static); only low-DOF phased arrays reconfigure electronically | static vs reconfigurable trade-off | *Nature* 2016; *Nat Commun* 2024 [55337-0](https://www.nature.com/articles/s41467-024-55337-0) | high |
| 8 | Ferromagnetic liquid droplets: **reversible** paramagnetic→ferromagnetic, write/erase shapes, dipole persists after field-off | reversible + remanent | *Science* 365:264 (2019) [aaw8719](https://www.science.org/doi/10.1126/science.aaw8719) | high |
| 9 | Field-directed colloidal assembly = **millions** of particles but **bulk lattices** — one global field, **not per-unit addressed** | millions, unaddressed | Bharti/Velev review, *Langmuir* 2015 | high |
| 10 | The one **dry, open-air, rigid-latching** field case: magnetic modular cubes assemble into programmable polyominoes/polycubes | **≤20 (2D) / 16 (3D)**, single global field, no per-unit addressing | Bhattacharjee et al., IEEE [9573309](https://ieeexplore.ieee.org/document/9573309/) | high |
| 11 | Frontier crack on persistence: **acoustic levitation + electrostatic charging** overcomes "acoustic collapse" to assemble/adapt many-particle structures (field-off rigidity **not** yet claimed) | new (2025) | *PNAS* 2025 [2516865122](https://www.pnas.org/doi/10.1073/pnas.2516865122) | med |

## Scorecard (same 8 gates + weights as the parent falsification scorecard)
Scored **best-case across the family** (air-HAT for open-air/discrete; the honest weakness is concentrated in two gates):

| Gate (weight) | Acoustic/field assembly | Rationale |
|---|---|---|
| Reversible reconfig (20) | **partial 0.5** → 10 | Phased arrays reprogram arbitrary patterns electronically, reversibly — but they position **sparse discrete beads**, not a filled reconfigurable body (same class as micro-robots' 0.5). |
| **Open-air operation (20)** | **demonstrated 1.0** → 20 | **The standout.** HAT manipulates 25 beads in **free air**; magnetic cubes run dry. The gate DNA (0.0) and micro-robots (0.25) both fail. |
| Discrete addressable units (15) | **demonstrated 1.0** → 15 | 25 particles **individually** positioned in air simultaneously (external addressing). |
| Actuation/speed (15) | **demonstrated 1.0** → 15 | 8.75 m/s single-bead; kHz array update. Genuinely fast. |
| Autonomy + onboard power/logic (10) | **absent 0.0** → 0 | Units are **fully passive** — nothing onboard. *Worse* than micro-robots (0.5). |
| Scale toward vast counts (10) | **low 0.25** → 2.5 | Addressable-in-air **hard-capped ~25** (DOF wall); millions only as **unaddressed bulk**. The heaviest disqualifier for "trillions." |
| Cycle lifetime (5) | **demonstrated 1.0** → 5 | Field is non-destructive; inert beads don't fatigue (beats micro-robots' 0.25). |
| Manufacturability (5) | **demonstrated 1.0** → 5 | Cheap COTS 40 kHz transducers (TinyLev-class) + inert beads. |
| **WEIGHTED TOTAL /100** | **72.5** | **Ranks #2** under this rubric (drones 95 > **acoustic/field 72.5** > micro-robots 56.25 > smart-dust 55 > DNA 52.5 > 4D-printing 50). |

## The load-bearing finding: the #2 score is REAL but EXPOSES a rubric weakness
Acoustic/field assembly scores high because it **uniquely combines open-air + fast + cheap + durable + discrete-addressable** — it beats every microscale candidate on exactly the gate they fail (**open air**). That is a genuine, non-obvious result: *the best open-air discrete-unit manipulator in the whole candidate set is acoustic levitation, not any "robot."*

**But the score is inflated by the rubric under-weighting the two things acoustic catastrophically fails.** The **~25-particle ceiling is a fundamental degrees-of-freedom physics wall** (force ∝ 1/N; authors project ~27 max, *PNAS 2019*) — **not** an engineering knob — and total passivity means zero self-coordination. For "utility fog = **trillions** of **self-coordinating** units," these are arguably the two MOST disqualifying facts, yet scale+autonomy carry only 20/100 combined.

**Sensitivity (honest, per the parent scorecard's own rule):** re-weight toward the foglet *spirit* (scale + autonomy heavier, e.g. 25+20) and acoustic/field **sinks below micro-robots** — its 25-unit hard wall + passivity dominate. So the ranking flip is the finding: *acoustic/field assembly is the best tech for **contactless handling of a handful of passive units in open air**, and the worst-positioned for **vast-number self-coordinating matter**.*

## Genuine niche (where it actually wins)
- **Open-air contactless manipulation / assembly of a few passive units** — the real, fielded strength (levitation handling, containerless processing).
- **Volumetric POV displays** — single-bead MATD (already scored in `swarm-pov-volumetric-displays-2026-07-14.md`); speed, not unit-count.
- **Acoustic bioprinting** — the FLUID variant + cure genuinely makes **real transferable solids** (thousands of cells, ~90 s) — a legitimate manufacturing tool, but a **bulk molding** process, not a programmable-matter substrate.
- **Watch item:** acoustic + **electrostatic charging** (*PNAS 2025*) is the first crack on "acoustic collapse" — the path toward persistent assembled structures; monitor whether field-off rigidity is ever demonstrated.

## Bottom line (fits the whole ranking)
Under the foglet-faithful rubric, **acoustic/field assembly ranks #2 (72.5)** — genuinely the open-air, fast, cheap, discrete-unit leader — **but its headline is a hard physics ceiling, not a promise**: independent open-air manipulation tops out near **~25 passive beads** (a DOF wall), and the units carry **zero autonomy**. It reinforces the season verdict: **no candidate is close to literal utility fog**; each leads on a different axis (drones = capability/scale-macro, DNA = molecular scale/precision, micro-robots = fast microscale reconfig, **acoustic = open-air contactless handling**), and **none** simultaneously clears open-air + vast-number + self-coordinating + rigid-3D.

## Decisions for Human Confirmation (cap 5)
| Claim | Source URL | Candidate use / Verification | Conf |
|---|---|---|---|
| Acoustic HAT open-air ceiling = 25 (2D)/12 (3D), force ∝ 1/N DOF wall | https://www.pnas.org/doi/10.1073/pnas.1813047115 | **Use:** the open-air discrete-unit ceiling for the ranking + the "hard physics wall not engineering knob" claim. **Verify:** re-fetch PNAS primary for verbatim 25/12/27. | high |
| Acoustic-fluid + cure makes real transferable solids (thousands of cells, ~90 s) | https://iopscience.iop.org/article/10.1088/1758-5090/add49e | **Use:** the fluid variant is a real bioprinting/molding tool (not PM substrate). **Verify:** cure time + cell count vs primary. | high |
| Acoustic/field scores 72.5 (#2) under the existing rubric; flips below micro-robots under scale+autonomy re-weight | (this synthesis) | **Use:** add as a new scorecard column + note the rubric-sensitivity flip. **Verify:** ratify gate scores. | med |
| Magnetic modular cubes = the rare dry open-air rigid-latching case (~20 units, single global field) | https://ieeexplore.ieee.org/document/9573309/ | **Use:** the dry open-air field-assembly datapoint. **Verify:** largest cube count. | high |
| Electrostatic-charge + acoustics (PNAS 2025) is the persistence frontier | https://www.pnas.org/doi/10.1073/pnas.2516865122 | **Use:** watch item for field-off rigidity. **Verify:** whether persistence-after-field-off is ever claimed. | med |

## Promotion Gate reminder
Input to the Promotion Gate, not approval. Gate scores are adjustable analyst judgments; the 72.5/#2 result + its rubric-sensitivity flip is the load-bearing finding to ratify before it lifts into the scorecard.
