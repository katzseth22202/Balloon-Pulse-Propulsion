# Keeping the lossless spring on its cycle: ask S48 (for puffsat_impact_simulation)

Raised 2026-10-20 in `Balloon-Pulse-Propulsion` (after `f5ba491`). **Written to be copied into
`puffsat_impact_simulation`.** Follows the sim's Result 17 (ADR-0068,
`docs/gas_spring_answers_for_parent.md`). The paper holds its text until this lands (Seth,
2026-10-20: "send the per-pulse trim to the sim first").

## The problem

Every Earth plate rides a nearly lossless nitrogen gas spring (the parent's
`sec:pusher_plate_damping` and `sec:charge_pusher_plume`; your Result 17). The plate is never
caught. It swings freely between pulses, and each pulse arrives as the plate swings toward the
stream and reverses it. The flown case: a 63.4 t plate, 7.35 MN s pulses at 2 Hz, theta = 2 pi/3,
an 8 m stroke, so a kick of `J/m` = 116 m/s and a swing of +-58 m/s. A push is ~2000 pulses.

A lossless spring never forgets an error. The parent's own chamber section
(`sec:hydrogen_pressure_shell`, the burst-and-coast paragraphs) makes this point for the
chamber: with 10% impulse scatter the motion random-walks off its steady cycle within ~25 pulses
and runs off the end of its stroke. The chamber fixes it by catching the chamber every pulse and
trimming the next charge's mass. **Burst and coast is ruled out for the plate**: its damper
would take 426 MJ a pulse, 0.85 TJ a push, about twice what vaporizes the 63 t plate. So the
plate needs a correction that keeps the spring lossless.

## The paper's ballpark (our estimate, not printed)

An impulse error `s` per pulse puts `s x 116` m/s of error into the swing, in a random
direction. With no correction it walks as `sqrt(N)`:

| scatter s | error per pulse | reaches the 58 m/s swing after |
|---|---|---|
| 2% | 2.3 m/s | ~625 pulses (5 min) |
| 5% | 5.8 m/s | ~100 pulses (50 s) |
| 10% | 11.6 m/s | ~25 pulses (12 s) |

Your Result 17 loss, 0.14-0.37% of the swing's energy a cycle, is the only damping. It is
0.07-0.18% of the amplitude a cycle, so the drift settles at an rms of `s x 116 / sqrt(2 d)`:

| bag loss a cycle | s = 2% | s = 10% |
|---|---|---|
| 0.14% | 62 m/s (1.1x the swing) | 310 m/s (5.3x) |
| 0.37% | 38 m/s (0.7x) | 191 m/s (3.3x) |

So unless the pulses repeat to about 1%, the plate needs active per-pulse correction. The
candidates we see, none computed:

1. **Trim the next charge.** The polyethylene charge is deployed by the craft before each pulse,
   so its mass (the slug ratio k) can be chosen. Measure the swing during the half-second
   interval and size the next pulse to cancel the error, as the chamber does. Needs the impulse's
   slope with k at fixed sheet mass.
2. **Trim the charge's standoff or position**, if the impulse is more sensitive to it than to
   mass.
3. **Trim the arrival time.** A sheet arriving early or late meets the plate at a different phase
   of its swing. The sheets carry cold-gas steering and can shift arrival by a small amount.
   Whether a timing shift corrects the swing's phase as well as its amplitude is the question.
4. **A switched orifice in the bags**: controllable damping engaged only to bleed a drift. It
   dissipates only the error's energy, not the plate's, but it adds a valve to a bag the paper
   calls sealless.

## S48. Wanted

1. **The scatter.** What sets the pulse-to-pulse impulse scatter for a floor-wide Kapton sheet on
   a polyethylene charge, and how large is each part? Candidates: sheet areal density on the
   meter scale, footprint offset (it also rocks the plate, which your Result 17 lists as not
   modelled), charge mass and standoff, sheet arrival time, and the plume's pulse-to-pulse
   variation. A number for each, or the sensitivity per unit error.
2. **The drift, solved.** On your nonlinear adiabatic spring (`gas_spring.py`), fly 2000 pulses
   with that scatter and your hysteresis loss. Show how far the plate wanders against the 8 m
   stroke with no correction.
3. **The trim.** For options 1-3 above (and 4 if cheap), the correction authority each gives per
   pulse, the residual drift with a realistic measurement of the swing (position and velocity
   read during the 0.5 s interval), and what it costs: charge mass carried, cold gas, or energy
   dissipated. Option 1 is our lead, since the chamber already relies on it.
4. **theta = pi.** Repeat item 2 for the stiffer spring the paper names as the gas-column fix
   (8.3 m column, 1.61x peak). It should be more forgiving, since its swing is closer to the edge
   of contact and its stiffness is higher, but the edge of contact is also closer.

Paper edits that wait on this: a sentence in `sec:charge_pusher_plume` (the spring needs per-pulse
trim, and what does it) and an item in `sec:charge_pusher_open`.
