# The loop without the Sun: answers for the child (`puffsats_for_datacenters`)

Answers 2026-10-25 to `docs/no_sun_loop_asks_for_parent.md` at child `60de421`, copied into this repo
as `docs/no_sun_loop_asks_from_child.md`. Parent `860b570`, aim `7ce7628`. **Written to be copied
into the child's `docs/`.**

Every number below is from a rerun of aim at `7ce7628`. `make plate-jupiter-loop` reproduces the
paper's growth and doubling columns exactly, and its 0.5 g and 1 g break-evens to within 0.5%.
The probe that reads the plate, pulse and seed lines out of the same ledger is
`nosun/probe.py` in the parent's scratchpad. The GNSS times are a two-body hyperbola,
`nosun/gnss_time.py`.

Short version:

| Item | Status |
|---|---|
| 2. Plate masses | **Answered. The premise is wrong both ways.** The plates weigh the same on both loops. |
| 3. Departure cadence | **Answered.** 1 Hz on every row. A slower cadence makes the bowl heavier. |
| 4. Time inside GNSS coverage | **Answered.** 10-13 min for the Jupiter-only streams, 7-9 for the dive's. |
| 5. Seed in tonnes and Starships | **Answered.** 183 t, 2.0-2.5 stripped Starships, at 0.5 g. |
| 1. Argon charges | **Bracketed, not priced.** The direction holds and the bound is large. The real number waits on S60, which does not yet cover this loop's speeds. |

## 2. The plate masses: the same plates, on a lighter ship

The Jupiter-only plates are **not** heavier than the dive's at the loop's best departure. Both loops
fly the same shared assembly: one gas spring with the flat push plate on one face and the holed
bowl on the other.

| Loop, departure | Assembly plate | Bags | Collar | Bowl line | Push stroke / bowl stroke | Departing ship |
|---|---|---|---|---|---|---|
| Dive, 9.86 R_sun, 0.25 g | 63.4 t | 5.4 t | 1.0 t | 69.8 t | 8.0 / 4.4 m | 567 t |
| Jupiter only, 0.25 g | 63.4 t | 5.4 t | 1.0 t | 69.7-69.8 t | 8.0 / 2.5-3.3 m | 143-308 t |
| Jupiter only, 0.5 g (best) | 63.4 t | 5.4 t | 1.0 t | 69.7-69.8 t | 8.0 / 5.4-6.9 m | 182-353 t |
| Jupiter only, 1 g | 87-111 t | 2.9-3.8 t | 1.0 t | 92-114 t | 4.6-5.8 / 8.0 m | 175-323 t |

Ranges run from the 2S windows (low) to the 3S windows (high). The dive flies no separate spring
for the Sun bowl here; that bowl and its spring are 16 t of dead mass on the Sun ship, outside
this table.

**Why they are the same.** The spring law fixes plate mass times stroke at 0.138 F/ν², where F is
the mean thrust and ν the pulse rate (aim `spring_plate_stroke`). The push sets it on both loops:
1 g on the 1500 t unit at 2 Hz gives 507 t m, so 63.4 t on the 8 m stroke. The Jupiter-only push
is the same push at the same rate on the same unit. Its slower stream changes the push's exhaust
speed, not its force. The bowl uses the same plate and needs less than the full stroke until
its own F/ν² overtakes the push's. That happens only at 1 g, where the bowl binds and the
assembly grows to 87-111 t.

**Why the paper says "heavier".** The sentence in `sec:why_sun_dive`, "The heavier spring plates
cost it most", compares the spring plates against the 12.2 t constant-force absorber they replaced
(aim ADR 0076). It does not compare the two loops. On ADR 0076's own split, the spring alone took
the Jupiter-only loop from 2.01x to 1.44x at 0.25 g, and the overtake law at 55-65 km/s did the
rest. The parent will reword it (see "Parent-side corrections" below). The child should not carry
"heavier plates" as a loop-against-loop claim in either direction.

**What does cost the Jupiter-only loop.** The same ~70 t assembly rides a ship a third to two
thirds the dive's mass, so it is 20-38% of the departing stack against the dive's 12%. The ship
is lighter for three reasons, all already in `sec:why_sun_dive`:

- the push's exhaust speed is 23-27 km/s against 36.5 km/s, because the stream is slower;
- the bowl's is 7.1-8.1 km/s against 10.4 km/s, because the stream is slower and nearly head-on
  (161-180 deg against 130 deg);
- the departure burn is 6.6-9.4 km/s against 4.21 km/s, because the loop must leave Earth faster.

So for the child's lighter-plate premise: the plates are no lighter, and no heavier. The premise
the parent can support is narrower. A Kapton push on a lightly loaded plate is cheap on both loops,
and the plate is the same.

## 3. The departure cadence

The bowl flies **1 Hz on every row**. The cadence is fixed by ADR 0073 (aim `DEPARTURE_RATE`), and
only the mean acceleration is traded. Seth's assumption of 1 Hz at 0.5 g is right.

| Loop, departure | Rate | Pulse | Burn |
|---|---|---|---|
| Dive, 0.25 g | 1 Hz | 2.02 MN s | 32 min |
| Jupiter only, 0.25 g | 1 Hz | 1.2-1.5 MN s | 46-63 min |
| Jupiter only, 0.5 g | 1 Hz | 2.5-3.2 MN s | 20-28 min |
| Jupiter only, 1 g | 1 Hz | 5.0-6.4 MN s | 9-13 min |

The push flies 2 Hz and 7.35 MN s on every row of both loops.

**A slower cadence would not lighten anything.** Plate mass times stroke goes as 1/ν², so slowing
the bowl raises its share of the stroke. At 0.5 g the bowl already uses 5.4-6.9 m of the 8 m. It
starts to bind below about 0.93 Hz on the 3S windows and 0.83 Hz on the 2S ones. At 0.75 Hz it
would need 9.6-12.3 m on the 63.4 t plate, so the assembly would grow to about 76-98 t. A faster
cadence does not lighten it either, because the push sets the plate. The bags are already the
push's.

## 4. Time inside GNSS coverage

Two-body hyperbolas from 40,000 km geocentric to the stream's pass. That radius reproduces the
paper's "about 11 min" at 57 km/s (`tab:jupiter_nav_phases`), so it is the paper's convention.

| Stream | Speed at its pass | Inside 40,000 km |
|---|---|---|
| Dive push (growth wave) | 99.2 km/s at 400 km | 6.7 min |
| Dive departure wave | 76.2 km/s at 600 km | 8.7 min |
| Jupiter-only push | 54-65 km/s at 400 km | 10.2-12.3 min |
| Jupiter-only departure wave | 52-63 km/s at 600 km | 10.5-12.9 min |

One correction to the ask. The dive departure's 84.0 km/s is the mean **closing** speed against the
burning ship at 130 deg. The stream's own speed relative to Earth is 76.2 km/s, and that is what sets
its time inside 40,000 km.

The child's ~7 min and ~11 min estimates hold. The Jupiter-only loop gets 3-6 more minutes of GNSS
per stream. It does not shorten the coast: both loops still fly about 16 days on the co-flyers
before GNSS takes over (`sec:jupiter_coflyers`). The parent would print the GNSS edge as "a few
more minutes of GNSS on each stream", and no more.

## 5. The Jupiter-only seed in tonnes and Starships

| Loop | Seed excess | Seed | Stripped Starship payload at that excess | Starships | Dear seed |
|---|---|---|---|---|---|
| Dive, 9.86 R_sun | 10.24 km/s | 567 t | 134-154 t | 3.7-4.2 | $4993/kg |
| Jupiter only, flown chain, 0.5 g | 11.99 km/s | 183 t | 72-92 t | 2.0-2.5 | $9293/kg |
| Jupiter only, flown chain, 0.25 g | 11.99 km/s | 145 t | 72-92 t | 1.6-2.0 | $9293/kg |
| Jupiter only, flown chain, 1 g | 11.99 km/s | 176 t | 72-92 t | 1.9-2.4 | $9293/kg |

The seed is one launch unit's departing ships in the loop's steady role split, as in the dive
(aim `value_chain`). The dive's 567 t matches the child's 566 t to rounding. Each Jupiter-only
seed tonne costs about 1.9 times as much because a stripped Starship carries about 60% as much to
12 km/s. The seed is still smaller in tonnes and Starships, because each Jupiter-only ship leaves
lighter. Item 2 gives the reason.

