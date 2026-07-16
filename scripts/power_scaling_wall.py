"""Illustrative L^2 power-scaling calc for the article's 'autonomy-vs-size wall' section.

Grounded claim (Sci Robotics 2024, adu6007): a self-powered unit HARVESTS power through its SURFACE,
so harvested power P ~ L^2. A functional node's minimum power draw (MCU + duty-cycled radio + actuation)
does NOT shrink with L. So as L falls, harvested power crosses BELOW the functional floor at some size.
This script computes where, for indoor vs sunlight harvesting against three real device floors.
Order-of-magnitude ILLUSTRATION (not an exact law); the L^2 relation + the ~100 nW Miskin floor are sourced.
"""
# harvest surface power density (W per cm^2 of unit cross-section)
SUN   = 15e-3   # ~100 mW/cm^2 sunlight * ~15% PV efficiency
INDOOR= 50e-6   # ~50 uW/cm^2 typical indoor PV
L0_cm = 1.0     # reference size 1 cm -> area 1 cm^2

sizes = [("1 cm",1.0),("1 mm",0.1),("100 um",0.01),("10 um",1e-3),("1 um",1e-4)]  # (label, L in cm)
floors = [("active node (motor+radio, ~1 mW)",1e-3),
          ("low-power node (~10 uW)",10e-6),
          ("extreme-subthreshold (Miskin ~100 nW)",100e-9)]

def fmt(p):
    for unit,scale in [("mW",1e-3),("uW",1e-6),("nW",1e-9),("pW",1e-12)]:
        if p>=scale: return f"{p/scale:6.2f} {unit}"
    return f"{p:.1e} W"

print("="*74); print("HARVESTED POWER vs UNIT SIZE  (P ~ L^2, area = (L/1cm)^2 cm^2)"); print("="*74)
print(f"  {'size':8s} {'area(cm^2)':>11s} {'sunlight':>12s} {'indoor':>12s}")
for lbl,L in sizes:
    a=(L/L0_cm)**2
    print(f"  {lbl:8s} {a:11.2e} {fmt(SUN*a):>12s} {fmt(INDOOR*a):>12s}")

print("\n"+"="*74); print("CROSSOVER: smallest size that still clears each functional floor"); print("="*74)
def crossover(density, floor):
    # P=density*(L/1)^2 >= floor -> L >= sqrt(floor/density) cm
    import math; L=math.sqrt(floor/density); return L*10.0  # cm -> mm
for fl_lbl,fl in floors:
    Ls=crossover(SUN,fl); Li=crossover(INDOOR,fl)
    print(f"  {fl_lbl:42s}  sunlight >= {Ls:8.3f} mm | indoor >= {Li:8.3f} mm")

print("\nFINDINGS:")
print("  - Harvested power falls 100x per 10x shrink (L^2). A ~1 mW ACTIVE node can't self-power below")
print("    ~1 mm even in full sun; indoors the wall is centimeters.")
print("  - Only by driving the functional floor down to ~100 nW (extreme subthreshold, as Miskin's")
print("    ~200 um robot does) can autonomy reach the ~10s-of-um scale -- and only in bright light.")
print("  - This is WHY sub-mm machines externalize power/control (fields): it's not a preference,")
print("    it's the L^2 surface-power wall. Beating it = harvest more, beam power in, or lower the floor.")
