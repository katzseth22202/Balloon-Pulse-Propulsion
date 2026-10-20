# An errant departure impactor on the bowl: ask S49 (for puffsat_impact_simulation)

Raised 2026-10-20 in `Balloon-Pulse-Propulsion`. **Written to be copied into
`puffsat_impact_simulation`.** Extends Result 14's bare-impactor case
(`docs/departure_hole_answers_for_parent.md` section 4) from a missing charge to a missed aim.

## The goal (Seth, 2026-10-20)

Survival is not the goal. A bad hit aborts the departure. The goal is that **the ship does not
become a cloud of solid debris**. Vapor and droplets are acceptable. Solid fragments are not,
because the departure starts at the 600 km periapsis of the 10-day orbit, 96 m/s short of escape.
Fragments made early in the burn stay on orbits whose perigee is in LEO.

## The geometry

The departure stream meets the ship at 130 deg to its thrust axis (117 deg at 4 R_sun), from the
ship's side of the bowl. Each graphite disk (~9 kg, ~8 mm, ~15 kg/m^2, at 84 / 108 km/s; 32-52 GJ)
threads the ~1 m hole near the vertex and strikes the charge at the focus. **The bags and spring
frame sit behind the bowl, off the approach line** (Seth). A disk that misses the hole therefore
strikes the bowl's convex back face from the ship's side.

Result 14 ran the nearest case, a bare disk on the far wall at 117 deg. The patch vaporizes
(386 MJ/kg, 55x iron), no spall, a hole of about the disk's 0.89 m^2 footprint, and the vapor
leaves along the stream at ~91 km/s. That wall was 3.2 mm of steel. The bowl is now one face of
a shared 63 t sprung assembly (aim ADR 0076), and its wall thickness has not been set.

## S49. Wanted

1. **Punch-through or crater, by wall thickness.** For a disk striking the bowl's back face at the
   flown angles, where along the wall's areal density (say 10-200 kg/m^2) does the hit change from
   a clean perforation, with the cloud leaving forward through the bowl and out its mouth, to a
   crater blast that throws vapor and spall back toward the ship's side? We expect the back face
   must be a deliberate thin, sacrificial layer, as the outer wall of a Whipple shield is. Give the
   thickest wall that still forces a clean punch-through.
2. **Solid fragments.** Around the vaporized patch the steel melts, then fractures. Give the mass
   and size of the solid fragments from the hole's rim, and their **speed distribution and
   directions** relative to the ship. Also give whether any leave toward the ship's side. Same
   for the hole's 1 t collar if the miss is small enough to hit it.
3. **The rest of the assembly.** The kick is ~0.8 MN s on about a square meter, off the plate's
   center. Does the sandwich floor crack, or a petal detach, elsewhere in the 63 t assembly? Does
   the off-center kick on the sprung plate tear the spring's mounts?
4. **The next impactors.** The ship stops deploying charges. Impactors already inside the divert
   window (1 Hz, a few seconds) still aim at the hole and should fly out the mouth bare (Result 14
   geometry). Confirm, and say whether the new hole or a slot sits on any of their lines.

5. **The charge stack as a shield** (added 2026-10-20, Seth). The ship carries ~370 t of departure
   charge. Stacked outboard on the stream's side, between the approach cone and the bags and
   frame, it is a thick sacrificial block, drawn from the inside out. For a disk striking that
   block (polyethylene, or the dark water snow of item 6): the crater's direction (we expect
   ejecta back out along the approach, away from the ship), the recoil on the ship (we guess
   0.8-1.6 MN s), the ejecta's sizes and speeds, and the block depth that keeps the shock off the
   frame behind it.
6. **Water snow as the departure charge** (added 2026-10-20, Seth). The departure charge is spent
   ~10 days after launch, so it need not be polyethylene. Water launched liquid, sprayed in orbit
   into thin, sealed polyethylene balloons where it freezes to snow (bulk density perhaps
   300-600 kg/m^3), darkened (a few % carbon black, or black film). Wanted: its push law in the
   bowl against polyethylene. Water's atomization is ~51 MJ/kg against polyethylene's ~84, so the
   bond toll may fall, and the lower density at the focus may change the capture. Also wanted:
   whether the balloon film matters.

Item 2's speed distribution also prices a proposed mitigation (below), so a histogram is more
useful than a peak value.

**Paper-side estimate behind item 6: dark ice is cleaner debris.** A tumbling 1 cm piece of clean
snow (albedo 0.9) in sunlight at 1 AU runs ~160 K and lasts ~2 years. At albedo 0.5 it lasts
~3 days, and at 0.1 ~1 day, near 190-195 K (sublimation balance, Clausius-Clapeyron vapor pressure;
no Earth shadow or Earth IR). So the darkening is what makes it short-lived.

## The mitigation it feeds (the paper's estimate)

Seth proposes flying the first 200-300 m/s of the departure on the methalox stage, so the ship
is already above escape when the PuffSat pulses start. At the 10-day orbit's periapsis that
leaves an excess of 1.50 / 2.10 km/s. A fragment stays bound only if thrown backward faster
than that margin. For fragments thrown in random directions at a single speed, the bound share
is:

| fragment speed | no pre-burn (hit at burn start) | 200 m/s pre-burn | 300 m/s pre-burn |
|---|---|---|---|
| 100 m/s | 98% | 0% | 0% |
| 300 m/s | 65% | 32% | 16% |
| 1 km/s | 52% | 42% | 38% |

So the pre-burn removes slow fragments entirely and roughly halves the bound share of fast ones.
Without it, only the first ~40 s of the 32-minute burn leaves the ship bound. With it, no part of
the PuffSat burn does, and a dead ship escapes too. The cost is ~34-50 t of net methalox per
launch unit, not yet priced in the ledger.
