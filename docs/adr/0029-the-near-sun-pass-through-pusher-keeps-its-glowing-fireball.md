# The near-Sun pass-through pusher keeps its glowing fireball; a magnetic pinch buys Isp, not projectiles

Status: accepted (2026-10-14). Resolved in a grill session. Paper: `sec:pass_through_pusher`,
`tab:pass_through_isp` (no text change). Terms in `CONTEXT.md` under **Pass-through X-ray
pusher**. Scratch calc: `todos/pinch_breakeven.py` (gitignored; method restated below).

## Context

The author proposed making the pass-through pusher's X-rays magnetically. The projectile flies
as two pieces on a rigid core. The trailing piece crushes a trapped field, and the compressed
current drives a z-pinch. The goal (author's choice) was **flash compression**: a short, small
flash so the radiation case gets lighter. Brightness was not the goal. At 618 km/s the baseline
fireball already radiates 71% of its heat, and the case's ~5 us hold around a 1.6 m tube is the
largest lever on specific impulse (5040 s at a 0 kg case, 2930 s at 5 kg).

The design the session settled on:
- a coaxial compressor whose inner conductor is a hollow few-cm aluminum tube on the projectile;
- a cascade seed, with the lead piece driving the first stage and the stages handing off by
  crowbar, timed by the core's spacing;
- a vacuum wire-array pinch load at the coax's astern end;
- a small radiation case around the pinch, an annular propellant plate, and the case's astern
  wall serving as the k = 2 anchor;
- the Orion standoff, kept.

## Decision

Keep the kinetic fireball as the near-Sun pass-through pusher's X-ray source. The magnetic
variant is priced out on the **projectile bill**, though it wins on specific impulse.

Method. The scratch model reproduces all eight rows of `tab:pass_through_isp`: energy to the
filler and propellant = 0.71 x 0.80 x 127.3 GJ, the pulse split of `eq:pulse_split`, an 80%
plate catch, and target plus case as dead mass. The variant swaps in E = eta x 127.3 GJ, where
the chain efficiency eta is the field-available energy that reaches filler and propellant
motion. The baseline's eta is 0.568. Dead mass is the 2 kg anchor plus the small case (0.25-2 kg)
plus the coax sleeve (0 / 1.7 / 3.4 kg). Masses are optimized for minimum bill at the 2650 s bar.

- The variant clears 2650 s at eta 0.15-0.27, with no sleeve.
- To match the baseline's bill-optimal 0.133 kg/kg it needs **eta 0.44-0.58**. That is 78-100%
  of the baseline's own efficiency, about 86% per hand-off over roughly four hand-offs. The
  optimistic omissions (annular-jet catch penalty, cascade hardware, capacitor) all favor the
  variant.
- The reason is that **case mass is a weak lever on the bill.** A free case cuts the baseline's
  bill only 24% (0.133 to 0.101 kg/kg). Once the case is light, the optimum adds propellant
  back down to the Isp bar, and impulse per projectile goes as sqrt(E x mass). The bill
  therefore tracks energy per projectile.

## Considered options

- **Immersing the wires or coax in filler or argon.** Rejected. Gas in the gap breaks down
  and shunts flux, and dense gas softens the implosion.
- **No case.** Rejected. An all-directions blanket caps the plate at the ~31% ray-count share
  (`5e7edbf`). A bare source lights a 0.4 m plate's edge at 9% of its center from 10 cm.
- **A contact-range pusher plate.** Rejected. The plate would take ~90 GJ of ~300 eV X-rays at
  its face.
- **A stationary inner post.** Rejected. It needs mm aim, against cm for the tube.
- **A radial line to a load ahead of the coax.** Rejected. Its inductance cuts gain.

## Consequences

- Revisit only if a mission is limited by ship mass rather than projectile count. Below
  blackbody closing speeds the question changes. See ADR 0030.
- **Open, for the author: the baseline's own operating point.** The paper prints 0.19 kg/kg at
  the 5 kg case with masses chosen for maximum Isp (2930 s, mass ratio 3.5). The same case run
  at the 2650 s bar (mass ratio 4, 23.9 kg spent per projectile) gives 0.133. That trades
  carried ship mass for fewer projectiles. If adopted, "nearly three times" the magnetic
  nozzle's 0.064-0.068 becomes about twice. Not applied.
