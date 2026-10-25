# The loop without the Sun: asks for the parent (`Balloon-Pulse-Propulsion`)

Raised 2026-10-25 against parent `860b570`. **Written to be copied into the parent's `docs/`**, so it
repeats context the parent already has. The child's `sec:no_sun_loop` and `tab:no_sun_loop` summarize
the parent's `sec:why_sun_dive` and its `tab:no_sun_loop`. Every number in them is the parent's except
where an item below says otherwise.

Ground rules are the usual ones. If a premise here is wrong, say so rather than working around it.

## The question (Seth, 2026-10-25)

Is the Earth-Jupiter-Earth loop the one people would try to validate first, before the Sun dive? Seth's
case for it:

- **Ease.** No solar heat shield, no coronal mass ejections, no disk train to aim at perihelion.
- **Navigation near Earth only.** Formation shaping can lean on GNSS, or on a dedicated constellation in
  Earth orbit.
- **Lighter plates.** A Kapton-sheet push on a lightly loaded growth plate, and a departure plate made
  lighter by 1 Hz, 0.5 g pulses.
- **Low bond losses.** With argon charges, the only chemical bonds left are the incoming Kapton sheets
  and a polyethylene charge for the departure wave.

What the parent already says, against that case:

- The loop on the same plates grows 1.65 times per 3.276 years at its best departure (0.5 g), against
  3.23 for the dive. Dear-seed break-even is $1881 against $158 per kilogram.
- "The heavier spring plates cost it most." That is the opposite of the lighter-plate premise.
- Both loops' Earth streams use the same approach ladder: co-flyers through the coast, then GNSS for
  the last ~11 minutes (`sec:jupiter_coflyers`). The Jupiter-only loop removes the Sun-wave ranging
  (`sec:sun_wave_ranging`). It does not move more of the job onto GNSS.
- The disks, sunshade, Sun bowl and carrier cost about $7 per kilogram at L1. 9.86 R_sun is a depth
  Parker has flown. The CME and particle-dose items in `sec:charge_pusher_open` are about 4 R_sun.

## Asks

1. **Argon charges on the Jupiter-only loop.** The child now prints this sentence, which the parent
   does not yet carry: *a bond-free argon charge would recover more of the bond toll in this loop than
   in the dive, because its collisions are slower.* It follows from `sec:why_sun_dive` (the simulated
   law runs 9-17% below linear at 54-65 km/s "because the charges' bonds take a larger share") and from
   the polyethylene toll in `sec:charge_pusher_cycle` (84 MJ/kg, ~12% of sheet energy at the dive's
   push). Please confirm it, then price it. Give growth per 3.276 yr and both break-evens for the
   Jupiter-only flown chain at 0.5 g with argon charges on the push and on the bowl, cryostat charged.
   Do the same for the dive. The child prints growth only, in kilograms, so growth is the number it needs. This rides on S60 (`snow_charge_asks_for_impact_sim.md`). If the parent
   will not carry the sentence, the child cuts it.

2. **The plate masses, and why they are heavier.** `tab:no_sun_loop` does not print the Jupiter-only
   plates. Please give the push plate, the bowl and the spring masses on both loops, and the reason the
   Jupiter-only ones come out heavier. Is it the bigger departure impulse, the head-on bowl, the slower
   streams needing more sheet per pulse, or something else? This answers Seth's lighter-plate premise
   directly.

3. **The departure cadence.** The table gives the bowl's mean acceleration, 0.25 / 0.5 / 1 g, but not
   its pulse rate. Seth assumed 1 Hz at 0.5 g. Please print the cadence and pulse size for each row,
   and say whether a slower cadence at 0.5 g would lighten the bowl or its spring.

4. **Time inside GNSS coverage.** If the child is to keep any GNSS edge, it needs a parent number.
   Please print how long each Earth stream spends inside ~40,000 km on both loops: the dive's push
   (99 km/s at 400 km) and departure (84.0 km/s), and the Jupiter-only push (54-65 km/s) and departure.
   Our rough estimate is ~7 min for the dive's push against ~11 min for a ~60 km/s stream.

5. **The Jupiter-only seed in tonnes and Starships.** The child prints the dive's seed as 566 t, 3.7 to
   4.2 stripped Starships. For the comparison, please give the Jupiter-only flown chain's seed in the
   same units, beside its $9293-per-kilogram dear-seed cost.

## What the child will do with the answers

Items 1 and 2 change the table (an argon row; a plate-mass row). Items 3 to 5 each become one sentence
or nothing. The child assumes every stage succeeds, so it does not ask what a failed Sun wave leaves. Until an answer lands, the child prints only what is listed above as the parent's.
