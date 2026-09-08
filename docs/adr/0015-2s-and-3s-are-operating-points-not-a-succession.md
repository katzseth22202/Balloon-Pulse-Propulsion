# 2S and 3S are operating points, not a succession

Status: accepted (2026-09-08 grill, against companion `src/fly_and_park.py`, its
`docs/paper_corrections_fly_and_park_2026-09-07.md`, and ADR 0030). **Numbers pinned
2026-09-08** by companion ADR 0031 and asks S5-S8; the framing survived, the figures moved,
and one of them was being counted two different ways. See *What landed* below. The framing
was recorded before the numbers because the obvious reading of the result is the wrong one.
A later pass will see that 2S doubles 1.4x faster, conclude it supersedes 3S, and quietly
drop the launch-window argument that the same subsection is built on.

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

Phase counts are `synodic_lock()`'s `phases_offering_one` at both targets, with the coast
charged, so both columns are the same test.

| | doubling, Isp 1200 | doubling, Isp 2214 | phases offering a lock, Isp 2214 |
| --- | ---: | ---: | ---: |
| **2S lock** | 1.082 yr | **0.873 yr** | 26 of 73 |
| **3S lock** | 1.377 yr | 1.189 yr | **73 of 73** |

2S doubles about 1.4x faster and buys it by giving back the launch window. The asymmetry is
sharper than the table alone shows: **2S at the top exhaust speed still has a narrower window
than 3S has at Isp 1200**, where 3S reaches 44 of 73. So the fast option is not merely
narrower, it is narrower than the slow option's own conservative case.

That matters because the launch window is not a convenience. It is the argument that the
architecture does not need every departure to leave at once. Trading it away for doubling
speed is a decision an operator should make deliberately, with both numbers in front of them,
and not one the paper should make silently by quoting the faster clock.

## The gate under both, which is easy to lose

**Methalox cannot fly the 2S lock, and cannot pay for padding at all.** Stated as "neither
lock exists on methalox" in the first cut of this ADR, which is wrong: at Isp 380 no cycle
pads to 2.00 S, but a 3S lock does exist at 12 of 73 phases and doubles in 3.641 yr. What
methalox actually fails is the *padding*. Fly-and-park's exchange rate gives a 0.99 km/s
budget at Isp 380 s against a maneuver that costs a median +1.04 km/s, so it misses by about
5% and wins at 1 departure phase of 11 for a best gain of 1.002. At Isp 1200 s the budget is 3.13 km/s against
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
has accepted a 26-of-73 window, at which point the launch-cadence result is decoration.

**Reporting doubling and omitting the coverage trade.** Quoting 0.873 against 1.189 yr and
leaving window coverage to the 3S discussion. Rejected because the two sit close enough in the
text that a reader who checks will find them in tension and will not be told why.

**Waiting for S5 and S8 before recording anything.** The 2S lock is constructed here and not
yet chain-checked, so its numbers may move. The framing does not: if 2S survives, it survives
as a narrow-window fast option, and if it fails the chain the trade is what explains why the
paper ever considered it.

## Consequences

The paper owes a sentence on the trade wherever either lock is quoted, not once at first use.
`sec:synodic_lock` carries it. **Synodic lock** carries the naming that keeps this 2S apart
from the Jovian dive's two-synodic bend closure, which remains short by 6.84 degrees and is
not touched by anything here.

## What landed (2026-09-08, companion ADR 0031, asks S5-S8)

**The framing held and the mechanism changed.** The trade is still a trade, but the 2S lock is
not a new trajectory built by padding. It is the two-synodic resonance the paper already flies,
reached to every digit once the park is charged honestly.

1. **The 9-day park was inadmissible, and asking about it found a bug.** The park is the bound
   near-escape orbit's period lengthened, so it cannot be shorter than one 20-day lap. The
   companion's `MINIMUM_PARK` was 0.02 S, about eight days, 2.5x under the coast it stood for.
   Charging it moves the lock from phase 0.781 to 0.8082 and the clock from 0.84 to **0.873 yr**.
2. **Fly-and-park does not produce the 2S operating point.** Its park *is* the mandatory coast,
   plus about ninety minutes, so there is no remainder to pad. Fly-and-park stays what ADR 0030
   said it was, a way to let a shorter, hotter flight hold the 3S clock.
3. **The chain check ran and the locks survived it.** At every exhaust speed the best repeating
   policy is a single self-looping cycle, which is a lock, and it is the one `synodic_lock()`
   picks. ADR 0030's N4.2 lookahead caveat is discharged.
4. **The window is not what forces the flown 3S returns.** All eleven flown cycles are already
   exact locks, drifting under 1e-4 S. The four 3S fallbacks are ADR 0011's perijove floor,
   where only 45 of 91 two-synodic windows over 200 years clear 4,000 km. So the 2S lock
   retires a difficulty the architecture did not have, and the honest cadence claim stays
   "2S with a 3S fallback about half the time".
5. **One count in this ADR was two different tests.** The 73-of-73 above came off the
   usable-phase fraction while the 28-of-73 came off lock admissibility. Re-derived on one
   test, the table now reads 26 against 73, and the conclusion is unchanged.

**Not recorded here because the paper does not restate them:** the companion's own figures moved
(padding beats plain 3S at 16 of 30 phases at Isp 1200, not 17; the perfect-retrograde premium's
median is 1.037 km/s over 29 phases).
