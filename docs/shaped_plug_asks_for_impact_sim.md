# A shaped plug spreads the bag, the bullet is the backup: ask S52 (for puffsat_impact_simulation)

Raised 2026-10-21 in `Balloon-Pulse-Propulsion` (after `29ca461`). **Written to be copied into
`puffsat_impact_simulation`.** It follows your S50 answers (Result 20, ADR-0071, carried here as
`docs/iapetus_bag_plate_answers_from_impact_sim.md` at `1d7cedf`). Nothing here is in the paper
yet.

## Seth's decisions on Result 20 (2026-10-21)

1. **The plug spreads the bag, not the gun.** The charge the bag strikes is shaped so that the bag
   and charge merge into a burst as close to a point as the plug allows. Seth: "the plug itself
   should be shaped to optimally spread the bag."
2. **The bullet is a backup against a miss only.** The gun fires only when the track predicts the
   bag will miss the plug. Seth: "we do need an ice bullet backup in case there is a miss to prevent
   it from destroying the ship." A bag that the gun also fails to spread is carried in the ledger as
   a labelled loss rate, not covered by a third layer.
3. **The bags get their own plate at Earth, the Earth bag plate.** It is a graded delta/D 0.5
   paraboloid with the charge at 2 F, as ADR-0071 recommends. It does not have to share the Kapton
   push's 0.30 bowl. All plates in this scenario are at Earth. At Saturn the water nuclear thermal
   stage does all the propulsion, and nothing at Iapetus catches PuffSats. This nuclear cycle is a
   new scenario, pursued because of NASA's renewed interest in nuclear propulsion. It sits beside
   the paper's existing PuffSat-propelled Iapetus scenario and does not replace it.
4. **Water ice charge** (your ADR-0071 item 1), adopted as is.

