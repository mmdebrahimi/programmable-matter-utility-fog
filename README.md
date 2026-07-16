# Programmable Matter vs. the Utility-Fog Dream

A scored engineering comparison of the **seven real "programmable matter" technology families** against the classic *utility fog* vision (J. Storrs Hall, 1993) — and the scaling law that explains why none has closed the gap yet.

## The headline

Ranked on an 8-gate, utility-fog-faithful rubric (0–100):

1. **Drone swarms — 95** · 2. **Modular self-reconfiguring robots — 87.5** · 3. **Acoustic / field assembly — 72.5** · 4. **Field micro-robots — 56.25** · 5. **Smart dust — 55** · 6. **DNA nanotech — 52.5** · 7. **4D printing — 50**

Two findings dominate:

1. **"Most promising" is undefined until you fix the application** — the ranking is a dot product of a capability vector and a weight vector; re-weight toward molecular precision and DNA jumps to #1.
2. **The autonomy-vs-size wall** — a self-powered unit harvests energy through its surface (∝ L²), while a functional node's power draw does not shrink, so onboard autonomy can't fit below ~1 mm. The combination utility fog needs — *autonomous **and** tiny **and** vast* — is walled off by physics, not just immature engineering.

## Contents

### Articles
- **`programmable-matter-utility-fog-medium-article-positive-2026-07-15.md`** — the main article: an accessible narrative (Part I) plus a technical deep-dive (Part II), with three figures.
- **`programmable-matter-utility-fog-medium-article-2026-07-15.md`** — an alternate, more analytical framing of the same findings.

### Figures (`article-figures/`)
- `fig1-scoreboard.svg` — the seven-technology scoreboard.
- `fig2-autonomy-vs-size-wall.svg` — the autonomy-vs-size map (the empty "foglet corner").
- `fig3-power-scaling.svg` — harvested power vs unit size (the L² wall), from Part F.

### Scripts (`scripts/`)
- `power_scaling_wall.py` — the L² power-vs-size scaling + crossover calculation behind Part F (run: `python power_scaling_wall.py`).
- `make_fig3_power_scaling.py` — regenerates `article-figures/fig3-power-scaling.svg` from that calculation.

### Research (`research/`)
The per-technology scored deep-dives that ground the ranking — a master falsification scorecard plus one memo per branch (acoustic/field assembly, macroscale modular robots, field micro-robots, 4D printing, and DNA nanotech with design-automation, immunogenicity, and manufacturing sub-digs). Each memo lists its primary sources.

## Method & honesty note

Scores are the author's analyst judgments on a deliberately utility-fog-faithful rubric; the weights are adjustable and the ranking flips with the target application — that dependence is finding #1, not a bug. The Part F power-scaling figures are an order-of-magnitude illustration built on the primary ∝ L² surface-power relationship (*Science Robotics* 2024); the ~100 nW electronics floor is the Cornell/Michigan sub-millimeter robot. Every per-technology number is anchored to a primary source listed inline in the article.

## License

- Code (`scripts/`): MIT.
- Prose & figures (articles, `article-figures/`, `research/`): © 2026 Farshad, released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
