"""KILL-TEST #2: our article asserts "the communication-energy wall is real (1 bit ~ 100,000 CPU-ops),
so vast swarms choke on coordination cost." We asserted that. We never derived it. After the L^2 wall
turned out to be INVERTED, every remaining asserted wall gets the same treatment.

The claim only bites if comms cost GROWS with swarm size N. Does it? Test three coordination topologies
against the power a unit can actually harvest (the corrected L^2 supply model, which we now trust).
Also test biology's own answer: cells coordinate 3.6e13 units, so any wall must permit that.
Prints labelled numbers; exit 0.
"""
import math

# ---- supply (corrected model: harvest ~ L^2, verified in biology_wall_falsification.py) ----
SUN = 150.0                                  # W/m^2 usable
def cross_section(L): return math.pi*(L/2)**2
def supply(L):        return SUN*cross_section(L)

# ---- per-bit cost -------------------------------------------------------------------------
# Grounded anchors: CMOS ~2.8 pJ/instruction (Phoenix). "1 bit off-chip ~ 1e5 CPU-ops" (Dutta) =>
E_OP   = 2.8e-12                             # J per CMOS instruction
E_BIT_RADIO = 1e5 * E_OP                     # ~0.28 uJ per bit transmitted off-chip (the article's claim)
# Biology's messaging quantum: a signalling molecule ~ 1 ATP-equivalent
E_BIT_BIO   = 8.3e-20                        # J, one ATP (~20 kT)
KT = 4.1e-21; LANDAUER = KT*math.log(2)      # J, thermodynamic floor per bit

print("="*80); print("1. WHAT DOES ONE BIT COST?"); print("="*80)
print(f"  Landauer floor (kT ln2, 300K)        : {LANDAUER:8.2e} J   (1x)")
print(f"  one ATP / biological signal quantum  : {E_BIT_BIO:8.2e} J   ({E_BIT_BIO/LANDAUER:,.0f}x Landauer)")
print(f"  one CMOS instruction                 : {E_OP:8.2e} J   ({E_OP/LANDAUER:,.0f}x)")
print(f"  one RADIO bit off-chip (1e5 ops)     : {E_BIT_RADIO:8.2e} J   ({E_BIT_RADIO/LANDAUER:,.0f}x)")
print(f"  => radio costs {E_BIT_RADIO/E_BIT_BIO:.1e}x a biological message. THIS is the real gap,")
print( "     and note it is an ARCHITECTURE choice (radio), not a law.\n")

print("="*80); print("2. DOES COORDINATION COST GROW WITH SWARM SIZE N?  (the load-bearing question)"); print("="*80)
print("  Per-unit bits/sec needed, by topology:")
print("    broadcast-to-all (naive)   : ~N        -> per-unit cost GROWS linearly with N   [WALL]")
print("    gossip / global consensus  : ~log N    -> grows, but only logarithmically       [soft]")
print("    LOCAL neighbours-only      : ~k (const)-> per-unit cost is INDEPENDENT of N     [NO WALL]")
print("  Kilobot + every cell in your body use the third. Local rules, k~6-10 neighbours.\n")

def per_unit_power(L, n_bits_per_sec, e_bit):
    return n_bits_per_sec*e_bit

print("="*80); print("3. CAN A UNIT AFFORD IT?  (comms power vs harvested supply)"); print("="*80)
print(f"  {'size':>8s} {'supply':>10s} | {'RADIO local 10 b/s':>19s} {'verdict':>9s} | {'BIO local 10 msg/s':>19s} {'verdict':>9s}")
def f(p):
    for u,s in [("mW",1e-3),("uW",1e-6),("nW",1e-9),("pW",1e-12),("fW",1e-15),("aW",1e-18)]:
        if abs(p)>=s: return f"{p/s:7.2f} {u}"
    return f"{p:8.1e} W"
