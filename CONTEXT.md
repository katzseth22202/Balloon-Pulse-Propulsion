# PuffSat Pulsed Propulsion

Canonical language for the *Aim Is All You Need* white paper and its companion
control simulation. These are the project-specific terms that recur across the paper,
the edit backlog (`updates_back_to_paper.md`), and the design discussions. Definitions
are tight and opinionated: where several words exist for one idea, one is canonical and
the rest are listed as aliases to avoid.

## Language

### Core propulsion

**PuffSat**:
A small expendable projectile (gas-generating or solid) sent to collide with a moving
rocket and transfer momentum for pulsed propulsion.
_Avoid_: pellet, slug (those evoke the pellet-beam prior art the paper distinguishes
itself from).

**Pusher plate**:
The momentum-buffer surface on the main craft that the PuffSat gas or solids strike,
mounted on a shock absorber. About 5 m wide in the near-term design, where it doubles as
a debris shield.
_Avoid_: target plate, impact plate.

**Medusa-style sail**:
A flexible pusher mounted *behind* the rocket on shock-absorbing struts. Because it sits
behind, its struts carry **compression** (and can buckle), unlike real Project Medusa's
front-mounted **tension** sail.
_Avoid_: calling ours simply "Medusa" without the behind/compression qualifier.

**Buffer invariant**:
The relation `m·s ≈ M a T²/4` tying buffer mass `m` and absorber stroke `s` for craft
mass `M`, acceleration `a`, and pulse period `T = 1/f`. The shared law behind both the
rigid plate (short stroke, heavy or high-frequency) and the Medusa sail (long stroke,
light).

**Fudge factor (`f`)**:
The energy-loss factor in the PuffSat-to-rocket mass-ratio law (`eq:PuffSat_ratio`): the
axial momentum a gas pulse delivers to the pusher plate as a fraction of the
full-capture, perfect-bounce ideal. Ranges `0.5` (perfectly inelastic, gas sticks) to `1`
(perfectly elastic, gas rebounds and pushes about twice as hard), and below `0.5` if some
gas misses the plate. The paper selects `f = 0.8`. A preliminary single-code hydrodynamic
simulation (companion repo `puffsat_impact_simulation`) finds `f ≈ 0.8` reasonable across
the 3.2–16 km/s gas-collision envelope; the same analysis finds **sideways spill** (gas escaping past the
plate edge, a.k.a. sideways escape; the geometric loss channel that pushes `f` toward and
below 0.5) subdominant in the LEO insertion band; the result is *not yet independently validated*, so
the paper cites it as plausible, not confirmed (see Flagged ambiguities).
_Avoid_: presenting `f = 0.8` as validated/confirmed; the symbol `f` also denotes pulse
frequency in the buffer invariant (`T = 1/f`), a distinct quantity; using `f` for the
prograde/retrograde collision-plus-nozzle case (that is **jet efficiency (`η_jet`)**, a
different quantity with a different failure mode); using `f` for the slug-augmented
head-on departure nozzle (that is **recovery (`e`)**, a collimation claim, not an elasticity one).

**Jet efficiency (`η_jet`)**:
The nozzle-side loss factor in the prograde/retrograde collision law (`eq:ve_general` in
`sec:jet_efficiency`): the mass-weighted mean *axial* exhaust velocity divided by the
loss-free gas speed `v_g`, both measured in the rocket frame over the whole expelled mass.
Cauchy-Schwarz and energy conservation bound it to `(0,1]`. It reaches 1 only if every gram
leaves at the loss-free speed in one direction. Its square is the fraction of available
collision energy represented by coherent axial momentum. This definition absorbs plume
divergence, exhaust-speed spread, radiation escaping before it can be turned, frozen-flow
(ionization/dissociation) losses, and mass the field fails to grip. Consequences: the optimal
mix is `m_rp = η_jet²/4`, i.e.
`(4/η_jet²) − 1` parts prograde to one retrograde, so **3:1 is the `η_jet → 1` endpoint of a
family, not a fixed number**; `v_e = η_jet² v_p / 2` at that optimum. Forward thrust vanishes
at the pass-through floor `η_jet = √m_rp` and reverses below it (0.5 at 3:1, 0.2 at 24:1).
Because a plate at any `f` still passes some momentum forward while a nozzle below its floor
produces net backward impulse, heavy dilution is the cheap insurance wherever the added
propellant is cheap. Values the paper pins implicitly: 0.77 (lunar cycle,
`sec:no_isru_rocket`), ~0.89 required (methalox rebuttal at its
$3200 pessimistic anchor), ~0.7 required (scale energy case). None is computed from a nozzle
model; all are requirements, in the same sense as the radiative-escape budget of
`sec:minimum_nozzle`. Published ceiling: Ahedo & Merino's plume efficiency of 0.63-0.83
(power-like, so its square root bounds `η_jet`) gives a divergence-only ceiling near
**0.79-0.91**. Axial velocity spread and other losses lower the full parameter. Their model is
collisionless,
electron-magnetized, current-free and low-β, so it anchors rather than settles the question.
_Avoid_: conflating with the **fudge factor (`f`)**; calling `η_jet` an efficiency in the power
sense; treating 3:1 as a validated optimum rather than the loss-free endpoint; conflating with
**recovery (`e`)**, which scales the impulse *after* the momentum debit and so has no floor.

**Recovery (`e`)**:
The third efficiency, and the steep axis of the Jupiter-only 30-year growth table
(`sec:jupiter_only_growth`, companion ADR `0013`). The fraction of the *ideal collimated
impulse* a real magnetic nozzle delivers on the slug-augmented head-on departure burn:
collimation, geometric capture and plasma coupling lumped into one number.
`v_e = e · w · (√(1+k) − 1) / k`, where `w` is closing speed and `k` the slug ratio.
Distinguished from the other two on purpose:
- vs **jet efficiency (`η_jet`)**: `η_jet` scales the jet *before* the incoming-momentum debit
  is subtracted (`v_e = η_jet v_g − 2 v_p m_rp`), which is why it has a pass-through floor at
  `√m_rp`. `e` scales the whole net impulse, debit already inside the bracket, so **`e` has no
  thrust-reversal floor**: any `e > 0` still pushes forward. The `e = 0.25` row of the growth
  table fails on *transport accounting* (the loop cannot pay its own costs), not on thrust
  reversal, and must not be described as a physics wall.
- vs **fudge factor (`f`)**: `f` is an elasticity claim about gas bouncing off a plate; `e` is a
  collimation claim about a plume. They coincide numerically only in the `k → 0` limit, which is
  why `astro_constants.STD_FUDGE_FACTOR = 0.8` is reused as the ideal-ceiling `e`. Different
  hardware claims; no source calibrates either. That same `k -> 0` limit is what makes a pusher
  plate the *no-slug nozzle*, and so decides the leg-1 device choice: see **Overtake leg vs
  head-on leg**.
ADR `0013` makes `e ≈ 0.3` the architecture's survival threshold and finds `f` worth about as
much as `e` (a 0.3 drop in `f` costs what a 0.2 swing in `e` does).
_Avoid_: quoting an `e` without the `f` it assumed, or vice versa; calling the `e = 0.25` row a
thrust floor; using `η_jet`'s 0.5 three-to-one floor as if it bounded `e`.

**Gas speed (`v_g`) vs effective exhaust velocity (`v_e`)**:
Two distinct quantities in `sec:dv_effective`. `v_g = 2 v_p √m_rp` is what the collision energy
alone allows, the speed the merged mass would carry if every gram left at one speed along one
axis. `v_e = η_jet · v_g − 2 v_p m_rp` is what the rocket actually gains per unit PuffSat mass
spent, after debiting the momentum the retrograde PuffSat brought in head-on. At the 3:1
optimum they differ by 2× (`v_g = v_p`, `v_e =
v_p/2`). Because `v_e` is a *difference* rather than a fraction, a fractional loss in `v_g`
appears roughly doubled in `v_e` at 3:1, and far more as `η_jet` nears the pass-through floor.
The retrograde share arrives externally, so total collision mass per final vehicle mass is
`[exp((1-m_rp) Δv/v_e) - 1]/(1-m_rp)`, not the conventional `exp(Δv/v_e) - 1`.
_Avoid_: calling `v_g` an "energy ceiling" on exhaust velocity; it ceilings `v_g`, not `v_e`.
That conflation produced a real error in `sec:methalox_rebuttal` (an assumed 25 km/s that
exceeded the 24 km/s ideal ceiling), corrected 2026-08-17.

**Impulse trim (mass-mismatch trim)**:
How a pre-placed transport formation absorbs the rocket plane's flight-day mass differing
from the mass the orbits were planned around (decided 2026-07-17 grill; lives at the end of
`sec:200_mile_high`). The formation is sized for the plane's **maximum takeoff mass**; every
lighter flight trims the delivered impulse *down*, since nothing already in orbit can add
impulse for a heavier plane. Three knobs in authority order: (1) **unit count** — withhold
surplus PuffSats (~1/N granularity; withheld units deorbit on their microthrusters or hold
for a later window); (2) **timing detune** — atomize early/late so the cloud arrives at the
plate off-shape, lowering the delivered momentum via the **fudge factor (`f`)**; fine vernier
only, because the impact sim's shape study (ADR-0028) finds `f` gently sloped and cliff-free
(max normalized sensitivity S ≈ 0.26 inside an *assumed* ±20% shape box) and the
timing-to-arriving-shape mapping (the deferred cloud-schedule study) is not yet simulated;
(3) **onboard ballast/fuel trim** — top off fuel or ballast toward the design mass and pump
fuel between tanks so the center of mass sits where the down-kick plate geometry
(`sec:pusher_plate_down_kick`) assumes it (Concorde trim-tank precedent, Rech & Leyman).
The retrograde deceleration formation inherits the same knobs with better information
(reentry mass is fixed at takeoff).
_Avoid_: presenting timing detune as a large-authority knob or quoting its S value without
the assumed-shape-box caveat; "axially symmetric mass distribution" (the requirement is the
center of mass on the impulse line through the impact point, not full symmetry).

**Magnetic nozzle**:
A magnetic field that redirects the conductive collision plasma with no material contact,
so there is no ablation and no thermal-fluence size floor. The plasma cooperates only when
it is hot enough to be a near-perfect conductor (high magnetic Reynolds number `Rm`), so a
magnetic nozzle is a *high-energy-regime* tool: favored near the Sun (fully ionized,
`Rm ~ 10⁷`), not at LEO insertion (weakly ionized gas, where a material plate wins). Used
two ways with opposite energy goals. In **propulsion** (near-Sun chamber,
`sec:periapsis_challenges`) it *reflects* the plasma near-elastically to redirect momentum
for thrust; the field is a conservative spring, and the momentum floor still reacts as J×B
on the coil. In the **Straw Way power plant** it *guides* the plasma (a ~90° turn from the
vertical tube into a horizontal, km-long MHD channel) so its kinetic energy can be
*extracted* as electricity; here braking the plasma is the point, not conserving its
momentum.
_Avoid_: implying it removes the momentum/mass floor (it removes ablation only); conflating
the propulsion "reflect for thrust" role with the power-plant "guide-then-extract" role.

**Field's share (of a pulse)**:
The fraction of each pulse's collision energy the magnetic nozzle's field must actually
catch and redirect, as opposed to energy that exits the open back unaided. Both the
virial floor and the standoff radius scale linearly with it. Working number **~1/2**
(band ~0.3–1), decided 2026-07-14: the 3:1 diluted fireball drifts at only Mach ~0.8
(155 km/s drift against ~200 km/s internal sound speed; ~75% of pulse energy
thermalizes), and the head-on stagnation region squirts radially into the field, so the
plasma is a slow explosion, not a collimated jet. Mini-Mag Orion's isotropic fission
burst has share ≈ 1. The only route below ~1/2 is the hybrid nozzle, where a sacrificial
low-Z absorber takes the bulk blast and the field stands the hot core off it. Posture
(revised 2026-07-14, same day): the paper's quoted numbers are the **pure magnetic case
at share ½**; the hybrid is mentioned as a conditional refinement (roughly 2× nozzle
mass saving at share ~0.15) whose viability hangs on an unverified wall-heating
fraction (f_wall ≲ 3e-4, an impact-sim deliverable), so it is not load-bearing for any
quoted mass.
_Avoid_: "the field only trims divergence" (pre-2026-07-14 wording; overstates
collimation); claiming a small share without invoking the absorber.

**Virial floor (magnet mass)**:
The minimum structural mass of any magnet holding field energy `E_B`:
`M ≳ (ρ/σ_eff)·E_B`, from reacting the Maxwell stress, independent of conductor
technology; chained through the standoff condition,
`M ≳ (ρ/σ_eff) × (field's share) × E_pulse`. `σ_eff` is **strain-throttled**, not the
material's tensile strength: structure at the winding radius stretches with the REBCO
tape (limit ~0.4% elongation), so it can only develop (modulus × 0.004). Adopted band
(2026-07-14) **0.4–1.2 MJ/kg**: standard carbon fiber plain build at 0.4; high-modulus
(M55J-class) fiber plus assembly pre-compression (~ −0.25% squash, widening the usable
window to ~0.65%) at 1.2. A Kevlar/aramid overwrap is an *implementation of
pre-compression* (its high elongation lets it be wound at high pre-tension), not an
escape from the strain limit; as plain stiffening its low modulus makes it worse than
carbon, and creep limits sustained pre-tension. Mini-Mag's 200 t at 340 GJ sits at or
below the strain-matched floor, so treat it as their claim, not a validated benchmark.
Verified against the sources 2026-07-14: AIAA 2003-4525 specifies the nozzle in one
sentence (5 coils over 11 m, 10 MA each, ~200 t total) with no conductor type, field
strength, structural material, or mass breakdown; Lenard & Andrews 2007 adds nothing on
the coil. The 200 t is an unengineered point-design allocation, and no shield fraction
can be extracted from it.
_Avoid_: sizing winding structure by tensile *strength* (strain compatibility throttles
it); framing the constraint as cryogenic material survival (cold mildly helps; the
stretch-together geometry is the constraint).

