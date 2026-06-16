# This is stuff that needs reconciliation with paper

* active transponder on PuffSat.  Measures both distance and doppler velocity shifts
* at least 4 coordinator nodes, with both perigee and apogee updated.   Consider also using GNSS signal below geostationary orbit.
* Big one.  GOCE level accelerometer is kilogram scale technology and is not something that fits on a PuffSat.  Probably why we can't get millimeter scale PuffSat working.
* We only target Puffsat accuracy to 1 meter.  Assumption is pusher plate can move, shock absorber can reshape to keep pulse centered.  Rockets on main craft also help.
* Van Allen radiation shielding is provided by Puffsat itself.  Relatively easy for outer Van Allen belt - time through inner belt with high energy protons is short enough to accept risk.   Triple mmjority redundance (used on SpaceX - need source)
*torque but if spacecraft is long, force may be small for reaction wheels - when there is an off center impact.
* is it easier to do 1mx1mx50m uncertainty of 2m sphere uncertainty and which is relevant?
* propose 3m/s omnidirectional thrust capability of rocket, Gaussian distributed with .5 m/s standard deviation, align once per second. 
* do we need GNSS if we have this precise measuring/broadcasting from the rocket coming up from the ground and any ground infrastructure, which seems like everything is much closer than GNSS to the key impact point
* What if the part of the trajectory above 800 km just needs accuracy within 30 km in absolute terms of where interception is, but then the PuffSat formation (each PuffSats relative position is accurate to within 1 meter radius)?  The rationale is the plane can fly to meet the formation.  Once the pusher impacts start, then the structure of the PuffSats should be constant - so the bottom one can be shifted as long as shape of every remaining PuffSat is within 2 meters of relative target.
* We should discuss that for 5 meter wide plate, its OK because plate needs some mass anyway to smooth acceleration without unreasonably long shock absorber.
* star maps may be enough for necessary angular resolution estimated at 10 micro-rad on the main plane
* torque correction is RCS + rocket engine - non,toxic fuel obviously
* note the plane can adjust its starting point by 10s of kilometers, so if there is systemic drift in PuffSats is OK as long as PuffSat formation shape is good looking.
* Explain issues with Medussa large strechy parachute, but possibility to do at sides.   
* explain possibility of 1/1 pusher plate
* explain hardware encryption of repeated signal.  Question need for coordinator nodes.  Two telescopes on opposite side of rockets, 10 microradians, satellites may only be hundres of kilometers apart in orbit even though the distance grows much larger at perigee.  At around 2500 km, bigger satellite changes orbits to raise perigee, come around one more time for its landing spot with another apogee burn.
* brief note about geopolitcal overflight risks of PuffSat suborbital travel
* slow down PuffSat can't be purely low Earth orbit because of atmospheric drag.
* space only GNSS.   ka-band higher frequency helps doppler and range accuracy.  Verifying no coordinator nodes needed.
* for shock physics, higher atmosphere - string of pearls shaping to elongate the design 

---

# Long note (2026-06-12): Medusa-behind geometry and rigid pusher-plate mass / frequency / absorber trade-offs

This note is a handoff for two edits we agreed to make later, plus a recommendation on what belongs in the main text versus an appendix. Nothing here is in the paper yet.

## 0. Resolved: behind = compression

The prompting message said "the struts are in tension"; confirmed that was a slip. Our behind-mounted sail puts the struts in **compression** (tension is real Medusa, sail in front). This note is written for the behind/compression design throughout. The front/tension option survives only as the uncrewed-cargo fork in Part A.

## A. Clarify: our Medusa-style sail is behind the rocket (compression), which makes it a different design from real Medusa (tension)

This is the gap in the current text. Line 717 says the flexible pushers are "mounted behind the rocket on shock-absorbing struts" but never states the structural consequence.

**Physics of the difference**
* Real Project Medusa: sail ahead, payload behind, bomb detonated in the gap. Every connective member is in tension. Tension members do not buckle, so Medusa cables can be very long and very light.
* Our design: PuffSats approach from the rear, so the sail is behind the rocket. To add forward momentum, the gas must move forward faster than the craft and strike the rear face of the sail, pushing it forward into the craft. The members between sail and craft therefore carry **compression**.
* Consequence: compression members buckle. Euler critical load P_cr = pi^2 E I / (K L)^2 falls as 1/L^2, so a roughly 100 m compression strut is a far harder structural problem than a 100 m Medusa tether. That is the real, substantive difference between our concept and Medusa.

**Why we keep the sail behind anyway (the rationale to state)**
* Forward acceleration with *external* reaction mass forces the source PuffSat to approach from behind and overtake the craft. A front-mounted (true-Medusa, tension) sail would require every PuffSat to thread past the crewed vehicle at km/s, making the crew cabin the first thing a mis-aimed hypervelocity solid meets.
* A rear sail is fail-safe by geometry: size the sail silhouette at least as large as the craft, and any PuffSat that misses the sail also clears the craft; overshoots and duds fly off into empty space behind. The expendable membrane always shields the crew.
* So the compression/buckling mass penalty is the price of keeping humans out of the firing line. This is the design justification the section is currently missing.
* Fork for uncrewed cargo: front/tension (light tethers, no buckling) becomes attractive when a rare strike is a lost vehicle, not lost lives. Connects to existing note line 17 ("possibility to do at sides") and the cargo case.

**Sail can be light relative to the craft**
* Long stroke buys a light sail. The sail sits on the same buffer invariant as the rigid plate (Part B): m_sail * s is approximately M a T^2 / (2 to 4).
* For a 100 m stroke and a few-m/s per-pulse delta-v on a 32 t craft at 3 g, the sail floor is about 100 kg, roughly 4 kg/m^2 over 25 m^2, about 0.3 percent of the craft. That areal density is also what the layered Nextel-720 / felt / Vectran-net sail needs for the heat, so the structural floor and the thermal floor coincide.

**Strut mass (compression, buckling-limited)**
* Peak strut load is set by the craft, F = M a, about 1 MN at 3 g (design about 2 MN at safety factor 2), independent of stroke.
* Monolithic CFRP tube, pin-ended, 100 m: about 10 to 12 t. Too heavy; the L^2 penalty dominates.
* Guyed or lattice CFRP boom (effective buckling length about 15 m via tension stays): about 1.5 to 2 t. Viable.
* Steel is about 4 to 5 times heavier than CF for the same buckling load. Buckling depends on stiffness E, and every steel has the same E of about 200 GPa, so "compression-resilient" high-strength steel buys yield strength we do not need and zero extra buckling margin. The buckling figure of merit is sqrt(E)/rho, where high-modulus CF beats steel by about 5x.
* The real "combination" that beats buckling is a compression member braced by tension guys (sailboat-mast principle): CF boom carries the compression, Vectran or thin steel stays carry tension and cut the effective buckling length. Reserve titanium or steel for joints, end fittings, and damper cylinders, where concentrated ~1 MN bearing loads, impact, and fatigue matter and CF is brittle and notch-sensitive.
* Telescoping helps for free: peak force occurs at maximum compression (shortest length); full extension (100 m) coincides with near-zero force. So the buckling-critical length at peak load is well under 100 m, and a naive fixed-100m-column estimate overstates the mass.
* Net pusher assembly: order 1.5 to 2 t of structure plus 0.1 to 0.3 t of sail, a few percent of a 32 t craft.

## B. Rigid pusher plate: mass / frequency / shock-absorber trade-offs

This formalizes note line 13 ("plate needs some mass anyway to smooth acceleration without unreasonably long shock absorber") and supersedes the worst-case "1/1 pusher plate" idea in note line 18 (we can reach about 10 percent of craft mass or less).

**The buffer invariant**
* A rigid plate on a shock absorber is a momentum buffer. To give the craft acceleration a, the average force is F = M a, so each pulse carries impulse J = M a T, with T = pulse period = 1/f.
* A pulse kicks the plate velocity by delta-v_p = J / m_p. The absorber arrests that recoil over stroke s at force about M a. Result:

    m_p * s  is approximately  M a T^2 / 4  =  M a / (4 f^2)

  The prefactor is 1/4 to 1/2 depending on the absorber's force-versus-stroke profile.
* At fixed stroke, m_p scales as T^2 = 1/f^2. So 1 Hz to 4 Hz is a 16x lighter plate. The product m_p * s is what is fixed; the plate is only "heavier than the craft" if you pair low frequency with a short stroke.

**Two views of the same curve (32 t craft, 3 g)**

Plate mass versus stroke at 1 Hz:

| Stroke at 1 Hz | Plate mass | Percent of 32 t craft |
|---|---|---|
| 2 m  | ~118 t | 370% (absurd) |
| 10 m | ~24 t  | 74% |
| 30 m | ~7.8 t | 24% |
| 73 m | ~3.2 t | 10% |

