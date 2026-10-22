# Ceres-made plates and Sun bowls: ask S57 (for `aim_is_all_you_need`)

Raised 2026-10-22 against aim `0aa5813` (S56's answer, ADR 0083). **Written to be copied verbatim
into `katzseth22202/aim_is_all_you_need`**, so it repeats context the paper repo already has.
Register entry: S57 in `docs/deferred_to_companion_repos.md`.

Same ground rules as your own handbacks. Neither document is the source of truth. If a number here
looks wrong, say so rather than working around it. The figures below are a parent scratch estimate
read off your `make ceres-dive` output. None of it is a companion result yet.

## The question (Seth, 2026-10-22)

S56 priced every plate, Sun bowl, bag and avionics unit as Earth hardware: $30/kg plus freight to
a Ceres depot ($4.40/kg at 4 R_sun). Seth asks what changes if a mature Ceres industry makes most
of that mass itself.

1. **Plates and Sun bowls are made at Ceres.** Ceres resembles CI/CM carbonaceous chondrites:
   about 18% iron and 1% nickel by mass in CI, largely oxidized (magnetite, iron-bearing clays).
   Hydrogen or carbon reduction on reactor heat gives the iron. The Mond carbonyl process, which
   needs only carbon monoxide, separates the nickel. Chromium and manganese come along at a few
   tenths of a percent.
2. **About 1% of the plate's mass is shipped from Earth.** Molybdenum is about 1 ppm in chondrites
   and cobalt about 0.05%, so the alloying elements a maraging or Cr-Mo steel needs beyond the
   iron, nickel, chromium and carbon come from Earth. Take 1% of plate and bowl mass at the Earth
   hardware price plus freight.
3. **Bags and tiles are made at Ceres too.** The Vectran bags are an aromatic polymer, the same
   chemistry class as the Kapton-grade film S56 already assumes Ceres makes. Silicon nitride
   comes from Ceres' clays and ammonia.
4. **Electronics stay Earth-made.** That covers the ship avionics and every PuffSat's steering
   package. Ceres has vacuum for deposition and etch, but not a semiconductor supply chain, and
   electronics are worth far more per kilogram than the freight.

## What the parent read off `make ceres-dive`

At 4 R_sun, X_C 110, the `sun_bowl` line is $0.076/kg at L1 at $34.40/kg ($30 + $4.40 freight),
or 0.0022 kg of Earth hardware per kg at L1. Re-priced at a Ceres price `p` with 1% at $34.40,
holding the design and the freight fixed:

| Ceres plate price `p` | saving, $/kg at L1 | total |
|---|---|---|
| $10 | 0.053 | 1.41 |
| $20 | 0.031 | 1.43 |
| $30 | 0.010 | 1.45 |

`ceres_plates` is $0.002 already, because the plate is recovered 100 times. The freight's own
capture plate and the Earth-side plates are left as they are in this scratch.

**A gap the parent found.** In `steady_loop` the `packages` line charges `prices.package` per
package with no mass and no freight. Packages bound for the Ceres stream are Earth electronics
and should pay the Earth-to-Ceres freight on their mass. The paper's package is "the electronics,
cameras, gyro, radio, valves, tank and battery each sheet, PuffSat and rod carries, at two per
60 kg of sheet". No package mass is printed in either repo that the parent could find.

## S57. Wanted

Extend `ceres_dive.py`; keep ADR 0083's headline reproducible beside the new one.

1. **A Ceres plate price.** Add `ceres_plate` to `CeresPrices` for the Ceres-made share of the
   Ceres plates, the disk plates, the Sun bowl, the bore collar and their bags. Default $10/kg (the
   structure price); sweep $10-30. Add `plate_import`, the Earth-made share, default 1%, at
   `earth_hardware` plus freight. Sweep 0.5-5%.
2. **Keep avionics as Earth hardware.** `avionics` stays at `earth_hardware` plus freight.
3. **Freight on the packages.** Give the steering package a mass, split into its Earth-made part
   (electronics, cameras, gyro, radio) and a part Ceres could make (valves, tank, battery case,
   structure). Charge freight on the Earth-made part wherever a package rides a Ceres-made pellet
   or sheet. State the mass you use and where it comes from. If the package is better kept whole
   from Earth, say so.
4. **Re-optimize** on the new book. The Sun bowl and the Ceres plate are cheaper, so the
   plate-policy choice of ADR 0083 item 7 (recover, expend, double as the Sun bowl) and the bowl's
   survival-floor trade may move. Report which policy wins and at what Hz and burn length.
5. **Does the freight leg change?** The freight now carries mostly avionics, packages and the
   1% import. Say whether its own capture plate should also be Ceres-made, and re-price it.
6. **Headline and sensitivities.** $/kg at L1 at 4 and 9.86 R_sun, the line-by-line breakdown, and
   re-run ADR 0083's item 8 rows that touch Earth hardware: Earth hardware $100, freight $3 / $10,
   and dead mass. Say how far the $100 Earth-hardware risk ($1.81 in ADR 0083) falls.
7. **What is left out.** The Ceres metallurgy's capital (reduction, carbonyl refining, rolling and
   forming) is not priced, as with the rest of the Ceres industry. List anything else that reaches
   $0.02/kg at L1.

The paper does not wait on this. Nothing goes into the paper until it is answered.