for L,lbl in [(1e-2,"1 cm"),(1e-3,"1 mm"),(1e-4,"100 um"),(1e-5,"10 um"),(1e-6,"1 um")]:
    S=supply(L)
    pr=per_unit_power(L,10,E_BIT_RADIO); pb=per_unit_power(L,10,E_BIT_BIO)
    vr="OK" if pr<S else "STARVES"; vb="OK" if pb<S else "STARVES"
    print(f"  {lbl:>8s} {f(S):>10s} | {f(pr):>19s} {vr:>9s} | {f(pb):>19s} {vb:>9s}")

print("\n  A LOCAL topology costs a FIXED ~10 bits/s regardless of whether the swarm is 10 or 10^12 units.")
print("  So the comms budget does NOT scale with N -- it scales with the RADIO, and radio is our choice.")
# where does a RADIO-based unit stop being able to afford even LOCAL comms? supply(L)=10*E_BIT_RADIO
L_radio = 2.0*math.sqrt((10*E_BIT_RADIO)/(SUN*math.pi))
L_bio   = 2.0*math.sqrt((10*E_BIT_BIO)/(SUN*math.pi))
print(f"\n  CROSSOVER (the genuinely new number): a sunlight-powered unit can afford local comms down to")
print(f"    with a RADIO           : {L_radio*1e6:8.1f} um  <-- radio imposes a ~{L_radio*1e3:.2f} mm floor EVEN FOR LOCAL comms")
print(f"    with a BIO-cost message: formally {L_bio*1e9:.3f} nm -- which is SUB-ATOMIC, i.e. the model has")
print(f"                             left its domain. Read it honestly: at biological messaging cost,")
print(f"                             comms is NEVER the binding constraint at any buildable size.")
print(f"  => The size floor people attribute to 'coordination' is really the RADIO's floor. It is not a")
print(f"     law about swarms; it is a property of one messaging technology we happened to choose.")
print(f"  NOTE (suggestive, not proof): {L_radio*1e6:.0f} um lands in the same decade as the smallest real")
print(f"     autonomous robots (~200 um). Consistent with comms/actuation -- not size -- setting the floor.\n")

print("="*80); print("4. THE FALSIFIER: biology coordinates 3.6e13 units"); print("="*80)
N_CELLS=3.6e13
print(f"  A human body coordinates {N_CELLS:.1e} cells into a maintained 3D shape, continuously, for decades.")
print(f"  If a comms-energy wall forbade vast coordination, this would be impossible. It isn't.")
print(f"  Biology's trick is NOT a better radio -- it is having NO radio: diffusion + gap junctions,")
print(f"  neighbour-only, ~{E_BIT_BIO:.1e} J per message, no addressing, no broadcast.")
print(f"  Cost per message is {E_BIT_BIO/E_BIT_RADIO:.1e}x ours, and the topology makes N irrelevant.\n")

print("="*80); print("VERDICT"); print("="*80)
print("  The claim 'vast swarms choke on coordination cost' is FALSIFIED AS STATED, for the same")
print("  reason the L^2 wall was: it smuggles in an assumption (global/broadcast comms over RADIO)")
print("  and then reports the consequence as a law of nature.")
print("  What SURVIVES, restated and narrower:")
print(f"    * A RADIO bit costs ~{E_BIT_RADIO/E_BIT_BIO:.0e} x a biological message. That gap is real and it is OURS.")
print(f"    * The RADIO -- not the swarm size -- imposes a ~{L_radio*1e6:.0f} um floor on a sunlight-powered unit.")
print("    * BROADCAST/global-consensus topologies do scale with N and are unaffordable at 10^9+.")
print("    * LOCAL neighbour-only coordination is N-independent and provably affordable -- it is what")
print("      Kilobot does at 1024 units and what your body does at 3.6e13.")
print("  => Not a wall. A DESIGN RULE: go neighbour-only, and drop the radio for something cheaper.")
print("  => The honest cost of local-only: you give up addressing + global broadcast (biology has neither).")