Stroke needed to hold the plate at 3.2 t (10 percent of craft) versus frequency:

| Pulse rate | Stroke for a 3.2 t plate |
|---|---|
| 1 Hz  | ~73 m |
| 2 Hz  | ~18 m |
| 4 Hz  | ~4.6 m |
| 10 Hz | ~0.7 m |

**Worked example we like (4 Hz, 4.6 m)**
* m_p about 3.2 t (10 percent of craft), stroke 4.6 m. Both buildable.
* Per-pulse impulse J = 235 kN.s. Plate recoil delta-v_p about 73 m/s. Plate's own deceleration about 60 g (fine, no humans on the plate). One pulse equals 25 kg of gas at about 5 km/s closing, self-consistent with the PuffSat design.
* Areal density 3.2 t / 25 m^2 is about 128 kg/m^2. Survivability floor is probably 10 to 50 kg/m^2, because PuffSat total impulse is orders of magnitude below Orion's (line 713), so about 0.25 to 1.25 t. Dynamics set the 3.2 t here, not the floor, with 3 to 12x margin. Higher f could ride the plate down toward about 1 t before survivability stops it.

**The ripple problem (the real work item at 4 Hz)**
* The plate pushes only during the compression half of each cycle, so a plain absorber gives the craft a force swinging roughly 0 to 6 g (twice the 3 g mean) at 4 Hz. 4 to 8 Hz vertical is the worst whole-body vibration band (ISO 2631).
* Plate mass does not fix this. A heavier plate just moves slower; ripple amplitude is set by duty cycle and absorber law, not by m_p. Smoothing comes from absorber design and frequency.

**The two-stage absorber (Orion heritage, the smoothing answer)**
* Orion connected the pusher plate to the vehicle through a two-stage absorber tuned to two different frequencies. The first-stage embodiment varied across iterations (toroidal gas bags or peripheral pneumatic cylinders), with a long central pneumatic/mechanical column as the second stage. The two-stage, frequency-separated principle is the constant.
* Cascaded mechanical low-pass filter:
  - First stage (plate to intermediate structure): stiff, short stroke, high frequency. Catches the sharp millisecond blow; the plate does its 60 g, 73 m/s bounce here. This is the about 4.6 m budget.
  - Second stage (intermediate structure to crew module): soft, long stroke, low natural frequency f_n. With f_n well below the pulse rate, it filters the ripple.
* Isolation at 4 Hz, transmissibility T is approximately 1 / ((f/f_n)^2 - 1):

| Second-stage f_n | Ripple attenuated by | Crew feels | Static deflection under 3 g |
|---|---|---|---|
| 1.0 Hz | ~15x | 3 g +/- ~0.2 g  | ~0.74 m |
| 0.7 Hz | ~32x | 3 g +/- ~0.1 g  | ~1.5 m |
| 0.5 Hz | ~63x | 3 g +/- ~0.05 g | ~3.0 m |

* A second stage at f_n about 0.5 to 1 Hz turns the 0 to 6 g swing into 3 g plus or minus a few tenths, with a second-stage static deflection of about 0.7 to 3 m under the mean 3 g load (very buildable). Two stages, not one: a single soft absorber would let the plate wander meters on every blow and could not take the peak pressure; a single stiff one transmits the jolt.
* With a good two-stage absorber, the duty-cycle skew (long push, quick re-cock) and multi-plate phasing become optional refinements, not necessities.

## C. What to put in the main text versus an appendix

Recommendation: keep the conceptual claims in the body and move all the formulas, tables, and the worked example into one appendix. The two topics share the buffer invariant m * s is about M a T^2 / 4, so they belong together.

**Main text, Medusa paragraph (line 717), 2 to 3 sentences**
* State that our sail is mounted behind the rocket, so its struts carry compression, unlike real Medusa's tension cables, and that compression members buckle (the L^2 penalty), which is the structural difference.
* State that the rear mount is a deliberate fail-safe choice: the expendable sail shields the crew and overshoots fly off behind, whereas a front/tension sail would force every PuffSat past the crew cabin.
* One sentence: the front/tension variant suits uncrewed cargo. Keep all buckling numbers out of the body.

**Main text, pusher-plate subsection (around line 739), 2 to 3 sentences**
* More frequent pulses let the plate be lighter; plate mass falls as 1/f^2 at fixed stroke, so we are not forced into an Orion-scale plate.
* A two-stage absorber as in Orion smooths the ride: a stiff short-stroke first stage catches the per-pulse blow, and a soft long-stroke second stage with natural frequency well below the pulse rate isolates the crew. Cite Orion. This slots in right where line 739 already lists MR fluids, magnetic braking, springs, and hydraulics.

**New appendix: "Buffer mass, stroke, and pulse frequency"** (single appendix, two subsections)
* Subsection 1, the rigid plate: derive m_p * s is about M a T^2 / 4 and the 1/f^2 scaling; the two trade tables; the 4 Hz / 4.6 m / 3.2 t worked example with derived quantities and the survivability-floor margin; the ripple analysis and the two-stage transmissibility table.
* Subsection 2, the Medusa sail and struts: the same invariant at long stroke giving the about 100 kg sail; the strut buckling numbers (monolithic vs guyed/lattice CF, the sqrt(E)/rho point, steel 4 to 5x penalty, titanium/steel only at joints); the telescoping-helps-buckling point; the front-vs-rear fail-safe argument with the overtaking kinematics.
* Rationale: the body keeps the three conceptual claims (lighter plate via frequency, two-stage smoothing, fail-safe rear mount); the appendix carries the math so a skeptical reader can check it without bogging down the narrative. Unifying thread: the sail (long stroke, light) and the rigid plate (short stroke, heavy or fast) are the two ends of one m * s invariant.

## D. Precision tiers: near-term meter-class (Section 2) vs later near-Sun millimeter-class, and the forgiving-plate consequence

This reframes the paper's navigation-accuracy claims. We can walk before we run, and the order is counterintuitive: the near-Earth near-term work needs only meter-class precision, and the tight millimeter precision belongs to the later near-Sun stages, where the dynamical environment is actually cleaner. It also revises the plate recommendation in Part B upward, on purpose.

### D.1 Near-term architecture (the Section 2 scenarios: LEO launch, suborbital transport, Starship-pushed)

Required interception tolerances. These are requirement ceilings, not best-case capability:
* Along-track (approach axis): about 100 m, equal to about 10 ms of timing slop at a roughly 10 km/s closing speed. In meters this scales with closing speed; at lower closing speeds the same 10 ms is fewer meters. This is cheap: detonation triggers on proximity (the ice-wire layer, line 201), the plate is moving and the absorber reshapes to keep the pulse centered (note line 6), and the rocket's RCS absorbs the 10 ms timing error. Along-track error mostly sets *when* the pulse lands, not *whether* it lands on the plate.
* Cross-track (lateral, on the plate face): up to 2 m. This is the binding one, because the pulse must land on the plate. A 2 m miss on a 5 m-wide plate (2.5 m half-width) still lands with about 0.5 m of edge margin.

The 5 m plate doubles as a disaster shield: if PuffSat gasification is imperfect and a solid fragment escapes (the 250 g dry mass, or incompletely vaporized propellant, see line 663 disposal strategies), the oversized plate catches it instead of the craft.

Consequence for plate mass and stroke (revises the Part B 3.2 t / 4.6 m point upward, which is fine):
* Accepting up to 2 m lateral miss means off-center impacts up to 2 m, which apply a torque (note line 8). A larger, heavier 5 m plate has more rotational inertia and resists tip-over from off-center hits; a longer absorber stroke buys more time to recenter the plate and let the RCS cancel the moment between pulses. So the relaxed cross-track requirement *justifies* a heavier plate and a longer stroke than the mass-minimizing point.
* This sits comfortably above the m_p * s buffer minimum (Part B), so it costs nothing in feasibility. A heavier plate plus a longer stroke just means we operate with peak-g and smoothness margin rather than at the minimum. We trade mass-optimality for forgiveness, deliberately, in the near term.
* Reframe the paper's current lateral claim. Lines 630 and 692 state centimeter-scale (5 cm std dev) centering as the near-term assumption. That should be reframed: cm-scale is the achievable/nominal capability (VISORS-class), but the near-term *requirement* is only about 2 m lateral on the 5 m plate. Stating the loose requirement, not the tight capability, makes the near-term feasibility case far more robust and honest. The cm capability becomes margin, not a load-bearing assumption.
* The RCS must still cancel the off-center torque from a 2 m miss (lines 684 and 692 already invoke this). A larger miss means more torque, so that is the cost we pay for the relaxed nav: more RCS authority, paid against a heavier plate's stability.

