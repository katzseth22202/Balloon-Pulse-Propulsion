# Staged PuffSat mass parks in the staging ellipse, not at a Lagrange point

Status: proposed (all figures are two-body coplanar hand calculations from the 2026-08-12
grill; none have been run in the companion repo)

The closing paragraph of `sec:periapsis_challenges` stages crewed launches in two steps.
Solar-dive PuffSats push an unmanned carrier of PuffSat mass to near-escape speed at the
200 km interception altitude, where the 3.7 g costs nothing because nobody is aboard. Later
that carrier deploys its own PuffSats to push a crewed vehicle at the 2 g of
`sec:pregnant_women`. The paragraph never says where the loaded carrier waits in between, and
the obvious answer is a Lagrange point, since that is where everyone parks infrastructure.
We decided the carrier **stays in the orbit the solar-dive push already delivered it to**: the
50 km x 150,000 km staging ellipse of line 1444, with its perigee raised clear of drag while
parked. No Lagrange point is used anywhere in the staged path.

This needs recording because the Lagrange option is not merely available, it is intuitive, and
a future reader will propose it again. It is also the option the author proposed. The reason it
loses is counterintuitive and does not survive being restated casually.

## Why the Lagrange points lose

**The two destinations sit at nearly the same energy.** The staging ellipse has its apogee at
150,000 km. The Earth-Moon Lagrange points sit at 326,000 km (L1), 384,400 km (L4/L5), and
449,000 km (L2). Nothing in that comparison is a large energy gap, so the intuition that a
Lagrange point is "further out and therefore expensive" is wrong, and so is the intuition that
it is a cheap coast away.

**The entire cost is angular momentum.** The ellipse crawls through apogee at 0.45 km/s. The
Lagrange points sweep around the Earth at 0.87 km/s (L1) to 1.02 km/s (L4/L5), because they
co-rotate with the Moon. Arriving means speeding up to match; leaving means shedding it again.
That difference, not the radius, is the bill.

Round trips from the ellipse:

| Destination | In | Out | Round trip | Buys |
|---|---|---|---|---|
| Staging ellipse (stay) | 0 | ~31 m/s perigee arming | **~50 m/s** | returns to apogee every 2.7 d for free |
| Earth-Moon L1/L2 | ~0.88 km/s | ~0.65 km/s | ~1.5 km/s | lunar-ISRU propellant, quiet thermal, no shell crossings |
| Earth-Moon L4/L5 | ~0.83 km/s | ~0.83 km/s + phasing wait | ~1.7 km/s | stability, no station-keeping |
| Sun-Earth L1/L2 | months | months | ~180 d of transit | best cryogenic environment |

The L1 round trip is roughly 35% of a loaded carrier as methalox. The Sun-Earth points fail on
cadence rather than propellant: at 90-day transits a carrier serves about two launches a year.

**The reusability the proposal wanted is already free.** The motivation for parking was that
co-flying sensor hardware is expensive and should be recovered rather than expended. But the
ellipse has a 2.7-day period, so anything left in it returns to apogee on its own, forever, at
no cost. There is nothing to send back because nothing ever left.

## What the paper's existing Lagrange numbers do not tell you

`sec:handling_space_debris` already prices Lagrange insertion at about 0.5 km/s for Earth-Moon
L1 and 0.18 km/s for L4/L5. Those figures are computed for a disposal package **falling inward
from the 900,000 km turnaround of a near-escape trajectory**, which arrives at lunar distance
around 1.2 km/s and needs only trimming. They do not transfer to a departure from the staging
ellipse, which approaches the same radius from below at a fifth of that speed and must be
accelerated rather than braked. Reusing them here would understate the cost by a factor of four.

## Consequences

- **Perigee is now a managed quantity.** The 50 km perigee of line 1444 exists to deorbit spent
  hardware, which is fatal to something meant to sit for months. Parked carriers hold a
  drag-free perigee and each deployed PuffSat spends about 31 m/s of its own microthruster
  budget to drop to the 50 km disposal perigee. The "very small rockets" of the original
  proposal turn out to be the PuffSats' existing thrusters.
- **Shell crossings become the architecture's exposed flank.** A parked carrier sweeps the LEO
  and GEO belts every 2.7 days, and `sec:handling_space_debris` line 543 sells lunar disposal on
  exactly the opposite property. The reconciling argument is that line 543 concerns
  *uncontrolled* objects, which arrive billions per year and can never participate in
  conjunction avoidance, while carriers are few, tracked, and maneuverable. Molniya and every
  GTO are the precedent. This argument owes a steady-state carrier population count.
- **Lunisolar perigee drift is unsized and gates the whole budget.** At 150,000 km apogee the
  carrier sits at 39% of lunar distance. Months of third-body tugging move perigee by an amount
  nobody has computed, and that number sets the parking margin, which sets the per-flight
  delta-v. If it comes out badly, raising the parking perigee to ~2500 km costs ~75 m/s each way
  and is the priced fallback.
- **Storage now has to be designed, which line 424 previously excused.** See the **storable
  PuffSat** entry in `CONTEXT.md`.