**REBCO tape term (conductor mass)**:
Second term of the two-term nozzle mass model. Ampere-turns ≈ `2RB/μ₀` regardless of
conductor quality, so tape mass ∝ `R²B/I_tape` ∝ `(share·E_pulse)^(2/3)·B^(−1/3)`.
It falls more slowly than structure as pulses shrink, so **tape dominates small
nozzles**. At the adopted 20 T / 20 K anchor (SPARC-class working point, 300–600 A per
4 mm tape) with the scenario's own pulse energy (477 GJ for 2.5 kg at 618 km/s closing,
share ½): 100 g pulse ≈ 18–36 t tape vs ≈ 8–24 t structure (total ~26–60 t, replacing
the paper's "single-digit tonnes"); 2.5 kg pulse ≈ 150–310 t tape vs ≈ 200–600 t
structure (total ~350–900 t). Those tape figures assume standard 3.5 g/m tape; the
adopted policy is thin-substrate/thin-copper tape (30 µm Hastelloy + 5 µm Cu/side,
~1.5 g/m, a commercial product) wherever tape is dominant or comparable, cutting totals
to ~16–40 t (100 g) and ~265–730 t (2.5 kg). The copper floor is quench protection, not
resistance. Full derivation in `todos/nozzle_rewrite_plan_2026-07-14.md`, destined for
a new paper appendix with the math inline (closed-form, hand-checkable; the main text
quotes only the thin-tape band totals and points there). A calc-repo module is optional
follow-up for a sweep figure, not a gate (revised 2026-07-14 from "repo first").
This term is the concrete identity of the former
"minimum-coil-size floors". Model lives in the calc repo with the `rebco_tapes`
(Senatore 2024) current-scaling relations.
_Avoid_: "conductor mass is negligible with REBCO"; the pre-2026-07-14 "single-digit
tonnes" claim.

**Minimum-rocket conclusion (two anchors + ship classes)**:
How sec:minimum_nozzle states its bottom line (decided 2026-07-14): quote both nozzle
totals at the adopted thin-tape architecture (2.5 kg pulse ~265–730 t; 100 g pulse
~16–40 t), quote bands rather than single best-case points, and translate each into its
ship class: a multi-thousand-tonne vehicle for the big pulse (the former "better still
more than a thousand" is now a requirement, not a preference), and roughly
Starship-class at the light end (~65–400 t, nozzle a tenth to a quarter of the ship)
for the small pulse. The main text carries only these headlines plus a pointer to a new
appendix holding the full model and worked arithmetic. Propagation (decided 2026-07-14): the only downstream edit is
the methalox section's "vehicle carrying hundreds of tonnes or more" (line ~647), which
becomes thousand-tonne-and-up; the cascade's cost arithmetic is ratios and is untouched.
The cooling-system floor stays named but qualitative (pulsed heat into a 20 K magnet,
each absorbed watt costing tens of watts of plant); no invented absorbed-fraction
number, since that input waits on the impact simulation. The fission-vs-plasma radiation
contrast stays qualitative too: neither Mini-Mag source publishes a shield mass to cite.
_Avoid_: "single-digit tonnes"; leaving the ship-class implication implicit; quoting a
cryoplant power number.

**Standoff radius**:
The radius where the expanding pulse plasma's pressure meets magnetic pressure,
`R ~ (2μ₀ · share · E_pulse / B²)^(1/3) ∝ B^(-2/3)`: a stronger field gives a physically
smaller nozzle at the same virial mass. The ceiling on `B` is itself mechanical (REBCO
windings are strain-limited near 0.4%), so material strength limits the field and field
pressure limits the radius.
_Avoid_: reading a smaller radius as a lighter nozzle (virial mass tracks contained
energy, not size).

### Heliocentric re-intercept (solar-dive return)

**Earth re-intercept**:
The requirement that a boosted solar-dive projectile arrive *where Earth actually is*,
not merely cross `1 AU` somewhere. The boosted orbit is hyperbolic and crosses 1 AU only
once, about 0.2 yr after launch, roughly 136° of heliocentric longitude from Earth. The
projectile whips ~295° around perihelion while Earth advances only ~70°, so the miss is
set by the whip-around, not by Earth's drift. Re-aiming at periapsis is prohibitive
(~5.4 km/s per degree at the 309 km/s, 4 R☉ periapsis speed).
_Avoid_: "interception" (reserved for the near-term LEO terminal-guidance sense below);
treating "crosses Earth's orbit" as if it meant "hits Earth."

**Phasing loop**:
A pre-dive maneuver that delays the deep dive until Earth reaches the fixed crossing point,
so the return re-intercepts Earth. Every boost is a PuffSat collision, not carried
propellant, so any of these can supply the impulse. Three realizations:
(1) *Two-impulse loop* (periapsis-lowering shallow dip, then deep dive): the two retrograde
boosts are colinear, so it is free in total impulse (~24 km/s, same as a direct dive) and
holds the doubling factor at two. It needs a second PuffSat boost node at 1 AU, off Earth,
where the loop returns; a mature network fields it, an early one may not. First resonance
~0.82 yr. Apoapsis-raising is the wasteful direction (opposing boosts, ~+7.6 km/s,
~1.82 yr).
(2) *Single-impulse resonant dive* (inject outbound to ~1.9 AU aphelion): needs only the
Earth boost node, but the boost grows ~24 → ~37 km/s (the direct dive's ~24 km/s retrograde
component plus a ~28 km/s outbound radial component), which spends more PuffSats and drops
the doubling factor below two. ~0.85 yr; the aphelion is the knob that closes the geometry.
(3) *Gravity-assist resonant return* (Venus/Earth flyby): impulse-free phasing, ~1--2 yr,
constrained by flyby timing.
_Avoid_: calling phasing impossible or requiring a "rocket burn" (PuffSat collisions
provide all impulses); presenting apoapsis-raising as the default; rotating the argument of
periapsis for a *fast* dive (no in-plane solution when launching from the aphelion of a
deep diver).

**Re-intercept cycle floor (~0.82 yr)**:
The shortest Earth-to-Earth solar-dive cycle that actually re-intercepts Earth, set by the
first phasing resonance. Supersedes the paper's earlier implied ~0.5 yr ("6 month") cycle.
At one payload doubling per cycle, a millionfold scaling takes ~16 yr, not under a decade.

### Interception navigation (near-term LEO)

**Common-mode error**:
An error shared by every PuffSat in the train, which slides the whole block together and
is cancelled by re-aiming.
_Avoid_: bias (overloaded with the optical calibration bias below).
_Aliases (informal, OK in prose)_: block-miss, block-slide.

**Per-unit scatter**:
How individual PuffSats differ from *each other*. Cannot be re-aimed away; must fit
inside the catch radius.
_Aliases (informal)_: spread.

**Centroid retarget**:
Shifting the swarm's collective aim point (up to about ±2 km) to absorb common-mode
error.

**Catch radius**:
The largest miss the projectile can still correct in the final seconds (about 475 m).
Set by engine thrust (a control/authority limit), *not* by sensing.

**PuffSat GNSS cross-check** (accepted 2026-08-20 grill, supersedes the 2026-08-12
blanket rejection):
A GNSS receiver on each PuffSat, differenced against a base receiver on the target, used
as an **independent cross-check** on the optical terminal chain. The optical chain stays
load-bearing; GNSS never becomes primary. Scope is the near-Earth LEO cycle only, and
within it the last ~13 minutes of the descent.
_Window_: the descent crosses the ~20,200 km GNSS shell 73 min before interception and
reaches near-terrestrial geometry (~3,000 km) 13 min out. The full-authority divert
horizon is ~487 s (½at² for 475 m at 4 mm/s²), so **GNSS arrives about 5 minutes before
the correction horizon closes**. That margin is the feasibility argument.
_Topology_: the target is the base and broadcasts; PuffSats receive and solve. This keeps
the no-transmitter-on-the-PuffSat commitment intact.
_Achievable grade_: **~18 mm**, the RSS of the GNSS terms alone (no troposphere at
altitude, and ephemeris/clock/most ionosphere cancel over a 5 km baseline).
_Spin phase is self-solving, not an input_ (resolved 2026-08-20). A tip-mounted antenna
rides a 12.5 m circle at 9.25 m/s, which writes a clean 0.118 Hz tone into the carrier
phase of every satellite. Measuring a 12.5 m amplitude at 1--2 mm carrier-phase precision
gives spin phase to ~0.005°, against the 0.09° that 2 cm needs. Ninety-two revolutions fit
inside the 780 s window, orbital motion has no content at 0.118 Hz, and a constant integer
ambiguity cannot affect a sinusoid, so this works on time-differenced phase without fixing
integers. Same principle as multi-antenna GNSS attitude determination, with the baseline
swept in time by one antenna instead of realized in space by two.
_Inertial package supplies the model, GNSS supplies the anchor_ (2026-08-20). The two are
complementary and **neither closes 2 cm alone**.
- The ADR-0002 accelerometer triad delivers the *geometry*. It reads `ω²r` directly, so
  with `r` known it gives ω to δa/2a = 7e-4 at a 1 mg floor, calibrating a 1--3% gyro
  scale factor down by 20--40x. It also resolves tether-pull direction to ~0.16 mrad with
  1 s of averaging against the 6.8 m/s² tip field, a factor of 10 inside the 1.6 mrad that
  2 cm needs. ADR-0002 already sized this leg at 8 mrad; 1.6 mrad is a 5x tightening, not
  a redesign.
- What the inertial package **cannot** supply is absolute azimuth about the spin axis. A
  gyro reads rate, an accelerometer reads specific force, and neither has an inertial
  azimuth reference on a spinning body. Dead-reckoning 780 s (33,072° of rotation) to 0.09°
  needs ω to **2.7 ppm**; the best accelerometer-calibrated figure is 7e-5, giving 2.3°.
  No MEMS part is within 25x. The shortfall is inherent to integrating a rate, not a
  matter of part selection.
- The split also runs in time. **Between burns** the arm is a clean circle and GNSS anchors
  phase. **During burns** the geometry is ADR-0002's 2.9 m kink and the triad carries it.
  The transverse tether mode at ~11.8 Hz (~100x spin) sits far above the estimation band.
_Paper scope_ (decided 2026-08-20): **one sentence**, in the redundancy-layer paragraph of
`sec:sensor_architecture` (near line 460), covered by that paragraph's existing "none of
this layer is simulated" closer. Everything below stays here, not in the paper, because
GNSS clears Tier 1 by orders of magnitude and a cross-check that is not load-bearing does
not earn a paragraph.
_Why the constellation cannot serve interception_: not link budget, geometry. A focused
beam closes the power side easily (a 3,300 km stream at 150,000 km needs 22 mrad = 1.26°,
worth ~44 dBi, from a 0.52 m Ka dish or 0.28 m at 60 GHz). But perigee and apogee sit at
opposite ends of the major axis with Earth between them. At the 200 km interception
altitude the true anomaly is 17.6°, putting the apogee direction **16.9° from nadir against
Earth's 75.8° angular radius**. The constellation is behind the planet, and no antenna gain
beams through a planet.
_The handover is forced, and it is clean_: occultation begins at ν ≈ 76° (r = 10,089 km),
**15 min before interception**. GNSS is available from the shell crossing at 73 min and
reaches good geometry at 13 min. So there is a **58-minute overlap and no gap**, and
neither number was designed.
_Downlink_ (decided 2026-08-20): **modulate the existing beacon**, 0 g. The blink pattern
is already read in every gated exposure by the target-side array, so no RF hardware, no
antenna, and line 446's no-transmitter commitment survives. Bandwidth is a few bits/s, set
by the tracker frame rate, which carries a disagreement flag and a coarse residual but not
raw observables.
_Mass and cost_: ~20 g for a purpose-built receiver (patch antenna dominates; DLR's Phoenix
flew PRISMA's cm-class relative nav at ~20 g, 0.85 W), i.e. **8% of the 250 g dry budget**.
Power is a non-issue (1.03 Wh over the full 73 min against ~3 Wh in a 5 g primary cell).
Cost is NRE, not per-unit: **do not buy space-qualified** ($10--50k each × 900 is
prohibitive). A 1.35-day, two-belt-crossing life is ~50x milder than the five-month park
CONTEXT already calls "deliberately cheap electronics", so commercial automotive silicon
serves. Budget ~$1--5M one-time for firmware (COCOM removal, ±60 kHz Doppler) and $50--500
per unit at volume.
_What the cross-check buys_: 2 cm at the co-flyer's 150 km standoff bounds the optical
angular error at **0.13 µrad**, 12x below the assumed 1.6 µrad fusion floor, from a single
unit with no averaging. This settles the flagged-open "is the 1.6 µrad floor noise or
bias?" question with flight data rather than a bench test.
_Antenna_: boresight **along the spin axis**, tip-mounted. The sky view is then fixed and
the antenna merely translates on a known circle at 9.25 m/s. Carrier phase wind-up (one
cycle, 19.03 cm on L1, per 8.5 s revolution) is deterministic and largely common across
satellites, so the receiver clock absorbs most of it.
_Avoid_: fusing the ~1 m GNSS vector into the ~1.6 cm optical estimate (it moves the answer
by nothing); assuming it helps anywhere off Earth (the Jupiter, solar-dive, lunar and
Parker cycles have no GNSS); assuming it reaches the gas-momentum centroid (it measures the
dry package, same as the beacon); a commodity receiver (COCOM cuts out above 515 m/s and
18 km, and L1 Doppler here runs to ±60 kHz).

**Cross-track knowledge** (`σ_θ · R`):
The projectile's lateral position error relative to the target, equal to angular
precision `σ_θ` times range `R`. The binding constraint on success, limited by a fixed
optical *calibration bias*, not by random noise.

**Plate capture**:
The mission-success criterion: a PuffSat landing anywhere within the ~5 m plate
(≥99 % probability), not hitting a precise point.
_Avoid_: "centimetre centring" as the *committed* requirement (see Flagged ambiguities).

**Feasibility tiers**:
The three confidence levels the interception claim is carried at, kept deliberately
separate. Tier 1: a 5 m plate capture, closed-loop simulated (companion repo
`puffsat_control_simulation`). Tier 2: a ~10 cm plate, *sized* (**surveyor-anchored
centring**, ADR 0022: nominal ~5.8 cm, 10 cm robust), not simulated; its binders are
bench characterizations a Monte Carlo cannot produce. Tier 3: a near-Sun/Parker
extension, an architectural sketch with open numbers. Only Tier 1 is a simulation
result. The tiers answer *different questions*, not one question at different
confidence: Tier 1 proves the closed-loop dynamics and nav grade (the committed
requirement); Tier 2 shows the metrology can center inside the funnel Tier 1 already
proved (capability). Neither demotes the other (2026-07-02 grill, provisional:
recommended framing adopted while Seth was away).

**Off-board nav assets (LEO)**:
The interception's support hardware, redistributed from the paper's original single
**coordinator node** into the three roles below. No dedicated per-mission co-flying
coordinator satellite is needed for LEO; the tracking-and-relay role is carried by
permanent infrastructure plus assets already in the architecture (the target, the reused
launch rocket).

**Apogee nav constellation**:
A permanent ~150,000 km Ka-band, authenticated *one-way broadcast* network that pins the
PuffSat's coast/apogee position; the PuffSat is a passive receiver. Sized to *match* (not
beat) the coast accuracy the corrector needs; ~3 members suffice. Clock/transponder
placement (ADR 0020, reconfirmed 2026-07-02 grill): precise clocks live on the
*constellation members*; the PuffSat carries a sub-gram verify-only receive ASIC, no
transmitter, and solves its clock bias from ≥4 members like a GNSS receiver; the target
and co-flyer rockets carry the full two-way crypto-nanosecond echo transponders.
_Avoid_: "GNSS at apogee" as the baseline (GPS side-lobe fixes have reached ~150,000+ km
on NASA's MMS, but they are weak, unauthenticated, and geometrically poor there; the paper
acknowledges MMS and explains why the dedicated constellation wins — resolved 2026-07-02
grill); "coordinator node" (this is permanent infra, not a co-flyer); putting an echo
transponder or precise clock on the PuffSat; treating a PuffSat **GNSS receiver** as a
*replacement* for the apogee constellation or for the optical terminal chain (it exists
only below the ~20,200 km GNSS shell, and only near Earth; see **PuffSat GNSS
cross-check**).
_Superseded_: the flat 2026-08-12 rejection of a PuffSat GNSS receiver. Two of its three
reasons do not survive the 2026-08-20 reframing. Range collapse does not apply to a
differential baseline, and phase-centre variation binds only at Tier 2. The lock-loss
reason assumed a radially-pointing antenna. See **PuffSat GNSS cross-check**.

**Target-side tracker array**:
The load-bearing terminal sensor: several (~5) independent, separately bench-calibrated
detectors on the target that image each PuffSat's optical beacon against a reference-star
field. Fusing them beats one detector by √N down to a common-mode floor (~1.6 µrad),
against a ~3.2 µrad requirement. Fallback (ADR 0019, paper alignment resolved 2026-07-02
grill): if bench calibration proves optimistic on the vibrating vehicle, about a dozen
cruder 10 µrad detectors average back to the required grade; the paper states both, in
these roles.
_Avoid_: calling it a coordinator node; expecting *ranging* to sharpen the lateral (angle
does the cross-track work); presenting the dozen-crude-detector fallback as the committed
configuration.

**Co-flying tracker**:
The *role* of a quiet off-board vantage holding the measurement from PuffSat deployment down
to the 2--3 s handover of ADR-0003, where it fuses with and yields to the **target-side
tracker array**. It is a role, not a vehicle: which vehicle fills it depends on the cycle.
- LEO cycle (`sec:starship_safelaunch`): the reused launch rocket.
  _Avoid_ treating it as a dedicated new satellite *there*; it is the launch rocket, reused.
- Staged crewed launch (`sec:periapsis_challenges`): the **tracker platform**, decided
  2026-08-12. The staged path has no launch rocket to reuse, because the PuffSats come from a
  **staging carrier** already in the ellipse and the crew vehicle's reusable ground launcher
  (line 752) never reaches the 10.9 km/s needed to fly alongside.
Sub-decisions: **plate-beacon differencing**, and a star channel decoupled from the 1 ms
beacon gate.
_Note_: this entry previously read "UNRESOLVED" and described the co-flyer as a redundant
hedge not required for the 5 m verdict. Both were stale as of ADR-0003; corrected 2026-08-12.

**Tracker platform**:
The permanent, refuelable sensor vehicle that fills the **co-flying tracker** role on staged
crewed launches. Parked in the **staging ellipse** at the same 2.7 d period as the carriers, so
phasing holds once set. Distinct from a **staging carrier**, which is a cheap tank that empties;
carriers proliferate as waves double each cycle, and the platform is the one asset worth
amortizing across many of them.
_Avoid_: coordinator node (legacy term for the rejected per-mission co-flying brain; the
platform is shared infrastructure, like the **apogee nav constellation**, which is the side of
the 2026-06-30 decision that was *accepted*), co-flyer satellite, tug.
_Budget_: parks at ~1000 km perigee to clear drag across the **storage interval**, drops to a
~200 km operating perigee for the push and returns, about 26 m/s each way, call it 50--100 m/s
per flight all in. Under 3% of vehicle mass per flight at methalox exhaust velocity, so roughly
30 flights per propellant load equal to dry mass. It never leaves the ellipse.
_Vantage_: the 200 km operating perigee against the PuffSats' 50 km disposal perigee is a
150 km **radial** offset bought for ~5 m/s at apogee, which must be paired with a comparable
along-track offset to satisfy the **miss plane** geometry. A purely radial offset is blind in
the radial miss axis.
_Refuelling_: the propellant rides up as a *dedicated consignment* in the **staging carrier**'s
payload, not scavenged from the PuffSat fill. Decided 2026-08-12. What matters is that it
arrives free with every wave, so there is no Earth tanker chain and no depot, which is the last
thing the Lagrange proposal was reaching for. Scavenging the carrier's water and running
**on-demand electrolysis propellant** was considered and set aside: it works, but it buys a
water plant and a several-kW array to avoid carrying a tank that costs a rounding error.
Every chemistry is affordable, because the platform's whole per-flight budget is 50--150 m/s
against the ~850 t a single crewed launch consumes (line 198):
- cold-gas propane (`sec:cold_gas_fluid_choice`), Isp ~70 s: ~2.4 t/flight for a 10 t platform,
  0.3% of a wave. Stores indefinitely, self-pressurising, no catalyst.
- peroxide/propane bipropellant (`sec:peroxide_propane_biprop`), Isp ~250--300 s: ~0.6 t/flight.
  Note the **storable PuffSat** exclusion of peroxide does *not* transfer here: that ruling was
  about 60% H₂O₂ inside a 250 g thin-skinned balloon, and bulk tankage with a real vent path and
  thermal control is a different problem.
_Preferred mechanism_: swap the tank rather than transfer fluid. The carrier brings a full one
and takes the empty. It needs no fluid interface, and it caps peroxide age at one wave interval
rather than at platform lifetime.
_Open_: which chemistry. Both close on mass; the decision is shelf life against dry mass.

**Plate-beacon differencing** (provisional, 2026-08-12 grill):
If the terminal measurement moves off the target, it must be a *differential angle*:
a strobed beacon on the plate rim is centroided in the same frame as the PuffSat
beacon, and only their angular separation is reported. This makes the co-flyer's
absolute position cancel to first order, leaving `miss ≈ θ_sep · D` with `D` the
scalar co-flyer-to-target range. Without it, an absolute line-of-sight measurement
must be registered to the plate through a separately-known co-flyer-to-target vector,
which the paper prices at ~2 m (GNSS, `sec:sensor_architecture`) and which alone
consumes the whole Tier 1 tolerance.
_Avoid_: assuming a co-flyer measurement is automatically referred to the plate. The
**target-side tracker array** gets that registration free by being bolted to the plate;
a co-flyer must buy it.

**Miss plane**:
The plane perpendicular to the PuffSat-target relative velocity, containing the two
error components that actually cause a miss: **radial** (altitude) and **cross-track**.
The third component, along the relative velocity, is *timing*, not miss. A tracker's
blind axis is its own line of sight, so vantage choice decides which miss component is
unobservable: a co-flyer directly overhead is blind in radial (bad), one offset purely
cross-track is blind in cross-track (bad), one offset **along-track** is blind only in
timing (good). For an offset with altitude `h` and along-track distance `x`, the radial
error is `(h²+x²)/x · σ_θ`, minimised at `x = h` (45° elevation) to give `2·h·σ_θ`.
_Avoid_: reading "closer is better" off `σ_θ · R` alone. Closest approach is exactly
when an overhead co-flyer is blind in radial. Range and observability fight.

**Differential astrometry** (star-differencing, the "Gaia trick"):
Measuring a beacon's bearing relative to reference stars in the *same* exposure, so the
focal-plane distortion common to beacon and nearby stars cancels. This is what "star maps"
buy: they attack the binding **cross-track knowledge** error, which is a fixed optical
*calibration bias*, not random noise.

**PuffSat self-homing** (redundancy layer, not yet simulated):
An optional autonomy layer: each PuffSat also carries a few-gram camera to image a bright
target beacon against stars and run its own terminal guidance, fused with the target-side
measurement. Strengthens the no-co-flyer story; costs a little non-volatile dry mass to
dispose of before impact. The sim modeled only the target-side path, so this is a
speculative addition, not a simulation result. Extended (2026-07-02 grill) to cover
inter-PuffSat bearing as part of the same optional layer: a camera pointed *backward*
images the follower's strobed beacon (pulsed LED or Q-switched laser plus narrowband
filter) against dark sky, exploiting the short inter-unit range; forward staring into the
impact flash is avoided per the sim's anchor-as-surveyor rule.
Cameras may be carried in threes for two-of-three majority voting: fault containment
(a systematic defect in one camera is rejected as an outlier), *not* a √3 precision
gain, which shared-batch distortion forbids (ADR 0019 independence rule).
_Avoid_: presenting it as the load-bearing baseline (the **target-side tracker array**
is); promoting inter-PuffSat bearing into Tier 1; claiming √N bias averaging across
same-batch cameras.

**Coordinator node** (fallback option, superseded as baseline for LEO):
The paper's original picture: a co-flying satellite that tracks each PuffSat and uplinks
commands. Superseded for LEO by the **off-board nav assets** above. The rewrite landed
2026-07-02: `sec:sensor_architecture` now holds the consolidated sensor/nav architecture,
with the coordinator node as its closing held-in-reserve paragraph, and
`sec:coordinator_node_dry_mass_disposal` retains only dry-mass disposal (label kept so
existing cross-references resolve).
_Avoid_: using it for the new architecture (name the specific asset instead).

**Surveyor-anchored centring**:
An optional metrology upgrade (a sacrificial "surveyor" projectile measured by an
independent instrumented gate, plus strobed beacons on each unit) that shrinks the
plate from 5 m toward ~10 cm without changing the baseline architecture. Now *sized*,
not just argued (sim repo `centering_budget.py`, ADR 0022, folded into the paper
2026-07-02 grill): the plate is the RSS of two legs, the hoop precision σ_hoop and the
camera scatter σ_θ·v/f. Nominal point ~5.8 cm (1 cm hoop ⊕ 3 µrad camera at the 2 Hz
link); 10 cm tolerates σ_hoop ≤ 2.9 cm; 5 cm needs *both* legs tightened. A Q-switched,
coarse-pointed beacon (~100 kW peak, few-hundred-mW average) plus narrowband filter and
matched gate keeps the intra-train link distortion-limited, not photon-limited.
Thermal-distortion hierarchy (ADR 0022 §5, reconfirmed 2026-07-02 grill): differential
astrometry is the *primary* lever (thermal figure error is smooth, so star-differencing
cancels it); thermal modelling with software correction (Gaia precedent) and a
reflective narrowband front element with edge-cooled diamond conduction (gyrotron
practice) are *backup/margin*, load-bearing only near the Sun.
_Avoid_: "achieved" (binders are unmeasured bench characterizations; right next rigor
is a bench test, not a sim); putting the diamond filter in the load-bearing LEO role.

**Beacon lever arm** (spinning tethered pair only, resolved 2026-08-11 grill):
The vector from a strobed beacon to the point guidance actually cares about, the center
body, which the tip packages of `sec:spinning_tension_detail` straddle at roughly ±12.5 m
on the 25 m bundle. Its length follows from the tether design; only its *direction* is
open. Scoped as a **refinement-only** error: 2 m of tolerance across a 12.5 m arm is
160 mrad (9.2°), which a taut tether never reaches, so the 5 m capture verdict does not
depend on it; the ~10 cm centring refinement needs 8 mrad and does.
_Avoid_: "the beacon is on the dry mass" as the statement of the problem. A beacon is
always dry mass (LED, battery, driver). The live choice is *which* dry mass carries it,
a tip package or the center body.

**Tip-beacon pair** (resolved 2026-08-11 grill):
Both end packages strobe, and the target-side array averages the two bearings. At near-equal
range the mean bearing *is* the bearing to the chord midpoint, with no range knowledge, no
package attitude, and no tether model, at σ_θ/√2 (~1.1 µrad). The 25 m separation subtends
417 µrad at 60 km, hundreds of times the precision, so the pair always resolves; blink-pattern
IDs already distinguish them. Chosen over inferring the lever arm from tip accelerometry,
which stacks gyro drift, a tip-tangent-vs-chord mode assumption, and a 12.5 m extrapolation.
Costs a few grams on the counterweight and doubles the beacons the tracker must associate.
_Avoid_: treating it as a complete solution. It cancels **antisymmetric bend** (S-curve, tips
swing oppositely) and is *blind to* **symmetric bow** (C-curve, tips stay put and the center
displaces), which is exactly what a transverse force on the center body produces. Detecting
that bow is the residual job left to accelerometry.

**Center-body kink** (the dominant deflection; ADR 0002, sized 2026-08-11 grill, not yet in the
companion repo):
Under thrust the 25 m bundle is not a bow but a shallow V, with the kink at the center body,
which the two half-tethers have to drag along. Force balance at the center gives
`sin θ = F / 2T`, half-angle θ, total thrust F, tether tension T. At F = 400 mN and
T = 0.85 N: **θ = 13.6°, putting the center body 2.9 m off the tip-to-tip chord.** Modulates
over the spin period, full amplitude when the tether axis is perpendicular to thrust and
zero when parallel (there the load is a tension differential, not a kink), so it is a
spin-synchronous signal with known phase. Proportional to thrust, so 3% thrust knowledge
buys 10 cm; the triad measures θ directly at ~0.15 mrad. Assembly integrity needs `2T > F`,
about 4x margin here. Disposal geometry survives: tips stay 12.15 m off the impact axis
against a 5 m plate.
_Avoid_: locating the deflection at the *thrusting tip* (a tip thruster firing in a fixed
body direction is a torque, not a bend; coordinated thrust from both tips cancels the torque
and translates cleanly, leaving the tethers radial at the tips); treating it as a **bow**,
which the **tip-beacon pair** would partly see, when a symmetric kink is exactly its blind spot.

**Tip-pull bend** (the small, benign companion term):
Each tip must be accelerated at the assembly's rate by its own half-tether, giving
`a_assembly / (ω²r)` = 2.4 mrad at 400 mN, 0.1 mrad at 17 mN drag cancellation.
Baseline: ω ≈ 0.74 rad/s (isobaric ceiling at a ~0.18 m charge radius), r = 12.5 m, tip
centrifugal 6.8 m/s², spin period 8.5 s. The tip sits ~70x further from the axis than the
charge, so the layout buys tension without touching the isobaric ceiling. Bare 100 µm bundle
drag at 200 km adds 0.09 mrad; the bundle weighs 0.27 g over 25 m and breaks at ~45 N against
0.85 N working load, so it is sized by handling and redundancy, not by load.
_Avoid_: comparing raw thrust to tether tension (off by the 200:1 assembly/tip mass ratio);
using the 400 mN figure as a drag number (tex:376 says it is actuator authority; the
simulation's drag is 17 mN).

**Quasi-static tether response** (resolved 2026-08-11 grill):
The fundamental transverse mode of each 12.5 m half-tether is `c/2L` with `c = √(T/μ)`,
about **11 Hz** for a 100 µm bundle (3.5 Hz for ten redundant strands), far above any
throttled-thrust bandwidth. So the tether tracks commanded thrust quasi-statically with no
ring to outlast, and **throttled thrust can run continuously to impact with no quiet period**.
Deflection is then a commanded quantity to subtract, not a transient to wait out. Solid-charge
impulses are the exception (step response overshoots ~2x and rings at 11 Hz), so they stay
early in flight.
_Avoid_: the "pendulum after thrust cutoff" model, which assumes a mode near the spin rate;
the real mode is ~100x the spin frequency.

**Accelerometer triad** (role settled 2026-08-11 grill):
Three co-located 3-axis MEMS parts (~1 g) on the **sensing** package, not the thruster package
(a 400 mN thruster on a 125 g tip is 3.2 m/s² of self-induced specific force against a
0.016 m/s² signal, a 200:1 swamp; the paper's existing thruster/sensor split gives this free).
Load-bearing, not a bound check: the **center-body kink** is the **tip-beacon pair**'s blind
spot and at 2.9 m overruns even the 2 m tolerance, so nothing else measures it. Three units
vote 2-of-3 against a silent bias, reusing the camera-triad logic of tex:443.
_Avoid_: justifying the count by signal strength (averaging buys only √N, 1.7x for three, which
one better part buys outright) or by the centrifugal gradient (`a₂−a₁ = α×r + ω×(ω×r)`, which
needs *spread* units and is already covered better by the gram-class MEMS gyro over the
few-second window, at ~0.17 mrad of drift); spreading them into an actual triangle, since a
vote wants identical inputs, not a baseline.

**Kink downlink** (resolved 2026-08-11 grill):
θ goes to the target-side estimator over the **low-bandwidth radio** already in the 250 g
budget, not encoded in the beacon blink pattern. 11 bits at the ~2 Hz link cadence is 22 bps,
so bandwidth is never the issue. Chosen because the optical channel goes dark whenever an
impact saturates the tracker's rearward view (tex:439), and a separate radio keeps the kink
data flowing through those gaps rather than losing it with the beacon; it also leaves the
beacon pulses purely metrological, undisturbed by data modulation that would have to share
the matched gate and the centroid.
_Avoid_: assuming the radio's current sizing covers this. It is budgeted for housekeeping
across a multi-day coast; this is a hard-real-time terminal duty cycle, live and pointed
through the last seconds.
Open: whether a command uplink already exists that would let the PuffSat do the arithmetic
onboard instead, making any downlink unnecessary. Not confirmed.

**Isobaric ceiling ⇒ kink is unavoidable** (ADR 0002; resolved 2026-08-11 grill; universal
across variants):
Holding θ ≤ 8 mrad at 400 mN without measuring needs T ≥ 25 N, so ω = 4 rad/s, which puts
0.29 g on the charge, 7x past the 0.04 g mark where the isobaric gradient is already 10%.
The sensitization chemistry caps ω, ω caps T, T sets the kink, so **measurement is mandatory,
not a convenience**. This is the number CONTEXT's "a fast-spinning variant needs rechecking"
was waiting for. Decided to hold ω = 0.74 rad/s and fly the triad on *all* variants rather
than let non-explosive units spin faster: a variant-dependent spin rate means two tether
designs, 20 g tips, a fatter bundle (25 N against a 45 N break is only 1.8x), and it opens
cavitation-sphere stratification on liquid payloads.
_Avoid_: reusing CONTEXT's buoyancy dismissal for a *liquid* payload. That is computed for
the 50 Pa·s emulsion; in bulk water at 10⁻³ Pa·s the same Stokes creaming runs ~50,000x
faster, so a 100 µm cavitation sphere migrates tens of metres over a multi-day coast even at
0.01 g and fully stratifies to the spin axis. A frozen payload is immune.

**Sheath stripping** (resolved 2026-08-11 grill):
The inflatable bumper / nitrogen tube of `sec:spinning_tension_detail` deflates or is jettisoned
before the drag phase, having served as Whipple protection through the coast. A 3 cm sheath over
the 25 m bundle is 0.75 m² broadside and, being light with its own area, is not divided down by
assembly mass: ~24 mN of drag against 0.85 N of tension, a **28 mrad quasi-static bow** (0.35 m
of center displacement), 300x the bare bundle and the largest single bow term if retained.
Stripping it also changes what accelerometry has to do, from tracking a slow DC drift against
MEMS bias instability to band-passing a clean ~0.7 Hz post-burn transient.
_Avoid_: keeping the sheath through descent on the grounds that its drag is "a modest price";
that holds for the coast, not for the drag phase. Open: the PETN variant loses its grain-strike
bumper exactly when the tether is most loaded.

### Near-Sun navigation

**Transverse-node differential ranging**:
Lateral knowledge obtained from a coordinator node placed off to the side of the line of
flight, measuring distances only to the controlled projectile and a reference, and using
the difference.

**GDOP** (geometric dilution of precision):
How anchor geometry converts range precision into lateral precision,
`σ_lateral ≈ σ_range / sin θ`. A transverse node gives good GDOP (`sin θ ≈ 1`); an
in-line anchor gives terrible GDOP (`sin θ → 0`).

**Deterministic-coast correction**:
Two-tier control (a gross early correction of ~tens of m/s plus a fine, late ~mm/s nudge
about 1 s before impact) that defeats the `v²` homing-miss floor by nulling a known,
pre-measured offset rather than chasing fresh navigation noise.

### Economics

**Momentum-amplification cascade** (in the paper as `sec:methalox_rebuttal`, "Moneyball Meets Methalox"):
The chain that answers the obvious skeptic ("how can heat-tolerant, formation-flying
projectiles beat a tank of methalox?"). Fast, expensive reaction mass transfers momentum
to progressively larger amounts of slow, cheap mass at each collision, so cost per kg falls
by roughly the mass-amplification factor at every stage. For the 4 R☉ transport case:
a retrograde projectile (worst-case ~\$3200/kg, projectile-cost-dominated, early generation,
aviation-scale manufacturing but pre-breeding) is mixed 3:1 with cheap prograde mass
(÷4 → ~\$800/kg reaction mass at effective exhaust u_eff ≈ 155 km/s), boosted ~34.5 km/s at
periapsis to a 150 km/s Earth crossing (propellant fraction e^(34.5/155)−1 ≈ 25%, ÷~4 →
~\$200/kg at 150 km/s), then at Earth its kinetic energy is spread over ~24× cheap onboard
water/plastic (u_eff ≈ 25 km/s exhaust, ÷25 → ~\$8/kg of exhaust) which lifts ~2.6 kg to LEO
per kg exhausted (e^(8/25)−1 ≈ 0.38) → **~\$3/kg to LEO**, competitive with methalox even at
the worst-case anchor. Doubling for return-trajectory launches keeps it well under methalox;
the costly fast-cycling ship amortizes because PuffSats decelerate and recover it in Earth
orbit. The terminal number is only as firm as the mixing-chamber efficiency (the **fudge
factor** `f` / f-sim frontier); the magnetic nozzle is legitimate here despite being an
Earth-arrival stage because a 150 km/s collision is fully ionized (near-Sun-class energy),
unlike the weakly-ionized 8 km/s LEO PuffSats.
_Avoid_: quoting the ~\$3/kg output without the mixing-efficiency caveat; presenting it as a
cost model rather than an order-of-magnitude rebuttal; conflating the worst-case ~\$3200/kg
projectile anchor with the optimistic ~\$80/kg materials build-up (the latter, blended with
~90% cheap bulk to ~\$8/kg fleet cost, feeds the Straw Way power economics of
`sec:strawway_economics`, not the transport rebuttal: the \$8/kg retrograde fleet dilutes
~16× en route to Earth (÷4 from 3:1 prograde mixing, ÷4 from spreading over 4× its mass of
thrown payload, the same 25% propellant fraction as the transport chain) to ~\$0.50/kg,
i.e. ~\$0.16/MWh raw at 150 km/s (3.1 MWh/kg), quoted in the paper as "comfortably under
\$1/MWh" after conversion losses, against a 1¢/kWh ($10/MWh) price.

**Space mortgage** (planned, `sec:jupiter_only_growth`, as a `\subsubsection` placed after the
growth paragraph and before "Inner Planet Assist Alternatives"; title "With Space Mortgages,
First-Time Buyers Win"):
A **mass-denominated equity stake** in the Jupiter-only growth fleet, not a launch slot and
not a loan. The customer buys kilograms of PuffSat fleet mass; the holding compounds at the
chain's annual growth rate (companion ADR `0013`) for as long as it stays in the loop; the
customer redeems it as delivered payload whenever they choose to stop compounding. The
"mortgage" is the operator side: seed launches toward Jupiter are financed against those
subscriptions, with the in-transit fleet as the appreciating collateral. Early buyers win
because their kilograms compound through more cycles, and because the data their cycles
return raises **recovery** (`e`) for everyone after them. At the reference point
(`e = 0.6`, `f = 0.8`) a kilogram bought into cycle 1 is a x83,070 claim by 2055 against
~x20 for one bought into cycle 8, at the same price.
_Avoid_: calling it a forward contract or a prepaid launch slot (those are the rejected
alternatives, and they make the exponential decorative rather than load-bearing); using the
strict-mortgage framing where the *operator* is the borrower (then "first-time buyer" has no
referent); quoting a compounding multiple without naming both `e` and `f`.

**Redemption is withdrawal** (the conservation caveat the multiples rest on):
In the two-wave ledger the parked payload splits into **craft** and **slug** and *both* go back
to Jupiter. That is where the growth comes from. So a kilogram taken as delivered product is a
kilogram not reinvested: the fleet grows at `r − d` for redemption rate `d`, and **x83,070 is
the no-redemption number**. The section states this in two sentences and names a compounding
phase followed by a harvest phase. Far from weakening the pitch, it is what makes "first-time
buyers win" literally true rather than a slogan: the valuable claim is the one with the most
cycles left ahead of it.
_Avoid_: presenting the multiples without the reinvestment assumption; promising delivery on
demand during the compounding phase; adding an optimal-harvest crossover number (not computed
in the companion repo, and quoting one would need new code in `two_wave_growth.py` first).

**Register (Space Mortgages only)**: deliberately plainer than the surrounding paper. Target is
an AP-Physics student for the propulsion parts and an interested layperson for the investment
parts. Short sentences, everyday words, the arithmetic shown rather than asserted. This is a
local exception, not a change to the paper's voice elsewhere; the stylebook in `CLAUDE.md` still
applies in full (no em-dashes, no colon-welded sentences, no rule-of-three, quantify don't hedge).

**Numbers printed**: the multiple compounded over the **11 flown cycles / 28.3930 yr**
(2026-11-09 to 2055-04-02), *not* ADR 0013's 30-year projection. The 30-year mortgage framing
stays in the title and prose; every printed figure is ephemeris-verified. At the reference point
(`e = 0.6`, `f = 0.8`) that is **x83,070**, against x157,700 if the rate is extrapolated the last
1.6 yr. _Avoid_: printing the projection; deriving the table from ADR 0013's rounded e-folding
column (regenerate from `two_wave_growth.py` / `ChainGrowth.mass_after(28.3930)` instead, worth
~1.4% at the top corner: my derived reference cell reads x83,184 against the ADR's x83,070).

**Citation**: `\cite{Katz_aim_is_all_you_need_2025}` only, as everywhere else in the paper. The
ADR number is deliberately *not* named in prose and gets no deep-link bib entry, for consistency
with the paper's other twelve companion-repo cites. Decided 2026-08-20 against the alternative.

**The table, as it goes in the paper** (regenerated 2026-08-20 from `python -m src.two_wave_growth`
in the companion clone, `total_growth` column; reproduces ADR 0013's reference cell exactly).
Multiple of launched mass compounded over the 11 flown cycles, 28.3930 yr, 2026-11-09 to
2055-04-02:

| `e` | f = 0.5 | f = 0.6 | f = 0.7 | f = 0.8 |
| ---: | ---: | ---: | ---: | ---: |
| 0.25 | x0.0953 | x0.311 | x0.816 | x1.83 |
| 0.30 | x1.28 | x4.54 | x12.8 | x30.5 |
| 0.40 | x40.2 | x161 | x506 | x1,328 |
| 0.50 | x363 | x1,587 | x5,371 | x15,100 |
| 0.60 | x1,676 | x7,827 | x28,060 | x83,070 |
| 0.70 | x5,182 | x25,460 | x95,480 | x2.94e5 |
| 0.80 | x12,350 | x63,180 | x2.46e5 | x7.83e5 |
| 0.90 | x24,590 | x1.30e5 | x5.21e5 | x1.71e6 |

Two cells carry the argument. **`e = 0.25, f = 0.5` returns x0.0953**, nine and a half cents on
the dollar, the underwater case. **At `f = 0.8`, `e = 0.4` grows 28.83%/yr to x1,328 and
`e = 0.9` grows 65.76%/yr to x1.71e6** — roughly twice the annual rate for **1,284x** the mass.
That ratio is the compound-interest intuition the mortgage metaphor exists to carry.
The chain-optimal slug ratio `k` runs 4.53 to 9.52 across the table and is interior to the
search box everywhere.

**Supersedes**: the existing growth paragraph's ADR 0009 claims are rewritten in the same edit.
The perijove burn no longer buys the two-wave split (real orbits give the Lambert pair a free
encounter time; 8 of 11 cycles pay under 1 m/s, chain mean 0.179 km/s), and "the chamber recovers
80\% of the ideal thrust" was attached to a 1.7-1.8 yr doubling that is really the `e = 0.6` row
(`e = 0.8` doubles in 1.45 yr).

**Jupiter-cycle nozzle scaling** (new paragraph in `sec:minimum_nozzle`, pointed to from Space
Mortgages):
`sec:minimum_nozzle`'s "hundreds of tonnes of payload, better still more than a thousand"
amortization floor was drawn for the **near-Sun** pulse and does not bind the Jupiter-only
outbound leg. At `k = 8.53` the arriving kilogram vaporises 8.53 kg of slug, so the reduced
mass is 0.895 kg and a 75 km/s closure carries **2.52 GJ**, against **477 GJ** for 2.5 kg at
618 km/s. A factor of **189**. On the section's own rule that coil mass scales with contained
energy, and the Mini-Mag anchor of ~200 t for 340 GJ, that is **~1.5 t of coils** against
~281 t. The nozzle is then 14.8% of a 10 t craft, **4.9% of a 30 t craft**, 1.5% of a 100 t
one, so the seed vehicle is Starship-class rather than thousand-tonne-class. This is what makes
the **space mortgage** fund something buildable.
Ionization check, at AP-Physics register and verifiable in one line: specific kinetic energy
`½v²` spread over carbon atoms gives ~**4 eV/atom at 8 km/s** (below carbon's 11.26 eV first
ionization, matching the paper's "weakly ionized" low-orbit gas) and ~**350 eV/atom at
75 km/s**, about 31x over it. The outbound leg is therefore firmly on the ionized side of the
paper's own dividing line, so a magnetic nozzle is legitimate there.
_Provenance_: derived in the 2026-08-20 grill session, not in the companion repo. It is one
division against a cited anchor (`ewig2003minimag`, `lenard2007minimag`), so it needs no new
code, but it is a **linear extrapolation** and the paragraph must say so.
_Avoid_: quoting the 1.5 t without the linear-scaling caveat; letting `sec:minimum_nozzle`'s
thousand-tonne sentence stand unqualified once this paragraph exists; reusing the *lighter
impactor* radiative caveat here (this pulse is lighter by **speed**, not by impactor mass, so
its plasma is cooler and less radiative, not more).

**Overtake leg vs head-on leg** (`sec:jupiter_only_growth`; first decided 2026-08-20 grill,
**verdict reversed later the same day** after the companion two-leg sweep was regenerated):
Which device catches the growth push. Superseded content: the earlier version of this entry
argued the plate wins on *payload delivered per kilogram launched off Earth* (plate 1.000 vs
nozzle 0.700) and turned on the claim that a plate simply *is* a no-slug nozzle. Both are
retired. The launched-mass metric charges the nozzle for its slug and never charges the plate
architecture for its own ground launch, and it omits the per-PuffSat side where the nozzle wins.
The `k = 0` identity is arithmetic only (see below).

**The geometry still stands, and is why leg 2 has no choice.** The two legs face opposite ways.
- **Earth boost (leg 1)**: an **overtake**. The returning PuffSat catches the craft from behind
  and pushes it from rest into the parking orbit. The arrival's momentum already points where the
  craft is going, so a plate only has to reverse it. Ideal impulse `1 + sqrt(1+k)` times the
  arriving momentum.
- **Jupiter departure (leg 2)**: **head-on**. The arrival's momentum points backward, so a plate
  would *brake* the craft. Ideal impulse `sqrt(1+k) - 1`, which is zero at `k = 0`. Vaporizing a
  slug is the only mechanism there, not an optimization of one.

**The `k = 0` identity is formal, not physical.** As `k -> 0` the nozzle's parked-mass term goes
to the plate's with `e1` in the role of `f`. But a magnetic nozzle steers a **conductor**, and a
vanishing slug dissipates nothing in the merge, so there is no plasma to grip. `k = 0` sits
*below* the plume ignition window. The two are genuinely different devices. Do not write "a
pusher plate is what a magnetic nozzle becomes when it carries no slug" as a physical claim.

**Constraints on `k`, in the order they bind:**
1. **Plume ignition window** (two-sided). Only the dissipated share `k/(1+k)` of the arrival's
   kinetic energy heats the blob, spread over `1+k` kg, so `eps_th = w^2 k / (2(1+k)^2)`. That
   peaks at `k = 1` and falls on **both** sides, giving a closed interval, not a ceiling. Too
   little slug dissipates nothing; too much spreads a fixed energy too thin.
2. **Evaluated at the coldest instant of the burn.** The push runs the craft 0 -> 10.95 km/s, so
   `w` *falls* through the burn as the craft catches up. The last pulse is the coldest and sets
   the ceiling.
3. **Fleet-wide intersection.** One nozzle loading flies all eleven cycles, so the admissible set
   is the intersection over cycles, and the slowest cycle wins.

**2S vs 3S cadence** (regenerated 2026-08-20, 10-day split; the ADR 0013 default is 20 days and
gives ~1.7 km/s higher, so always pass `split_days=10`):

| cadence | cycles | growth-wave `v_b` | departure burn | cold end | `k1` ceiling | plate ratio at `f=0.8` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 synodic | 7 | 61.83-65.13 (mean 63.02) | 6.84-7.17 | 50.88-54.18 | 13.26-15.32 | 8.21-8.69 |
| 3 synodic | 4 | 56.53-57.43 (mean 57.17) | 5.32-5.54 | 45.58-46.48 | **10.21**-10.70 | 7.43-7.56 |

Both follow from one cause: squeezing Earth -> Jupiter -> Earth into two synodic periods forces a
more energetic transfer, which costs more to depart on *and* comes home faster. The 3S cycles are
the cheap-to-leave, slow-to-return ones, and they cap the fleet at `k1 = 10.21` where the best 2S
cycle alone would allow 15.32.

**Ignition bill**: 84.41 MJ/kg for water with a 1% potassium seed at 15,000 K. Atomisation
(H2O -> 2H + O) is **59.7%**, translational 36.7%, vaporisation 3.5%, seed ionisation **0.13%**.
The intuition that ionisation dominates is wrong once you seed. Hand check for the AP-Physics
register: atomisation costs 9.50 eV per molecule, heating the 3 atoms to 15,000 K costs
`4.5kT` = 5.82 eV, so chemical beats thermal by 1.63x; **the two cross at 24,500 K**. _Avoid_:
quoting 68% or any figure above 63.2% (that is chemical *including* vaporisation); forgetting the
model charges **no** water ionisation, only the seed, which is what pushes the bill down (5% of
hydrogen ionised takes it to 94 MJ/kg and drops `k1` to 8.94).

**Ground-launch ledger**: 2/3 of liftoff is launcher propellant, 1/4 of the remainder is launcher
dry mass, so **1/4 of liftoff reaches intercept**, and the loop must return **1/15 of liftoff**.
Applied per flown cycle. **This is what actually binds**: across the 8x8 grid it is active in
**56 of 64 cells** while the plume window is active in **one**. 15,000 K is a low bar for a
46 km/s impact; what stops `k` is that the water has to be launched.

**The verdict (reversed 2026-08-20): lead with the nozzle winning, at matched recovery.**
Comparing a nozzle at `e1` against a plate at `f = e1`, both over the flown chain:

| matched `e = f` | nozzle | plate | ratio |
| ---: | ---: | ---: | ---: |
| 0.25 | 0.000133 | 0.000309 | **x0.4 (nozzle loses)** |
| 0.30 | 0.0295 | 0.0291 | x1.0 (tie) |
| 0.40 | 13.2 | 6.96 | x1.9 |
| 0.60 | 6.63e4 | 7,827 | **x8.5** |
| 0.80 | 2.83e7 | 7.83e5 | x36.2 |
| 0.90 | 3.35e8 | 4.79e6 | x70.0 |

The advantage **switches on near `e = 0.3`** and only then compounds; below it the launch floor
crushes `k1` onto the window's lower root (~0.1) and the nozzle degenerates toward a plate while
still paying to launch slug. What breaks the tie in the nozzle's favour is that **`f = 0.8` is
the least defensible number in either architecture**: it was swept at 3.2-16 km/s
(`sec:mass_fraction`) and this leg runs 45-65 km/s. Nothing rebounds elastically at 46 km/s.
Against that `f = 0.8` specifically the crossover is `e1 ~ 0.6` at a good departure leg, rising
to ~0.7 at a mediocre one, and the paper states that number so a skeptic has it.

_Note the currency_: the companion writeup's "~25%" is a **growth-rate** advantage
(e-foldings/yr). In delivered mass over the 28.3930 yr chain the same cells are x4 to x70.
Always say which.

**Assumptions the verdict rests on, both directions:**
- Wrong-way bulk drift the overtaking nozzle must reverse is only `1/(1+k1)` of the blob energy,
  **8.9%** at the fleet ceiling. Argues `e1 ~ e2`. **In the nozzle's favour.**
- The overtake puts impactor entry and exhaust exit at the **same end** of the vehicle, so each
  arriving PuffSat flies up the previous shot's plume. Argues `e1 < e2`, possibly strongly, and is
  **unmodelled**. ADR 0014 calls it probably the largest missing effect. The head-on leg has no
  such problem (in the front, out the back). **The one thing that could reverse the verdict, and
  the paper must name it.**
- Impactor and slug both given water's caloric properties. Fine for `k >= 3` (blob is >75% slug);
  the window's lower root is indicative only.
- Water fixed **by choice, not by optimisation**: the impulse law has no molar-mass dependence, so
  the model would always pick whatever is cheapest to ionise per kg (Xe) and reject what a real
  nozzle wants (Li).

_Provenance_: regenerated 2026-08-20 from the companion clone at `23ceb9b` via
`python -m src.two_leg_nozzle_sweep` (reproduces ADR 0014 exactly) plus per-cell
`price_chain_two_leg(...).total_growth`. **ADR 0014 concludes the opposite** ("the plate stays"),
because it compares against `f = 0.8` rather than at matched recovery; a draft **ADR 0015**
reversing the verdict on the same arithmetic is to be written locally and pushed by Seth.
_Avoid_: quoting the ~25% rate figure as if it were mass; claiming the nozzle wins below
`e ~ 0.3`; claiming one nozzle could serve both legs as-is (leg 1 must exhaust back out the
aperture the arrival entered, leg 2 passes front to back, so same coils, different topology).

**Watering It Down, Literally** (new `\subsubsection`, decided 2026-08-20 grill; sits *before*
the plate-vs-nozzle subsection because it establishes why the slug is water and seeded):
Why the growth cycle's slug is seeded water rather than a cheaper-to-ionise species. Four
arguments in this order, and the ordering matters because each one answers the objection the
previous raises.

**Bag material: high-strength polyethylene fiber** (decided 2026-08-21 grill). The film-mass
coefficient is `(3/2) x rho_f Rg T / (M sigma)`, so what matters is **specific strength**
`sigma/rho`, not strength. Handy identity: **tenacity in cN/dtex x 0.1 = specific strength in
MJ/kg, exactly**, so the Toyobo table reads off directly.

| fiber | GPa | g/cm^3 | MJ/kg | melts |
| --- | ---: | ---: | ---: | ---: |
| PBO (Zylon AS) | 5.8 | 1.54 | 3.77 | 650 C |
| **HS polyethylene** | **3.5** | **0.97** | **3.61** | **150 C** |
| p-aramid (HM) | 2.8 | 1.45 | 1.93 | 550 C |
| polyester (HT) | 1.1 | 1.38 | 0.80 | 260 C |

All four verified from `toyobo_zylon` (datasheet fetched and text-extracted, not recalled).
Coefficient at half the quoted strength for weave and seams: **`4e-4 x T`**, giving 1.3% of slug at
Jupiter and 4.2% at Earth.
- _Why PE and not the cheaper fibers_: HT polyester and HT polypropylene both sit at 0.7-0.8 MJ/kg,
  so the bag is 12.5 kg instead of 2.8. **Delivering the extra 10 kg costs ~$50k at the near-term
  fare; the feedstock gap between commodity fibers is ~$100.** Two to three orders of magnitude, so
  the paper argues the *gap*, not the prices (UHMWPE $20-60/kg, aramid ~$15/kg, polyester a few
  dollars -- volatile, and deliberately **not** cited in the paper).
- _Why the 150 C melting point is not the usual disqualifier_: the mist runs 306 K (Jupiter) and
  **328 K (Earth boost, the binding case), leaving 95 K of margin**. The cold-mist decision is what
  legalises PE here; a 1000 K bag would have melted it. Creep, its other standard objection, needs
  sustained load and this bag is loaded for seconds. `sanborn2014dyneema` measured SK76 from 1e-3 to
  1e3 /s with failure strength *rising* to a plateau near 1/s, so fast loading is favourable.
- _Why it also wins on chemistry_: pure C and H, so no halogen, sulfur or metal in the plume.
  Consistent with the existing chlorine, lead and halogenated-plastic refusals, and it is the **same
  polyethylene** already chosen for the airlock pipe and the pusher-plate slab. **Avoid a metallized
  barrier film** (aluminium in the plume, and the upper-atmosphere metals-loading objection); the bag
  holds only 4.9 kPa for seconds, so a plain PE liner suffices and weave and barrier weld as one
  polymer.

**Solar power at Jupiter, and why the cold end is an asset** (added 2026-08-21 grill). The ship
must hold **two temperatures at once**: electronics fail well below 122 K, coils want colder than
that. MLI zones a warm bus against a cold magnet; the warm side needs power.
- _Flux_: inverse square puts 5.2 AU at 1/27 of 1361 W/m^2, **~50 W/m^2**.
- _Flight proof, no RTG_: **Juno** is the one that has actually operated on solar at Jupiter. Three
  9 m arrays, 18,698 cells, **~14 kW at Earth, ~500 W at Jupiter** (`bolton2017juno` for the
  mission, `jpl_juno_solar_record` for the numbers; JPL release verified by direct fetch). Galileo
  used RTGs. **JUICE and Europa Clipper are still in cruise as of 2026-08** -- do not write them up
  as having operated there.
- _Concentrators_: **SCARLET** on Deep Space 1, line-focus silicone Fresnel lenses at ~8x, ran the
  bus and the ion engine for the mission's 38 months (`stella2000scarlet`, NTRS 20000057570,
  verified). Prefer **non-imaging** mirrors where pointing is disturbed by pulses: forming no image
  buys a wider acceptance angle, hence looser Sun-pointing.
- _The payoff that makes this more than housekeeping_: Carnot work to lift a joule from 77 K is
  `(T_h - T_c)/T_c`, so **2.9 J against a 300 K radiator but 0.95 J against Jupiter's ~150 K one**.
  Cryogenics is **3x cheaper at Jupiter** than at Earth. The distance that endangers the electronics
  is what makes the magnet affordable to keep cold.
_Avoid_: quoting SCARLET's W/m^2 or W/kg figures (seen only in secondary summaries, not verified
against the primary); giving Galileo's RTG wattage (same reason).

**Copper takes the eddy currents, not the superconductor** (added 2026-08-21 grill). Two layers,
in this order.
- _Outside the coil_: a **normal-conducting copper shell** between the plume and the coil is the
  lower-impedance path for a rapidly changing field, so the induced current flows there and warms
  copper at mount temperature instead of the cold mass. **Precedent is in this exact application**:
  Romanelli, Mignone & Cervone's multi-coil parabolic pulsed-fusion chamber gives each ring a
  superconducting **seed** coil plus a separate conducting **thrust coil** that carries the current
  the expanding plasma induces (`romanelli2017pulsed_fusion_nozzle`, Acta Astronautica 139:528-544,
  2017, verified via Crossref).
- _Inside the conductor_: **copper stabilizer** on the REBCO tape. Marchevsky: normal zones spread
  slowly in REBCO so voltage-based quench detection is hard, and raising stabilizer cross-section
  **0.16 -> 0.40 mm^2 halved hot-spot temperature** in current-dump tests on insert coils
  (`marchevsky2021quench`, Instruments 5(3):27, 2021, verified via OSTI).
- _Why the shell comes first_: stabilizer copper carries no supercurrent, so more of it costs
  engineering current density. The shell costs none.
- _The number that motivates both_: removing a joule at 77 K against a 300 K sink costs 2.9 J at
  Carnot and **~20 J with a real cryocooler**. Keeping the loss out of the cold mass is worth ~20x.

1. **The nozzle must be cooled, and radiators are heavy.** Two heat sources. (a) **Edge currents**:
   the plume is diamagnetic and excludes the field with a surface current layer, which dissipates
   resistively because the plasma's conductivity is finite. Magnetic diffusion time
   `mu0 sigma L^2` is ~1.6 ms at `sigma = 574 S/m`, `L = 1.5 m`, against a ~200 us expansion, so
   the field holds but leaks at the percent level per pulse. A pulsed field also drives AC losses
   in the coils, which for a superconductor must be removed at cryogenic temperature. (b) **An
   opaque plume radiates as a blackbody**: 15,000 K gives **2.87 GW/m^2**.
2. **Water is the heat sink that replaces the radiator.** 300 K liquid to 1000 K steam absorbs
   **3.88 MJ/kg**, against 1.16 for LN2 and 1.38 for dry ice. Latent heat is **2.26 of that 3.88
   (58%)**, so the comparison already counts the phase change; water wins because its `h_fg` is 11x
   nitrogen's, not because the others were denied theirs.
   **And the heat is not spent, it is recycled**: energy put in as waste heat is energy the
   collision no longer supplies, taking the ignition bill 85.1 -> **81.3 MJ/kg** and the `k1`
   ceiling 10.10 -> 10.69.
   Water also **stores passively** across the whole trajectory (278 K at 1 AU, 122 K at Jupiter).
   LN2 boils at 77 K and needs active cryo at both ends of a 2.18-3.28 yr cycle; CO2 has a ~40 bar
   vapour pressure at 278 K and needs a pressure vessel.
   **BUT 3.88 MJ/kg is a ceiling the bag cannot buy** (resolved 2026-08-21 grill, see *Bag film
   mass* and *The bag runs as a cold mist* below). Everything above the latent heat is sensible heat
   of hot steam, and sensible heat is exactly what pressurises the bag. The matched operating point
   is **0.31 MJ/kg**, not 3.88, and it **exceeds the demand by construction rather than by 15x**.
   _Avoid_: quoting "1.49% of the pulse energy at `k = 4`" as the delivered figure (that is the
   1000 K ceiling at an illustrative `k`; the flown chain runs `k ~ 8.5` and 0.31 MJ/kg); framing
   the competitor as LN2 or dry ice at all. **The competitor is a radiator**, and the figure of
   merit is not MJ per kg of coolant but **MJ per kg of hardware carried**, where the slug's
   hardware is its bag film: `h_fg / (9.7e-4 T)` ~= **7,700 MJ per kg of film** at 311 K,
   independent of slug mass, bag radius and vapour fraction. No radiator is within three orders of
   magnitude. That is the buried advantage the original wording missed.
3. **Potassium carbonate, 1.77% by mass, gives 1% potassium.** The nozzle steers a *conductor* and
   water at 3000-6000 K is not one. Why the carbonate: it dissolves, and the slug *is* water, so the
   seed distributes itself with no feed system and no settling over a multi-year cruise. **KCl is
   rejected for chlorine** (ozone-catalytic), consistent with the paper already rejecting lead
   primaries at line 243 for atmospheric reasons. K metal is pyrophoric in water, KOH caustic,
   KNO3 an oxidiser. Cost: the extra carbonate adds **0.36 MJ/kg, 0.42% of the bill**.
   **Solubility is not the binding constraint** (corrected 2026-08-21 grill). 1.77% K2CO3 by slug
   mass is **1.80 g per 100 mL**, against ~110 available: a **61x margin**. _Avoid_: rejecting
   **K2SO4 as "barely soluble"** -- sulfate needs 2.27 g/100 mL against ~12 at 25 C, a 5.3x margin,
   so it dissolves fine. Reject sulfate for **putting sulfur in the plume**, the same stratospheric
   logic that already retires chlorine. Carbonate stays the delivery form regardless: cheaper and
   easier to handle than metallic K.
   **The carbonate does not evaporate, and the vent is a separation step** (resolved 2026-08-21
   grill). K2CO3 has no meaningful vapour pressure below its ~1170 K decomposition, so **dry steam
   would arrive carrying no seed at all** and the "distributes itself, no feed system" claim above
   would be defeated by the very venting step that follows it. The mist is what rescues it: at
   `x = 0.13` **87% of the slug never leaves the liquid phase**, so the droplets carry the seed,
   enriched only by `1/0.87 = 1.15x`. **Decision: droplets only, no separate seed feed.** Rejected
   alternatives -- a two-stream clean-steam-plus-brine-spray (redundant once the mist exists; the
   skin-only-seeding saving it would buy is ~0.2% of the bill); dry powder entrained into the vapour
   as open-cycle MHD does (K2CO3 is hygroscopic, cakes over a 2-3 yr uninspectable cruise, and a
   caked seed is a dead pulse); a small metered trim feed for in-flight re-seeding (attractive
   because `tab:seed_window`'s 2500 K cold edge is exactly what a flight measures, but it is a
   second fluid system on a ship that otherwise has none).
   **Why potassium and not cesium**: at *equal mass* K beats Cs above ~3,800 K, because Cs ionises
   more easily but weighs 3.4x as much, so once ionisation saturates you carry fewer atoms per kg.
   `Rm` at 5,000 K is 238 (K) against 138 (Cs). Cs wins only below ~3,500 K, and by 87 K.
   Same trade that standardised open-cycle MHD on K2CO3.
4. **The payoff: the seed lets the plume recombine while staying steerable.** Recombination
   window and `Rm` at 1% seed by mass, `rho = 1 kg/m^3`, `L = 10 m`, `v = 50 km/s`:

| T | K ionised | `Rm` | water chemistry |
| ---: | ---: | ---: | --- |
| 2,000 K | 0.01% | **0.1, field lets go** | recombined |
| 3,000 K | 1.14% | 9.2 | recombined |
| 4,000 K | 10.95% | 76.5 | recombined |
| 5,000 K | 38.03% | 237.8 | mostly recombined |
| 6,000 K | 70.12% | 400.2 | dissociating |
| 15,000 K | 99.90% | 360.7 | fully dissociated |

**Coldest grip at `Rm = 10`, 1% by mass**: Cs 2,942 K, **K 3,029 K**, Rb 3,061 K, Li 3,396 K,
Na 3,461 K. Sodium works but needs **2.5% at 5,000 K, 5.4% at 4,000 K, 12.7% at 3,000 K** to match
1% potassium.

**The bag runs as a cold mist, and its state is derived rather than chosen** (resolved 2026-08-21
grill). Three results, in dependency order.

_Bag film mass._ A spherical film at working stress `sigma` holding an ideal gas obeys
`m_bag/m_slug = (3/2) rho_f Rg T / (M sigma) ~= 9.7e-4 * x * T` at `rho_f = 1400 kg/m^3`,
`sigma = 1 GPa`, where `x` is the vapour fraction. **The radius cancels.** This is a *second*
invariant sitting beside the stored-field-energy one already recorded below: a bigger bag changes
neither the coil mass nor the film mass. What it changes is peak field and radiative loss.
Consequence: **1000 K steam costs ~1 kg of film per kg of slug**, destroyed every pulse. That is
what kills the 3.88 MJ/kg operating point.

_In vacuum the steam runs cold, and the floor is its own saturation curve._ 373 K is where water's
saturation pressure hits 1 atm, and there is no atm. The floor is set by the **bag's own density**:
dew point is 395 K at 1.0 m, 355 K at 1.55 m, 321 K at 2.5 m for a 5 kg slug. **A bigger bag is a
colder bag.** _Avoid_: saying vacuum makes the steam *easier to contain* -- containment is strictly
harder, because the film carries the full differential with nothing outside to balance it. On Earth
a bag of saturated steam at ambient carries **zero** differential.

_The heat balance derives `x` and `T`; nothing is chosen._ The ship has no radiator, so **all** waste
heat must boil water, and `x = Q / (m_slug h_fg)` with `T` following off the saturation curve.
Using line 972's own recipe (radiated share x sky fraction x pulse energy, coils filling ~a tenth of
the sky) at the **213 kg** anchor:

| term | per kg of slug |
| --- | ---: |
| radiated (1.2% at 5.3 m, scales as `M^-1/3`) | 1.02 MJ |
| intercepted at a tenth of the sky | 0.102 MJ |
| field and coil dissipation (~1% of 20.8 MJ/kg stored) | 0.21 MJ |
| **demand Q** | **0.31 MJ** |
| **-> x = Q/h_fg** | **0.13** |
| **-> T (dew at `rho_vap` = 0.13 x 0.32)** | **311 K** |
| **-> P** | **~4 kPa** |
| **-> film** | **3.9% of slug (8.3 kg)** |

**The mist is a thermostat**, and this is the sentence the section was missing. Two-phase water is
pinned to its saturation curve, so a thermal overrun converts into **vapour fraction, not
temperature**: the bag boils a little more and holds 311 K. A single-phase coolant would run hotter
and raise bag pressure with it. The mist also **keeps the seed in suspension** (see point 3 above),
so two independent arguments land on the same design.

_Avoid_: presenting `x` or `T` as design choices; quoting a bag temperature without saying which
slug mass it came from.

**Bag sizing, bounded on both sides** (5 kg slug at 15,000 K -- **illustrative only; the flown chain
carries ~213 kg, see the anchor-mass entry below**). Venting the slug as steam into a bag
lowers density, hence pressure, hence the field needed to stand it off (`B ~ R^-3/2`). But
blackbody loss grows as `R^2`, and the plume must stay optically thick (`tau = kappa rho 2R >= 1`)
or it radiates volumetrically instead of from its surface:

| radius | density | `B` at `beta = 1` | radiated in 200 us | share of `E_th` |
| ---: | ---: | ---: | ---: | ---: |
| 0.5 m | 9.55 | 22.3 T | 2 MJ | 0% |
| 1.0 m | 1.19 | 7.9 T | 7 MJ | 2% |
| 1.55 m | 0.32 | 4.1 T | 17 MJ | 4% |
| 2.5 m | 0.076 | 2.0 T | 45 MJ | 11% |
| 5.0 m | 0.010 | 0.71 T | 180 MJ | 43% |
| 8.0 m | 0.002 | 0.35 T | 462 MJ | 109%, cannot sustain |

**Sweet spot ~1 to 2.5 m radius at 2-4 T.** Optical depth agrees: max radius 1.09 m at
`kappa = 0.5 m^2/kg`, 3.45 m at `kappa = 5`. A third bound is a **matching condition, not a cap**
(resolved 2026-08-21 grill): the bag and the arriving cloud want the *same frontal area*. A bag
wider than the cloud leaves slug unswept; a cloud wider than the bag spills impactor mass past it.
Both mismatches cost, so the correct statement is match, not "keep the bag small". **On the nozzle
legs the footprint is a free knob**, unlike everywhere else in the paper: line 511 pins the *plate*
footprint at about half the plate radius, squeezed between a facesheet cliff (342 MPa against a
400 MPa limit; 0.3 R takes it to 1470 MPa and destroys the plate) and the `eta_capture` rim spill,
but a magnetic nozzle has no facesheet to over-pressure and no rim to spill past, and its own scale
length (`L = 10 m`) sits well above the 1-2.5 m bag. The cloud is therefore sized *for the bag*,
using the atomization-timing knob the fleet already flies (CONTEXT **impulse trim**, knob 2). The
impactor is already a gas cloud before arrival (line 86), so this is a sizing choice, not a new
capability.
_Avoid_: saying a bigger bag makes the plume **hotter** (temperature is `eps_th = w^2 k/2(1+k)^2`,
which has no volume term; a bigger bag is the *same* temperature at lower pressure); claiming the
bag makes the nozzle **lighter** (stored field energy is invariant at 103.8 MJ by the virial
theorem, so `sec:minimum_nozzle`'s energy-scaling rule gives the same coil mass -- the win is peak
field and hoop stress, which goes as `B^2`); worrying about particle magnetisation (`r_L/L` stays
under 3.5e-5 across the whole range).

**Anchor mass for the growth leg: 25 kg impactor, 213 kg slug** (decided 2026-08-21 grill). This
exposes a units mismatch in `sec:minimum_nozzle`. **Line 968 quotes the growth-leg pulse *per
arriving kilogram* (2.5 GJ) and then sizes the nozzle from it as though that were the whole pulse**,
while the near-Sun figure it is compared against (477 GJ) is the whole 2.5 kg projectile. At a 25 kg
impactor the pulse is **63 GJ** and the Mini-Mag rule returns **~37 t**, not 1.5 t. An independent
check agrees: the virial bound for a self-supported magnet, `M >= rho_struct E_field / sigma`, with
the paper's own invariant field energy (20.8 MJ per kg of slug -> **4.4 GJ** at 213 kg) and REBCO
structure at 1 GPa / 8000 kg/m^3, gives **35 t**. Two routes, same answer, so the number is not an
artifact of the Mini-Mag ratio.
_What breaks_: line 790's "masses on the order of a tonne rather than hundreds of tonnes" and line
968's "about 5% of a 30 tonne craft and 1.5% of a 100 tonne one". Both become **tens of tonnes and a
few Starship loads**.
_Why 25 kg anyway_: **bigger pulses radiate less.** Radiated share goes as `M^-1/3`, so the 25 kg
pulse loses ~1.2% where a 1 kg pulse loses ~4%. By line 972's own square-root rule that is worth
roughly 3 points of `e2`, and `tab:space_mortgage_growth` pays orders of magnitude for points of
`e2`. A 37 t nozzle that recovers better beats a 1.5 t one that does not. It is also the same
argument line 819 already makes in reverse ("a smaller fireball cools and radiates faster, so a
scaled-down shot returns a recovery that does not carry over to flight").
_The one lever not yet priced_: `beta = 1` is required **at the throat**, not through the whole
plume volume, and the stored-field invariant assumes the field fills the sphere. A throat-only field
would contain less. Unquantified; belongs with the radiation-hydrodynamic calculation already owed.

**Dry-mass plug ring** (decided 2026-08-21 grill):
A dense ice or plastic annulus at the *front face* of the vented slug bag, held **off the ship's
axis**, that catches a **softened** dry-mass discard so the PuffSat's <=250 g of non-volatile
solids couple into the pulse instead of leaving as a **Heliocentric package**.
*Why it needs its own part*: the package arrives with roughly 25 kg/m^2 of areal density against
the bag's ~1 kg/m^2 through the centre at the sweet spot, so the steam alone couples only a few
percent of it. *Sizing*: ~0.1 m of ice, ~3 kg, about 1.5% of the ~200 kg slug a 25 kg PuffSat
carries at `k ~ 8.5`. *Payoff*: under 1% of the pulse recovered (dry mass is <1% of PuffSat mass
at the same arrival speed), but the larger win is retiring the **upper-atmosphere metals loading**
objection the 2026-08-11 grill left open as "the objection a reviewer is most likely to raise",
by consuming the solids rather than shedding them. Metals help rather than contaminate here:
Al ionises at 5.99 eV and Si at 8.15 against ~12.6 for water, the opposite of the LOX-plate case
at line 279 where the same metallisation was landing on a physical surface.
*Why a ring, and why softened rather than replaced*: **discard stays fail-safe**. The shaped
charge's kick is tuned down from "clear the target radius" to "clear the ship's silhouette", so a
plug that misses or under-performs sends debris *past* the hull rather than through it. Both legs
otherwise point the dry mass down the ship's axis (head-on it enters the front, on the overtake it
enters the back), and an on-axis plug replacing the discard would be fail-dangerous: ~700 MJ at
75 km/s relying on 10 cm of ice.
_Avoid_: presenting the plug as a **mixing aid for the gas plume** (the volatilised plumes mix on
their own; the plug exists only for the non-volatile remnant); calling it **ship protection** (the
discard is what protects the ship and is retained); sizing it against the **5 kg bag-table slug**
(wrong scale -- that table is a small-unit illustration, and dry mass belongs to a 25 kg unit).
_Open_: the aim spec on the softened kick; whether the **departure leg** (head-on, ~75 km/s) has
any dry-mass resolution in either repo, since the **Heliocentric package** covers only the Earth
encounter on the growth push.

**The PuffSat/slug asymmetry, worth one sentence in the paper**: line 250 atomises the PuffSat's
water into droplets *because* that "requires much less energy than vaporization", while the slug is
deliberately boiled. Not a contradiction. The PuffSat has no waste heat to spend; the ship has a
nozzle it must cool anyway.

**Recombination is assumed recovered** (decided 2026-08-20 grill, on the physics above):
The ~50 MJ/kg locked in `H2O -> 2H + O` is **a loan, not a cost**. Three-body recombination time
scales as `1/n^2`: 0.01 us at 1 kg/m^3 and 1 us at 0.1, against a ~200 us expansion, so it
completes with orders of magnitude to spare. It freezes only **below ~0.01 kg/m^3**, which is the
one condition the paper must name. Two supporting facts: dissociation energy carries **no
pressure**, so a dissociated plume holds 84 MJ/kg while pressing with only its 31 MJ/kg of
translation and returns the rest during expansion where the field is weaker; and the frozen-flow
bound `e1 <= sqrt(1 - phi)` (0.675 at `k = 10.21`, 0.870 at `k = 4.02`) is therefore the
**pessimistic** limit, not the expected one.
_Provenance_: derived in the 2026-08-20 grill, not in either repo. Saha + electron-neutral
conductivity at a fixed 1e-19 m^2 cross-section, so the >=6,000 K rows overstate `sigma` (Coulomb
collisions take over above ~30% ionisation); the 3,000-5,000 K rows carry the argument and are
electron-neutral limited. **The fireball density is uncomputed in both repos and decides this**,
the same gap `sec:minimum_nozzle` already defers to a radiation-hydrodynamic calculation.
_Avoid_: extending `e`'s definition to cover frozen chemistry without saying recombination is
assumed (`eta_jet` at line 1521 already lists "frozen ionization or dissociation energy", `e` at
line 793 does not, and that asymmetry is now deliberate).

**Carry-over to the near-Sun case, prograde only** (raised 2026-08-20 grill; belongs in this
subsection with an `\autoref` to `sec:solid_PuffSats` and `sec:jupiter_gravity_initial`):
The same "slug doubles as coolant" argument plausibly applies to the **prograde** three quarters of
the near-Sun split (`sec:dv_effective`, prose at line 734), where the reaction mass rides aboard a
shielded rocket and never sees the Sun directly. The prograde vehicle can carry a heat shield over
its payload, so water is admissible there and brings the same radiator-replacing heat sink to a
chamber running far hotter than the Jupiter cycle's.
**It does not carry over to the retrograde quarter.** Those projectiles are released and fly their
own Sun-grazing retrograde orbit unshielded, so they must survive close solar approach on their
own. That is exactly why `sec:solid_PuffSats` specifies low-Z carbon and ceramic solids from the
Parker Solar Probe's thermal protection lineage, with a little iron for X-ray opacity. Water would
be lost long before periapsis.
_Avoid_: presenting this as a priced result (it is an observation, and no near-Sun slug/coolant
budget has been computed); implying the prograde and retrograde legs differ in **periapsis** (they
share it) rather than in **whether the mass rides behind a shield**.

**References, verified and added 2026-08-20** (all four checked against primary sources, not
memory; `crc_handbook` already existed and is reused for K2CO3 solubility):
- `kerrebrock1964nonequilibrium` -- alkali seeding / two-temperature conduction. **My recalled
  citation was wrong**: it is *AIAA Journal* **Vol 2, No 6, 1072-1080, 1964**, not Vol 3 (1965).
  Confirmed off the scanned page header. Its worked example is argon plus potassium at 2000 K.
- `rosa1968mhd` -- Rosa, *Magnetohydrodynamic Energy Conversion*, McGraw-Hill 1968.
- `messerle1995mhd` -- Messerle, Wiley 1995, UNESCO Energy Engineering Series.
- `molina1974ozone` -- Molina & Rowland, *Nature* **249**(5460), 810-812, 1974. Cited for why the
  seed is a carbonate and not a chloride.
_Avoid_: citing Kerrebrock as 1965 or Vol 3 (a real error I made from memory and corrected).

**Applied to `templateArxiv.tex` 2026-08-20** (builds clean, 104 pp, 0 errors):
- `tab:mass_scenarios` row for `sec:jupiter_only_growth` now reads **56.5--65.1 km/s** and
  **7.4--8.7**, with a note that 69.270 is the *unphased* retrograde Hohmann arrival the phased
  chain never reaches.
- The **three** (not four, as first miscounted) 9x prose claims are now "about 8 times": lines
  785, 790, 1616. There was no such claim at line 157.
- Line 1616's "about 69 km/s" -> **61** (chain mean), and line 828's "69 km/s return velocity"
  -> the 56.5--65.1 range.
- `tab:space_mortgage_growth` top two rows refloored to **0.011/0.022/0.039/0.059** and
  **1.0/3.2/7.7/15**; caption now states the 1/15 ground-launch floor and that it binds only in
  those two rows. Prose at line 817 updated from `x0.095` "under ten cents" to **`x0.011`, about a
  cent on the dollar**. Everything at `e >= 0.40` is unchanged, so the **1,284x** headline stands.

**Both subsections are now in the paper** (2026-08-20, builds clean at **107 pp**, 0 errors, all
five cites resolving):
- `sec:watering_it_down` ("Watering It Down, Literally") and `sec:two_leg_nozzle` ("Two Nozzles
  Beat a Nozzle and a Plate") sit between Space Mortgages and Inner Planet Assist Alternatives,
  as `\subsubsection`s. New tables: `tab:seed_window`, `tab:bag_sizing`, `tab:two_leg_growth`,
  `tab:equivalent_plate`.
- The old line-794 paragraph is replaced by a two-sentence pointer to both.
- **`e -> e_2` relabel done**, 10 occurrences across `sec:space_mortgages` including the
  `tab:space_mortgage_growth` header; the caption now says why. No bare `$e$` remains in that
  subsection, and there were no `e^` exponentials in range to catch by accident.
- Citations wired: `kerrebrock1964nonequilibrium` + `rosa1968mhd` + `messerle1995mhd` on the
  alkali-seed sentence, `crc_handbook` on the K2CO3 solubility, `molina1974ozone` on chlorine.

**Outbound-leg ground-test gap** (`sec:jupiter_only_growth`, the Space Mortgages argument):
Why **recovery** (`e`) on the Jupiter-only outbound leg can only be measured by flying, which
is what makes early cycles an asset rather than a cost. Four commitments, in this order:
1. *Energy is explicitly conceded not to be the wall.* 70 kg at 70 km/s is 171.5 GJ, about
   41 t TNT equivalent; 1 kg at 75 km/s is 2.81 GJ, about 0.67 t. Both are conventional-test
   scale. **Do not claim the pulse is nuclear-scale** — a reader with a calculator catches it.
   (A defensible nuclear sentence exists but is about *power density*, not yield: only a
   nuclear device can dump 2.81 GJ into a kilogram fast enough, the Casaba-Howitzer wall
   Orion hit. Optional, currently not used.)
2. *Acceleration is the wall.* `a = v²/2L` to 70 km/s: 2.5e6 g over 100 m, 2.5e5 g over 1 km,
   **2.5e4 g even over 10 km**, 2.5e3 g over 100 km. No guided projectile carrying a slug
   survives that, and no evacuated 10 km launcher exists.
3. *Delivering the energy is a second wall.* 171.5 GJ against Sandia Z's ~20 MJ stored is
   ~8,600x, before launcher efficiency (the 1 kg case is still 141x).
4. *The path must be evacuated.* ~6 GPa stagnation pressure at 70 km/s in sea-level air. The
   range is therefore a km-scale vacuum tube, i.e. the **Straw Way** — downstream
   infrastructure the working cycle has to pay for first. Worth one sentence of circularity.
Backstop that closes the sub-scale loophole: `e` is **not scale-invariant**, by
`sec:minimum_nozzle`'s own radiative-escape argument (a 100 g pulse cools and radiates faster,
so it returns an `e` that cannot be extrapolated to flight).
Ground anchor already in the bibliography: First Light Fusion's two-stage gas gun at
\SI{6.5}{\kilo\meter\per\second} (`firstlight2022fusion`, cited in `sec:epstein_drives`);
its shaped target drives *target material* past 70 km/s, but only as a mm-scale converging
implosion, never a free-flying kilogram.
_Needs citation before use_: the kilogram-class launcher record near 11 km/s, and Sandia Z's
milligram flyer plates near 45 km/s. Both currently unsourced.
_Avoid_: leading with energy or treaty language; asserting untestability without conceding
what *is* groundable (the nozzle magnet itself scales to ~1.6 t of coils at this pulse energy,
against Mini-Mag's 200 t for 340 GJ, so the driver is the unbuildable half, not the magnet).

**Launch-cadence asymmetry (E2E critique)**:
The 2026-07-17 grill's framing for the launch-cadence disadvantage of Starship
Earth-to-Earth in `sec:200_mile_high`. Four commitments. (1) *Mechanism is closure, not
blast*: helicopters are excluded from the shore-to-platform corridor because every launch
and reentry closes the surrounding airspace and sea lanes against a possible vehicle
failure (range safety), and at SpaceX's own projected cadence the closure windows tile the
operating day; "rocket blast makes helicopters unsafe" is the rejected wording. (2) *Cadence
anchor is SpaceX's own number* (Shotwell's dozens of E2E flights per day), matching the fare
section's use-their-optimism discipline; the hub-traffic derivation is the fallback only.
(3) *Pad spacing is grounded on the LC-39 precedent* (LC-39A/B sited ~2.7 km apart for
Saturn V, a smaller propellant load than Starship's), not a bare "1 km" figure.
(4) *Boomerang guard*: the paper concedes 2.5x launch capacity in `sec:fare_comparison`, so
the critique is stated as a **city-end** asymmetry: PuffSat cadence lands at a few remote
dedicated spaceports on infrastructure schedules (formations pre-placed), while E2E runs its
full cadence, exclusion zones, and multi-pad sprawl at every served city. Placement: the
closure argument extends the existing Logistical Inefficiency bullet; pad sprawl is one new
bullet; the asymmetry sentence lives in the rocket-plane paragraph, not in a bullet.
_Avoid_: blast-hazard wording for the helicopter point; quoting a cadence band SpaceX never
claimed; adding the disadvantage without the city-end guard sentence.

### Intercity rocket plane (`sec:200_mile_high`)

**Takeoff**:
The rocket plane's departure: an ordinary runway takeoff from an existing urban airport on
air-breathing engines. There is no launch anywhere in this architecture.
_Avoid_: "launch" for anything the rocket plane does. That word belongs to Starship, and the
whole community-noise argument rests on the two being different events.

**Transit leg**:
The subsonic cruise from the departure airport out to the **ignition point**. Flown on
turbofans, carries no orbital-mechanical meaning, and is therefore free to dogleg away from
the great circle. About ten minutes at the 150 km baseline.

**Ignition point**:
Where the rocket engines first fire: roughly \SI{12}{\kilo\meter} altitude, one **ignition
standoff** from the nearest populated area. The only loud event in the architecture, and the
only one whose position is a free variable.
_Avoid_: conflating it with the airport. The formation's orbital plane must contain the
ignition point and the destination, *not* the departure airport. That decoupling is the
argument.

**Ignition standoff**:
Horizontal distance from the **ignition point** to the nearest populated area. Baseline
\SI{150}{\kilo\meter}, chosen because two Raptors there read as about one wide-body departure
in A-weighted sound exposure, which is the claim Table 1 already makes. Continuously
adjustable, so a single town under the track is cleared by lengthening it rather than
doglegging.

**Community-noise asymmetry (E2E critique)**:
The 2026-08-13 grill's framing for the noise disadvantage of Starship Earth-to-Earth,
sibling to the **Launch-cadence asymmetry** entry above and carrying the same boomerang
guard. Five commitments. (1) *The distance anchor is Musk's own*: ~20 miles / 30 km offshore,
which he named and tied explicitly to "frequent daily flights." Do not assert a distance he
never claimed; the 2026-08-13 session opened with "20 km," which is wrong. (2) *Levels are
measured, not modelled*: Gee's BYU group, 1.0--35.5 km, Flights 5/6/9. 145.7 dB at 1 km,
125.2 dB at 10 km, 115 dBA sound exposure at 10 km (= 1000 wide-body departures), flyback
boom 9 psf at 10 km and 1.5x Concorde loudness at 20 km. (3) *Cadence is argued from
institutional precedent, never from DNL* -- see the Flagged ambiguity below. (4) *The
rocket-plane counter-case is the movable standoff, not a quieter source*: an offshore
platform must be passenger terminal and ignition point at once, and those want opposite
distances from shore, which is what pins Musk at 30 km. Splitting the roles costs ten
minutes of cruise. The corollary is reach: offshore platforms can only ever serve coastal
cities, while rural overland ignition opens Phoenix and Chicago. (5) *Boomerang guard*: the
architecture burns ~2.5x the launch capacity (`sec:fare_comparison`) and is therefore louder
in total. The claim that survives is that the noise is relocated off the passenger schedule
and away from cities, not that there is less of it. Concede this inside the bullet.
_Avoid_: claiming the rocket plane is quieter per passenger; claiming its ascent boom
vanishes (it is Falcon-9-class, ~1.90 psf max and mostly under 0.5 psf, and it still travels
150 km); presenting the Starbase suit as findings rather than allegations.

### Cryogenics, thermal, and ISRU propellant

**Passive standoff sunshade**:
A JWST-style detachable multilayer (aluminized Kapton) shade carried in front of a
cryogenic PuffSat to block sunlight, distinct from the conformal solar-white coating on
the skin. Tune the layer count to the target temperature (more layers, colder). Jettisoned
a short time before impact so it does not foul the gas plume or have to survive the
collision. Not retained as reaction mass: the benefit is sub-kg, and its metallization
(Al, doped Si) would contaminate the non-combustible LOX pusher plate.
_Avoid_: calling it a "heat shield" (that evokes the near-Sun ablative chamber and the
Parker-class sunshade, which are different hardware).

**Passive-shielding temperature law**:
A shaded radiator equilibrates with the attenuated sunlight, so its temperature scales as
`T ∝ r^(−1/2)` with heliocentric distance `r`. Anchored at JWST's ~40 K at ~1 AU, this
gives ~24 K at Ceres (2.77 AU) and ~13 K at Saturn/Phoebe (9.6 AU). The 40 K reach is
colder than LOX wants (oxygen freezes at 54.4 K), so for LOX use a lighter shade (~60–80 K);
the full reach is the lever for storing LH₂ farther out.

**Passive-LH₂ threshold**:
The heliocentric distance (~1.5 AU) beyond which passive shielding can hold hydrogen below
its 33 K critical temperature, so liquid hydrogen becomes storable. Inside it (Moon,
Mercury) no shield keeps H₂ liquid at any pressure; outside it (Ceres and beyond) LH₂ is
storable at modest pressure (a few bar at Ceres' ~24 K). This is why LOX/methalox serve the
inner system and LH₂/LOX is a Ceres-and-out option.

**On-demand electrolysis propellant**:
Store water (not a pressurized cryogen) and electrolyse it with onboard solar power into
hydrogen and oxygen at the moment of use, feeding either a chemical thruster (Imperial
ICE-Cube) or a Hall-effect thruster (Imperial WET-HET). The closer-in alternative to stored
LH₂/LOX, sharing the "make propellant on demand, no pressurized tank" principle with the
PuffSat fine-control thrusters.

**Effervescent (carbonation) atomization**:
Dissolving CO₂ into the icy PuffSat's meltwater so exsolving gas helps shatter it into
droplets on release, supercharged by the vacuum pressure ratio. A speculative assist that
trims the micro-explosive load, viable only where carbon is abundant (icy moons such as
Ceres and Phoebe), not on the carbon-poor Moon. Clathrate storage is rejected: its
endothermic, self-preserving dissociation releases gas too slowly for millisecond
atomization and over-pressurizes the liner if it dissociates while confined.

**Centrifugal stirring geometry** (`sec:spherical_water_thermal`, `sec:tethered_ring`):
Which convection architecture a spinning water body needs depends on whether it is
centered on the spin axis. A **centered** body (the baseline 100 kg sphere, and the hub
bag of the tethered ring) sees `omega^2 s` pointing cylindrically outward, which vanishes
along the whole spin axis. Its coldest surfaces, the spin poles, sit exactly on that null,
so they cannot be stirred and are instead prevented from getting cold with aluminum-out
low-emittance caps. An **off-axis** body (the ten ring bags at R = 2 m) sees a nearly
uniform `omega^2 R` outward, varying only ~6.5% across a 0.129 m bag and vanishing nowhere.
Its permanently dark caps (facing along the spin axis) then sit broadside to the field,
which is a side-heated cavity with no critical Rayleigh number, so it convects at any dT
and needs no polar caps. Off-axis bags are also stirred ~12x harder at the same spin rate (`omega^2 R` at 2 m against
the volume-mean `omega^2 <s>` = 3*pi*a/16 = 0.17 m inside a 0.29 m sphere).
Rests on the bags co-rotating rigidly with the ring. **Co-rotating means one turn per lap, same
face to the hub: tidally locked in geometry, like the Moon to Earth, though by hardware rather
than by tidal friction.** Circling the axis and spinning about one's own center are separate
motions; the spoke compels only the first. Locked to the HUB is fine (the Sun still sweeps past
once per rotation, and the flux-average argument shows the inward and outward faces collect
identical mean flux anyway). Locked to the STARS is the failure, since that bakes one hemisphere.
A spoke ending at a single point pulls
through the bag's center and exerts zero torque, so a bag is torque-free and simply keeps the
spin it was deployed with. The failure is spin-up after the spokes are taut: the bags never
start turning, stay fixed in inertial space while orbiting the axis, and park one bumper
hemisphere in permanent sun (~150 C) with the other permanently dark, which kills the
light-and-shade cycling the thermal balance needs. Fix is a 3-line bridle per spoke, which
only ever carries spin-up and disturbances, never a steady load.
_Note_: centrifugal gravity is always perpendicular to the spin axis, so the
Chandrasekhar `g || Omega` rotational suppression of onset never applies to either case.
But that only frees the *threshold*, not the *speed*. At omega = 1 rad/s the Ekman number is
~7e-6 and the Rossby number ~0.02, so Coriolis dominates: convection organizes into columns
aligned with the spin axis, columnar onset sits orders of magnitude above the plane-layer
1708 (margin of tens, not tens of thousands), and overturn is minutes to tens of minutes, not
the tens of seconds a non-rotating free-fall estimate gives. Still fast against a 15 d coast.
Bonus: axis-aligned columns carry little flow *along* the axis, a second reason the spin
poles of a centered body are the worst-mixed points.
_Sun-angle independence (off-axis only)_: an off-axis bag stays side-heated at **every**
Sun angle, not just at the baseline perpendicular attitude. Decompose the Sun direction in
the bag's co-rotating frame: the component along the spin axis is constant, and the
in-plane component turns once per rotation. Averaging the Sun *vector* is not the argument,
since a facet of normal n absorbs as `max(0, n.s)`, which is nonlinear in s. Average that
instead: over one rotation s sweeps a cone about the spin axis, so the mean depends on n only
through its angle to that axis. The bag's outward and inward faces share that angle, so they
collect identical mean flux and no mean gradient forms along the field. Verified numerically
to 1e-11 across Sun angles 0, 0.6, pi/2 rad.
The stagnant case, a hot cap parked on the "ceiling" with warm fluid buoyantly stuck, would
need the Sun over the bag's inward-facing cap, and that direction sweeps a full circle in
inertial space once per rotation, so no fixed source can sit there. Only the **centered**
hub bag can get a permanently stagnant hot cap, and only when the axis points at the Sun.
_Sun at the hub's equator is the good case_: the hub bag straddles the axis, so it has its
own field, zero on the axis but rising to omega^2 a = 0.13 m/s2 at its equator (about 0.45x
the 100 kg body, 26x weaker than a ring bag). In the thermal attitude the Sun sits in that
equatorial plane, heating lands where the field is strongest and sweeps once per rotation,
warm water at the rim is hot-at-the-bottom and overturns, and the cold poles are handled by
the aluminum-out caps. Only the axis-at-Sun attitude is bad. Do NOT say the hub bag has no
centrifugal drive; the drive vanishes only ON the axis, not throughout the bag.
_How bad is that cap_: bounded by transient conduction, not steady state. The cap is stuck
because warm water floats toward the axis and the sunlit pole already sits on the axis.
Steady conduction would give ~33 K, but that is never reached: crossing the bag takes
a^2/kappa = 32 h against a 3 h hold, so heat stays in a sqrt(kappa t) = 4 cm skin and the
surface rise is 2q sqrt(kappa t/pi)/k. That is 6 K on the lit-hemisphere mean
(76 W/m^2) and 11 K at the sub-solar point for a cos-theta distribution. Both ignore the
vapor-space heat pipe and the ~0.5 W/K by which net intake falls as the cap warms, and the
cos-theta case is pessimistic since the water sees the bumper's inner face, not the Sun.

**Thermal attitude vs impact attitude** (`sec:tethered_ring`, `sec:spin_reorientation`):
The two directions the ring's spin axis is asked to hold. The **thermal attitude** is
perpendicular to the Sun-line, wanted by centrifugal stirring. The **impact attitude** is
along the closing velocity, wanted so the ring plane arrives square to the pusher plate.
Mission geometry decides whether they agree; worst case is 90 deg apart. Resolution: hold
the thermal attitude through the coast, re-point in the last hours. Cost of the worst case
is ~63 N.s, an equivalent 0.63 m/s on the 100 kg assembly. Firing time depends on how the
400 mN of `sec:fine_control_thrusters` is read: it is a whole-vehicle drag figure, so the
conservative split is 200 mN per end, a 5 N.m couple, 150 rotations, 942 s. Sizing each
package for the full 400 mN halves that to 471 s. Impulse and propellant unchanged either way.
Against the propellant: the drag leg of `sec:estimate_cold_gas` is only 18 N.s before margins
(20 mN x 300 s + 400 mN x 30 s), so the re-point is ~3.5x that leg; the 500 g tank holds
123 N.s at the pessimistic Isp = 25 s and 211 N.s at the flown 43 s, so the re-point is about
half the tank on the first figure and under a third on the second.
_Key scaling_: `dv = 2 sin(theta/2) * omega * k^2 / r`, where `k` is the radius of gyration
and `r` the thruster moment arm. Cheap only because the water stays compact at R = 2 m
while the thrusters ride at the 25 m tether bundle's ends (r = 12.5 m). Putting the same
100 kg out at 25 m radius instead costs ~41 m/s on the arc formula the appendix actually uses
(an earlier note said 37 m/s, which was the chord lower bound), which is why that variant is
not the architecture.

### Energetics and sensitization

**Chemical gassing (nitrite gassing)**:
Sensitizing an emulsion explosive by injecting sodium nitrite (NaNO₂), which decomposes in
the acidified aqueous phase and nucleates nitrogen bubbles in situ. Those bubbles are the
**hot spots**. The canonical sensitizer for the PuffSat emulsion of `sec:explosive_puffsat`,
because it is added late in flight, which is the safety property line 230 already claims.
_Avoid_: "sodium nitride" (Na₃N, a different and essentially non-existent compound, and not
what any energetic formulation uses); confusing it with sodium azide (NaN₃), which
`sec:cold_gas_generators` explicitly rejects for its silicate slag.

**Hot spot**:
A small gas-filled void that heats by adiabatic compression when a shock passes, initiating
the surrounding matrix. Must contain a **non-condensable** gas. A void filled with water
vapor condenses under compression instead of heating, so it is a poor hot spot even at the
correct void fraction. This is the constraint that sets the charge fill pressure.

**Charge fill pressure (~5 kPa)**:
The explosive PuffSat's emulsion is held a few kPa above vacuum, not at one atmosphere and
not vacuum-referenced. Chosen as the lowest pressure keeping bubble contents nitrogen- rather
than steam-dominated: the supersaturated AN phase sits near 1 kPa of water vapor at 290 K, so
5 kPa is ~80% nitrogen, and ~94% if the charge runs at 273 K. Stays inside line 232's "very
thin layers" (membrane stress `Pr/t`), where a full atmosphere would demand a real pressure
vessel. Nitrite dose scales down with pressure, which is the same dose-against-head
calculation mining already does down a borehole, extrapolated the other direction.
_Avoid_: "low vapor pressure environment" for the flight condition. Vapor pressure is a
property of a liquid at a temperature. The environment is low **ambient** pressure, and the
mechanism runs the opposite way from what that phrase suggests.

**Sensitizer-set thermal band (273--300 K)**:
The explosive PuffSat's thermal-trim target, squeezed from both sides by the gassing
chemistry. Below 273 K the nitrite reaction is too slow to finish inside the pre-intercept
window and the supersaturated ammonium nitrate phase risks crystallizing out. Above 300 K
aqueous vapor pressure crowds the nitrogen fill and the matrix coarsens. Held passively by
the louver of `sec:louver_thermal_trim`, which currently lists a target for every variant
*except* the explosive one. Means colder is **not** strictly better for a gassed charge,
qualifying line 232's reflective-liner argument.

**Isobaric charge (low-gravity advantage)**:
In free fall the charge has no hydrostatic head, so bubble size, density, and sensitivity are
uniform throughout. A 10 m borehole carries ~137 kPa of head and must be dosed against depth.
Holds to within a few percent for any acceleration below ~0.01 g; near 0.04 g the gradient is
back to 10%, so a fast-spinning variant needs rechecking. The paired cost is **mixing**: an
emulsion matrix is a yield-stress paste (~100 Pa) that neither convects nor settles, so
gassing must happen during a chamber-to-chamber transfer where shear distributes the reagent.
Buoyancy itself is a non-issue at this timescale. Stokes creaming of a 100 µm bubble in
50 Pa·s matrix is 0.6 µm/s at *full Earth gravity*, or 2 mm over the whole gassed window.

**Bubble populations (four, do not conflate)**:
The paper uses "bubble" for four distinct things doing different jobs.
(1) **Gassing bubbles**, nitrite-generated N₂ in the emulsion, are hot spots that initiate the
explosive (`sec:explosive_puffsat`).
(2) **Cavitation bubbles**, pre-formed gas-filled plastic spheres in the bulk water, shape what
the shock does to the water and cap droplet size (`sec:icy_puffsat`, line 239).
(3) **Effervescent bubbles**, exsolving dissolved CO₂, stretch ligaments during late breakup
(see **Effervescent (carbonation) atomization**).
(4) **Crevice nuclei**, gas trapped on unwetted foam-strand surfaces, seed cavitation in the
water (line 245).
(1) initiates the charge; (2), (3), and (4) act on the water after it fires.

### Materials

**Halogen-free vaporizables rule**:
Any material expected to vaporize, decompose, or ablate in flight, ice-wire coatings, the
airlock's sacrificial plastic, and (see **Second-surface radiator skin** below) balloon
PuffSat outer skins, must be halogen-free, no fluoropolymers (PTFE/FEP/Teflon) or other
halogenated plastics. Rationale, stated twice already in the paper for other components:
halogenated combustion/decomposition products are toxic in the near term (HF,
perfluoroisobutylene-family compounds) and persistent in the long term (PFAS chemistry),
and the paper's own fleet-scale argument for aluminum reentry debris (small per-event,
real in aggregate at billions-of-disposals cadence) applies at least as strongly here.
Prefer polyethylene (airlock plastic) or polyimide/Kapton (thermal-control skins) even
where a fluoropolymer would otherwise be the obvious choice for UV durability.
_Avoid_: FEP Teflon or any PTFE-family polymer anywhere in flight hardware that vaporizes
on orbit or on impact.

**Second-surface radiator skin** (superseded by **passive louver thermal trim**, `sec:louver_thermal_trim`):
The formerly-resolved thermal-control construction for balloon/water-bag PuffSat outer skins: a
clear, halogen-free, UV-tolerant polymer (Kapton, matching the paper's existing JWST
sunshade citation) faces the sun, with aluminum vapor-deposited on its *inner* face rather
than the outer one. Sunlight still reflects off the aluminum (low solar absorptivity
preserved), but the surface radiating to space is the polymer's own, with IR emissivity
around 0.6–0.8 versus bare (first-surface) aluminum's 0.02–0.05. This fixes an
unfavorable α/ε ratio: an isothermal sphere with bare first-surface aluminum (α≈0.1–0.2,
ε≈0.03–0.05) equilibrates near 330–450 K at 1 AU, at or above water's boiling point,
independent of any internal conduction scheme. The second-surface construction drops that
estimate to roughly 186 K, trading an overheating problem for a large cooling margin that
can be dialed back down (partial coverage, material choice) rather than fought from a
deficit. Kapton's UV durability is worse than FEP's over a multi-year mission, but a
PuffSat's exposure is a multi-day coast, not years, so the margin FEP would buy is likely
unnecessary. Not yet backed by a citation for Kapton's or aluminum's exact α/ε values;
flagged for verification before this goes in the paper.
_Avoid_: "metallized skin" without specifying which face carries the aluminum,
first-surface (outward-facing metal) and second-surface (metal on the inner face of a
transparent polymer) give very different emissivity and are not interchangeable.

**Passive louver thermal trim** (in paper, `sec:louver_thermal_trim`, replaces **second-surface
radiator skin** above):
The resolved thermal-control mechanism for all PuffSat variants (icy/water, LOX, balloon), each
at a different target temperature. A movable louver flap adds fine control on top of a body's
baseline reflective coating, driven by one of two passive, self-triggering (no electronics)
actuator technologies: a bimetallic strip, with real flight heritage from Pioneer 10/11's
louvers and Goddard's Dellingr CubeSat, or a nitinol shape-memory wire drawable to single-digit
micron diameters. The actuator senses the PuffSat's own body temperature rather than the flap's
sun-facing side, so a short pull cable separates actuator from flap instead of integrating them.
Both actuator and flap stay light enough, the wire especially so, that neither is a major
shrapnel risk against the pusher plate on its own; a spin-stabilized PuffSat can additionally
reel the whole assembly clear on its tension tether before impact (see **spinning tethered
pair**, `sec:spinning_tension_detail`). Thermal trim also simply stops in the last ~10 minutes
before impact: extended flaps add drag that perturbs the terminal trajectory at low altitude,
and unshaded absorption over that interval only raises a water body's temperature by a few
tenths of a kelvin, negligible against the margin already banked.

### Straw Way vacuum pumping (`sec:vacuum_tube_details`)

**Straw Way wall stack**:
Metallized plastic carrying a roughly 100 nm aluminum inner layer, sized for mass rather than for
vacuum performance (settled 2026-08-19 grill).
_Avoid_: heavy-metal liner, tantalum liner (see Flagged ambiguities; tantalum is not merely
unnecessary here, it breaks the pumping mechanism).

**Reflector skin**:
A few nanometers of iron over the projectile nose, present so that argon has something heavier
than itself to bounce off. Argon is 40 amu, so it cannot backscatter from carbon (17.5 deg maximum
single-collision deflection), oxygen (23.6), aluminum (42.5) or silicon (44.7). Iron, titanium,
calcium, tantalum and tungsten all permit backscatter.
_Avoid_: conflating with the **high-Z cap** of `sec:solid_PuffSats`, which exists for opacity;
defaulting to tungsten (iron is cheaper, and its lower `E_d` costs only window ceiling).

**Displacement threshold (`E_d`)**:
The minimum energy an incoming atom must hand a lattice atom to knock it permanently out of its
site. Below `E_d` the incoming atom bounces off the lattice acting collectively; above it, the
atom displaces its way in. Orientation-averaged values: Al 25 eV, C 30, Fe 40, Ta and W 90.
Directional minima run roughly 40% lower (Fe near 17-20 eV, Al near 16 eV), so every window edge
below carries that spread.
_Avoid_: treating `E_d` as a sharp cliff; it is a threshold with real orientation spread.

**Reflector window**:
The projectile-speed band in which argon reflects off the **reflector skin** and then implants in
the **Straw Way wall stack**. Its floor is set by the wall (the rebounding argon must clear
aluminum's `E_d`) and its ceiling by the skin (the incoming argon must *not* clear iron's `E_d`).
Argon transfers 96-97% of its energy head-on to either Al or Fe, so both edges are sharp in speed:
**6.2 km/s to 14.1 km/s** for an iron skin, rising to 27.2 km/s for tantalum or tungsten. Earth
escape speed at the 200 km interception altitude is **11.01 km/s**, so every bound-orbit arrival
sits inside the iron window automatically, with 28% of margin, and needs no per-source analysis.
Direct interplanetary arrivals do not: Ceres Hohmann lands at 12.70 km/s (inside), Jupiter prograde
Hohmann at 14.09 (at the edge), Saturn at 15.08 (outside iron, inside W).
_Avoid_: quoting the ceiling as a hard number without the `E_d` spread; taking iron's directional
minimum drops it to about 10 km/s, which would put the 11 km/s case just outside.

**Captured-either-way (the claim the paper makes)**:
The robust form of the pumping argument, chosen over the window itself because it survives the
`E_d` spread. Argon is removed from the tube on both sides of the reflector ceiling, only by
different pumps. Below it, argon reflects and implants about 1.5 nm into the aluminum wall. Above
it, argon displaces skin atoms and buries itself in the projectile, which carries it out of the
tube. **Both outcomes occur at every speed** (settled 2026-08-19): backscatter off a heavy cap is
kinematically allowed at any energy, and sub-threshold trapping in the skin happens at low speed
too. Closing velocity shifts the odds between the two, it does not switch between them. The single
genuine failure mode is falling below the **floor**, where the rebound is too soft to enter either
material and the argon rattles around indefinitely. That floor corresponds to a drop from about
3250 km apogee, which nothing in the architecture approaches.
_Avoid_: presenting the two regimes as success and failure, or as mutually exclusive. Reflection
coefficients are probabilities, not switches.

**Noble-gas ladder**:
Which NEG-immune gases the projectile mechanism can bury. Two criteria, and they split the gases
differently. By **displacement** (clearing aluminum's `E_d` on rebound) the minimum projectile
speeds are Xe 4.0 km/s, Kr 4.4, Ar 5.6, Ne 7.8, He 25.9, so only helium fails below Earth escape
speed (11.01 km/s at the 200 km interception altitude). But displacement is the wrong criterion
for a small atom, which can enter **interstitially** without moving anything. Against aluminum's
59 pm octahedral site, He (31 pm) and Ne (38 pm) fit; Ar (71 pm), Kr (88) and Xe (108) do not.
So Ar/Kr/Xe must displace and the `E_d` criterion governs them, while helium has a second door.
_Avoid_: calling helium capture impossible below 25.9 km/s (see Flagged ambiguities; corrected
2026-08-19). The `E_d` criterion bounds displacement, not entry.

**Rebound ceiling (`2V`)**:
Reflection off a body moving at `V` bounds the rebound at `|v_out| <= 2V + |v_in|`, and that bound
does not compound. After one hit an atom moves down-tube faster than the projectiles, so it cannot
be overtaken and struck on the nose again; the next encounter is with a receding tail, which slows
it. Reversing axially needs wall bounces, and those outnumber projectile hits about 66 to 1 even at
1 ktonne/s, so accommodation drains energy faster than projectiles add it. A 4000-atom Monte Carlo
over 10 s peaked at 12.2 eV against helium's 55.6 eV requirement.
_Avoid_: appealing to the tail of the velocity distribution to rescue helium. Thermal spread needs
a 38-sigma tailwind; there is no Fermi-style ratchet to supply the rest.

**Blunt-nose condition**:
Argon reflects specularly, so a local surface normal at angle `theta` to the flight axis returns it
at `2 v cos(theta)` and `cos^2(theta)` of the energy. Wall implantation therefore needs the normal
within about **59 deg** of the axis, i.e. a cone **half-angle above about 31 deg**. A hemispherical
nose delivers about 74% of its swept argon above threshold; a slender needle delivers none. Costs
nothing, since these projectiles transit in hard vacuum.

**Sweep-limited pumping speed**:
`(mdot / projectile areal density) x tube length x capture probability`. Independent of projectile
size, since halving the projectile doubles the count. At 1 kg/s of traffic and 1% capture it is
10^3 L/s, a large turbomolecular pump; at the 1 ktonne/s of `sec:death_star` it is 10^9 to 10^11
L/s. Argon crosses a 3 m bore thermally in 7.5 ms, so successive projectiles sample a fresh draw
rather than re-sweeping a cleared channel. Rate is not what limits this mechanism.

### Lunar disposal (`sec:handling_space_debris`)

**Disposal package**:
The sub-250 g dry-mass remnant of a spent PuffSat, steered to a lunar impact instead of reentry.
_Avoid_: waste, garbage, trash, debris (reserve **debris** for the ejecta it throws).

**Disposal site**:
One of a handful of fixed lunar impact points, spread in longitude so one always sits near the
low-$\Delta V$ approach geometry as the Moon rotates.

**Ejecta trap**:
A roofed disposal site (sintered enclosure or lava tube) whose small aperture subtends a narrow
cone from the impact point.
_Avoid_: baffle, shield. Contrast with **open pit**.

**Open pit**:
An unroofed disposal site, natural crater or excavation, whose rim blocks ejecta launched below
$\arctan(H/R)$ and whose slope relaxes to the 35° angle of repose if unbonded.
_Avoid_: open crater, baffled crater.

**Latitude separation**:
Siting disposal at the lunar equator while settlement stays polar, so 2729 km of arc separates
them.
_Avoid_: geographic separation, polar standoff, antipodal siting (the separation is 90°, not 180°).

**Pole-reach threshold**:
1.53 km/s, 64% of lunar escape speed, the slowest ejecta that can fly equator-to-pole; raised to
1.57 km/s by a 35° rim, and to escape (route closed) by a 67° one.

**Azimuth window**:
The ±5° of launch azimuth about the meridian that reaches latitude 85°+ from an equatorial site,
5.6% of all azimuths; the actual protection **latitude separation** provides.

**Fast tail**:
The ejecta mass fraction launched above the **pole-reach threshold**, the only material that can
reach a polar settlement at all.

### Heliocentric disposal, Jupiter cycle (`sec:jupiter_only_growth`)

**Heliocentric package**:
The dry-mass remnant shed by a Jupiter-cycle PuffSat at the Earth encounter. It keeps the
PuffSat's incoming orbit almost unchanged, because at 60--69 km/s Earth's gravity barely bends it
and the discard kick is metres per second: retrograde, Jupiter-crossing, perihelion *inside* 1 AU,
aphelion at or beyond Jupiter, period 5--9 yr. The Earth encounter is a crossing, not a tangency;
the package arrives with a large inward radial component and continues to a perihelion well below
1 AU. Exact $q$, $Q$, $P$ not yet pinned from the companion repo.
_Avoid_: **disposal package** (reserved for the Earth-orbit remnant steered to a lunar impact; the
heliocentric one is never disposed of), **debris** (reserved for lunar ejecta), "widely dispersed
debris".

**Dispersal ratio**:
The volume argument that excuses the Jupiter cycle from the disposal machinery the LEO cycle needs.
LEO packages stay gravitationally bound inside a shell of order $10^{21}$ m³, the same volume
satellites occupy. Heliocentric packages are unbound and spread through a torus of order
$10^{35}$ m³, about $3 \times 10^{14}$ times larger. That ratio, not the word "dispersed", is the
argument.

**Satellite-collision metric**:
The hazard the heliocentric package population is judged against, chosen 2026-08-11 over two
rejected alternatives (Earth-impact hazard, which is a harmless 70 km/s meteor, and upper-
atmosphere metals loading). At $10^8$ t/yr of PuffSats and a 1% dry-mass fraction, so $10^6$ t/yr
and ~4 billion packages a year, a century of accumulation gives ~$7 \times 10^{-24}$ packages per
m³ near 1 AU: one hit per $10^9$ years on a 100 m² spacecraft, ~0.04 hits/yr across the whole
in-transit fleet. Ignoring the population is the baseline.

**Jupiter phasing**:
The optional route that clears the population instead of ignoring it. The orbit already crosses
5.2 AU twice a revolution, so this is a *timing* problem, not a shape problem, and timing is set by
orbital energy. The burn therefore belongs at **perihelion**, not apoapsis: $\Delta E = v \cdot
\Delta v$, and the package moves 9--18x faster at perihelion than at aphelion. Target is Jupiter's
gravitationally focused capture disk, ~205,000 km radius at a ~22 km/s $v_\infty$, so arrival must
land inside a ~6 hour window.
_Avoid_: "phasing burns at apoapsis" (imports the wrong folklore; apoapsis is cheap for changing
perihelion and plane, not period).

**Sunlight trim**:
The propellantless actuator for **Jupiter phasing**. Sunlight only pushes outward, so a fixed area
cancels itself over a symmetric pass; asymmetric deployment between the inbound and outbound legs
does not. A single flap, of the kind `sec:louver_thermal_trim` already flies, gives a 250 g package
at 0.08 m²/kg about 7 m/s of radial impulse per deep perihelion pass, worth ~3--4 m/s of tangential
perihelion burn and ~5 days of Jupiter-arrival shift. Two orders of magnitude more authority than
needed, so the design problem is throttling it down. Must be **commanded**, not passively
hysteretic: a one-way drift only reshuffles a phase sampling that is already near-random at ~80°
per revolution, so it concentrates no probability on Jupiter and collapses back into ignoring the
population.

### Staged crewed launch (`sec:periapsis_challenges`, closing paragraph)

**Staging carrier**:
The unmanned vehicle that holds *undeployed* PuffSat mass between a Parker-return delivery and the
crewed launch it will feed. It is the "unmanned payload" of the closing paragraph of
`sec:periapsis_challenges`, named. Being uncrewed, it absorbs the full 3.7 g of an 11 km/s solar-dive
push, which is the whole point of staging.
_Avoid_: depot (implies a fixed station), tanker, tug.

**Staging ellipse**:
The 50 km x 150,000 km orbit (`v_p` = 10.916 km/s, period 2.7 d, apogee speed 0.45 km/s) that the
solar-dive PuffSats deliver the **staging carrier** into, and where it parks. Same orbit the PuffSats
themselves fly in `sec:starship_safelaunch`, so no injection burn is ever needed.
_Avoid_: "apogee at lunar distance" (that is the `tab:mass_scenarios` row description; the operational
orbit of line 1444 and the companion sim is 150,000 km. Both happen to give `v_p` ~ 10.916 km/s).

**Arrival-declination floor**:
The lowest inclination a **staging ellipse** can be given for free, equal to the declination of
the solar-dive carrier's incoming hyperbolic asymptote. Choosing where perigee falls around that
asymptote selects the inclination at zero cost, and the same PuffSat collisions that deliver the
boost do the aiming, so upstream aiming beats a plane change. Decided 2026-08-12. Solar-dive
returns run near the ecliptic, so the floor sits near the 23.4° obliquity: every inclination from
there up is free (Cape Canaveral 28.5°, Baikonur 51.6°), and near-equatorial ones are not
(Kourou 5.2°). The paper should state the constraint rather than leave a reader to find it.
_Fallback, priced_: turning the plane at apogee costs `2 v sin(Δi/2)` at v = 0.45 km/s, so 218 m/s
for 28°. Negligible on the 10 t **tracker platform** (~0.6 t) and expensive on a loaded carrier
(~6% of an 850 t wave, ~52 t, every delivery). The asymmetry is the point: let the platform turn,
never the carrier.

**Perigee arming**:
Dropping the parked carrier's perigee from its drag-free parking value back to the 50 km deployment
perigee when a crewed launch is scheduled, and raising it again after. About 31 m/s each way at
apogee, because the carrier is crawling at 0.45 km/s there. This is the "very small rocket" the
Lagrange proposal wanted, and it is small only because the carrier never left the ellipse.

**Storage interval**:
Months, worst case ~0.8 yr, set by the **re-intercept cycle floor**: solar-dive mass arrives in waves
about 0.82 yr apart while crewed launches draw it down continuously. Decided 2026-08-12. It is the
number that binds lunisolar perigee drift, propellant shelf life, and cryogenic boiloff.

**Storable PuffSat**:
The variant qualified to sit in a **staging carrier** across the **storage interval**: water-ice or
ANFO fill, cool gas generator thrusters (`sec:cold_gas_fluid_choice`, line 419), no 60% peroxide
bipropellant and no LOX fill. Decided 2026-08-12. It retracts, for staged flights only, the line 424
premise that "PuffSats are single-use and operate for only half of a single orbit", which is what
licensed the paper to ignore shelf life everywhere.
_Rationale_: ice and ANFO keep indefinitely; airbag generants (guanidine nitrate with basic copper
nitrate) are qualified for ~15 yr of thermal cycling and sit *unpressurized* until fired, so the
storage phase carries no pressurized tank at all. Peroxide is excluded because the paper itself names
"catalytic decomposition and oxygen buildup in a closed volume" as the governing in-flight hazard,
which over months is a slow loss of oxidizer. LOX is excluded because holding 60--80 K through ~50
perigee passes of Earth albedo and IR is a different problem from holding it at 1 AU.
_Sustained-flow debt, discharged_: line 395 makes sustained flow, not total impulse, the binding
cold-gas requirement across the 300 s drag pass, and a gas generator is a one-shot device. The
T³µPS architecture already cited resolves this: generators charge a **plenum** and the plenum meters
sustained flow, firing more generators as pressure falls. The pressurized volume then exists only
during the half-orbit of use, never during storage, which preserves the exact property the storage
case wanted.
_Open_: belt dose. The **staging ellipse** crosses the Van Allen belts twice per 2.7 d period, so a
five-month park is ~100 crossings against deliberately cheap electronics. The mitigation is that
stowed PuffSats are shielded by the carrier hull and by each other, so only the outer layer of the
rack takes full dose. Unsized.

## Relationships

- A **PuffSat** strikes the **pusher plate** (or the **Medusa-style sail**); plate and
  absorber obey the **buffer invariant**.
- **Common-mode error** is cancelled by a **centroid retarget**; only **per-unit
  scatter** must fit inside the **catch radius**.
- **Plate capture** is the success criterion. The claim runs in **feasibility tiers**:
  Tier 1 (5 m) is simulated; **surveyor-anchored centring** is the Tier 2 (~10 cm) path,
  argued not simulated.
- For LEO, the **apogee nav constellation** pins the coast; the **target-side tracker
  array** (plus the **co-flying tracker**, and optionally **PuffSat self-homing**) does
  terminal homing via **differential astrometry**. Together these are the **off-board nav
  assets** that replace the dedicated **coordinator node** of the original paper.
- Near the Sun, lateral knowledge comes from **transverse-node differential ranging**
  with good **GDOP**; control is **deterministic-coast correction**. The **apogee nav
  constellation** does double duty here, since an Earth-to-Sun transfer departs from Earth.
- Straw Way argon pumping runs skin-then-wall: the **reflector skin** bounces argon, the
  **Straw Way wall stack** absorbs it, and **displacement threshold (`E_d`)** sets both edges of
  the **reflector window**. Earth escape speed sits inside that window, so **capture into a bound
  ellipse first, then drop through the straw** turns any interplanetary source (lunar, Ceres,
  Jupiter-cycle secondary payloads) into a guaranteed in-window arrival. The returning Jupiter
  PuffSats themselves arrive retrograde near 69 km/s and are six times outside it.
- Heliocentric distance sets the cryogen via the **passive-shielding temperature law**:
  LOX/methalox inside the **passive-LH₂ threshold** (~1.5 AU), LH₂/LOX beyond it; where a
  stored cryogen is unwanted, **on-demand electrolysis propellant** carries water instead.

## Example dialogue

> **Author:** "If a stochastic atmosphere scatters the whole salvo by a kilometre, doesn't
> that blow the **plate capture** budget?"
> **GNC expert:** "Only if it's **per-unit scatter**. A shared atmosphere is mostly
> **common-mode** — it slides the block as one, and a **centroid retarget** cancels it for
> free. What has to fit the **catch radius** is how the units differ from each other."
> **Author:** "And the catch radius is a sensing limit?"
> **GNC expert:** "No — it's the engine. The sensing limit lives in the **cross-track
> knowledge**, `σ_θ · R`, and that's a calibration bias, not noise."

## Flagged ambiguities

- **Does argon implantation in the tube wall work at the low arrival speeds of lunar, Ceres and
  Jupiter-cycle payloads? - RESOLVED 2026-08-19 (grill): yes, and the mechanism in the paper is
  currently attached to the wrong case.** `sec:vacuum_tube_details` claims argon rebounds off the
  150 km/s projectiles and implants in the wall, citing the sputter-ion pump. Two errors:
  - At 150 km/s argon meets the projectile at 4.66 keV, far above every `E_d`, so it does not
    rebound at all. It buries 5.9 nm into the skin and rides out of the tube. The projectile is
    the pump; the wall gets nothing. A "few nanometers" of iron is a window at this energy, not a
    mirror.
  - At 11 km/s argon meets the skin at 25 eV, below iron's `E_d`, so it does reflect, and reaches
    the wall at up to 100 eV, above aluminum's `E_d`, so it does implant. The paper's stated
    mechanism happens **only** in the low-speed case.
  Depth also needs restating. "A few nanometers" is about right at 100 eV (1.5 nm in Al) but
  understates the fast case by an order of magnitude (34 nm in Al at 18.6 keV). Decision: state
  **captured-either-way** as the claim and use the **reflector window** as supporting detail.
- **Does helium break the pumping story? - RESOLVED 2026-08-19 (grill): no, but not by
  implantation.** Helium needs a 25.9 km/s projectile to clear aluminum's `E_d`, and the
  **rebound ceiling (`2V`)** makes that unreachable below escape speed by any route, including the
  velocity tail. **Corrected later the same session:** that does not make helium capture
  impossible, only uncertain. `E_d` bounds whether an atom can *make* a hole, not whether it can
  *fit through* one, and helium's 31 pm radius clears aluminum's 59 pm octahedral interstitial
  site. Tungsten fuzz forms under 20-60 eV helium plasma, where helium can deliver at most ~5 eV
  against tungsten's ~90 eV threshold, so sub-displacement helium retention is experimentally
  established. Tunneling is not the route (4.5 pm de Broglie wavelength against 286 pm spacing).
  The retained *fraction* stays unknown, since helium is also highly mobile in metals. What saves
  the argument is influx, not pumping. Leak-driven helium sits 5e6 inside a budget
  of 1e-7 mbar per monthly refurbishment cycle. Permeation would dominate through bare polymer
  (bare 50 um PET needs a barrier improvement factor of 123x, Kapton 368x), but a single metallized
  layer buys 100-1000x. Cited in the paper via `baldwin2008helium` (60 eV He loads into W below
  the physical sputtering threshold) and `kajita2009tungsten` (fuzz threshold above 20 eV). Decision: **no dedicated helium pump**; the refurbishment cycle absorbs it,
  and the 100 nm aluminum layer is the helium barrier. Consequence: that layer now carries four
  jobs (atomic-oxygen/UV barrier, magnetic-steering conductor, argon absorber, helium barrier), and
  three of the four require it to stay *continuous*. The refurbishment driver is therefore pinhole
  growth from micrometeorites and sputtering, not bulk erosion, which is not close to binding
  (2.4e21 Ar impacts/m2 to sputter 100 nm away, against 1.8e14 per tube-fill).
- **Should the tube carry a tantalum liner to suppress argon instability? - RESOLVED 2026-08-19
  (grill): no, and the existing sentence must be cut.** `sec:vacuum_tube_details` recommends a
  heavy-metal liner such as tantalum on the sputter-ion-pump analogy (cathode-to-ion mass ratio,
  `vaumoron1970argon`). It fails twice here. It contradicts the mass budget, which wants
  metallized plastic over roughly 100 nm of aluminum. And tantalum's `E_d` of 90 eV exceeds the
  59 eV a 100 eV argon atom can transfer to it, so a tantalum wall would **reflect** the argon
  instead of trapping it, breaking the pumping mechanism outright. Aluminum is both the lighter
  and the better absorber, for the same reason: it is lighter than argon. The `vaumoron1970argon`
  cite was kept, reframed: the cathode-to-ion mass ratio runs the *unfavorable* way for an aluminum
  wall, and what offsets it is the low rebound energy at slow speeds plus the fact that fast
  projectiles carry their argon out rather than leaving it in the wall. The instability worry
  that motivated tantalum also mostly evaporates at low speed, since the Ar-on-Al sputter yield at
  100 eV is 0.05 against a 32 eV threshold, versus 2.5 at 18.6 keV.
- **Does the 3:1 prograde/retrograde optimum survive a real magnetic nozzle? — RESOLVED
  2026-08-17 (grill): no, it is the loss-free endpoint; the paper keeps it and names the
  parameter.** `sec:dv_effective` derived 3:1 assuming the merged fireball leaves as a single
  collimated jet, which is the momentum-maximizing bound for a given mass and energy, not an
  approximation. Reframed via **jet efficiency (`η_jet`)** the optimum is `(4/η_jet²) − 1`,
  moving to ~5:1 at `η_jet = 0.8` and ~7:1 at 0.7. Decision: **keep 3:1 as the stated result**,
  because it answers the idealized question, because the peak is flat (holding 3:1 costs ~1% of
  achievable thrust at `η_jet = 0.9`, ~6% at 0.8, ~18% at 0.7), and because the downstream
  mission numbers already assume a lossy nozzle at that mix. A ~5:1 minimax split would stay
  within 4% across `η_jet ∈ [0.7, 1.0]`, so the *design* bias runs prograde even though the
  *derivation* stays at 3:1. Two corrections fell out and were applied:
  - The center-of-mass motion of the merged fireball does **not** need re-thermalizing. It
    carries a fraction `m_rp` of the energy (25% at 3:1), already points retrograde, and its
    momentum exactly equals the incoming projectile's, so alone it yields **zero** net thrust.
    All thrust comes from collimating the thermal `1 − m_rp` share. That is the nozzle's job,
    and roughly half of that heat starts out moving *toward* the ship and must be mirrored.
  - `sec:methalox_rebuttal` conflated `v_g` with `v_e` at the Earth step, assuming 25 km/s
    where the head-on ideal ceiling is 24. Corrected; the headline ~$3/kg survives at
    `η_jet = 1`, but break-even against methalox now sits at `η_jet ≈ 0.89`.
  - A later review found that the cost cascade had inserted `v_e`, defined per total collision
    mass, into a conventional rocket equation even though the retrograde share arrives
    externally. The corrected mass ratio is `eq:external_reaction_mass`. It is strictly below
    `exp(Δv/v_e) − 1` at any `m_rp` in `(0,1)`, so the correction **lowers** the collision mass
    a burn needs and makes every cascade step cheaper. At full precision the ideal one-way cost
    falls from $3.32/kg to $3.20/kg, and break-even falls from 0.9007 to 0.8906. Any restatement
    of this correction that shows the cost *rising* is comparing a rounded old number against a
    full-precision new one.
  _Still open_: (1) no nozzle model supplies `η_jet`; the required 0.89 at the pessimistic
  anchor is asserted as a requirement, not estimated. (2) The magnetic pressure needed at the
  throat to mirror the ship-facing half of the fireball is uncomputed, and belongs with the
  deferred radiation-hydrodynamic calculation of `sec:solid_PuffSats`. (3) What published
  magnetic-nozzle results say about 0.89 was checked 2026-08-17: Ahedo & Merino
  (`ahedo2010magnetic`, already cited) report plume efficiency 0.63-0.83. Its square root gives
  a divergence-only ceiling near **0.79-0.91**. The 0.89 the pessimistic anchor needs sits near
  the top of that band. This reopened the 5:1 option (its six-fold rather than four-fold dilution
  of the expensive retrograde mass moves methalox break-even to `η_jet ≈ 0.80`) and the
  decision was **reaffirmed at 3:1**, because 0.89 is a rhetorical break-even at a $3200/kg
  early-generation projectile price, not a physics or architecture requirement. Recorded as
  `docs/adr/0006-three-to-one-split-stays-at-the-loss-free-optimum.md`.

- **Where does staged PuffSat mass park between delivery and use? — RESOLVED 2026-08-12
  (grill): the staging ellipse, not a Lagrange point.** The proposal was to park incoming
  PuffSat mass (and the reusable co-flyer carrying it) at Sun-Earth or Earth-Moon Lagrange
  points, with small rockets pushing it into the deployment orbit when needed. Rejected on
  angular momentum. The **staging ellipse** and the Earth-Moon Lagrange points sit at nearly
  the same *energy*, so the entire cost of moving between them is angular momentum: the
  ellipse crawls through apogee at 0.45 km/s while the Lagrange points sweep around Earth at
  0.87 (EML1) to 1.02 km/s (EML4/5). Round-trip costs, two-body coplanar, from the ellipse:
  - EML1/EML2 halo: ~0.88 km/s in, ~0.65 km/s out, ~1.5 km/s round trip, roughly 35% of the
    loaded carrier as methalox. Buys lunar-ISRU propellant access and a quiet thermal
    environment.
  - EML4/EML5 (the stable pair of `sec:handling_space_debris`): ~0.83 km/s each way plus a
    phasing wait, since departure is locked to 60° from the Moon.
  - Sun-Earth L1/L2: ~90 day transits, so ~2 flights/yr per carrier. Cadence is the killer.
  - Staging ellipse: 0 m/s to insert (it is already there), ~31 m/s of **perigee arming**
    each way, and it returns to apogee every 2.7 days for free.
  The reusability the proposal wanted therefore comes free from the ellipse's own period.
  Note the paper's Lagrange numbers in `sec:handling_space_debris` (0.5 km/s to EML1, 0.18 km/s
  to EML4/5) are computed for a package *falling from the 900,000 km turnaround* and do not
  transfer to a departure from the staging ellipse.
  _Shell crossings, answered 2026-08-12_: the ellipse's one real defect is that it sweeps the
  LEO and GEO belts every 2.7 days with a loaded carrier, and `sec:handling_space_debris`
  line 543 sells the lunar disposal route on precisely the opposite property ("never descends
  through the low Earth orbit and geostationary belts"). The reconciling distinction, which the
  paper does not yet draw and should: **line 543 is an argument about *uncontrolled* objects.**
  Disposal packages are inert, uninstrumented, and arrive billions per year, so they can never
  participate in conjunction avoidance. Carriers and the **tracker platform** are few, tracked,
  and maneuverable. Precedent for long-duration eccentric orbits crossing both belts is Molniya
  (perigee ~500 km, apogee ~40,000 km, twice daily, decades, dozens of spacecraft) and every
  GTO ever flown. Priced and held in reserve if the population number comes out badly: raising
  the parking perigee above the LEO debris shell to ~2500 km costs ~75 m/s each way (per-flight
  budget 50 -> 150 m/s, still ~20 flights per load); parking clear of LEO at ~10,000 km costs
  ~247 m/s each way (~5--6 flights per load, and it still crosses GEO).
  _Still open_: (1) the steady-state carrier population, which is the number the controlled-vs-
  uncontrolled argument owes. (2) Lunisolar perigee drift across the **storage interval**,
  unsized: at 150,000 km apogee the carrier sits at 39% of lunar distance, and months of
  third-body tugging moves perigee by an amount nobody has computed. It sets the parking
  perigee margin, so it also sets the per-flight budget above.

- **Should the load-bearing terminal sensor move from the target to the co-flyer? —
  RESOLVED 2026-08-12 (grill): split by phase, fused, handover at 2--3 s to impact.**
  The co-flyer is load-bearing from deployment down to roughly 2--3 s before impact; the
  **target-side tracker array** takes over inside that, and the two are *fused* rather than
  switched. Motivation for reopening: the target is disturbed by propellant slosh, repeated
  PuffSat impacts, and its own RCS/gimbal corrections between pulses, while the co-flyer is a
  quiet platform. What decided it:
  - The target-side array looks straight down the approach corridor, so its blind axis is the
    **miss plane**'s *timing* component. Both real miss axes are observable at every instant,
    with no singular geometry, by construction. A co-flyer never has this.
  - `σ_θ·R` collapses for the target because `R → 0` at impact, and does not for the co-flyer
    whose standoff `D` is roughly fixed. The target-side array at its nominal 1.6 µrad beats a
    50 mas co-flyer inside 45 km. The terminal phase *is* those last seconds.
  - The target's degraded conditions and its relaxed requirement coincide. Impact gating only
    exists once impacts are happening, which is when `R` is already small enough that the
    existing grade delivers centimetres. A **10× platform degradation still delivers 10 cm with
    0.57 s to spare.** This is a far stronger defence of the current architecture than the
    shock-isolator-and-Copperhead argument the paper actually makes, and it should replace it.
  - 2--3 s is simultaneously the metrology crossover and roughly the *control* horizon (a 10 cm
    divert takes 0.3--0.6 s to execute), so nothing is lost by handing over there.
  Sizing that falls out: the handover time pins the co-flyer at **~25--35 mas**. Below ~30 mas
  the co-flyer is **registration-limited** by the cm-class body-beacon-to-plate chain, not
  optics-limited, so Gaia-class metrology buys nothing. Build the 30 mas scope and spend the
  rest on absorber metrology.
  _Avoid_: the paper's current claim that the co-flyer "shortens `R`" for *terminal* homing.
  True in mid-course, false in the terminal phase where the target is nearer by construction.
  Also settled along the way:
  - The measurement must be **plate-beacon differencing**, not absolute line-of-sight
    (registration to the plate is otherwise ~2 m and eats all of Tier 1).
  - The **star channel decouples from the 1 ms beacon gate** (10–100 ms free-running star
    exposure on its own detector, gyro bridging to each beacon epoch). This is the actual
    reason a quiet platform wins: star *photons*, not vibration immunity. It is impossible
    on the impact-hammered target and easy on the co-flyer.
  - Vantage must satisfy the **miss plane** geometry: primarily along-track offset, with
    `x ≈ h`. A purely radial offset (the "350 km vs 200 km periapsis" idea) is blind in the
    radial miss axis unless paired with a comparable along-track offset.
  - Sizing: `σ(radial) = 2·h·σ_θ`. At `h` = 150 km, Tier 1 (~2 m) passes at any grade
    considered; Tier 2 (~10 cm) needs `σ_θ ≤ ~69 mas`, so the paper's current 330 mas fails
    and the premise 100 mas also fails. ~50 mas closes it. A half-metre-aperture, ~2–5 m
    focal-length scope reaches ~5–8 mas on rough photon-budget grounds, i.e. Tier 2 is not
    metrology-limited once the co-flyer exists.
  - The co-flyer's overflight singularity is real geometry but operationally harmless. Riding
    the PuffSat orbit at 10.8 km/s past a target accelerating 0→8 km/s, it sweeps ~2040 km of
    along-track offset per 300 s push and must transit `x = 0`, where the radial axis goes
    singular for ~50 s (~150 of ~900 units). It does not matter, because the mid-course only
    has to deliver into the **catch radius** (475 m against a 224 m entry spread), and even the
    worst overflight moment gives ~1 m.
  - Which disturbances actually threaten a 1 ms exposure, by frequency: **slosh (~0.9 Hz) does
    not** (0.33° of phase across the exposure, so constant rate, which centroids at mid-exposure
    and differences away like a rigid shift). RCS ringing (5--100 Hz) and impact ringing
    (hundreds of Hz) do. Slosh instead lands on the body-beacon-to-plate registration leg, which
    matters more now that the beacon has moved onto the body.
  Still open: the co-flyer's station-keeping and phasing against an accelerating target, and
  the migrated error terms below.
- **Terms that bind once `σ_θ·D` drops under ~1 cm — NONE ARE SIZED ANYWHERE
  (raised 2026-08-12 grill).** Listed in rough order of how badly they are neglected:
  *PuffSat beacon to gas-momentum centroid.* Tier 2 assumes "the PuffSat's position" is
  meaningful at 10 cm. The PuffSat is a balloon that atomises, the plate receives a gas
  cloud's momentum centroid, and the beacon rides on the dry-mass package that detaches or
  passes through the plate aperture before impact. `sec:spinning_tension_detail` already
  concedes the beacon sits off the aim line and fixes it with an accelerometer reading
  tether-pull direction, but that fix is sized for metres.
  *Loop latency.* At 11 km/s, 1 µs = 1.1 cm and light-time alone from a 1000 km standoff is
  3.3 ms = 37 m. Tolerable only because the measured state is ballistic and predictable, but
  that shifts the requirement from position knowledge to *velocity* knowledge.
  *Light-time lead.* The beacon appears displaced by `v_rel/c` ≈ 7.57 arcsec, independent of
  range. Deterministic, but needs `v_rel` to 0.027% to leave 1 cm.
  *Differential stellar aberration.* ~130 mas per degree of field angle at 10.8 km/s, i.e.
  larger than the whole 100 mas premise. Deterministic given co-flyer velocity to ~1%.
  *Differential distortion across the dichroic.* The paper's star-differencing argument says
  "the same front optics" cancel distortion, but beacon and stars land on **different
  detectors through different back-end paths** behind the splitter. Only the front element is
  common. Plausibly the true floor; unsized.
  *Plate-beacon to plate-centre structural/thermal flex.* mm–cm class, unmeasured.
- **Is the 1.6 µrad floor noise or bias? — OPEN (raised 2026-08-12 grill).** The paper
  insists it is a fixed calibration bias ("a bent ruler", averaging cannot help), while this
  glossary describes it as a "common-mode floor" reached by "√N" fusion, which is noise-like
  language. A rough photon budget (10 cm aperture, 1 ms exposure, ~20 stars) lands near the
  same few-hundred-mas value, which suggests the paper's own floor may be star-photon shot
  noise mislabelled as bias. If so the paper is *understating* its margin, since noise
  averages and bias does not. Needs decomposing in the companion sim.
- **Jupiter-cycle dry mass: which hazard? — resolved 2026-08-11 (grill).** The metric is
  **satellite collision**, and by that metric the population is ignorable by many orders of
  magnitude (see **satellite-collision metric**). Two alternative framings were raised and set
  aside. Earth impact is a harmless 70 km/s meteor. Upper-atmosphere metals loading is *not*
  obviously ignorable: if $10^{-4}$ to $10^{-3}$ of the population eventually reenters, that is
  100--1000 t/yr of mostly-aluminium ablation against a natural aluminium influx near 600 t/yr, on
  top of the burden `murphy2023metals` already measures. Deliberately out of scope for this
  paragraph; it is the objection a reviewer is most likely to raise, and the reentry fraction is
  the single number that would decide it. Salvage (a cislunar depot) is closed: the packages arrive
  at 40--70 km/s relative to everything near Earth, so the Moon and the Lagrange points are
  unreachable for them, unlike for the Earth-orbit **disposal package**.
- **"centimetre centring" vs "plate capture"** — resolved: **plate capture** (about 2 m
  on the 5 m plate) is the *committed* requirement; centimetre precision is achievable
  *capability* and an optional later tightening (surveyor-anchored centring), not the bar
  the baseline must clear.
- **"coordinator node" — resolved 2026-06-30 (grill).** No dedicated per-mission co-flying
  coordinator satellite is needed for LEO. The role is redistributed into the **off-board
  nav assets**: a permanent **apogee nav constellation** (one-way broadcast) for the coast,
  and a **target-side tracker array** + reused-rocket **co-flying tracker** for terminal
  homing, optionally backed by **PuffSat self-homing**. The companion control sim closed
  this at the 5 m (Tier 1) level. "Coordinator node" is now a *legacy* term for the original
  co-flying-brain framing; name the specific asset instead. The rewrite landed 2026-07-02
  as `sec:sensor_architecture` (grill session; see the **Apogee nav constellation**,
  **Target-side tracker array**, and **PuffSat self-homing** entries for the decisions).
- **Medusa "behind" = tension** was a slip; the behind-mounted sail is in
  **compression**. Real Medusa (front-mounted) is tension.
- **"hydrolyze" → "photodissociate"** (resolved 2026-06-30, §8 ozone subsection
  `sec:ozone_policy`). Water released by PuffSats at ~200 km is destroyed by
  **photodissociation / photolysis** (solar UV splits H2O into H + OH, the H escapes to
  space), *not* hydrolysis. Use "photodissociate" for any upper-atmosphere water-breakup
  claim. The ozone it could threaten sits in the stratosphere at 15--35 km, far below the
  200 km release.
- **"launch" applied to the rocket plane — RESOLVED 2026-08-13 (grill): it never launches, it
  takes off.** Every rocket-plane departure is an ordinary runway takeoff from an existing
  urban airport; the rockets first fire at ~12 km, one **ignition standoff** downrange. The
  distinction is load-bearing, not cosmetic: the liftoff roar (full thrust at zero altitude
  over a hard reflecting pad, radiating for tens of seconds at close range) is what dominates
  the complaint record at Starbase and Vandenberg, and this architecture has no such event at
  all. Reserve "launch" for Starship. Use **takeoff**, **transit leg**, **ignition point**.
- **Can the E2E noise critique be made on cumulative exposure (DNL)? — CLOSED NO, 2026-08-13
  (grill).** Tempting, because Musk tied his own 30 km figure to "frequent daily flights," and
  the FAA regulates residential compatibility at DNL 65 dB. The blocker is propagation
  uncertainty past 10 km. Gee's group describes the decay beyond 10 km as "sporadic" and
  meteorology-driven, and reports A-weighted sound exposure at 35 km coming in **18 dB below**
  the FAA Environmental Assessment model. Carrying that spread through the DNL arithmetic at
  30 km gives **7.8 events/day** to reach DNL 65 under naive spherical extrapolation and
  **491 events/day** under the full 18 dB haircut. A 63x swing settles nothing, and any
  referee who knows these papers will say so. The paper therefore argues cadence from
  institutional precedent instead: the California Coastal Commission rejected **50 Falcon 9
  launches per year** at a site with a 15 km buffer (overridden federally), against Shotwell's
  projected dozens per day. No estimate required. Reopen only if measured SEL-vs-distance
  data past 20 km is published; the figure exists in the Flights 5/6 comparison paper but the
  numbers were not extractable from the open-access text.