### D.2 Later architecture (near-Sun direct collisions: no-ISRU rocket, World Set Free, interplanetary highways)
* Here we switch from gas puffs hitting a plate to solid projectiles colliding head-on directly (lines 335, 351), at very high speed (100 to 250 km/s effective-exhaust regimes). This *does* demand millimeter precision, and line 351 already says so.
* The burden is shared, not all on the projectile: the main rocket's sensors and RCS make the terminal adjustments to meet a slightly-off-target incoming retrograde projectile (consistent with line 684). So millimeter precision is the closing-gap requirement of the rocket-plus-projectile pair, not a standalone per-projectile miracle.

### D.3 The framing to add to the millimeter-accuracy assumptions (walk before run)
The credibility point. Make explicit, wherever the paper invokes millimeter precision (lines 96, 351), that:
* Millimeter precision is a *later-stage* requirement (near-Sun direct collisions), not needed for the Section 2 near-term work, which runs on meter-class tolerances (D.1).
* Counterintuitively, the tight precision is feasible precisely where the environment looks most extreme. Near the Sun there is no atmosphere, so no drag perturbations; radiation pressure is large but can be modeled, and the orbital mechanics are deterministic. It is thermally and radiatively brutal, but navigation is predictable. The paper already makes this point locally (line 351 "corona's low perturbation environment," lines 366 and 578 for Ceres); D.3 states the general principle once and ties it to the walk-before-run order.
* The genuinely hard navigation environment is the near-Earth low-periapsis regime, where atmospheric drag, gravity anomalies, and sensor dropouts bite (lines 686, 636). That is exactly why we keep the near-term requirement loose (meters, D.1) and do not ask for millimeters there.
* One-line summary for the paper: we demand only meter-class precision where the air is thick (near Earth, near term), and we earn millimeter precision later where the vacuum is clean (near the Sun). Walk, then run.

### D.4 Where this goes (extends Part C)
* Main text, near the first millimeter-precision claim (line 96) or as a scoping sentence in Section 2: the walk-before-run tier statement from D.3. One or two sentences. It defends a headline assumption, so it belongs in the body.
* Main text, Section 2 / pusher-plate: state the near-term interception tolerances (about 100 m along-track, about 2 m cross-track on a 5 m plate that doubles as a debris shield), and that this is why the near-term plate is deliberately heavier and on a longer absorber. Reframe lines 630 and 692 from "5 cm required" to "about 2 m required, cm achievable."
* Appendix (Part B subsection): the off-center-torque and rotational-inertia argument, and the note that heavier-plate-plus-longer-stroke sits above the m_p * s minimum, with the numbers.

## E. Open decisions to resolve next session (before any paper edits)

Nothing in this note is in the paper yet. Resolve these four, then turn the note into main-text and appendix edits and run ./build.sh.

1. **Appendix structure:** one appendix with two subsections (rigid plate; sail and struts), or two separate appendices? Lean: one, because both share the m_p * s buffer invariant.
2. **Front-vs-rear safety argument:** short paragraph in the body, or appendix-only? It is the strongest design rationale (overtaking kinematics, fail-safe shielding), so it could earn body space. Currently slotted in the appendix.
3. **Worked example (4 Hz / 4.6 m / 3.2 t):** put one concrete number set in the body as an anchor, or keep it appendix-only? Body lands the concept; appendix-only keeps the body clean.
4. **Reframe lines 630 and 692 (needs explicit OK, changes already-committed text):** from "about 5 cm std-dev centering" to "about 2 m required laterally on the 5 m plate, cm achievable." This deliberately loosens a stated assumption (see Part D.1). 

# Proposed sharpening of §"Navigation Challenges Near Periapsis" (sec:periapsis_challenges)

*Blurb to append to `updates_back_to_paper.md` in the Balloon-Pulse-Propulsion repo.*
*Refines the "Like Proba-3, we target millimeter-scale precision" claim in
`sec:solid_PuffSats` and the nav discussion in `sec:periapsis_challenges`.
Derived in a design grilling session 2026-06-15; numbers are order-of-magnitude
sizing, not a simulation result.*

---

## The "like Proba-3" claim needs a scale correction

Proba-3 achieves millimetre relative precision at a separation of **~144 m**, where
1 mm corresponds to an angular precision of **~7 µrad** — easy for an optical
metrology instrument. For prograde/retrograde projectiles converging at Parker-class
periapsis, the geometry the precision must be established over is **hundreds of km**,
not 144 m. At a 300 km baseline, 1 mm corresponds to **~3 nrad**. That is *not*
reachable by angular measurement (astrometry / star tracker):

| target angular precision | diffraction-limited aperture (λ = 500 nm) |
|---|---|
| 5 µrad (≈ 1 arcsec, ordinary star tracker) | ~12 cm |
| 1 µrad | ~0.6 m |
| 100 nrad | ~6 m |
| **3 nrad (= 1 mm at 300 km)** | **~200 m** |

A 200 m telescope on a projectile is absurd, and star-referenced astrometry is in any
case capped by a focal-plane **distortion floor** (a ~µrad-class systematic that more
photons cannot beat). So at this scale the precision lever **cannot** be "like
Proba-3" angular metrology. It must be ranging.

## The lever: differential ranging from a transverse node (good GDOP)

The right architecture is a coordinator node placed **off to the side** (transverse
to the line of flight, e.g. ~300 km off-axis) measuring **distances only** (laser or
carrier-phase two-way) — not a star map, not angles.

- **Why transverse.** Lateral position error from a range is
  `σ_lateral ≈ σ_range / sin θ`, where θ is the angle the anchors subtend at the
  target — the *Geometric Dilution of Precision* (GDOP). Anchors nearly **in line**
  with the target (an along-track stream, or two head-on projectiles ranging each
  other) give θ → 0 and `1/sin θ → ∞`: range is blind to the lateral. A **transverse**
  node gives θ ≈ 45–90°, `1/sin θ ≈ 1`: a millimetre range becomes a millimetre
  lateral. The node offset should be comparable to the sensing range for good GDOP.
- **Why differential.** The node ranges *two* things at once — the controlled
  projectile and a reference (the chamber beacon, or the opposing projectile) — and
  uses the difference. This cancels the node's own position/clock error. (Near the Sun
  there is no GNSS to pin the node absolutely; differencing makes that irrelevant.)
- **Why ranging wins here when angle wins elsewhere.** Range precision (~mm via laser
  carrier phase) is essentially **range-independent** and needs only a laser +
  retroreflector, *not* a 200 m aperture; angular precision is distortion-floored and
  aperture-limited. So at the mm / long-range scale the conclusion **inverts**
  relative to ordinary close-formation flying: ranging is the practical lever, angle
  is the impractical one. The work is **relative orbit determination over the
  approach arc** (the geometry rotation builds the lateral), not a last-moment
  snapshot.

## Why ~mm ranging at hundreds of km is realistic (carrier phase)

The architecture rests on ~mm-class *range* precision over hundreds of km, by
carrier-phase ranging. This is not a stretch — it is well inside flight-proven
capability, and the deep-space environment makes it *easier* than its terrestrial
form:

- **Raw phase precision is a small fraction of the wavelength, and range-independent.**
  A carrier-phase observable is typically measured to ~1% of a cycle. At Ka-band
  (~30 GHz, λ ≈ 1 cm) that is ~0.1 mm; at optical (laser, λ ≈ 1 µm) it is far finer.
  Precision degrades only through SNR with range, not through range itself — so
  hundreds of km is a link-budget question (solved with modest gain + a
  retroreflector/transponder), not a precision wall.
- **The integer-ambiguity problem is resolvable here, several ways at once.** Carrier
  phase gives range modulo the wavelength; the whole-cycle integer must be fixed. It is
  pinned by (a) a coarse **code / time-of-flight** range to within a few candidates,
  (b) **dual-frequency wide-laning** (a long synthetic wavelength makes the integer
  trivial, the fine carrier then supplies precision), (c) the **geometry rotation over
  the approach arc** (the "500 measurements" over-determine the integers jointly with
  the relative trajectory, as in kinematic GNSS / orbit determination), and (d)
  **continuous phase tracking** once locked — the ambiguity is fixed *once* at
  acquisition and then merely cycle-counted.
- **Differential processing cancels the biases.** Single- and double-differenced
  carrier phase (node-ranges-two-targets, differenced) removes clock and hardware
  biases — the same CDGPS / satellite-laser-ranging heritage that delivers mm
  relative positioning operationally.
- **No atmosphere — the dominant terrestrial error sources are simply absent.** The
  ionospheric and tropospheric delays that limit ground carrier-phase ranging do not
  exist in the coast regime or near the Sun. The corona carries some dispersive plasma,
  but it is tenuous and dual-frequency-removable. Vacuum is the *friendly* case.
