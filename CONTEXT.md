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

**Coordinator node**:
A support satellite supplying ranging or metrology to an interception.

**Surveyor-anchored centring**:
An optional metrology upgrade (a sacrificial "surveyor" projectile measured by an
independent instrumented gate, plus strobed LED beacons on each unit) that shrinks the
plate from 5 m toward ~10 cm without changing the baseline architecture.

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
- **Plate capture** is the success criterion; **surveyor-anchored centring** is the
  optional path that shrinks the plate.
- Near the Sun, lateral knowledge comes from **transverse-node differential ranging**
  with good **GDOP**; control is **deterministic-coast correction**.
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
- **"coordinator node" — still open.** The architecture is actively questioning whether
  dedicated coordinator nodes are needed at all, versus ranging off ground/rocket
  infrastructure or a space-only GNSS. Use the term, but do not assume coordinator nodes
  are settled.
- **Medusa "behind" = tension** was a slip; the behind-mounted sail is in
  **compression**. Real Medusa (front-mounted) is tension.
