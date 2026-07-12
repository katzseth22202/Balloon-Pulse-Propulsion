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
frequency in the buffer invariant (`T = 1/f`), a distinct quantity.

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
transponder or precise clock on the PuffSat.

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
The reused launch rocket serving as a closer terminal vantage (shorter range `R`, so
smaller `σ_θ · R`); a redundant hedge, *not* required for the 5 m capture verdict.
_Avoid_: treating it as a dedicated new satellite (it is the launch rocket, reused).

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
`sec:strawway_economics`, ~\$2.6/MWh cost against a 1¢/kWh ($10/MWh) price, not the transport
rebuttal; the more aggressive ~\$1/MWh that also credits the breeding gain is kept out of the paper).

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