- **Flight precedent (the decisive point).** GRACE / GRACE-FO perform inter-satellite
  ranging at ~220 km separation to ~1 µm (microwave K-band) and ~nm (the GRACE-FO
  laser interferometer); satellite laser ranging routinely reaches mm-class to
  spacecraft at hundreds–thousands of km; lunar laser ranging reaches cm-class at
  ~3.8×10⁵ km. So **mm at hundreds of km is roughly three orders of magnitude inside
  demonstrated inter-spacecraft ranging** — the requirement here is conservative, not
  aggressive.

## Control: two-tier, deterministic-coast — not terminal homing

At ~400 km/s head-on closing, classical terminal homing is hopeless: the homing-miss
floor scales as `σ_θ² v² / a_max`, so hitting mm would demand ~25 nrad nav. The escape
is exactly the paper's own argument — the **predictable** corona environment lets the
push be set up in advance:

- **Gross setup, early.** A light (few-kg) projectile has ample lateral authority
  (~50 m/s of Δv) to place itself in the path of the incoming opposing projectile.
  Authority is *not* the binding constraint.
- **Fine touch, late, fine precision.** The residual lateral miss is
  `≈ δv_lateral · t_go`. So the *final* correction must be both **late** and executed
  to **fine velocity precision**:

  | final correction at t_go | required δv precision for 1 mm |
  |---|---|
  | 1 ms (≈ 400 m out) | 1 m/s |
  | **1 s (≈ 400 km out)** | **1 mm/s** |
  | 10 s | 0.1 mm/s |

  i.e. ~mm/s execution (a micro-thruster impulse bit) applied ~1 s before impact —
  *not* the ~1 m/s that suffices for the gross setup.
- **Why this beats the v² floor.** That floor assumes fighting *nav noise* in the
  endgame. In a deterministic environment you are instead nulling a **known,
  slowly-evolving offset** that the differential-ranging arc has already measured to
  mm. The binding number becomes `(mm/s execution) × (~1 s reaction) ≈ mm`, and the
  high closing speed stops being the enemy.

## SRP near the Sun: huge in absolute terms, irrelevant to the collision

Absolute SRP at Parker periapsis (~9.86 R_sun ≈ 0.046 AU) is ~470× the 1 AU value:
~15 µm/s² on a 1 kg projectile (A/m ≈ 0.005 m²/kg) → ~75 mm of displacement over a
100 s arc. That is large and must be in the trajectory model. But what the collision
cares about is the **relative** SRP between the two converging projectiles, and that
stays sub-mm:

- **Common-mode cancellation.** Both projectiles share the same heliocentric position
  (same flux, same outward SRP direction) and — for thermal survival — must point heat
  shields sunward, so they present the *same* sun-facing geometry. The absolute SRP
  cancels in the difference; the residual scales with the *mismatch* (A/m,
  reflectivity), ~1% at matched manufacturing → ~0.15 µm/s² → ~7.5 µm over 10 s,
  ~0.08 µm over the 1 s final coast. The near-Sun environment that makes SRP large
  also *enforces* the symmetry that cancels it.
- **Track, don't predict.** Continuous differential ranging measures the actual
  relative trajectory (incl. ablation-driven drift); only SRP during the short final
  coast must be modelled, and over ~1 s even the *full* SRP moves <10 µm.
- **Flux gradient** over the inter-projectile gap is negligible (~22 µm over 100 s
  even at 1000 km separation; nothing at the meters-apart endgame).
- **The one non-cancelling term** is velocity-dependent SRP (aberration /
  Poynting–Robertson): prograde and retrograde velocities are opposite, so the
  ~(v/c)·SRP tilt *differences* rather than cancels — ~2×10⁻⁸ m/s² → ~0.1 mm over
  100 s. It is **deterministic** (fixed by known velocity), i.e. exactly the
  "relativistic effects are predictable but must enter the trajectory calculations"
  already flagged — bakeable, not a stochastic risk.
- An on-board solar-intensity detector (sub-gram photodiode) is a useful third layer,
  but its higher-value role is as a **sun sensor for attitude** (attitude sets A_eff,
  the term that does *not* auto-cancel); the SRP-prediction problem itself mostly
  dissolves under cancellation + tracking.

## Net architecture for the chapter

- **Lateral knowledge** → differential ranging from a transverse node (good GDOP),
  *not* astrometry (which would need a ~200 m aperture at 300 km).
- **Control** → two-tier (gross ~50 m/s early + ~mm/s fine at ~1 s t_go),
  deterministic-coast, defeating the v² homing floor.
- **Dominant residual risk** → SRP on the long arc (tracked out) + projectile
  attitude/area matching (engineered); unpredictable solar luminosity is a ~0.1%-TSI
  effect, smaller than the chapter currently implies.

This is sharper and more defensible than "like Proba-3, mm precision": at the 300 km
scale Proba-3's *angular* metrology cannot reach mm, so the precision lever is
transverse-node differential **ranging** with good GDOP, with control made tractable
by the deterministic-coast / early-correction structure the predictable corona allows.

# White-paper architecture deltas — near-term LEO + near-Sun expansion

*Hand-off list for the `Balloon-Pulse-Propulsion` repo. Each item is the **delta**
between what the paper's architecture currently describes and what the closed-out
control simulation now supports — a bulleted headline followed by a paragraph or
two in the paper's voice, ready to fold into the document. Work through them there.*

*Two parts. **Part 1 (near-term LEO)** numbers are **simulation results** from this
repo (Rungs A–D, closed out 2026-06-15/16), not order-of-magnitude sizing. **Part 2
(near-Sun)** is option-level sizing for the speculative chapter, same status as
`paper_update_periapsis_nav.md`.*

*Jargon convention: every specialist term is kept (the paper serves rigorous
professionals) **and** glossed once in plain terms in italics, so a technically
literate reader who is not a space-GNC specialist can follow — e.g. the
**block-miss vs. common-mode** distinction in Item 2.*

---

## A 60-second terminology primer (recurs throughout)

- **Common-mode vs. per-unit error** *(the "block-miss" idea).* When a whole group
  of projectiles share the same error — they all drift the same way — that is a
  *common-mode* error: the **block** slides as one. When each projectile differs
  from its neighbours, that is *per-unit* scatter: the block **spreads**. The trick
  that runs through the whole design is that a block-slide can be cancelled by
  moving the aim point, whereas spread cannot — so the two need completely
  different fixes.
- **Catch radius** *(how close is "close enough").* The largest miss the projectile
  can still correct in the final seconds. It is set by **engine strength**, not by
  how well the projectile can see — a thrust limit, not a knowledge limit.
- **σ_θ · R** *(angular precision × range = position error).* If you measure a
  direction to an angular precision σ_θ and the target is a distance R away, your
  sideways position error is σ_θ · R. The same angle that is precise up close is
  sloppy far away — which is why range R matters as much as the sensor.