We use **plug** here for the ship-held charge the bag strikes (your **Charge**, in the Earth
wave's overtake). The bag arrives from beyond it and the fireball drifts onto the plate. This is
not the head-on chamber's plug.

## Why the plug's shape matters, from your own numbers

Ice, 2 F paraboloid, 51.1 km/s, leverage in kg pushed to 10.916 km/s per kg of bag (frozen-rebound
edge in brackets):

| k | compact column (simulated) | point fireball (the ideal) | bag pre-spread to a 2.5 m disk |
|---|---|---|---|
| 2 | not run | 7.89 (7.11) | not run |
| 4 | **8.12 (7.26)** | 8.42 (7.53) | 8.22 (7.35) |
| 8.5 | 7.20 (6.21) | **8.83 (7.67)** | 8.35 (7.24) |
| 15 | 4.52 (3.87) | 8.37 (7.35) | 7.47 (6.53) |
| 20 | 3.28 (2.72) | 8.06 (7.00) | 6.99 (6.02) |

The compact column loses because at k = 8.5 it is 1.84 m long. The bag ploughs along it and the
fireball forms along a line, and a paraboloid only focuses a point well (`eta_jet` 0.53 against
the point fireball's 0.66). At k = 4 the column is about 0.87 m long, nearer a point, and the gap
to the ideal is only 0.3x. A plug that stops the bag in about the bag's own depth should sit near
the point-fireball column at every k. That is the shape this ask wants sized.

The parent's reading is that the shaped plug pays off two ways. First, leverage at k above about
4, worth up to 1.6x at k = 8.5. Second, **catch radius**, the largest lateral miss of the bag's
centre that still lands the whole bag on the plug. A plug wider than the bag accepts a miss
without the backup. The compact column in the bag's own footprint has a catch radius near zero.

## The squat lens (parent sizing, to check)

The hydrodynamic penetration law (Birkhoff et al. 1948) erodes a projectile over a depth of about
`L sqrt(rho_p / rho_t)`. Water on ice gives `sqrt(1000/917)` = 1.04. So a plug about 0.38 m deep
stops the 0.363 m bag. A cylinder of that depth holding `k x 25 kg` of ice (917 kg/m^3) has radius:

| k | plug mass | radius at 0.38 m deep | catch radius (plug minus bag radius 0.18 m) |
|---|---|---|---|
| 2 | 50 kg | 0.21 m | 0.03 m |
| 4 | 100 kg | 0.30 m | 0.12 m |
| 8.5 | 212.5 kg | 0.44 m | 0.26 m |
| 15 | 375 kg | 0.59 m | 0.41 m |

Your Result 20 gives the bag's track at 6 km as known to 0.1-0.15 m. At k = 4 that is about the
whole catch radius, so the backup would fire often unless the plug's last ~100 ms of steering
closes most of the error. A thinner, wider plug has a larger catch radius but risks the bag
punching through. That trade is the main thing to size.

## S52. Wanted

1. **The lens sweep.** On the 2 F paraboloid, with an ice plug, sweep plug depth from 1x to 2x the
   bag's depth (at constant mass, so radius follows), at k = 2, 4, 8.5 and 15. Include the compact
   column as the control. For each, report leverage (and its frozen-rebound edge), `eta_jet`, face
   peak, exit direction and the graded floor's ringing. Say whether the plug's height above the
   vertex should move from 2 F for a near-point burst. A concave front face (a dish that cups the
   bag) is a welcome extra case if it is cheap.
2. **Punch-through.** The thinnest plug, as a share of the bag's depth, that still stops the bag
   with no residual jet reaching the plate. Report the face peak just past that limit. This sets
   the widest plug, and so the largest catch radius, at each k.
3. **The safe overlap.** Your 2-D code is axisymmetric, so this may need a ray trace or a hand
   bound. If the bag strikes the plug off centre, part of it passes beside the plug as a compact
   jet. What share of the bag's face can miss the plug before the face peak passes maraging's
   2.3 GPa? That share sets the gun's trigger. The gun fires whenever the predicted overlap falls
   below it.
4. **The backup pulse.** The gun has fired and the spread bag passes beside the plug, or clips
   its edge. Report the face peak and the impulse delivered (your Result 20 miss row gives
   2.22 MN s and 1.03 GPa with no charge in place, production grid). Say whether the plug
   survives the pulse and stays usable for the next bag, or should be counted as spent.
5. **The trigger window.** The 100 g bullet's meeting point (~30 m) is set by how far the merged
   cloud must spread, so the gun fires at ~6 km, about 120 ms before arrival. That is before the
   plug's last ~100 ms of steering. Confirm the firing range for the lens case. If a lighter or
   faster bullet lets the gun fire later without the miss's peak passing 2.3 GPa, report it, since
   a later decision sees a tighter track.
6. **Earth bag plate for the lens load.** Re-grade the 25-32 t paraboloid to the lens's load profile and
   report plate mass, centre thickness, ringing and graphite liner consumption per pulse and per
   push. Include the liner's consumption on a backup pulse (your miss row's inner rings take
   about 53 MJ/m^2).
7. **Lower k.** Your compact ice optimum may lie below k = 4, the lowest run. Run k = 1-4 for the
   lens and the compact column. The ship-carried plug mass is the largest Earth-side ledger line, so the
   companion `aim_is_all_you_need` will choose k on dollars per kilogram, not on leverage.

The parent needs items 1, 2 and 3 first. Items 1 and 7 set the leverage curve for the ledger.
Items 2 and 3 set the catch radius and the trigger, and so how often the backup fires.

## What the ledger is carrying meanwhile

The parent's S51 update (`docs/iapetus_cycle_ledger_asks_for_aim_repo.md`) prices the push as a
band. The compact column is the simulated base and the point fireball the labelled optimistic
ceiling for the lens, each with its frozen-rebound edge. Backup pulses are weighted by a
placeholder miss rate of 5%. Your item 3 answer replaces that placeholder.

Paper edits that wait on this: the Earth bag plate and its spreading. The Iapetus cycle is not
in the paper yet; it waits on S51 as well.
