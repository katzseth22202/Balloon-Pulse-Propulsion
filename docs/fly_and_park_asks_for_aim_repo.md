# Fly-and-park deliverables owed by `aim_is_all_you_need`

Raised 2026-09-08, grilling `docs/paper_corrections_fly_and_park_2026-09-07.md` (ADR 0030,
`src/fly_and_park.py`) against `sec:jupiter_only_growth`. **Written to be copied verbatim
into `katzseth22202/aim_is_all_you_need`**, so it repeats context the paper repo already has.

These are items **S5-S8** of the paper repo's register, `docs/deferred_to_companion_repos.md`,
which keeps a summary table and points here for the full text. Backing decision:
`docs/adr/0015-2s-and-3s-are-operating-points-not-a-succession.md`.

**Nothing has been written into `templateArxiv.tex`.** Three of the four asks are holds: the
paper does not quote the number until the ask lands. Reply in `docs/paper_changes_owed.md`
as usual.

Same ground rules as your own handbacks: **neither document is the source of truth**; if a
number here looks wrong, say so rather than working around it.

---

## What the paper accepted without change

The 3S fly-and-park result, as published. Arrival `v_b` **68.7 km/s against 61.3**, flight
2.735 S, park 0.265 S, departure burn 6.74 against 5.56, the park costing 0.2% of mass ratio.
The **exchange rate** and its verdict, that methalox misses by ~5% and any impactor-driven
departure clears. The **usable-phase fractions**, 18% at Isp 380 to 100% at 1900. Your N4 in
full, including that the higher exhaust speed does not buy a shorter clock.

C1 turned out **not to be owed**. The paper never quotes x74.8, x90.2 or a ninth cycle. Note
one hazard if you sweep for it: the paper does contain the phrase *"a second steering knob"*,
at a different referent. It is about **real ephemerides** letting the transfer choose when it
meets Jupiter, and it is correct. Do not let a grep retire it.

---

## Vocabulary the paper has settled, because "2S" was overloaded

Recorded in the paper's `CONTEXT.md`. Three senses of "2S" now live in that document and they
do not interchange:

1. **Three-synodic closure (3S)**, the *Jovian solar dive*'s bend feasibility. 2S there is
   short 6.84 degrees and does not close unpowered at any perijove burn.
2. **2S vs 3S cadence**, the *Jupiter-only chain*'s return policy. Both routine; the flown
   11-cycle chain takes seven 2S returns and four 3S.
3. **Synodic lock**, new: flight plus park summing to an exact whole number of synodic
   periods, so the cycle returns to its own departure phase and repeats unsteered. The
   operating points are the **2S lock** and the **3S lock**.

**Fly-and-park** stays your name for the mechanism. **Synodic lock** names the property it
buys. Your T1 terms (**departure phase**, **sweet phase**, **usable phase**) are adopted
verbatim.

---

## S5. Implement, test and chain-check the 2.00 S synodic lock

**The claim.** Your N4 calls a repeatable 2S cycle the largest open question this analysis
raised, and reports that the chain search never sustains one. The mechanism for the failure is
already in your CONTEXT.md seam entry: the good short cycles land at **2.09 S**, which does
not return to its own departure phase, so each one hands its successor a worse phase.
**Fly-and-park is exactly the tool that removes that drift.** Pad a sub-2.00 S flight up to
exactly 2.00 S and the cycle is a phase fixed point by construction, in the same sense your
3.00 S padding already is.

**What was found, using your module unchanged.** One exists at departure phase **0.781**:

| | flight | park | `dv` | `v_b` | growth, Isp 2214 |
| --- | ---: | ---: | ---: | ---: | ---: |
| **2.00 S lock** | 1.978 S (2.16 yr) | 0.022 S (**9 d**) | 7.25 km/s | 63.2 km/s | 6.021 |
| 3.00 S lock | 2.735 S | 0.265 S (104 d) | 6.74 km/s | 68.7 km/s | 6.754 |

The 2S growth reproduces **your own quoted 6.021** to three digits, and the harness reproduces
your published 3S row exactly, which is the check that it agrees with your device before
anything new is read off it.

| padded to | doubling, Isp 1200 | doubling, Isp 2214 | phases offering one, Isp 2214 |
| --- | ---: | ---: | ---: |
| 2.00 S | **1.00 yr** | **0.84 yr** | 28 of 73 |
| 3.00 S | 1.38 yr | 1.19 yr | 73 of 73 |

**What is wanted.** The construction implemented in `src/fly_and_park.py` behind a target-synodic
argument rather than a hard-coded 3.00, pinned by tests, and **run through the chain search**.
The fixed-point argument says the successor is the same cycle, but your own N4.2 records a
single-cycle optimum that did not survive the chain lookahead, so it needs running rather than
arguing.

**Also unresolved, and the paper cannot read it off the model.** The lock needs a **9-day**
park, which is *shorter* than the 20-day `PUFFSAT_CYCLE_ORBIT_PERIOD`, where 3S fly-and-park
lengthens that coast to ~104 days. Is a 9-day coast admissible? If it is not, does a longer
sub-2.00 S flight exist that leaves a 20-day remainder?

**Harness.** Drop-in, no physics added:

