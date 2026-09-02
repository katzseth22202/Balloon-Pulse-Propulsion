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

## Resolved 2026-09-02: all three prices came back, and two of them went the other way

Companion `docs/paper_changes_owed.md` P2--P5b answers S1, S2 and S3. **Status is now
resolved.** The three holds are lifted, but only one of them is lifted in the direction this
ADR was waiting for.

**The dominance claim (S1) is retired, not lifted.** The far node does not need mass at
1.9649 AU, it needs mass moving at 153.35 km/s there against a vehicle doing 13.45. A
delivery arriving co-moving is worth nothing as an impactor. Buying that speed from 1 AU
costs 113.20 km/s of Earth departure excess (co-linear, a bound; 125.80 for the perpendicular
arrival actually made) and delivers 1.0% of what is launched. Charged, the partial split's
1.536 kg/kg becomes **3.552 against the paper's 2.365**, so it no longer beats the dive it
was said to dominate. `sec:split_dive_growth` strikes the dominance framing rather than
strengthening it, and keeps the partial split as the family's rate optimum *before* delivery
is charged. The structural result that replaces it is that the phased closures' leftovers are
the only affordable source of far-node ammunition, because the cheap way to make fast mass is
to drop it down the Sun's well first.

**The architecture claim at shallow depth (S2) is answered against the split.** 38.10 km/s of
perihelion burn, 1.059x the paper's tuning, holds the direct departure conducting out to the
22.93 R☉ pad floor, and the cycle still grows there at 2.505 per pass and 0.657 yr doubling.
The extra 6% costs 7.4% of node survival and about 1% of clock, and the clock moves the
helpful way. So the conduction crossing shows the direct route cannot fly shallow *at the
paper's tuning*, not that the split is required. **The weaker claim this ADR chose to publish
was the true one**, and ADR 0023's stronger reading does not survive. The depth window stays
withdrawn for a new reason: at 38.10 km/s the crossing (23.01 R☉) rises *above* the pad floor
(22.93), so the band is empty.

S2 also returned a larger finding this ADR did not anticipate. `sec:self_cooling_departure`'s
"doubling degrades only from 0.305 to 0.358 yr" was an artefact of holding node survival at
0.60 down the whole depth dial. Derived, survival falls to 0.2589 at 22.93 R☉ and 0.1629 at
32, and doubling runs 0.3075 / 0.6570 / 0.9484 yr. The near-flatness of the held column was
the illusion that made backing the dive out look nearly free. `tab:derived_node_survival` is
the correction. The published 4 R☉ headline is unaffected; the two agree to 0.9% there.

**The ledger gap (S3) is traced, and it retires this ADR's planned restructure.** No ledger
charges the opposing stream's placement, so the omission was real. Charged, it is worth
1.0014x to 1.0075x of doubling on the Jovian cycle and 1.0063x to 1.0112x on the paper's
dive, and 0.45--2.00% of pad return, flipping no verdict. The reason is mass rather than
impulse: at `k` = 30 the node wants only 0.17--0.49 kg of opposing stream per impactor
kilogram of payload. **So the two-arrival asymmetry does not become `sec:split_dive`'s
spine.** Leading a subsection with an effect worth under 1.2% of doubling would misrepresent
its size. `sec:split_dive` keeps the Delta-v family as its opener and
`sec:opposing_stream_depth` states the asymmetry with its bound and with the architecture the
35.48--44.94 km/s belongs to, since the Jovian cycle places the same stream for 11.06--11.83.

**A separate decision landed in the same pass** and has its own record: node-depth
admissibility, `docs/adr/0008`.

**One further bound came back that this ADR did not ask for.** "The split buys the pad" was
only ever made in launched-slug currency. Scored on the committed fifteenth with survival
derived, the split clears the floor over (4, 5.58] R☉ and its edge over the direct route
shrinks 1.80x to 1.29x to 1.09x from 4 to 22.93 to 32. At the recommended shallow end neither
architecture earns its launch. `sec:self_cooling_departure` now opens with that.

