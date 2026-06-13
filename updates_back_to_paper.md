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