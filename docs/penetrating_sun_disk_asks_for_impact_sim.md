# Does a penetrating Sun disk couple better? Ask S65 (for `puffsat_impact_simulation`)

Raised 2026-11-16 against sim `1eb4115` (Result 24, ADR-0075) and paper `f47fef4`.
**Written to be copied verbatim into `katzseth22202/puffsat_impact_simulation`.** Register entry:
S65 in `docs/deferred_to_companion_repos.md`. Companion ask on the growth sheet: S64,
`docs/perforated_sheet_asks_for_impact_sim.md`.

Same ground rules as your own handbacks. If a premise here is wrong, say so rather than working
around it.

## Why

The headline Sun disk is a 1 kg, 40 cm, 8 kg/m^2 plate (2.8 mm graphite plus its pod) striking a
20 kg polyethylene charge 1.2 times its radius, about 11.6 cm deep, at 392 km/s (Result 24). By
Birkhoff's `L sqrt(rho_p / rho_t)` the plate erodes only about 3.9 mm into the charge, 3% of its
depth. Everything it brings is laid down on the mouth-side face, and a decaying shock carries it
through the rest.

Seth asked whether a disk shaped as a bed of spears, long enough to reach into the charge, would
spread the energy through its depth and couple better. Parent scratch: spears reaching two-thirds
of the depth are about 5.6 cm of graphite, and the same graphite then covers about 5% of the face
(some 60 spears of 1 cm^2 at ~4.5 cm pitch).

The parent does not know the sign. Momentum is conserved either way, and the mean energy is
3.5 GJ per kilogram of merged gas, so no layer stays solid. Shape moves only the losses, and two
of them pull opposite ways:

- **For spears.** A face-deposited pulse makes a very hot mouth-side layer. Radiation goes as
  `T^4`, and Result 22 found argon pushing 16% less than polyethylene on this bowl because it
  radiates into the face. Spreading the energy through the depth cools that layer.
- **Against spears.** On this bowl the useful exhaust leaves through the mouth. A hot layer that
  blows straight out of the mouth may already be the efficient part of the pulse.

Two facts already in hand bear on it. Result 24 notes that radiation from the dense charge is not
in the 2-D gas at either speed, so the 2-D runs cannot see the first effect. And Result 23's
2.5 kg, 1 cm plate on its best charge coupled 1.177x its matched charge against the thin disk's
1.074x. That may be the charge's width rather than the disk's depth.

## Ask

1. **The loss budget today.** For the headline thin disk on x1.2 at 392 km/s, how much of the
   pulse is lost to radiation and to frozen ionization and bonds, in whichever model carries
   radiation? Also give the specific energy or entropy of the charge against depth just after the
   shock crosses it. If those losses are a few percent, say so and stop: no shape can win back
   more than they hold.
2. **Thick against thin, per kilogram.** Put Result 23's 2.5 kg, 1 cm plate and Result 24's 1 kg
   thin disk on one footing, as J/mv on each one's best charge. Is any of the thick plate's
   1.177x a depth effect, or is it all charge width?
3. **A penetrating disk.** If item 1 leaves room, run a 1 kg disk whose graphite reaches about
   two-thirds of the charge's depth. In the axisymmetric code that can be a central rod plus one
   or two concentric rings of the same mass, on the x1.2 charge. Report J/mv against the thin disk.
   A rod or ring that runs through the charge and strikes the bowl's floor is a failure: say at
   what length that starts.
4. **The pod.** The paper's open item on a disk with a central 3 cm pod (`sec:sun_wave_ranging`)
   is the same physics at one-tenth the mass. If item 3 runs, run the pod disk beside it.
5. **4 R_sun.** Only if item 3 moves J/mv by more than 2%: repeat it at the 4 R_sun closing speed,
   since radiation is the one loss that grows with speed.

## Outcome

If spears lose or win under 2%, the paper keeps the flat disk and says in one sentence that
penetration depth does not set coupling at this speed. A gain above 2% goes to aim. There,
`make disk-train-aim` must also price what spears cost the aim: a rod off-centre kicks the ship
sideways, and the bore's clearance changes. The pod answer closes the open item either way.
