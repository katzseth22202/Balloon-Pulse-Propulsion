# The split dive ships at held strength, weaker than the companion ADR that produced it

Status: accepted (2026-09-01 grill). The decision is to publish claims *weaker* than the
companion repository already supports, so it needs recording or the next pass will read
companion ADR 0023, read `sec:split_dive`, conclude the paper is stale, and strengthen it
back.

`sec:split_dive` applies companion ADR 0023, "The split dive buys the pad, not the clock."
That ADR states two results in strong form. The **partial split** at an outbound perihelion
of 0.4918 AU is "the only strictly dominating result in this repository's solar-dive work."
And the direct single-impulse departure "goes cold at 19.80 solar radii," which ADR 0023
reads as the split being what makes the recommended shallow dive flyable.

The paper states neither. It reports the same numbers and stops short of both conclusions,
because three prices are missing and each one could move a conclusion rather than a decimal.

## What is held, and what would lift it

**The dominance claim.** `split_dive_ledger()` charges the impactors *consumed* at both
nodes. It charges nothing for **delivering them to 1.96 AU**, and the partial split does not
satisfy outer-node co-location, so the returning beam does not reach its far node. That is a
second boost node away from Earth, the same class of cost the two-impulse phasing loop
carries at 1 AU, and the paper already knows how to talk about it ("a mature network
provides it, and an early one may not"). Lifting the hold needs a price for a dedicated
delivery to a 1.96 AU node. The paper says "better on both axes the ledger scores" until
then.

**The architecture claim at shallow depth.** The 19.80 solar-radii crossing is far more
sensitive to the perihelion burn than to the expansion margin ADR 0023 quotes it with. Swept
in `direct_departure_conduction_depth()`:

| perihelion burn | crossing |
| ---: | ---: |
| 20 km/s | 5.58 R☉ |
| 30 | 12.71 |
| **35.98 (the paper's 4 R☉ tuning)** | **19.80** |
| 40 | 26.04 |
| 45 | 35.91 |

Roughly 1.9 solar radii per km/s. **38.15 km/s holds the direct departure conducting out to
23 solar radii**, the depth `sec:depth_cost` recommends starting at, and that is 6% more
burn than the tuning the crossing is quoted at. So "the direct architecture has no departure
at the recommended depth" is really "none without boosting 6% harder at perihelion," and
nothing prices that 6%. `paper_resonant_dive_ledger()` does not settle it: it takes the
stream speed and the Earth burn and charges the node nothing for the larger boost, so it
reports the extra burn as a free improvement, which cannot be right. Lifting the hold needs
the node-side cost of a larger perihelion burn.

**The ledger gap.** Placing the opposing stream costs 35.48 km/s of heliocentric impulse at
4 solar radii, rising to 44.94 at 32, against the payload's own 24.09 falling to 14.62. That
is the same order as the payload's whole injection and it grows as the dive is backed out.
`sec:jovian_dive_open` sets the opposing side aside twice, once as 1.34--2.15% of the vehicle
consumed at the node and once as "one-way and expendable, so their trajectory has to exist
and be timed." Both concern the projectiles *once they are in place*. Neither concerns the
impulse that puts them there, and in this architecture that impulse is itself a PuffSat
collision charged to a pad. Lifting the hold needs a trace of whether any existing growth or
pad ledger already absorbs it.

## Consequences

The third hold is the expensive one, because it blocks a restructure rather than a sentence.
The grill concluded that the strongest surviving result in `sec:split_dive` is that **the
dive node needs two arrivals and the paper has only ever priced one**, with the two legs
crossing near 8 solar radii and the split saving 1.70x to 1.84x on the leg that gets dearer.
That was to become the subsection's spine. It cannot lead until the trace says whether the
paper's growth numbers are affected, so `sec:split_dive` keeps its present order in the
meantime and leads with the Delta-v family instead.

Two things from ADR 0023 are *not* held, because they are corrections rather than claims,
and both landed in `sec:earth_reintercept` as well as in the new subsection. The
single-impulse resonant dive is already a raise-then-drop, aphelion 1.9259 AU, boost 28.80
km/s radial plus 24.07 retrograde, so the outbound leg is not the novelty and only the
splitting is. And 37.53 km/s buys the payload's arrival at the dive perihelion and not the
opposing stream that has to meet it there.

The naming also moved. `sec:split_push`'s manoeuvre is now called the **two-wave departure**
in prose, its existing synonym, so that "split" means only the heliocentric split dive. The
section label is unchanged, so no cross-reference moved.

The three prices are worklisted in `docs/deferred_to_companion_repos.md`.