## 1. Argon charges: the direction holds, the price waits

**The sentence is right in direction.** On the S60 convention (polyethylene's 84 MJ/kg of bonds
charged on the charge's share of the merged mass, against the dissipated energy per kilogram), the
bonds take a larger share on the slower loop:

| Plate | Dive | Jupiter only |
|---|---|---|
| Push | ~13% at 99 km/s, k 6.4 | 24-35% at 54-65 km/s, k 5.0 |
| Bowl | ~30-32% at 84 km/s, k 12.4 | 37-46% at 69-77 km/s, k 12.1 |

**An upper bound, from aim's own switches.** aim carries two bond-free variants. The first is the
bowl's "bonds returned" law (its `condensed` rows). The second is the push's `linear` law, the
100 km/s rows scaled by speed, which removes the extra toll a slower stream pays. Re-optimized at
each loop's headline:

| Case | Jupiter only, 0.5 g: growth / doubling / BE cheap / dear | Dive 9.86 R_sun: growth / doubling / BE cheap / dear |
|---|---|---|
| Headline (polyethylene) | 1.65x / 4.56 yr / $759 / $1873 | 3.23x / 1.94 yr / $131 / $158 |
| Bowl bonds returned | 2.22x / 2.85 yr / $265 / $440 | 3.52x / 1.80 yr / $122 / $141 |
| Bowl bonds returned, push linear | 2.52x / 2.45 yr / $194 / $266 | 3.63x / 1.76 yr / $117 / $131 |

So a fully bond-free charge would recover far more on the Jupiter-only loop: $1607 of its dear
break-even against $27 on the dive. Even then the dive stays ahead, at $131 against $266.

**Why this is not yet the argon price.** It is a bound, and it is optimistic in four ways:

- argon has no bonds but does ionize, and its first ionization alone is ~38 MJ/kg, about 45% of
  polyethylene's bond energy per kilogram (S60 item 3 asks for its frozen toll);
- the `linear` push is the 100 km/s law scaled, not a bond-free law;
- the cryostat and argon's price are not charged;
- solid argon (1620 kg/m^3) and argon snow do not have a simulated coupling yet.

**S60 does not cover this loop.** S60 asks for argon at the dive's three plates only: the push at
99 km/s and k 6.4, the bowl at 84 km/s and 130 deg, and the Sun bowl. The Jupiter-only push at
54-65 km/s and the bowl at 161-180 deg and 69-77 km/s are outside it. The parent proposes
adding them to S60 as an item 8, if the simulation can take it while S60 is running. Then aim
reprices both loops with argon charges and the cryostat.

**For the child now.** The parent will not print the sentence until S60 lands. A bond-free charge
is an unpriced upside, and the bound above leaves argon's ionization uncharged. The child should
cut the sentence for now. If the child wants to say something, the parent can stand behind this
much: *the charges' bonds take a larger share of this loop's slower collisions, 24-46% against
13-32% in the dive.* That restates `sec:why_sun_dive` in numbers and claims no gain.

## Parent-side corrections found while answering

These are in the parent's `sec:why_sun_dive`, not the child's. They are listed here so the child
knows which printed numbers will move.

1. **"The heavier spring plates cost it most"** reads as a loop-against-loop claim. Proposed:
   *"Moving every plate onto its spring costs it most. The 63 t assembly is the dive's, but it
   rides a ship a third to two thirds as heavy."*
2. **`tab:no_sun_loop`'s steady-cost column is stale.** aim ADR 0077 now prices the steady column
   over a whole chain, with the fleet held level. At `7ce7628` the flown chain's steady cost is $270 /
   $189 / $214 at 0.25 / 0.5 / 1 g, against the printed "none sold" / $1474 / $2560. The 3S-only
   rows are $463 and $217, against $1264 and $254. The caption's "At 0.25 g the flown chain grows
   too slowly to sell anything once the fleet is level" no longer holds. Break-evens move by
   under $10 at 0.5 g and 1 g. At 0.25 g the dear break-even falls from $11184 to $10505
   (flown) and from $14975 to $14595 (3S only).

The headline comparison is unchanged: $1873 at the loop's best against the dive's $158.
