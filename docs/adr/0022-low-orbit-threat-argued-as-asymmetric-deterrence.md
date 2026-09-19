# The low-orbit data-center threat is argued as asymmetric deterrence, and concentration is conceded

Status: accepted (2026-09-19 grill). Recorded because a later reader will ask why a propulsion
paper argues deterrence economics in `sec:space_data_centers`, and why the section concedes a
vulnerability that the proposed Lagrange-point site shares.

The section used to state the low-orbit threat as capability plus countermeasure. Ground-launched
weapons exist, a tight cluster is a soft target, spacing and dodging answer part of it. Naming the
2007 FY-1C test as the demonstrated capability opens an objection that framing cannot answer.
FY-1C is still the only destructive intercept above 500 km in nineteen years, and every later test
was flown low on purpose so the fragments would fall: USA-193 at about 250 km, Microsat-R at about
283 km, Cosmos-1408 at about 480 km. Read as capability alone, that record says the attack is one
states have looked at and declined to repeat.

The answer is that the restraint is priced in assets held in the band. An attacker with little
there to lose is not paying that price, and the debris that deters the owner is part of what the
attacker is buying. The threat is therefore stated as an exchange rather than as a capability.

- One medium-range ballistic missile and **300 kg** of gram-class pellets, against an
  **81-satellite** cluster (Suncatcher, section 2.2). Both halves were already sourced.
- The attack needs **one** successful lob. Counterforce that cuts an arsenal by an order of
  magnitude leaves the threat intact, so production-rate arguments do not bear on it.
- A struck data center can be rebuilt. A contaminated shell stays degraded for **decades**, and
  the replacement cluster inherits a conjunction environment the original did not have. Calibrated
  deliberately: "cannot be re-occupied" is too strong, because operators do fly debris-rich bands
  (Starlink at 550 km). Months against decades is the comparison that carries the argument. If a
  referee pushes, the reserve answer is that a formation-flying cluster tolerates conjunctions far
  worse than Starlink does, since every dodge perturbs the formation it is holding.

What distance buys is priced separately, because only part of it survives scrutiny. A vertical lob
to 650 km needs **3.40 km/s** of burnout speed. A shot to Sun-Earth L1 or lunar distance needs
near-escape, **11.01 km/s** at 200 km, which is **22 times** the mass ratio on solid propellant at
250 s and 12 times on storable liquid at 310 s. Nothing with that mass ratio is road-mobile. The
FY-1C interceptor went off a transporter-erector-launcher, while the deep-space shot needs a fixed
pad and a campaign that can be watched. Days of transit then buy what minutes cannot, which is
emergency dispersal and interceptor activation.

Concentration is conceded. A Lagrange-point data center puts the same compute and the same launch
demand in one place, and is harder to duplicate than a low-orbit one. Distance changes the price of
the shot and the recoverability of the site. It does not change how much sits in one place.

## Considered options

- **State the threat as capability only and never raise debris.** Shortest, and defensible since
  the pellet cloud's own debris is a question the paper never opens. Retired: it leaves the
  nineteen-year gap standing as an unanswered objection and gives up the strongest argument
  available for distance.
- **Answer the gap in the crowding paragraph instead**, with the general point that an attack
  anywhere in the band threatens everyone in it. A good argument for distance, and it stitches a
  seam that is currently open between the threat material and the traffic material. Retired as the
  primary answer: it explains why the band is fragile, not why an attacker would proceed.
- **Extend the pellet model to large-area architectures.** Retired: `pi R^2 / sigma` counts hits,
  not kills. Starcloud's 4 km by 4 km unit gives `sigma = 1.6e7 m^2` and the formula returns about
  1.6 pellets, which is not a result. The model is scoped to one-hit-one-kill satellites instead,
  and the inversion is worth one sentence: compact clusters are pellet-fatal, large-area designs
  are pellet-tolerant but impossible to miss.
- **Name a state as the deterring actor and assert its strategy.** Retired: the paper can assert
  what an actor demonstrably did, the March 2026 strike and Qaem-100's reach, without imputing
  intent it cannot source. A referee would read an intent claim politically.
- **Count the attacker's satellites to quantify the asymmetry.** Retired: a count invites a quibble
  over the number when the claim is about what the attacker values, and the available sources are
  tracking sites rather than publications of record.
- **Price the exchange in dollars.** Retired: it needs a data-center capital cost, which
  `sec:space_data_centers` deliberately excludes. The section says its transport figures "exclude
  the purchase and operation of the data center itself."
- **Price the exchange by mass.** Retired: the Suncatcher paper gives no per-satellite mass and no
  constellation mass. Only Starcloud-1's 60 kg demonstrator bus is public, and that is not an
  operational unit.
- **Carry crypto as a third concentrated sector.** Retired: `sec:space_data_centers` already says
  miners need prompt block updates, and that penalty vanishes at 650 km. Crypto is the one workload
  that prefers the orbit being argued against, so naming it hands over a counterexample.

## Consequences

- `sec:space_data_centers` splits its threat paragraph into four, one job each: the target and
  who has already hit this orbit class; the cheap unguided shot and its reach; why debris does not
  deter; what distance changes. Three was the plan, but the pellet arithmetic and the reach claim
  would not share a paragraph with the Fengyun-1C material without running past 250 words.
- **The concession closing the fourth paragraph is deliberate. Do not delete it as self-undermining.**
  It is what keeps the rest defensible, because a referee who notices that the Lagrange site
  concentrates just as much will otherwise raise it unprompted.
- The pellet count now carries a scope clause. Any later citation of a large-area architecture must
  not be read as covered by it.
- "Pellet" now has two protected senses, hostile weapon and never a **PuffSat**. Both are recorded
  in `CONTEXT.md` under **Orbital data-center threat model**, with the collision logged under
  Flagged ambiguities.
- Starcloud enters as a second exemplar alongside Suncatcher: sun-synchronous, about 06:00
  crossing, 600 to 850 km, up to 88,000 satellites filed with the FCC in March 2026. Its band
  contains the FY-1C intercept altitude of 845 to 865 km, which carries the reach claim with no
  arithmetic. The Qaem-100 lob calculation stays, because it covers a different actor reaching
  Suncatcher's 650 km.
- The DIA citation stays for the Russian half of the capability claim, since FY-1C says nothing
  about Nudol.
- New `references.bib` entries owed: CRS RS22652, NASA Orbital Debris Quarterly News 11-2, the
  Starcloud FCC filing via SpaceNews, and Starcloud-1. Arsenal figures, if used, go to CSIS
  Missile Threat or IISS rather than the advocacy-leaning outlets that carry the rebuild reporting.
