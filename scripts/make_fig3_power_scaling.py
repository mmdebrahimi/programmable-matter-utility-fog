"""Emit article-figures/fig3-power-scaling.svg — the L^2 autonomy-vs-size wall as a log-log chart.

Visualizes Part F: harvested power (sunlight, ~15 mW/cm^2 PV, scales as L^2) vs unit size, crossing
below three functional-power floors. Marks the crossover sizes + the real Kilobot and Miskin datapoints.
Coordinate math done in code (verified), SVG emitted as a pure string (no deps). Prints crossover check.
"""
import math

# ---- data (matches scripts/power_scaling_wall.py) ----
SUN = 15e-3  # W per cm^2 at 1 cm reference
def P(size_m):  # harvested power (W) at a given unit size, P ~ area ~ L^2
    L_cm = size_m*100.0
    return SUN*(L_cm/1.0)**2
harvest = [1e-2,1e-3,1e-4,1e-5,1e-6]                      # sizes (m): 1cm..1um
floors = [("active node ~1 mW",1e-3),("low-power ~10 uW",1e-5),("subthreshold ~100 nW",1e-7)]
def crossover_m(floor): return math.sqrt(floor/SUN)/100.0  # size (m) where P==floor

# ---- log-log coordinate transforms ----
XL,XR = 120,690     # 1cm .. 1um  (exponent -2 .. -6 in metres)
YT,YB = 70,430      # 1e-1 .. 1e-10 W
def x(size_m):
    e=math.log10(size_m); return XL+(XR-XL)*((-2)-e)/4.0
def y(P_W):
    pe=math.log10(P_W);   return YT+(YB-YT)*((-1)-pe)/9.0

def esc(s): return s
out=[]
out.append('<svg xmlns="http://www.w3.org/2000/svg" width="760" height="490" viewBox="0 0 760 490" font-family="Helvetica,Arial,sans-serif">')
out.append('<rect width="760" height="490" fill="#ffffff"/>')
out.append('<text x="30" y="34" font-size="22" font-weight="700" fill="#111">Why autonomy dies below a millimetre</text>')
out.append('<text x="30" y="55" font-size="13" fill="#666">Harvested power scales as size² (L²); the power a working node needs does not. Where the line drops below a floor, self-power fails.</text>')
# axes
out.append(f'<line x1="{XL}" y1="{YT}" x2="{XL}" y2="{YB}" stroke="#333" stroke-width="1.5"/>')
out.append(f'<line x1="{XL}" y1="{YB}" x2="{XR}" y2="{YB}" stroke="#333" stroke-width="1.5"/>')
# x ticks
for lbl,s in [("1 cm",1e-2),("1 mm",1e-3),("100 µm",1e-4),("10 µm",1e-5),("1 µm",1e-6)]:
    xx=x(s); out.append(f'<line x1="{xx:.1f}" y1="{YT}" x2="{xx:.1f}" y2="{YB}" stroke="#eee"/>')
    out.append(f'<text x="{xx:.1f}" y="{YB+16}" font-size="11" fill="#555" text-anchor="middle">{lbl}</text>')
out.append(f'<text x="{(XL+XR)/2:.0f}" y="{YB+34}" font-size="12" fill="#333" text-anchor="middle">unit size (smaller &#8594;)</text>')
# y ticks (every 3 decades)
for pe in [-1,-4,-7,-10]:
    yy=y(10**pe); lab={-1:"100 mW",-4:"100 µW",-7:"100 nW",-10:"100 pW"}[pe]
    out.append(f'<line x1="{XL}" y1="{yy:.1f}" x2="{XR}" y2="{yy:.1f}" stroke="#f2f2f2"/>')
    out.append(f'<text x="{XL-8}" y="{yy+4:.1f}" font-size="11" fill="#555" text-anchor="end">{lab}</text>')
out.append(f'<text x="34" y="{(YT+YB)/2:.0f}" font-size="12" fill="#333" text-anchor="middle" transform="rotate(-90 34 {(YT+YB)/2:.0f})">harvested power (sunlight)</text>')
# floor lines
fc=["#e34a33","#fb8d3d","#3182bd"]
for (lbl,fl),c in zip(floors,fc):
    yy=y(fl); out.append(f'<line x1="{XL}" y1="{yy:.1f}" x2="{XR}" y2="{yy:.1f}" stroke="{c}" stroke-width="1.4" stroke-dasharray="6 4"/>')
    out.append(f'<text x="{XR-4}" y="{yy-5:.1f}" font-size="11" fill="{c}" text-anchor="end">{lbl}</text>')
# harvest polyline
pts=" ".join(f"{x(s):.1f},{y(P(s)):.1f}" for s in harvest)
out.append(f'<polyline points="{pts}" fill="none" stroke="#111" stroke-width="2.5"/>')
out.append(f'<text x="{x(1e-2)+6:.1f}" y="{y(P(1e-2))-8:.1f}" font-size="12" font-weight="700" fill="#111">P &#8733; L²</text>')
# crossover markers (where harvest meets each floor)
for (lbl,fl),c in zip(floors,fc):
    cm=crossover_m(fl); xx=x(cm); yy=y(fl)
    out.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="4.5" fill="{c}"/>')
    mm=cm*1000
    out.append(f'<text x="{xx:.1f}" y="{yy+18:.1f}" font-size="10" fill="{c}" text-anchor="middle">{mm:.2g} mm</text>')
# real datapoints
for lbl,s,note in [("Kilobot",1e-2,"3.3 cm · fully autonomous ✓"),("Miskin robot",2e-4,"~200 µm · autonomous only via subthreshold + bright light")]:
    xx=x(s); yy=y(P(s))
    out.append(f'<circle cx="{xx:.1f}" cy="{yy:.1f}" r="6" fill="none" stroke="#111" stroke-width="2"/>')
    out.append(f'<text x="{xx:.1f}" y="{yy-12:.1f}" font-size="11" font-weight="700" fill="#111" text-anchor="middle">{lbl}</text>')
out.append(f'<text x="{XL}" y="475" font-size="10.5" fill="#999">Order-of-magnitude illustration (sunlight PV). The L² relation is from Science Robotics 2024; the ~100 nW floor is the Miskin robot.</text>')
out.append('</svg>')
svg="\n".join(out)+"\n"
open("article-figures/fig3-power-scaling.svg","w",encoding="utf-8").write(svg)

# ---- verify-in-batch: print crossovers + datapoint headroom ----
print("crossovers (size where harvest == floor):")
for lbl,fl in floors: print(f"  {lbl:22s} {crossover_m(fl)*1000:8.3f} mm")
print("datapoint power vs floors:")
for lbl,s in [("Kilobot 1cm",1e-2),("Miskin 200um",2e-4)]:
    p=P(s); print(f"  {lbl:14s} harvests {p*1e6:9.2f} uW  -> {'ABOVE' if p>1e-7 else 'below'} 100nW floor")
print("SVG written:", len(svg), "bytes")
