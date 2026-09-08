# 2S and 3S are operating points, not a succession

Status: accepted (2026-09-08 grill, against companion `src/fly_and_park.py`, its
`docs/paper_corrections_fly_and_park_2026-09-07.md`, and ADR 0030). The numbers on the 2S
side are still under test as asks S5 and S8; the framing this records does not depend on
their exact values, and needs recording now because the obvious reading of the result is
the wrong one. A later pass will see that 2S doubles 1.4x faster, conclude it supersedes
3S, and quietly drop the launch-window argument that the same subsection is built on.

We adopt **two operating points**. The **3S lock** is the robust default and the **2S lock**
is the fast-doubling alternative, and the paper states the trade between them wherever it
states either. Neither replaces the other.

Jargon, since all three terms are new. A **synodic lock** is a cycle whose flight plus park
sums to an exact whole number of Earth--Jupiter synodic periods, so it returns to its own
departure phase and repeats with no steering. **Fly-and-park** is how one is built: fly
shorter and hotter than the window, then park the payload in the bound near-escape cycle
orbit for the remainder. A **usable phase** is a departure phase from which some closing
cycle actually grows the payload.

## Why this is a trade and not a ranking

The two claims the subsection wants to make pull against each other, and both are real.

| | doubling, Isp 1200 | doubling, Isp 2214 | usable phases, Isp 2214 |
| --- | ---: | ---: | ---: |
| **2S lock** | 1.00 yr | **0.84 yr** | 28 of 73 |
| **3S lock** | 1.38 yr | 1.19 yr | **73 of 73** |

2S doubles about 1.4x faster and buys it by giving back the launch window. The asymmetry is
sharper than the table alone shows: **2S at the top exhaust speed still has a narrower window
than 3S has at Isp 1200**, where 3S reaches 44 of 73. So the fast option is not merely
narrower, it is narrower than the slow option's own conservative case.

That matters because the launch window is not a convenience. It is the argument that the
architecture does not need every departure to leave at once. Trading it away for doubling
speed is a decision an operator should make deliberately, with both numbers in front of them,
and not one the paper should make silently by quoting the faster clock.

## The gate under both, which is easy to lose

**Neither lock exists on methalox.** Fly-and-park's exchange rate gives a 0.99 km/s budget at
Isp 380 s against a maneuver that costs +1.04 km/s, so it misses by about 5% and wins at 1
departure phase of 11 for a best gain of 1.002. At Isp 1200 s the budget is 3.13 km/s against
the same cost, roughly 3x headroom. The whole subsection is therefore conditional on driving
the Earth departure with the returning stream through the head-on nozzle rather than with
chemistry, which is the companion's **departure-burn accounting seam** and is unresolved as a
question of which model is right. It does not need resolving here: the result is a sweep
across the seam, reported as a continuum in departure Isp.

Two thresholds ride on that continuum and they are not the same number. Fly-and-park clears
its exchange rate at **Isp 1200 s**. Continuous departures, meaning every phase usable, need
**Isp 1900 s**. Both sit under the departure-nozzle ledger's own 2214 s.

## Considered and rejected

**2S as the target, 3S as the fallback.** The stronger claim, and it undercuts the
thundering-herd argument in the same subsection. A reader who accepts 2S as the design point
has accepted a 28-of-73 window, at which point the launch-cadence result is decoration.

**Reporting doubling and omitting the coverage trade.** Quoting 0.84 against 1.19 yr and
leaving window coverage to the 3S discussion. Rejected because the two sit close enough in the
text that a reader who checks will find them in tension and will not be told why.

**Waiting for S5 and S8 before recording anything.** The 2S lock is constructed here and not
yet chain-checked, so its numbers may move. The framing does not: if 2S survives, it survives
as a narrow-window fast option, and if it fails the chain the trade is what explains why the
paper ever considered it.

## Consequences

The paper owes a sentence on the trade wherever either lock is quoted, not once at first use.
`CONTEXT.md`'s **2S lock: constructed, not yet pinned** entry holds the 0.84 yr figure out of
the paper until S5 lands, and **synodic lock** carries the naming that keeps this 2S apart
from the Jovian dive's two-synodic bend closure, which remains short by 6.84 degrees and is
not touched by anything here.
