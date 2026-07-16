# Macroscale Modular Self-Reconfigurable Robots — foglet tech-ranking deep-dive
<!-- memo-schema: 0.4 -->

> Captured 2026-07-15. Source: Claude Code (`/soraya` conversational-executor) → 3-way parallel `/research`-by-hand sweep (Kilobot / M-Blocks+3D-SOTA / claytronics+miniaturization) + scored synthesis. Slug: macroscale-modular-self-reconfig-robots-2026-07-15.
> Program: foglet/programmable-matter tech-ranking. Scores on the **same 8-gate rubric** as `dna-foglet-falsification-scorecard-2026-07-14.md`. This is the **most-BUILT** programmable-matter lineage and the literal descendant of Hall's Utility Fog — the last un-scored branch.
> **All findings primary-pointered** (Science/Nature/IEEE/CMU/MIT); gate scores are adjustable analyst judgments (same honesty rail as the parent scorecard).

## The headline finding (the reason this branch matters most): the AUTONOMY-vs-SIZE wall
This branch surfaces the **deepest structural law of the whole ranking** — a *physics* reason no candidate reaches utility fog, not just an engineering gap. **[grounded]** (Sci Robotics 2024 [adu6007](https://www.science.org/doi/10.1126/scirobotics.adu6007) + micro-robotics taxonomy [PMC5063027](https://pmc.ncbi.nlm.nih.gov/articles/PMC5063027/)):

> **Onboard power scales with surface area (∝ L²); stored energy + real compute + comms do not shrink proportionally.** So **onboard autonomy only fits at mm–cm scale.** Shrink below ~1 mm and a unit *must* externalize power + control via applied fields — at which point it **becomes the field-driven micro-robot** (which scored 56.25, *losing autonomy*). At micro-scale the physics regime also flips (low Reynolds number: drag dominates, onboard actuation is inefficient), reinforcing the fork.

This law **unifies the entire "no candidate is close to utility fog" verdict** under one constraint:

| Family | Has | Missing | One-line |
|---|---|---|---|
| **Macroscale modular robots** (this dive) | onboard autonomy + open-air + reconfig | tiny size, vast 3D count | **right architecture, wrong scale** (cm, ~24 in 3D) |
| Microscale field robots (56.25) | µm scale + fast | onboard autonomy (externally driven) + fluid-bound | **right scale, wrong autonomy** |
| DNA nanotech (52.5) | µm scale + 10¹² count + precision | open-air, motility (wet + static) | **right scale, wrong medium/dynamics** |

**You cannot have onboard-autonomous AND tiny AND vast simultaneously** — the L² power wall forbids it. That is the season's load-bearing physics result: utility fog is blocked by a scaling law, not merely immature engineering.

## Findings (primary-sourced)
| # | Finding | Value | Source | Conf |
|---|---|---|---|---|
| 1 | **Kilobot**: largest self-organizing robot swarm — 1,024 units compile a human-specified **2D** shape from 3 local rules (edge-follow / gradient / trilateration) | **1,024, 2D only** | Rubenstein/Cornejo/Nagpal, *Science* 345:795 (2014) | high |
| 2 | Kilobot is **fully autonomous + self-powered**: onboard MCU + Li-ion + IR neighbor-comms (~10 cm, 30 kb/s) + RGB LED; 3–12 h runtime | onboard everything | *Science* 2014; Rubenstein *RAS* 2013 | high |
| 3 | Kilobot is **cheap-mass-manufacture by design**: ~**$14/unit**, ~5 min assembly/robot | $14, 5 min | Rubenstein *RAS* 2013 | high |
| 4 | Kilobot hard limits: **2D/flat only**, ~**1 cm/s**, ~**12 h per 1,024-unit shape**, seed-dependent, edge-follow drift/traffic jams | slow + planar + imprecise | Harvard SEAS; Wikipedia | high |
| 5 | **M-Blocks 2.0**: autonomous fleet of **16** momentum-driven cubes (flywheel 20,000 RPM, magnetic edges), barcode IDs, self-recognize | 16 cubes | MIT News 2019; IROS 2013 | high |
| 6 | **3D M-Blocks** (ICRA 2015): torque about 3 axes → magnetic cubic-lattice 3D reconfiguration — but **small N** (single-digit–low-tens), no large-count 3D demo | small-N 3D | Romanishin et al., *ICRA* 2015 | high |
| 7 | **Record for reliable physical 3D self-reconfiguration = M-TRAN III, ~24 modules** (>100 connection changes). **No macroscale hardware exceeds ~100 units in true 3D rigid reconfiguration.** | **~24 (3D record)** | M-TRAN III, *IJRR* 2008; MSRR survey 2019 | high |
| 8 | "**Million modules**" (M-Blocks) + "**millions of sub-mm catoms**" (claytronics) are **stated VISION, not built** | vision only | MIT News 2019; Goldstein *IEEE Computer* 2005 | high |
| 9 | **Claytronics catom** real prototype = **44 mm cylinder, 24 electromagnets, no moving parts**; largest real ensemble = **≤7 modules**; sub-mm catom = concept | 44 mm, ≤7 units | CMU claytronics; *IEEE Computer* 38(6) 2005 | high |
| 10 | Claytronics' 2005 roadmap projected core capability "**< a decade**"; **~20 yr later unmet** — no mm-scale autonomous modular catom exists | roadmap missed 2×+ | *IEEE Computer* 2005 (claim) | med |
| 11 | **Reconfiguration planning is NP-complete** (proven for chain + 3D lattice cubic modules); config space explodes exponentially with module count | NP-complete | MSRR survey 2019; planning-complexity papers | high |
| 12 | The autonomy-vs-size fork's endpoints: smallest **autonomous** robot = Miskin ~**200 µm** (but NOT modular); smallest **modular** micro-unit = "smartlets" **≤1 mm³** (harvested power, aqueous, low autonomy) | 200 µm vs 1 mm³ | *Sci Robotics* adu6007; Miskin/Blaauw | high |

## Scorecard (same 8 gates + weights)
| Gate (weight) | Modular robots | Rationale |
|---|---|---|
| **Reversible reconfig (20)** | **demonstrated 1.0** → 20 | The **defining act** — self-reconfiguration into arbitrary shapes on command. The most literal "reconfigure into shapes" of any candidate. |
| **Open-air operation (20)** | **demonstrated 1.0** → 20 | All operate in air / on surfaces. |
| Discrete addressable units (15) | **demonstrated 1.0** → 15 | Each robot discrete + individually addressable (M-Blocks 2.0 barcode IDs). |
| Actuation/speed (15) | **partial 0.5** → 7.5 | Kilobot ~1 cm/s, ~12 h/shape (slow); M-Blocks pivot fast but multi-move sequences slow + NP-hard planning. |
| **Autonomy + onboard power/logic (10)** | **demonstrated 1.0** → 10 | **The standout** — each unit is self-powered + self-coordinating (onboard battery+MCU+comms). Best-in-class with drones; DNA/micro-robots only 0.5. |
| Scale toward vast counts (10) | **partial 0.5** → 5 | 1,024 (Kilobot) but **2D**; 3D rigid reconfig caps at **~24**. cm-scale, not µm; "trillions" fails hard. |
| Cycle lifetime (5) | **demonstrated 1.0** → 5 | Reusable indefinitely (rechargeable, mechanical). |
| Manufacturability (5) | **demonstrated 1.0** → 5 | Kilobot purpose-built for cheap scale ($14, 5 min/unit, 1,024 built). |
| **WEIGHTED TOTAL /100** | **87.5** | **Ranks #2** (drones 95 > **modular robots 87.5** > acoustic 72.5 > micro-robots 56.25 > smart-dust 55 > DNA 52.5 > 4D 50). |

## The 87.5/#2 score is REAL but exposes the SAME rubric weakness (twice over)
Modular robots differ from the #1 drones (95) **only on speed** (7.5 vs 15) — they are essentially *"drone swarms that physically fuse into rigid shapes, but slower."* On the foglet act (forming a connected rigid structure) they are arguably **more** faithful than drones. But the high score hides two disqualifiers the rubric under-weights:

1. **Unit SIZE is un-gated.** The rubric scores unit *count* (scale, 10) but has **no "small unit size" gate** — so a swarm of 1,024 **3.3 cm** robots scores identically to 1,024 µm units. Modular robots are **~1,000–10,000× too large** for the "tiny" foglet spirit, and the rubric can't see it.
2. **3D vast-count is absent.** 1,024 is **2D**; the physical 3D rigid-reconfiguration record is **~24 modules** (M-TRAN III, 2008) — and planning is **NP-complete**, so even with better hardware the motion-sequencing does not scale.

**Sensitivity (per the parent scorecard's rule):** add a unit-size gate + weight 3D-scale, and modular robots **fall sharply** — their cm size + ~24-in-3D ceiling dominate. Same "ranking is rubric-dependent" finding, now sharpened by a concrete missing dimension (**unit size**) the rubric should arguably add.

## Genuine standing (where it actually leads)
- **The most foglet-*architecturally*-faithful candidate:** the only family combining onboard autonomy + open-air + discrete units + on-command reconfiguration into connected rigid shapes. If "foglet" means the *mechanism*, this is the closest real thing.
- **Kilobot is the canonical proof** that ~1,000 cheap autonomous units + local rules → a global programmed shape. That collective-autonomy result is real and unmatched.
- **Its wall is scale, and the scale wall is physics** (autonomy-vs-size L² law + NP-complete planning), not cost/process — so unlike the camo-door "engineering knob" cases, this ceiling won't yield to more money.

## Bottom line (closes the candidate set)
Macroscale modular self-reconfigurable robots rank **#2 (87.5)** — the **right architecture at the wrong scale**: genuinely autonomous, open-air, reconfiguring into rigid shapes, but stuck at **cm units** and **~24-in-3D** by a **surface-area power law + NP-complete planning**. Combined with the mirror-image failures of DNA (right scale, wrong medium) and field micro-robots (right scale, wrong autonomy), the branch delivers the season's unifying result: **utility fog is blocked by a scaling law — you cannot get onboard-autonomous + tiny + vast at once — not by immature engineering.** No candidate is close, and now we know *why* at the level of physics.

## Decisions for Human Confirmation (cap 5)
| Claim | Source URL | Candidate use / Verification | Conf |
|---|---|---|---|
| Modular robots score 87.5 (#2); differ from drones only on speed | (this synthesis) | **Use:** new scorecard column. **Verify:** ratify gate scores + whether to add a unit-SIZE gate. | med |
| Autonomy-vs-size wall: onboard power ∝ L² ⇒ autonomy only at mm–cm; sub-mm must externalize control | https://www.science.org/doi/10.1126/scirobotics.adu6007 | **Use:** the season's unifying physics finding. **Verify:** re-read adu6007 full text for the L² statement. | high |
| Physical 3D self-reconfig record = ~24 modules (M-TRAN III); nothing macroscale >100 in 3D | IJRR 2008 (M-TRAN III) | **Use:** the 3D-scale ceiling. **Verify:** any newer >24-module 3D hardware demo. | high |
| Reconfiguration planning is NP-complete (chain + 3D lattice) | MSRR survey 2019 | **Use:** the planning-scale wall. **Verify:** exact reduction. | high |
| Kilobot 1,024 units, 2D, $14, ~12 h/shape, fully autonomous | *Science* 345:795 (2014) | **Use:** the collective-autonomy proof + its planar/slow limit. **Verify:** re-fetch Science primary. | high |

## Promotion Gate reminder
Input to the Promotion Gate, not approval. The 87.5/#2 result, the proposed **unit-size gate**, and the **autonomy-vs-size physics wall** are the load-bearing items to ratify before they lift into the canonical scorecard.