- **Feed-forward** *(plan it, don't chase it).* Computing a disturbance in advance
  and cancelling it on a schedule, instead of reacting to it after it has pushed you
  off course.

---

## Part 1 — Near-term LEO interception architecture (the delta to add)

### 1. The success criterion is *capturing the pusher plate*, not centimetre centring.

- **Add/replace:** mission success = the projectile arriving within a **~5 m pusher
  plate** with **≥99 %** probability (per-unit arrival scatter held to σ ≤ ~1.65 m,
  arrival-timing error ≤ 10 ms). The earlier "few-centimetre terminal centring"
  framing is retired as the *committed* requirement.

The momentum transfer the mission exists to perform (paper §2) happens whenever the
projectile lands on the plate; it does not require hitting a point. Re-stating the
requirement as *plate capture* rather than *centimetre centring* is not a softening —
it is the correct statement of what physically has to happen, and it is what the
closed-loop simulation actually demonstrates. *In plain terms: the goal is to hit a
dinner-plate-to-table-sized target reliably, not to thread a needle.* The
centimetre-class number returns only as an **optional** later tightening (Item 9),
not as the bar the baseline must clear.

### 2. Block-miss vs. spread: the swarm's shared error is cancelled by re-aiming, only the per-unit scatter must fit the plate.

- **Add:** treat the train of projectiles as a **block**. The part of the error that
  is **common to all of them** (shared coefficient bias, the same atmosphere, a
  deployer offset they all inherit) moves the whole block together and is removed by
  **re-pointing the aim point** by up to ±2 km — essentially free. Only the
  **per-unit scatter** — how the projectiles differ from *each other* — has to fit
  inside the catch radius. This split is the single most important conceptual lever
  in the architecture.

*In plain terms: if every projectile is off by the same 1 km, you just aim the whole
salvo 1 km the other way and they all land on target; you only have a real problem
if they are scattered relative to one another.* Formally, the common-mode component
is absorbed by a **centroid retarget** (shifting where the swarm is collectively
told to go), so the binding requirement is not the absolute miss but the residual
**per-unit dispersion** about that re-aimed centre. This is why a stochastic
atmosphere and an uncertain drag coefficient — which hit all the projectiles
nearly identically — turn out *not* to be the threat they first appear: they are
mostly common-mode, and common-mode is cheap to cancel.

### 3. The catch radius is a thrust-limited *funnel* (~475 m), set by the engine, not by the sensor.

- **Add:** the terminal endgame can correct any miss up to a **catch radius of
  ~475 m**, and that number is fixed by how far the engine can pull the projectile
  sideways in the time remaining — the familiar ½·a·t² of constant acceleration —
  *not* by navigation quality.

Because the projectile is descending fast, the time-to-go shrinks continuously, and
with it the reachable sideways distance: the correctable region is a **funnel** that
closes toward the plate. *In plain terms: the closer you get, the less room you have
to swerve, and the size of the last possible swerve is decided by your rocket, not
your eyesight.* The practical consequence for the paper is a clean separation of
concerns — **authority** (engine strength) sets *how big* a miss is recoverable, and
the projectile arrives with margin to spare on that axis (the budgeted entry error is
~2× inside the funnel). The limit lives elsewhere, in Item 4.

### 4. The binding constraint is terminal cross-track *knowledge*, and it is a calibration *bias*, not random noise.

- **Add:** the one quantity that actually decides success is **how accurately the
  projectile knows its sideways position relative to the target in the last seconds**
  — the cross-track error σ_θ · R. The simulation shows the requirement is an
  effective **~3 µrad** angular precision on the target tracker, and crucially that
  this is limited by a **fixed calibration bias** in the optics, *not* by random
  noise.

This distinction reorders the engineering priorities and is worth stating plainly in
the paper. *In plain terms: the problem is not a shaky picture you can steady by
taking more exposures — it is a ruler with a slightly bent end. Averaging more
measurements cannot fix a bent ruler; only re-calibrating or cross-referencing it
can.* Two whole families of "obvious" fixes therefore do **nothing** here — more
engine, later burns, bigger thrusters (the limit is knowledge, not control) and
longer integration, faster sensors, heavier filtering (the limit is a bias, not
noise). The levers that *do* work are spatial and geometric: sharpen the angle
(better calibration, or differencing against known stars) or shorten the range R.

### 5. Terminal homing rides a *fused tracker array* (plus an optional close co-flyer), not a single sensor.

- **Add:** the ~3 µrad effective grade is delivered not by one exquisite sensor but
  by **fusing several cruder (~10 µrad) detectors** on the target plate, optionally
  augmented by a **co-flying rocket** much closer to the action. The array beats a
  single sensor by averaging independent errors (∝ 1/√N), and the co-flyer wins by
  shortening the range R.

Each detector does its own star-referenced measurement with its own separately
calibrated optics, so their distortion biases are largely independent and partly
average away — five 10 µrad detectors give ~1.6 µrad. *In plain terms: five ordinary
cameras that each make their own small, different mistakes beat one expensive camera,
because their mistakes partly cancel when you combine them.* The co-flyer contributes
on the **other** handle in σ_θ · R: sitting closer to the converging projectiles, its
modest angular precision still yields a small sideways error because R is small. The
paper should present terminal navigation as this **redundant, fused** architecture —
it is both more accurate and more robust than any single-sensor story, and the
redundancy is what protects the result if the calibration of any one optic proves
worse than hoped.

### 6. Navigation is GNSS-free end-to-end: a Ka-band apogee constellation for the long coast, optical target-tracking for the endgame.

- **Add:** there is **no GNSS** anywhere in the chain. Position knowledge during the
  multi-day coast comes from a **Ka-band, authenticated ranging constellation**
  parked near apogee (~150 000 km), and terminal knowledge comes from the optical
  tracker array of Item 5. The midcourse correction is computed against this coast
  solution; the endgame against the optical one.

Relying on GNSS for a mission whose whole point is high-energy interception would be
fragile and, near the Sun (Part 2), impossible. *In plain terms: the projectiles
navigate by ranging off a small fleet of "lighthouse" satellites high up during the
cruise, then switch to looking directly at the target for the final approach — no
reliance on the GPS network at all.* The constellation is sized only to **match** the
accuracy the coast actually needs (a few hundred metres of position knowledge at the
hand-off), which a minimum of **3–4 members** supplies with large margin; it does not
need to be a precision instrument. This is a genuine architectural addition — the
current paper does not specify how the coast state is known.

### 7. Atmospheric drag is *feed-forward-cancelled*, not fought in the loop; the real coefficient risk sits upstream in the coast.

- **Add:** during the terminal descent, drag is removed by **computing it ahead of
  time and thrusting against it on a schedule** (feed-forward), not by a reactive
  drag-rejection loop. Drag does **not** set the terminal miss. The place where an
  uncertain drag/solar-pressure coefficient *does* matter is far earlier — it
  slightly biases the long coast, and that is handled by the midcourse correction
  (Item 8), not the endgame.

The simulation makes this concrete: an *entirely uncompensated* drag pass displaces
the crossing by only ~8.5 cm (drag concentrates in the final seconds), and the
feed-forward profile reduces even that to ~2 mm. *In plain terms: near the target the
air is so thin that drag barely nudges you, and the small nudge it does give is
predictable enough to cancel by planning, not by chasing.* The consequence for the
paper is that the much-feared coefficient uncertainty is **not** a terminal-accuracy
problem; it lives upstream as a small, mostly common-mode coast bias — which Item 2
has already shown is cheap to absorb.

### 8. The midcourse burn acts on a *ground prior* — no on-board estimator runs before it.

- **Add:** because deployment, apogee, and the first correction burn all occur at
  nearly the same time and place, **no in-flight navigation filter can usefully run
  before the burn**. The midcourse correction is therefore planned against the
  **ground-determined prior** (the best pre-flight estimate of state and
  coefficients), and the simulation confirms this prior is more than good enough.

This is a subtle but important honesty in the architecture. *In plain terms: the
projectile does not get a chance to "figure out" its drag in flight before it must
act — there isn't enough time or distance — so it uses the number measured on the
ground, and that number turns out to have ample margin.* The measured tolerance is
wide: the correction stays accurate across a coefficient error band ~34× larger than
the ground prior's actual uncertainty. The paper can state plainly that **in-flight
coefficient estimation is unnecessary for the midcourse**, which removes a whole
speculative subsystem from the near-term story.

### 9. Propellant stays under 2 %, and the low (~50 km) perigee is an *intended disposal feature*, not a failure.

- **Add / reinforce:** the full closed-loop propellant budget — cruise corrections
  plus the terminal aim — lands **under 2 % of the 25 kg projectile mass** even in
  the worst sampled case. Separately, the deliberately **low perigee (~50–65 km)** is
  a *designed* outcome: it de-orbits the spent projectile and burns up any unit that
  misses, for clean debris disposal (paper §9). Low perigee is **good**, not a fault.

The paper already claims <2 % propellant; the contribution here is that a *simulated
closed loop* — corrector, terminal guidance, finite-thrust execution, dispersed
environment — confirms it rather than asserting it. *In plain terms: the whole job
costs less than one part in fifty of the projectile's mass in fuel, and a miss
self-disposes by re-entry instead of becoming space junk.* It is worth making
explicit in the text that perigee is a **diagnostic where lower is safer**, not a
target to be hit — otherwise a reader sees "50 km perigee" and mistakes the disposal
feature for a navigation error.

### 9-optional. Optional stretch — *surveyor-anchored centring* shrinks the plate from 5 m toward ~10 cm.

- **Add as an explicitly optional §2 tightening:** the plate can be shrunk roughly
  **50×** (5 m → ~10 cm) by adding two metrology aids, *without* changing the
  baseline above. (1) A **sacrificial "surveyor" projectile** whose true crossing is
  measured by an **independent instrumented gate** (a "hoop" using laser or microwave
  ranging — deliberately *not* the optical tracker, which would be checking itself,
  and *not* a real impact, which would throw off-centre debris and glare) pins the
  swarm's shared optical bias to the plate. (2) **Strobed, known-pattern LED
  beacons** on each projectile let the units measure each other's relative positions
  like a rigid body, driving the per-unit scatter to centimetres.

This is firmly a **knowledge/metrology** upgrade, not a control one — the centimetre
trims it asks for sit deep inside the 475 m thrust funnel, so the engine is never the
limit. *In plain terms: one projectile is sacrificed as a "test shot" measured by an
independent gauge to fix the whole group's aim, and the projectiles wear blinking
markers so they can see exactly where each sits relative to the others — shrinking
the plate without needing a better tracker or a bigger engine.* The achievable plate
size is then set by two bench numbers: the gate's ranging precision (≤1 cm → a 5 cm
plate; ~3 cm → a 10 cm plate) and the camera's own calibrated distortion floor. The
honest committed claim is **10 cm (robust); 5 cm as a stretch** contingent on a ≤1 cm
gate and a well-calibrated camera; a 2 cm plate is *not* claimed.

