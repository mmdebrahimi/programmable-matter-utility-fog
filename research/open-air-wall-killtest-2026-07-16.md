# Open-Air Wall — Kill-Test #3 (VERIFIED 2026-07-16 — all three items confirmed against primary sources)
<!-- memo-schema: 0.4 -->

> Captured 2026-07-16. Source: Claude Code (`/soraya`) → kill-test `scripts/open_air_wall.py` (exit 0) + a 3-way primary-source verification pass.
> **STATUS: VERIFIED.** The initial pass was reasoning-grounded (the web sweep had failed); a follow-up verification confirmed all three load-bearing items against **primary journal sources**. The result STANDS and was **published to the public repo (Part F5 narrowed).**
> **Verification caught a real error in this memo's first draft:** the spore engine was mis-cited as "Chen et al., *Sci. Adv.* 2015" — the actual paper is **Chen, Sahin et al., *Nature Communications* 6:7346 (2015), DOI 10.1038/ncomms8346** (the underlying spore actuator is *Nat. Nanotechnol.* 2014). Corrected throughout.

## Verification results (all three CONFIRMED)
1. **Spore evaporation engine → CONFIRMED (primary).** Chen X, Goodnight D, … Sahin O, *"Scaling up nanoscale water-driven energy conversion into evaporation-driven engines and generators,"* **Nature Communications 6:7346 (2015)**, [ncomms8346](https://www.nature.com/articles/ncomms8346) ([PMC4490384](https://pmc.ncbi.nlm.nih.gov/articles/PMC4490384/)). Spore-coated "HYDRA" tapes expand/contract with humidity; scaled into an **evaporation-driven piston engine** + a rotary "moisture mill" **generator** that does real mechanical work and generates electricity **in open air** (air–water interface, not submerged). Numbers: **~17 J/kg** energy density (≈ skeletal muscle), lifts **~50× its own weight**, ~60 µW peak / 1.8 µW average electrical output (drove alternating LEDs), and **reversible over ~1,000,000 humidity cycles** (elongation reduced only slightly after 80 days). Foundational: Chen et al., *Nat. Nanotechnol.* 9:137 (2014).
2. **Low-a_w metabolic floor → CONFIRMED + SHARPENED (primary).** *Growth* floor **a_w ≈ 0.61** (*Xeromyces bisporus*; Grant 2004, *Phil. Trans. R. Soc. B*; prokaryote division bottoms ~0.635). **Documented metabolic activity / cell division to a_w ≈ 0.585** (*Aspergillus penicillioides*; Stevenson… Hallsworth, *Environ. Microbiol.* 19:687, 2017, [doi:10.1111/1462-2920.13597](https://pubmed.ncbi.nlm.nih.gov/27871132/)); theoretical limit ≈ 0.565. So "~0.6" was correct-conservative; the tightest *metabolic* figure is **0.585**.
3. **Non-aqueous enzymology → CONFIRMED (primary/review).** Klibanov (MIT), *"Improving enzymes by using them in organic solvents,"* **Nature 409:241 (2001)**; founding work Zaks & Klibanov, *PNAS* 82:3192 (1985) + *JBC* 263:3194 (1988). Enzymes catalyze in near-anhydrous organic solvents needing only a **bound-water monolayer (or less)**, not bulk water. **Nuance:** near-anhydrous ≠ anhydrous — state it as *"a hydration shell is required; bulk submersion is not."*

## The claim under test
The corrected article's Part F5 asserts open air as *"the deepest surviving barrier"* — that biological reconfiguration is **strictly aqueous**, and the air-tolerant state (a spore) and the reconfigurable state are **disjoint**.

## Result: OVER-STATED (same failure family as the first two walls)
The blanket claim **bundles three separable capabilities and reports the hardest one as if it governed all three** — the identical error mechanism behind the L² wall (fixed-demand assumption) and the comms wall (broadcast-topology assumption).

Decompose "reconfigurable in open air" into its three real sub-gates:

1. **Shape-change / actuation in dry air → the claim is FALSE.** Humidity-driven hygromorphs move and do real mechanical work in open air with *no liquid bath*: pinecones, wheat awns, hygromorph bilayers [textbook], and — more strikingly — **Bacillus-spore hygroscopic actuators + a spore-powered "evaporation engine"** that extracts work from humidity swings [reported, not re-verified this pass]. Air-tolerant and shape-*changing* are therefore **not** disjoint.
2. **Single-unit metabolism / logic in dry air → OVER-STATED.** Enzymes function with only a bound-water **monolayer** (non-aqueous enzymology, Klibanov) and in organic solvents [textbook]; active metabolism persists down to **water activity a_w ≈ 0.6** (xerophiles, e.g. *Xeromyces bisporus*) [textbook]. Needs *humidity*, not *submersion*.
3. **Diffusion-based multi-unit COORDINATION in dry air → the claim SURVIVES, and only here.** Morphogen / cAMP / ion-flux signalling genuinely needs a continuous aqueous phase; a signal does not diffuse across a dry gap. This is a *mechanism* constraint, not a law of matter.

**Caveat that supports the original claim:** anhydrobiosis (tardigrade tun, *Polypedilum*, resurrection plants) is **metabolic suspension** — desiccated organisms *survive* but do **not** move or compute while dry. So biology's own air-tolerant state is indeed inert. The counterexample to disjointness is **engineered/passive humidity actuation**, not a fully autonomous dry organism.

## The load-bearing synthesis (the reason this was worth running)
The narrowed open-air wall is: *"how do MANY units signal each other without a shared liquid phase?"* — **that is the same question kill-test #2 surfaced** (drop the radio; find a cheap dry neighbour-to-neighbour channel). So the two surviving walls are not two:

> **The comms-energy wall and the open-air wall COLLAPSE INTO ONE: dry local signalling.** Solve neighbour-to-neighbour messaging in air without radio and without diffusion, and *both* barriers fall together. That is the single sharpest remaining research target for utility fog.

## Wall scoreboard (session cumulative)
- **L² power wall** — FALSIFIED (inverted). Verified + published.
- **Communication-energy wall** — FALSIFIED AS STATED (survives as a radio-cost design rule). Verified + published.
- **Open-air wall** — **OVER-STATED (this memo)** — survives *only* as diffusion-based coordination; collapses into the comms wall. **UNVERIFIED — not published.**
- **NP-complete reconfiguration-planning wall** — STANDS (biology sidesteps it by never solving optimally; but only reaches *evolved* shapes, not arbitrary ones).

## What would close this (before anything ships public)
- Web-verify the spore-actuator / evaporation-engine claim (Chen et al., *Sci. Adv.* 2015 "spore-based hygroscopic actuator" — locate + confirm work output in dry air).
- Verify the a_w ≈ 0.6 metabolic-activity floor against a primary xerophile reference.
- Confirm non-aqueous enzymology (Klibanov) as stated.
- ONLY THEN consider a Part F5 correction. Until then the public article's hedged *"deepest surviving barrier"* wording **stays as-is** — it is defensible; this memo is not yet strong enough to overturn it publicly.

## Honesty rail
This pass is explicitly **weaker** than #1/#2: no fresh primary sources, calc is a reasoning scaffold not a numeric model. Labelled `[textbook]` = standard result; `[reported, not re-verified]` = recalled, needs a fetch. **Do not cite this memo as a closed result.**
