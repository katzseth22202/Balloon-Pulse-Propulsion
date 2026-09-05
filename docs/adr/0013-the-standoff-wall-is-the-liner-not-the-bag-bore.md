# The standoff wall is the liner, not the bag bore, which takes the cap below 12 T

Status: **proposed** (2026-09-05, from the user's question of whether a flare and a hybrid
nozzle could buy a peak field under `0012`'s cap). Amends `0012` rather than superseding it,
because it changes one input to that ADR's method and leaves the method alone. **Conditional on
R15**, which asks the impact simulation to settle which surface the standoff requirement is
written against. Nothing enters the paper until R15 lands.

## What forced the question

The question asked was whether a flare, a hybrid nozzle, or both could get the peak field below
12 T. The flare half is answered here. **The hybrid half is answered no, and the reason is
structural rather than numerical.**

`0012` establishes that the field upstream of wall contact is a flat shelf, and that the shelf
height is the standoff demand at the contact station. So the peak field is set at exactly one
place, the station where the snowplow front first touches the wall. **R8's physical bell and
R11's magnetic extension both live downstream of the bag**, past every station that sets the
shelf. Neither can lower the peak field. They buy detachment and divergence, which is a different
account.

## What `0012` measured to

`0012` **answers this question against itself, two paragraphs apart.** Under "What the field at
the chamber is for" it states the job outright: *"wall standoff. The field is there to keep plasma
off the liner."* The table immediately below it then reads, at every row, **"wall at 3.02 m"**.
That is `eq:bore_from_length`'s bag bore, not the liner, and it is the same identification `0011`
was written to break.

So this is not a disagreement between two ADRs. **It is a single ADR naming the liner as the
surface and then measuring to the bag.**

`0011` puts the liner, the pyrolytic graphite surface that must not be hit, at **3.50 m at the
chamber flaring to 5.17 m at the throat**. The bag is 12 um of polyethylene that vaporises in the
collision, so it stands nothing off. The rest of the repository already agrees: `CONTEXT.md`
takes the liner's area as 631 m^2 over `0011`'s flared bore when it counts the radiating wall,
and R12 uses the same 82% sky fraction. **The cap calculation is the one place that still uses
the bag bore.**

`0012` amends `0011` in the same session, and its cap table never picked up `0011`'s flare.

## The decision, proposed

**Evaluate the contact station against the liner, and read the flown profile there.** Nothing
else moves. The downstream profile stays exactly as derived, so P9's 5 T exit is untouched and
`0011`'s flare geometry is used as it already stands.

| spreading | wall | contact | flown profile there | cap |
| --- | --- | ---: | ---: | ---: |
| 1.9x bracket, 41.3 deg | bag bore 3.02 m, flat (`0012`) | 3.27 m | 11.75 T | **12 T** |
| **1.9x bracket, 41.3 deg** | **liner 3.50 m, `0011` flare** | **4.14 m** | **10.59 T** | **11 T** |
| sound speed, 24.9 deg | bag bore 3.02 m, flat (`0012`) | 6.18 m | 8.87 T | 9 T |
| **sound speed, 24.9 deg** | **liner 3.50 m, `0011` flare** | **8.50 m** | **7.71 T** | **8 T** |

The cap column rounds up to the next whole tesla, which is the margin discipline `0012` used when
it took 12 T from 11.75 T. **The proposed cap is 11 T**, and 8 T if R9 confirms the sound-speed
spread. Shelf field energy falls to 0.78x of the 12 T case, and to 0.73x against 9 T.

## Why this is bookkeeping rather than a new design

No hardware changes. No new section of magnet, no bell, no regrading, and no change to the flare
`0011` already decided. **The same geometry is read against the surface that actually has to
survive.** That is why it is worth having even though it is worth only 1 T at the binding
bracket. It costs nothing.

It also does not depend on the radial scaling of the standoff demand, which is the weak step in
the deferred option below. The flown profile is a function of `z` alone, so moving the contact
station downstream and reading the same curve there needs no assumption about how demand varies
with bore.

## The flare is cheaper in conductor than `0011` priced it

Worth recording, because it changes how the next flare question should be argued rather than
anything decided here. Tape mass runs as the integral of `B r` along the column, and the standoff
demand runs as `B ~ 1/r`. **The product is bore-independent, so widening the winding is close to
free in tape wherever the field is standoff-limited.** `0011` priced its flare at 1.18x to 1.50x
conductor because it sized the flare by flux-tube accommodation and held the field at the flown
values. Once `0012` establishes that the field's job is standoff, that pricing is too harsh.

## Considered and deferred: let the whole profile follow the flared bore

If the standoff demand really scales as `1/r`, the field can fall along the whole column rather
than only on the shelf, and the peak reaches **8.44 T** at the binding bracket. The expansion
ratio improves rather than degrading, from `A/A*` = 2.40 to 2.94, because the exit demand falls
faster than the peak does.

**Deferred, because it drops the exit to 2.87 T against P9's 5 T.** P9 states that the 5 T exit
is a collision requirement, and a collision requirement is not ours to trade against bore. Taking
it would need P9 reopened, which is asked as the second half of R15 rather than assumed here.

## What could take this back

- **The wall may genuinely be the bag bore.** If the standoff requirement is written against the
  mist column rather than the liner, because the front has to be held inside the mist it is still
  sweeping, then `0012` is right as written and this ADR is void. This is the first question of
  R15 and the whole decision rests on it.
- **The coupling could move.** `k` = 7.2 is set by the front filling the 3.00 m bag, and the bag
  does not flare. Expanding into the clearance gap dilutes pressure without reducing swept mass,
  which is neutral to favourable, but it is unverified.

## Provenance

Paper-side probe, `todos/peak_field_vs_flare.py`. It reproduces `0012`'s own two rows before it
is used for anything else (8.87 T against the ADR's "9 T", 11.75 T against its "11.8 T"). Same
first-order caveats as `0011` and `0012`. Owed back to `puffsat_impact_simulation` as R15.