---

## Part 2 — Near-Sun / Parker-periapsis case: expansion options

*Context: `paper_update_periapsis_nav.md` already corrects the "like Proba-3,
millimetre precision" claim and establishes transverse-node differential ranging as
the lateral-knowledge lever at the hundreds-of-km scale. The items below are the
**menu of architectural options** to expand that chapter — what else the near-Sun
case can use, and where the LEO logic inverts because there is no GNSS anchor and the
projectiles' *spread* relative to each other becomes the whole game.*

### A. Primary lever — transverse-node differential carrier-phase ranging (good GDOP).

- **Restate as the chapter's baseline:** lateral knowledge near the Sun comes from a
  coordinator node placed **off to the side** of the line of flight, measuring
  **distances only** to both the controlled projectile and a reference, and using the
  difference.

The geometry term is **GDOP — geometric dilution of precision** — and it is the crux.
*In plain terms: a distance measurement tells you a lot about sideways position only
if the measuring station is off to the side; a station straight ahead or behind tells
you almost nothing sideways, the way one eye gives poor depth perception.* A
transverse node converts millimetre ranging into millimetre *lateral* knowledge;
differencing two ranges from the same node cancels the node's own position and clock
errors, which matters precisely because near the Sun there is no GNSS to pin the node
absolutely. This is the option the chapter should lead with, because at the 300 km
scale ordinary angular metrology would need an absurd ~200 m telescope.

### B. Precision-boost option — a VLBI-style coherent-aperture swarm.

- **Offer as an upgrade path:** several projectiles acting as one **synthetic
  aperture** (the radio-astronomy "very-long-baseline interferometry" trick) can in
  principle sharpen the relative-position fix beyond a single ranging node.

*In plain terms: many small antennas spread out and combined can see as sharply as
one impossibly large one.* This is the only option that could genuinely *beat* the
single-node precision rather than merely match it. It is included here, rather than in
the LEO chapter, for two honest reasons that the text should state: in LEO it would be
insurance against a failure that the entry-limited capture analysis says does not
bind, and its precision depends on knowing the **baseline orientation** between units
to high accuracy — which ranging alone does not give (ranging measures baseline
*length*, not its sideways tilt). Near the Sun, where relative geometry *is* the
mission and there is no anchor floor, the trade is more attractive, so it belongs in
this chapter as a stretch option.

### C. Close-endgame option — optical LED-beacon cameras layered on RF ranging.

- **Offer as the terminal collision sensor:** in the final approach, **strobed LED
  beacons + small cameras** between the converging projectiles can supply the
  last-instant relative bearing, on top of the RF differential ranging that does the
  long-range work.

Here the LEO logic **inverts**, and the chapter should say so explicitly. In LEO,
inter-projectile cameras were the *wrong* tool — they measure how the swarm is spread
relative to itself, which is already handled, and are blind to the block-slide that an
external anchor must fix. *Near the Sun there is no external anchor, and the spread
between two converging projectiles is exactly the quantity that decides the
collision* — so the very sensor that was redundant in LEO becomes useful as the
close-in collision sensor. *In plain terms: when two objects must hit each other and
there is no outside referee, they are best off watching each other directly through
the last stretch.* This is a layered backup to ranging, not a replacement for it.

### D. Control structure — deterministic-coast, two-tier correction (defeats the v² homing floor).

- **Restate as the control architecture:** a **gross early correction** (~tens of m/s
  of Δv to get roughly into the path) plus a **fine, late, high-precision correction**
  (~mm/s applied ~1 s before impact). Not last-moment terminal homing.

At ~400 km/s head-on closing, classical homing is hopeless — its miss floor grows
with closing speed squared. *In plain terms: you cannot "steer in" at the last second
when you are closing this fast; instead you set up the shot early in a predictable
environment and apply one tiny, precisely-timed nudge at the end.* The reason this
works is that the corona environment is **predictable**, so the projectile is nulling
a *known, already-measured* offset rather than fighting fresh sensor noise — which is
what lets a millimetre-per-second nudge a second out translate to a millimetre miss.
The chapter should frame the high closing speed as something the structure *defeats*,
not something it fights.

### E. Disturbance handling — solar-pressure common-mode cancellation, "track, don't predict."

- **Offer as the SRP argument:** the enormous absolute solar radiation pressure near
  the Sun (~470× its 1 AU value) is **largely irrelevant to the collision**, because
  both converging projectiles share nearly the same sun-facing geometry and so feel
  nearly the same push — it is **common-mode and cancels in the difference**.

This is the Part 1 block-miss idea reappearing in a new setting, and the chapter can
lean on it. *In plain terms: a strong wind that pushes both racers equally does not
change who reaches the line first — only the difference between them matters, and that
difference is small.* The residual scales with the *mismatch* in area and
reflectivity (a percent at matched manufacturing), the actual relative trajectory is
**measured continuously** by the ranging arc rather than predicted, and only the brief
final coast must be modelled. The one term that does *not* cancel — a velocity-
dependent relativistic tilt that differs between the prograde and retrograde
projectiles — is **deterministic** and can be baked into the trajectory, not a
stochastic risk.

### F. Attitude aid — a sub-gram sun-sensor photodiode setting the effective area.

- **Offer as a light third layer:** a tiny solar-intensity photodiode is most
  valuable not as a navigation sensor but as a **sun sensor for attitude**, because
  attitude sets the sun-facing area — the one solar-pressure term that does *not*
  auto-cancel.

*In plain terms: the cheapest way to keep the un-cancelled part of sunlight pressure
under control is to keep the projectile pointed consistently, and a pinhead-sized
light sensor is enough to do that.* It is worth one line in the chapter as the
low-cost closure on the residual SRP term, distinct from the ranging and camera
options above.

---

## Cross-reference for the other repo

- Part 1 numbers trace to this repo's ADRs: criterion (0015/0016), catch-radius &
  terminal guidance (0014), multi-tracker fusion (0019), apogee nav constellation
  (0020), drag feed-forward (0021), coefficient prior (0013), Rung-D closeout (0018).
- Part 2 traces to `todos/paper_update_periapsis_nav.md` (the differential-ranging
  chapter) plus the near-Sun inversions noted in the relative-ranging and
  optical-sensing design discussions.
- The surveyor-anchored centring scheme (Item 9-optional) is documented as a CONTEXT
  term in this repo; it is a paper-side option, deliberately not built in simulation.

# White-paper architecture deltas — near-term LEO + near-Sun expansion

*Hand-off list for the `Balloon-Pulse-Propulsion` repo. Each item is the **delta**
between what the paper's architecture currently describes and what the closed-out
control simulation now supports — a bulleted headline followed by a paragraph or
two in the paper's voice, ready to fold into the document. Work through them there.*

*Two parts. **Part 1 (near-term LEO)** numbers are **simulation results** from this
repo (Rungs A–D, closed out 2026-06-15/16), not order-of-magnitude sizing. **Part 2
(near-Sun)** is option-level sizing for the speculative chapter, same status as
`paper_update_periapsis_nav.md`.*

*Jargon convention: every specialist term is kept (the paper serves rigorous
professionals) **and** glossed once in plain terms in italics, so a technically
literate reader who is not a space-GNC specialist can follow — e.g. the
**block-miss vs. common-mode** distinction in Item 2.*

---

## A 60-second terminology primer (recurs throughout)

- **Common-mode vs. per-unit error** *(the "block-miss" idea).* When a whole group
  of projectiles share the same error — they all drift the same way — that is a
  *common-mode* error: the **block** slides as one. When each projectile differs
  from its neighbours, that is *per-unit* scatter: the block **spreads**. The trick
  that runs through the whole design is that a block-slide can be cancelled by
  moving the aim point, whereas spread cannot — so the two need completely
  different fixes.
- **Catch radius** *(how close is "close enough").* The largest miss the projectile
  can still correct in the final seconds. It is set by **engine strength**, not by
  how well the projectile can see — a thrust limit, not a knowledge limit.
- **σ_θ · R** *(angular precision × range = position error).* If you measure a
  direction to an angular precision σ_θ and the target is a distance R away, your
  sideways position error is σ_θ · R. The same angle that is precise up close is
  sloppy far away — which is why range R matters as much as the sensor.