```python
import math
from src.fly_and_park import (
    enumerate_phase_grid, exhaust_speed_from_isp, _EARTH_JUPITER_SYNODIC_YEARS as SYN,
)
from src.jovian_flyby import puffsat_cycle_periapsis_speed
from src.astro_constants import PUFFSAT_CYCLE_ORBIT_PERIOD

grid = enumerate_phase_grid()
v_rf = float(puffsat_cycle_periapsis_speed(PUFFSAT_CYCLE_ORBIT_PERIOD).to_value("km/s"))

for isp in (1200, 2214):
    ve = exhaust_speed_from_isp(isp)
    for target in (2.0, 3.0):
        best, n = None, 0
        for phase, cycles in grid.items():
            ok = [c for c in cycles
                  if c.flight_synodics <= target and c.growth(ve, v_rf) > 1.0]
            if ok:
                n += 1
                b = max(ok, key=lambda c: c.growth(ve, v_rf))
                if best is None or b.growth(ve, v_rf) > best.growth(ve, v_rf):
                    best = b
        g = best.growth(ve, v_rf)
        rate = math.log(g) / (target * SYN)
        print(f"Isp {isp} pad->{target:.2f}S: {n}/{len(grid)} phases, g={g:.3f}, "
              f"doubling {math.log(2)/rate:.3f} yr, flight {best.flight_synodics:.3f} S, "
              f"dv {best.departure_burn:.2f}, v_b {best.collision_speed:.1f}")
```

---

## S6. Emit one doubling ladder, with the scorer named on every rung

**Why.** `sec:jupiter_only_growth` already publishes 4.0 yr on chemical, 3.0 yr with the
head-on catch, and **1.74 yr at `f` = 0.6 / 1.45 yr at `f` = 0.8**. The figures above land at
**1.19 yr** (3S) and **0.84 yr** (2S) at that same `f` = 0.8. These are not the same quantity.
Yours is a single padded cycle at its best phase scored as `M(v_b)*exp(-dv/v_e)`; the paper's
is an eleven-cycle ephemeris chain that includes the expensive cycles it is forced to fly.
Dropped in unlabelled, one subsection would carry four doubling times that appear to disagree
at matched `f`, and no reader can be expected to infer why.

**What is wanted.** One table. Every rung tagged with its scorer, its model (ephemeris chain
against circular phased chain), and whether it is a chain result or a single-cycle result.

**What would settle it.** Whether 1.19 yr is a refinement of 1.45 yr or a different measurement
of a different thing. The paper needs to know which sentence it is writing.

---

## S7. Absorb the launch-window layout, which the fractions do not show

**Why.** You publish the usable-phase *fraction* by Isp and a day-offset table at Isp 380 and
2214 only. Neither says whether the usable phases form one window or several, and the paper's
launch-cadence sentence has to say which.

**What was found.** One **contiguous arc** at every exhaust speed tested, widening about the
sweet phase. Cyclic run-length over the same 73-phase grid:

| Isp (s) | 380 | 700 | 1000 | **1200** | 1500 | 1800 | **1900** |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| usable phases | 13/73 | 26/73 | 36/73 | **44/73** | 56/73 | 69/73 | **73/73** |
| widest window (d of 399) | **71** | 142 | 197 | **241** | 306 | 377 | **399** |
| separate windows | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

The Isp 1800 row wraps through phase 0, which the run-length has to treat cyclically or it
reports two windows. Your finer -36/+24 day read at methalox agrees with the 71 days here to
within one grid cell.

So the paper's claim becomes "**one window, 3.4x wider** at Isp 1200" rather than "a set of
windows", which is both simpler and the stronger operational statement.

**What is wanted.** The layout computed inside `fly_and_park.py` and pinned, so the paper cites
`make fly-park` rather than a scratch script.

---

## S8. Say whether the 2S lock is a cycle the paper already flies

**Why.** The paper's **2S vs 3S cadence** table carries 2-synodic departure burns of
**6.84-7.17 km/s** and growth-wave `v_b` of **61.83-65.13 km/s**. The 2.00 S lock sits at `dv`
**7.25** and `v_b` **63.2**: inside one range, just outside the other. If it is a padded member
of that family, the paper's claim becomes "**lock a cycle we already fly**", which is markedly
easier to defend than "fly a new one".

**The caution.** Different models. `sep-split`'s ephemeris chain against the circular phased
chain, so the resemblance may be coincidence. That is why it needs checking rather than
asserting in either direction.

**What would settle it.** Whether any 2-synodic cycle in the cadence run pads to an exact
2.00 S total and holds its departure phase.

---

## How the paper will frame the answer, whatever it is

Recorded as the paper's ADR 0015, so you know what the numbers are being asked to support.
**2S and 3S are two operating points, not a succession.** 2S doubles about 1.4x faster and buys
it by giving back the launch window, and the asymmetry is sharp: 2S at Isp 2214 covers 28 of 73
phases, narrower than 3S manages at Isp 1200's 44 of 73. The paper will state that trade
wherever it states either lock, rather than quoting the faster clock and letting the window
argument quietly lapse. If S5 kills the 2S lock in the chain, the trade is what explains why it
was considered.
