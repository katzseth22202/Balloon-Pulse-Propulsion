# Bare-sheet hits and the abort spray: asks for `puffsat_impact_simulation`

Raised 2026-10-16, while the paper adopts the solar-dive charge pusher (your Results 10-12,
ADRs 0060-0063; aim ADR 0072) as its lead growth cycle. **Written to be copied verbatim into
`katzseth22202/puffsat_impact_simulation`.** Register items **S30-S31**
(`docs/deferred_to_companion_repos.md`). Your E1-E6 and G5-G9 are being answered separately, in
`docs/solar_environment_answers_for_impact_sim.md`.

## Context: the Earth-side abort the paper will describe

If a charge fails to deploy, the next Kapton sheet strikes the flat plate bare. At ~2 Hz the ship
cannot dodge the sheets behind it (0.5-8 g to move a 1500 t unit ~10 m in 0.5-2 s). So:
1. The ship stops the train. Sheets more than a few seconds out divert by tens of metres on their own
   cold gas and leave on hyperbolic paths at ~100 km/s, so they never become debris.
2. The few sheets inside that window (~2-5 s, 4-10 sheets) cannot divert. After the first detected
   failure, the ship sprays liquid methane onto the plate face, timed to each sheet, as the spray cup
   does, so these become ordinary gas-on-plate pulses at a low slug ratio (k ~ 1-2).
3. Sheets aim off the plate until their unfurl is confirmed, so a failed unfurl misses.

The author's judgement is that ~1 s of bare hits is more than the plate can take. The paper wants
that tested, not asserted.

## S30. Bare-sheet hits on the flat plate

For the flat skirted plate at ADR 0072's sizing (30 kg/m^2 survival floor scaled as pulse
energy^(2/3); ~40-50 t), and for the push-wave sheet (~12.5 kg at ~87-128 km/s, face-on overtake at
400 km) and the departure-wave sheet (~60 kg on the ~4 MN s pulse, ~101 degrees canted):
1. Peak face pressure and duration of one bare hit, against the plate's rating.
2. Does the face spall, and if so, what fragment mass, size and speed, and in which direction?
   Spall is the debris risk here, not the sheet.
3. How many consecutive bare hits at 2 Hz before the plate loses function?
4. On the canted departure, does a sheet with no charge in its path strike the plate at all, or
   slide past it? If it slides past, that leg is benign and only the push needs the spray.
5. A furled sheet (a compact roll of the same mass) striking the plate: penetration or not.

## S31. The smallest buffer spray that makes a bare hit survivable

1. The lowest k of liquid methane sprayed on the face that keeps a bare-hit pulse inside the plate's
   peak-pressure rating, for both sheets.
2. How long the spray must lead the sheet, and how far it spreads in that time, so that the timing
   and injector requirement is stated.
3. Methane is the default (fuel side of the correction reserve; no LOX sprayed). Say if water or
   argon would be materially better as a buffer.