- **Feed-forward** *(plan it, don't chase it).* Computing a disturbance in advance
  and cancelling it on a schedule, instead of reacting to it after it has pushed you
  off course.

---

## Part 1 — Near-term LEO interception architecture (the delta to add)

### 1. The success criterion is *capturing the pusher plate*, not centimetre centring.

- **Add/replace:** mission success = the projectile arriving within a **~5 m pusher
  plate** with **≥99 %** probability (per-unit arrival scatter held to σ ≤ ~1.65 m,
  arrival-timing error ≤ 10 ms). The earlier "few-centimetre terminal centring"
  framing is retired as the *committed* requirement.

The momentum transfer the mission exists to perform (paper §2) happens whenever the
projectile lands on the plate; it does not require hitting a point. Re-stating the
requirement as *plate capture* rather than *centimetre centring* is not a softening —
it is the correct statement of what physically has to happen, and it is what the
closed-loop simulation actually demonstrates. *In plain terms: the goal is to hit a
dinner-plate-to-table-sized target reliably, not to thread a needle.* The
centimetre-class number returns only as an **optional** later tightening (Item 9),
not as the bar the baseline must clear.

### 2. Block-miss vs. spread: the swarm's shared error is cancelled by re-aiming, only the per-unit scatter must fit the plate.

- **Add:** treat the train of projectiles as a **block**. The part of the error that
  is **common to all of them** (shared coefficient bias, the same atmosphere, a
  deployer offset they all inherit) moves the whole block together and is removed by
  **re-pointing the aim point** by up to ±2 km — essentially free. Only the
  **per-unit scatter** — how the projectiles differ from *each other* — has to fit
  inside the catch radius. This split is the single most important conceptual lever
  in the architecture.

*In plain terms: if every projectile is off by the same 1 km, you just aim the whole
salvo 1 km the other way and they all land on target; you only have a real problem
if they are scattered relative to one another.* Formally, the common-mode component
is absorbed by a **centroid retarget** (shifting where the swarm is collectively
told to go), so the binding requirement is not the absolute miss but the residual
**per-unit dispersion** about that re-aimed centre. This is why a stochastic
atmosphere and an uncertain drag coefficient — which hit all the projectiles
nearly identically — turn out *not* to be the threat they first appear: they are
mostly common-mode, and common-mode is cheap to cancel.

### 3. The catch radius is a thrust-limited *funnel* (~475 m), set by the engine, not by the sensor.

- **Add:** the terminal endgame can correct any miss up to a **catch radius of
  ~475 m**, and that number is fixed by how far the engine can pull the projectile
  sideways in the time remaining — the familiar ½·a·t² of constant acceleration —
  *not* by navigation quality.

Because the projectile is descending fast, the time-to-go shrinks continuously, and
with it the reachable sideways distance: the correctable region is a **funnel** that
closes toward the plate. *In plain terms: the closer you get, the less room you have
to swerve, and the size of the last possible swerve is decided by your rocket, not
your eyesight.* The practical consequence for the paper is a clean separation of
concerns — **authority** (engine strength) sets *how big* a miss is recoverable, and
the projectile arrives with margin to spare on that axis (the budgeted entry error is
~2× inside the funnel). The limit lives elsewhere, in Item 4.

### 4. The binding constraint is terminal cross-track *knowledge*, and it is a calibration *bias*, not random noise.

- **Add:** the one quantity that actually decides success is **how accurately the
  projectile knows its sideways position relative to the target in the last seconds**
  — the cross-track error σ_θ · R. The simulation shows the requirement is an
  effective **~3 µrad** angular precision on the target tracker, and crucially that
  this is limited by a **fixed calibration bias** in the optics, *not* by random
  noise.

This distinction reorders the engineering priorities and is worth stating plainly in
the paper. *In plain terms: the problem is not a shaky picture you can steady by
taking more exposures — it is a ruler with a slightly bent end. Averaging more
measurements cannot fix a bent ruler; only re-calibrating or cross-referencing it
can.* Two whole families of "obvious" fixes therefore do **nothing** here — more
engine, later burns, bigger thrusters (the limit is knowledge, not control) and
longer integration, faster sensors, heavier filtering (the limit is a bias, not
noise). The levers that *do* work are spatial and geometric: sharpen the angle
(better calibration, or differencing against known stars) or shorten the range R.

### 5. Terminal homing rides a *fused tracker array* (plus an optional close co-flyer), not a single sensor.

- **Add:** the ~3 µrad effective grade is delivered not by one exquisite sensor but
  by **fusing several cruder (~10 µrad) detectors** on the target plate, optionally
  augmented by a **co-flying rocket** much closer to the action. The array beats a
  single sensor by averaging independent errors (∝ 1/√N), and the co-flyer wins by
  shortening the range R.

Each detector does its own star-referenced measurement with its own separately
calibrated optics, so their distortion biases are largely independent and partly
average away — five 10 µrad detectors give ~1.6 µrad. *In plain terms: five ordinary
cameras that each make their own small, different mistakes beat one expensive camera,
because their mistakes partly cancel when you combine them.* The co-flyer contributes
on the **other** handle in σ_θ · R: sitting closer to the converging projectiles, its
modest angular precision still yields a small sideways error because R is small. The
paper should present terminal navigation as this **redundant, fused** architecture —
it is both more accurate and more robust than any single-sensor story, and the
redundancy is what protects the result if the calibration of any one optic proves
worse than hoped.

### 6. Navigation is GNSS-free end-to-end: a Ka-band apogee constellation for the long coast, optical target-tracking for the endgame.

- **Add:** there is **no GNSS** anywhere in the chain. Position knowledge during the
  multi-day coast comes from a **Ka-band, authenticated ranging constellation**
  parked near apogee (~150 000 km), and terminal knowledge comes from the optical
  tracker array of Item 5. The midcourse correction is computed against this coast
  solution; the endgame against the optical one.

Relying on GNSS for a mission whose whole point is high-energy interception would be
fragile and, near the Sun (Part 2), impossible. *In plain terms: the projectiles
navigate by ranging off a small fleet of "lighthouse" satellites high up during the
cruise, then switch to looking directly at the target for the final approach — no
reliance on the GPS network at all.* The constellation is sized only to **match** the
accuracy the coast actually needs (a few hundred metres of position knowledge at the
hand-off), which a minimum of **3–4 members** supplies with large margin; it does not
need to be a precision instrument. This is a genuine architectural addition — the
current paper does not specify how the coast state is known.

### 7. Atmospheric drag is *feed-forward-cancelled*, not fought in the loop; the real coefficient risk sits upstream in the coast.

- **Add:** during the terminal descent, drag is removed by **computing it ahead of
  time and thrusting against it on a schedule** (feed-forward), not by a reactive
  drag-rejection loop. Drag does **not** set the terminal miss. The place where an
  uncertain drag/solar-pressure coefficient *does* matter is far earlier — it
  slightly biases the long coast, and that is handled by the midcourse correction
  (Item 8), not the endgame.

The simulation makes this concrete: an *entirely uncompensated* drag pass displaces
the crossing by only ~8.5 cm (drag concentrates in the final seconds), and the
feed-forward profile reduces even that to ~2 mm. *In plain terms: near the target the
air is so thin that drag barely nudges you, and the small nudge it does give is
predictable enough to cancel by planning, not by chasing.* The consequence for the
paper is that the much-feared coefficient uncertainty is **not** a terminal-accuracy
problem; it lives upstream as a small, mostly common-mode coast bias — which Item 2
has already shown is cheap to absorb.

### 8. The midcourse burn acts on a *ground prior* — no on-board estimator runs before it.

- **Add:** because deployment, apogee, and the first correction burn all occur at
  nearly the same time and place, **no in-flight navigation filter can usefully run
  before the burn**. The midcourse correction is therefore planned against the
  **ground-determined prior** (the best pre-flight estimate of state and
  coefficients), and the simulation confirms this prior is more than good enough.

This is a subtle but important honesty in the architecture. *In plain terms: the
projectile does not get a chance to "figure out" its drag in flight before it must
act — there isn't enough time or distance — so it uses the number measured on the
ground, and that number turns out to have ample margin.* The measured tolerance is
wide: the correction stays accurate across a coefficient error band ~34× larger than
the ground prior's actual uncertainty. The paper can state plainly that **in-flight
coefficient estimation is unnecessary for the midcourse**, which removes a whole
speculative subsystem from the near-term story.

### 9. Propellant stays under 2 %, and the low (~50 km) perigee is an *intended disposal feature*, not a failure.

- **Add / reinforce:** the full closed-loop propellant budget — cruise corrections
  plus the terminal aim — lands **under 2 % of the 25 kg projectile mass** even in
  the worst sampled case. Separately, the deliberately **low perigee (~50–65 km)** is
  a *designed* outcome: it de-orbits the spent projectile and burns up any unit that
  misses, for clean debris disposal (paper §9). Low perigee is **good**, not a fault.

The paper already claims <2 % propellant; the contribution here is that a *simulated
closed loop* — corrector, terminal guidance, finite-thrust execution, dispersed
environment — confirms it rather than asserting it. *In plain terms: the whole job
costs less than one part in fifty of the projectile's mass in fuel, and a miss
self-disposes by re-entry instead of becoming space junk.* It is worth making
explicit in the text that perigee is a **diagnostic where lower is safer**, not a
target to be hit — otherwise a reader sees "50 km perigee" and mistakes the disposal
feature for a navigation error.

### 9-optional. Optional stretch — *surveyor-anchored centring* shrinks the plate from 5 m toward ~10 cm.

- **Add as an explicitly optional §2 tightening:** the plate can be shrunk roughly
  **50×** (5 m → ~10 cm) by adding two metrology aids, *without* changing the
  baseline above. (1) A **sacrificial "surveyor" projectile** whose true crossing is
  measured by an **independent instrumented gate** (a "hoop" using laser or microwave
  ranging — deliberately *not* the optical tracker, which would be checking itself,
  and *not* a real impact, which would throw off-centre debris and glare) pins the
  swarm's shared optical bias to the plate. (2) **Strobed, known-pattern LED
  beacons** on each projectile let the units measure each other's relative positions
  like a rigid body, driving the per-unit scatter to centimetres.

This is firmly a **knowledge/metrology** upgrade, not a control one — the centimetre
trims it asks for sit deep inside the 475 m thrust funnel, so the engine is never the
limit. *In plain terms: one projectile is sacrificed as a "test shot" measured by an
independent gauge to fix the whole group's aim, and the projectiles wear blinking
markers so they can see exactly where each sits relative to the others — shrinking
the plate without needing a better tracker or a bigger engine.* The achievable plate
size is then set by two bench numbers: the gate's ranging precision (≤1 cm → a 5 cm
plate; ~3 cm → a 10 cm plate) and the camera's own calibrated distortion floor. The
honest committed claim is **10 cm (robust); 5 cm as a stretch** contingent on a ≤1 cm
gate and a well-calibrated camera; a 2 cm plate is *not* claimed.

