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

## Amendment, 2026-09-19 (second grill): the signature argument

The section now argues that an orbital data center is easier to *hit* than an ordinary
satellite, not only more valuable to hit. The claim is deliberately **permissive rather than
motivating**. It says the bright signature lowers the technical bar and strips the defences,
and it leaves motive where the rest of the ADR already puts it, in concentration plus the
demonstrated March 2026 outage. The strong version, that brightness explains why data centers
are struck and other satellites are not, was retired: a science platform is brighter than
almost anything in orbit, has been reachable for decades, and removing it buys an attacker
nothing.

The physics is that computing does no mechanical work and stores no energy, so the signature
is the power draw. `eq:orbital_radiator_area` puts **5 GW** at about **12 km^2** of emitting
area at 300 K, which is the scale of the **4 km** panels Starcloud filed, so the published
panel size is a measurement of the waste-heat problem. A collector that size intercepts about
**16 GW** of sunlight against the ISS's **3.4 MW** over 2500 m^2, so about **5000x**, and
about **70x** in seeker acquisition range by the inverse-square law.

`wright2005_physics_space_security` turned out to analyse this exact attack, and its headline
verdict is *against* the paper: a simple pellet ASAT "may have limited effectiveness." The
section states that verdict and answers it, because both of the manual's limits scale with the
target. Orbit determination and missile CEP were priced for satellites a few metres wide, and
the manual doubts a low-capability state could even obtain a ranging radar. That promoted
trackability from a one-sentence aside to a load-bearing claim, reversing an earlier decision
in the same grill. The manual also supplies two figures the paper had been asserting uncited:
its own model carries **500 kg** of pellets to 600 km on a Nodong-class missile, above the
paper's 300 kg, and it puts the shielding floor near **1 g** and **1 cm**, which is the
paper's pellet.

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
- **Claim that orbital data centers nullify space launch as well as AI.** Retired on the
  mechanism, not on the politics. Destroying a cluster does not remove launch demand, it creates
  replacement demand. The only route from a strike to a stalled launch market runs through denial
  of the band, and that claim was deliberately calibrated down from "cannot be re-occupied" to
  "degraded for decades." What is asserted instead, in the first paragraph, is that a cluster
  holds the accumulated delivery of a launch campaign, so one cloud reaches all of it at once.
  That is a statement about concentrated capital and it needs no forecast.
- **Carry crypto as a third concentrated sector.** Retired: `sec:space_data_centers` already says
  miners need prompt block updates, and that penalty vanishes at 650 km. Crypto is the one workload
  that prefers the orbit being argued against, so naming it hands over a counterexample.

- **Argue the signature as the reason this target class is selected.** Retired: the ISS and
  Hubble are brighter and easier than an ordinary satellite and have never been attacked.
  Brightness is permissive. Motive stays with concentration and the demonstrated outage.
- **Keep radar cross-section as a co-equal pillar with infrared.** Retired at first, then
  partly reinstated. A flat panel returns a large echo only near normal incidence, while
  thermal emission leaves both faces over a broad angle, and the SSN already tracks 10 cm
  objects. But the manual makes orbit-determination accuracy one of two factors deciding
  whether the cheap attack works at all, so trackability carries real weight. It is argued as
  target size defeating the manual's stated limit, not as a seeker claim.
- **Print an absolute seeker acquisition range.** Retired: it needs an aperture and a noise
  floor for a seeker nobody has published. The ~5000x ratio and the square-root scaling are
  claimed instead.
- **Re-derive the 300 kg cloud from the aiming error rather than the cluster radius.**
  Retired: coverage and aiming are different requirements that favour opposite target sizes,
  and 300 kg answers coverage. Aiming is stated separately. Recorded in `CONTEXT.md` under
  **Coverage versus aiming** so a later reader does not "fix" one into the other.
- **Cite `wright2005_physics_space_security` only where it supports the paper.** Retired: a
  referee who opens the source finds the "limited effectiveness" verdict on the same pages.
- **Open a separate ADR for the signature argument.** Retired: it is the same section, the
  same framing decision and the same exemplars, so it amends this one.

## Consequences

- `sec:space_data_centers` splits its threat paragraph into four, one job each: the target and
  who has already hit this orbit class; the cheap unguided shot and its reach; why debris does not
  deter; what distance changes. Three was the plan, but the pellet arithmetic and the reach claim
  would not share a paragraph with the Fengyun-1C material without running past 250 words.
- Concentration is now argued in both directions, on purpose. The first paragraph asserts it
  positively: a cluster on one track has no equivalent of the third availability zone that
  survived the March 2026 strike, and it holds a launch campaign's accumulated delivery. The
  fourth paragraph concedes that distance does not fix it. Neither half stands alone.
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
- Three paragraphs are added after "A cluster on a fixed orbit is the softer target": the
  published pellet benchmark and the aiming/tracking answer; the irreducible signature with
  its arithmetic and the homing claim; what the signature takes away from the defender
  (no hiding, no decoys, a dodge that only answers an unguided cloud, and a seeker that finds
  the compute rather than the panels). The last of these closes with the filter clause, that
  brightness alone is not a reason to be attacked.
- The countermeasures paragraph's Starcloud sentence gains one clause, "The homing shot above
  is what turns that exposure into a kill." Without it the paper concedes that large-area
  designs beat the cheap attack and never says what kills them.
- **The filter clause is deliberate, like the concentration concession above. Do not delete it
  as self-undermining.** It is what keeps the permissive framing honest.
- New `references.bib` entries, all verified against the live sources on 2026-09-19:
  `wright2005_physics_space_security` (American Academy of Arts and Sciences, 2005),
  `nrc2012_bmd` (National Academies Press, DOI 10.17226/13189), `nasa_iss_solar_arrays`.
- "Terminal guidance" stays reserved for the PuffSat rendezvous sense. The threat model says
  *homing*, *seeker* or *homing interceptor*. Logged under Flagged ambiguities in `CONTEXT.md`
  alongside the "pellet" collision.
