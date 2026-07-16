"""KILL-TEST of our own published claim: "onboard autonomy can't fit below ~1 mm because
harvested power scales as surface area (L^2)."

The claim's hidden assumption: demand is held CONSTANT while size shrinks. Biology violates that.
This script computes the supply/demand RATIO vs size for (a) a biological cell whose demand scales
with volume, and (b) an engineered node with a fixed electronics/actuator floor. If biology's ratio
IMPROVES as it shrinks, the claim as published is FALSIFIED and must be restated.

Numbers are primary-sourced (BioNumbers / DeLong 2010 PNAS / Prochlorococcus MMBR 1999 + PLOS One).
Prints labelled numbers; exit 0.
"""
import math

SUN_FULL = 150.0      # W/m^2 usable PV/photosynthetic (15 mW/cm^2, same figure our article used)
PAR_OPT  = 43.6       # W/m^2  Prochlorococcus irradiance optimum (200 umol/m^2/s x 218 kJ/mol)

def cross_section(L):  return math.pi*(L/2)**2       # m^2, spherical unit of diameter L
def volume(L):         return (math.pi/6)*L**3       # m^3

# ---- demand models -------------------------------------------------------------------
CELL_PWR_DENSITY = 1e6      # W/m^3  (E. coli: 1 pW / 1 um^3) -- BioNumbers
def demand_bio(L):   return CELL_PWR_DENSITY*volume(L)          # scales as L^3
FLOOR_ACTIVE = 1e-3         # W, an active engineered node (motor+radio) -- our article's figure
FLOOR_SUBTH  = 100e-9       # W, extreme subthreshold (Miskin-class budget)
def demand_eng(L, floor): return floor                          # FIXED -- does not scale

print("="*78); print("SUPPLY vs DEMAND as a unit shrinks (full sun, 150 W/m^2)"); print("="*78)
print(f"  {'size':>8s} {'supply':>11s} | {'BIO demand':>11s} {'ratio':>9s} | {'ENG(1mW)':>9s} {'ratio':>9s}")
for L,lbl in [(1e-2,"1 cm"),(1e-3,"1 mm"),(1e-4,"100 um"),(1e-5,"10 um"),(1e-6,"1 um"),(6e-7,"0.6 um")]:
    S=SUN_FULL*cross_section(L); Db=demand_bio(L); Re=S/FLOOR_ACTIVE; Rb=S/Db
    def f(p):
        for u,s in [("mW",1e-3),("uW",1e-6),("nW",1e-9),("pW",1e-12),("fW",1e-15)]:
            if p>=s: return f"{p/s:6.2f} {u}"
        return f"{p:.1e} W"
    def r(v): return f"{v:8.3f}x" if v < 10 else f"{v:8.0f}x"
    star = "  <-- demand EXCEEDS supply (why BIG cells can't be sunlight-autonomous)" if Rb < 1 else ""
    print(f"  {lbl:>8s} {f(S):>11s} | {f(Db):>11s} {r(Rb)} | {f(FLOOR_ACTIVE):>9s} {r(Re)}{star}")

print("\n"+"="*78); print("THE DECISIVE ASYMMETRY"); print("="*78)
print("  supply ~ L^2 ; BIO demand ~ L^3  =>  supply/demand ~ 1/L  -> IMPROVES without bound as L falls")
print("  supply ~ L^2 ; ENG demand ~ const =>  supply/demand ~ L^2 -> COLLAPSES as L falls")
print("  => The L^2 law is NOT a small-scale barrier. It is a small-scale ADVANTAGE for anything")
print("     whose demand scales with its volume. Our published claim had the argument backwards.\n")

print("="*78); print("THE EXISTENCE PROOF: Prochlorococcus (0.6 um, obligate photoautotroph)"); print("="*78)
L=6e-7; S_opt=PAR_OPT*cross_section(L); S_sun=SUN_FULL*cross_section(L)
D_measured=1e-13   # ~0.1 pW banked (8.8 fg C/cell/hr x 39 kJ/g)
print(f"  intercepts at its OWN light optimum : {S_opt*1e12:6.2f} pW")
print(f"  intercepts at full sun              : {S_sun*1e12:6.2f} pW")
print(f"  measured power banked               : {D_measured*1e12:6.2f} pW")
print(f"  -> margin {S_opt/D_measured:.0f}x at optimum, {S_sun/D_measured:.0f}x at full sun (implies ~1% photosynthetic")
print( "     efficiency -- exactly the textbook 1-2% range, so the numbers close self-consistently).")
print(f"  This unit is {1e-3/L:.0f}x SMALLER (linear) than our claimed 1 mm 'wall' -- and it is the most")
print( "  abundant photosynthetic organism on Earth. The claim is not marginally wrong; it is inverted.\n")

print("="*78); print("SO WHERE IS THE REAL WALL? (what we actually measured)"); print("="*78)
ecoli=1e-12; phoenix_active=230e-9; phoenix_sleep=30e-12
print(f"  E. coli whole cell (1 um^3, ~1e7 ATP/s) : {ecoli*1e12:8.3f} pW")
print(f"  best CMOS MCU, ACTIVE (Phoenix 0.18um)  : {phoenix_active*1e12:8.0f} pW  = {phoenix_active/ecoli:8.0f}x a whole cell")
print(f"  best CMOS MCU, SLEEP (leakage floor)    : {phoenix_sleep*1e12:8.1f} pW  = {phoenix_sleep/ecoli:8.1f}x a whole cell")
print("  ATP hydrolysis      ~8.3e-20 J/op = ~20 kT  ~= a single CMOS transistor switch (parity!)")
print("  CMOS per INSTRUCTION ~2.8e-12 J/op        ~= 1e9 x Landauer, ~1e7 x one ATP")
print("  Miskin robot budget: actuators dominate -- SEA transduction ~1e-4, PV->SEA coupling ~1%.")
print("\n  => The real wall is NOT power SUPPLY vs size. It is that our DEMAND does not shrink:")
print("     (1) CMOS spends ~1e7 ATP-equivalents per useful instruction (thousands of switches +")
print("         wire capacitance), where a molecular machine spends ONE chemical event; and")
print("     (2) engineered actuators transduce at ~1e-4, where F1-ATPase runs near 100%.")
print("     Biology doesn't beat the L^2 law -- it makes its demand fall faster than its supply.")