---

## Part 2 — Near-Sun / Parker-periapsis case: expansion options

*Context: `paper_update_periapsis_nav.md` already corrects the "like Proba-3,
millimetre precision" claim and establishes transverse-node differential ranging as
the lateral-knowledge lever at the hundreds-of-km scale. The items below are the
**menu of architectural options** to expand that chapter — what else the near-Sun
case can use, and where the LEO logic inverts because there is no GNSS anchor and the
projectiles' *spread* relative to each other becomes the whole game.*

### A. Primary lever — transverse-node differential carrier-phase ranging (good GDOP).

- **Restate as the chapter's baseline:** lateral knowledge near the Sun comes from a
  coordinator node placed **off to the side** of the line of flight, measuring
  **distances only** to both the controlled projectile and a reference, and using the
  difference.

The geometry term is **GDOP — geometric dilution of precision** — and it is the crux.
*In plain terms: a distance measurement tells you a lot about sideways position only
if the measuring station is off to the side; a station straight ahead or behind tells
you almost nothing sideways, the way one eye gives poor depth perception.* A
transverse node converts millimetre ranging into millimetre *lateral* knowledge;
differencing two ranges from the same node cancels the node's own position and clock
errors, which matters precisely because near the Sun there is no GNSS to pin the node
absolutely. This is the option the chapter should lead with, because at the 300 km
scale ordinary angular metrology would need an absurd ~200 m telescope.

### B. Precision-boost option — a VLBI-style coherent-aperture swarm.

- **Offer as an upgrade path:** several projectiles acting as one **synthetic
  aperture** (the radio-astronomy "very-long-baseline interferometry" trick) can in
  principle sharpen the relative-position fix beyond a single ranging node.

*In plain terms: many small antennas spread out and combined can see as sharply as
one impossibly large one.* This is the only option that could genuinely *beat* the
single-node precision rather than merely match it. It is included here, rather than in
the LEO chapter, for two honest reasons that the text should state: in LEO it would be
insurance against a failure that the entry-limited capture analysis says does not
bind, and its precision depends on knowing the **baseline orientation** between units
to high accuracy — which ranging alone does not give (ranging measures baseline
*length*, not its sideways tilt). Near the Sun, where relative geometry *is* the
mission and there is no anchor floor, the trade is more attractive, so it belongs in
this chapter as a stretch option.

### C. Close-endgame option — optical LED-beacon cameras layered on RF ranging.

- **Offer as the terminal collision sensor:** in the final approach, **strobed LED
  beacons + small cameras** between the converging projectiles can supply the
  last-instant relative bearing, on top of the RF differential ranging that does the
  long-range work.

Here the LEO logic **inverts**, and the chapter should say so explicitly. In LEO,
inter-projectile cameras were the *wrong* tool — they measure how the swarm is spread
relative to itself, which is already handled, and are blind to the block-slide that an
external anchor must fix. *Near the Sun there is no external anchor, and the spread
between two converging projectiles is exactly the quantity that decides the
collision* — so the very sensor that was redundant in LEO becomes useful as the
close-in collision sensor. *In plain terms: when two objects must hit each other and
there is no outside referee, they are best off watching each other directly through
the last stretch.* This is a layered backup to ranging, not a replacement for it.

### D. Control structure — deterministic-coast, two-tier correction (defeats the v² homing floor).

- **Restate as the control architecture:** a **gross early correction** (~tens of m/s
  of Δv to get roughly into the path) plus a **fine, late, high-precision correction**
  (~mm/s applied ~1 s before impact). Not last-moment terminal homing.

At ~400 km/s head-on closing, classical homing is hopeless — its miss floor grows
with closing speed squared. *In plain terms: you cannot "steer in" at the last second
when you are closing this fast; instead you set up the shot early in a predictable
environment and apply one tiny, precisely-timed nudge at the end.* The reason this
works is that the corona environment is **predictable**, so the projectile is nulling
a *known, already-measured* offset rather than fighting fresh sensor noise — which is
what lets a millimetre-per-second nudge a second out translate to a millimetre miss.
The chapter should frame the high closing speed as something the structure *defeats*,
not something it fights.

### E. Disturbance handling — solar-pressure common-mode cancellation, "track, don't predict."

- **Offer as the SRP argument:** the enormous absolute solar radiation pressure near
  the Sun (~470× its 1 AU value) is **largely irrelevant to the collision**, because
  both converging projectiles share nearly the same sun-facing geometry and so feel
  nearly the same push — it is **common-mode and cancels in the difference**.

This is the Part 1 block-miss idea reappearing in a new setting, and the chapter can
lean on it. *In plain terms: a strong wind that pushes both racers equally does not
change who reaches the line first — only the difference between them matters, and that
difference is small.* The residual scales with the *mismatch* in area and
reflectivity (a percent at matched manufacturing), the actual relative trajectory is
**measured continuously** by the ranging arc rather than predicted, and only the brief
final coast must be modelled. The one term that does *not* cancel — a velocity-
dependent relativistic tilt that differs between the prograde and retrograde
projectiles — is **deterministic** and can be baked into the trajectory, not a
stochastic risk.

### F. Attitude aid — a sub-gram sun-sensor photodiode setting the effective area.

- **Offer as a light third layer:** a tiny solar-intensity photodiode is most
  valuable not as a navigation sensor but as a **sun sensor for attitude**, because
  attitude sets the sun-facing area — the one solar-pressure term that does *not*
  auto-cancel.

*In plain terms: the cheapest way to keep the un-cancelled part of sunlight pressure
under control is to keep the projectile pointed consistently, and a pinhead-sized
light sensor is enough to do that.* It is worth one line in the chapter as the
low-cost closure on the residual SRP term, distinct from the ranging and camera
options above.

---

## Cross-reference for the other repo

- Part 1 numbers trace to this repo's ADRs: criterion (0015/0016), catch-radius &
  terminal guidance (0014), multi-tracker fusion (0019), apogee nav constellation
  (0020), drag feed-forward (0021), coefficient prior (0013), Rung-D closeout (0018).
- Part 2 traces to `todos/paper_update_periapsis_nav.md` (the differential-ranging
  chapter) plus the near-Sun inversions noted in the relative-ranging and
  optical-sensing design discussions.
- The surveyor-anchored centring scheme (Item 9-optional) is documented as a CONTEXT
  term in this repo; it is a paper-side option, deliberately not built in simulation.

