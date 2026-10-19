# Consolidating sim Results 16-18 into the ledger: ask S47 (for aim_is_all_you_need)

Raised 2026-10-19 in `Balloon-Pulse-Propulsion`. Answers in, and follow-up to, aim `efe6121`
(ADR 0076, `docs/spring_plates_and_fast_law_for_parent.md`) and the impact simulation's
`1bed1c6` (Results 16-17) and `9bcc8be` (Result 18).

## What the paper did

ADR 0076's addendum checked Results 16-17 but not Result 18, which landed after it. Result 18
computes the push plate's backward plume and finds that **Kapton as wide as the plate holds
through 137 km/s**. Seth's call (2026-10-19): Kapton is fine, with a carbon veil as the backup;
the sheet is as wide as the plate; the springs are nitrogen.

The paper now prints a **paper-side rerun** of ADR 0076's ledger with three overrides (script
below), reproducing ADR 0076's own headlines exactly first (3.38x / $144; 5.31x / $91):

| closure | ADR 0076 | + Kapton to 140 | + nitrogen bags | + 2.5 F bowl < 122 deg (printed) |
|---|---|---|---|---|
| 9.86 R_sun, 60 | 3.38x, $93 / $144 | same | 3.36x, $94 / $146 | **3.36x, 1.87 yr, $94, $124 / $146** |
| 4 R_sun, 90 | 5.31x, $77 / $91 | 5.32x, $72 / $84 | 5.28x, $73 / $85 | **4.99x, 1.41 yr, $74, $84 / $87** |

Also rerun on the same overrides: the depth sweep, the fast-return rows, the 3/5/10-day gaps, the
sensitivities, the seed table (566 / 672 t; 3.7-4.2 / 4.8-5.6 ships; fleet x82 / x426; seed
$30-113 / $7-25 per fleet kg) and `make plate-jupiter-loop` (best 1.65x / $1881 dear at 0.5 g).
The paper labels all of them "our rerun of" ADR 0076.

## S47. Wanted

1. **Adopt Result 18's sheet rule.** Kapton up to 140 km/s on a floor-wide sheet (maraging-300
   face), carbon fabric above; retire the 100-130 km/s band switch. Result 18's `plume_sheet.csv`
   has the per-closure floor and ceiling.
2. **Nitrogen bags.** gamma 1.4, R 296.8 J/(kg K), plus the bladder. We scaled the bladder as
   1.3/2.9 of the gas mass (the sim's whole-floor 52 kPa row); use the sim's
   `gas_spring_design.csv` if you prefer a pressure choice. That gives 5.5 t per Earth plate.
3. **The 2.5 F bowl where the bare impactor would hit the rim** (theta < 122 deg, i.e. 4 R_sun at
   117 deg). We multiplied `hole_ve` by 0.909 / 0.912 / 0.922 at k 10 / 20 / 30 (log-interpolated)
   from `band_far_bowl.csv`. A proper capture table at 2.5 F is better.
4. **The theta = pi row** with nitrogen: we get +$4 / +$1 dear. The paper flies 2 pi/3 and prints
   theta = pi as the fix for the 18.6 m gas column (Seth).
5. **9.86 R_sun, 60 vs 75 km/s.** On these overrides 75 is $1 cheaper ($145 vs $146) at equal
   growth. The paper keeps 60 and calls it a tie. Confirm or say which the code should headline.
6. **The Jupiter-only loop's steady column.** At 0.5 g the steady cost ($1474) exceeds both
   break-evens ($761 / $1881), and at 0.25 g there are no steady deliveries. Is that a definition
   effect (the `C_g/(G-1)` reinvestment near G = 1, against a valuation that harvests early) or a
   bug? The paper prints the figures as they come.
7. **The Moon and the push.** ADR 0076 found roughly a ninth of lunar phases put the Moon near the
   ship's path to apoapsis. The paper now says the push must be timed against the Moon and that
   the schedule is unsolved. A launch-window rule (which phases are allowed, what it costs the
   cadence) would close it.

## The override script (paper side, scratch)

Run from an aim checkout at `efe6121` with its `.venv`:
`AIM=$PWD CONSOLIDATE=kapton137,nitrogen,bowl25 .venv/bin/python -I consolidate.py --sweep --gaps`.

```python
"""Paper-side rerun of aim's ADR 0076 ledger with the sim's Results 16-18 folded in.

Switches (env CONSOLIDATE, comma-separated):
  kapton137  Result 18: floor-wide Kapton holds through 137.1 km/s, so the
             Kapton/carbon cutoff (price and overtake-law impactor) moves 130 -> 140.
  nitrogen   Result 17: nitrogen bags (gamma 1.4, R 296.8) plus a bladder at
             1.3/2.9 of the gas mass (the sim's whole-floor 1.3 t on 2.9 t).
  bowl25     Result 16: the charge at 2.5 F below 122 deg, v_e x(0.909-0.922 by k).
Then runs src.solar_dive_growth.main with the remaining argv.
"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.environ["AIM"])
import src.solar_dive_growth as g  # noqa: E402

flags = set(filter(None, os.environ.get("CONSOLIDATE", "").split(",")))

if "kapton137" in flags:
    g.KAPTON_FAILS = 140.0

if "nitrogen" in flags:
    g.HELIUM_GAMMA = 1.4
    g.HELIUM_GAS_CONSTANT = 296.8
    _orig_bag = g.bag_mass

    def bag_mass(pv, theta, fittings=0.0):
        gas = pv / (g.HELIUM_GAS_CONSTANT * g.BAG_TEMPERATURE)
        return _orig_bag(pv, theta, fittings) + gas * (1.3 / 2.9)

    g.bag_mass = bag_mass

if "bowl25" in flags:
    _orig_hole = g.SolarDiveLaw.hole_ve if hasattr(g, "SolarDiveLaw") else None
    cls = next(
        c for c in vars(g).values() if isinstance(c, type) and "hole_ve" in vars(c)
    )
    _orig_hole = cls.hole_ve

    def hole_ve(self, k, w, theta_deg):
        ve = _orig_hole(self, k, w, theta_deg)
        if theta_deg < 122.0:
            # sim Result 16 band_far_bowl at 117 deg: k 10/20/30 -> 0.909/0.912/0.922
            ve *= float(np.interp(math.log(k), np.log([10, 20, 30]), [0.909, 0.912, 0.922]))
        return ve

    cls.hole_ve = hole_ve

print(f"# consolidate flags: {sorted(flags)}", flush=True)
g.main(sys.argv[1:])
```
