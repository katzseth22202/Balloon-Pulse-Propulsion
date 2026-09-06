# Replies owed back to `puffsat_impact_simulation`

Answers, corrections and new asks arising from working
`puffsat_impact_simulation` @ `49a5e49`, `docs/nozzle_asks_answered.md` (the P1--P10 reply to
this repository's N1--N7). Written to be copied into that repository, so it repeats context
this repo already has.

Numbered R1 onward, to avoid collision with N1--N7 (our asks), P1--P10 (their answers) and
S1--S4 (`deferred_to_companion_repos.md`, targeting `aim_is_all_you_need`).

## Current status, 2026-09-06

The paper-side review of P11–P26 in `docs/nozzle_replies_answered.md` at
`puffsat_impact_simulation` revision `6fe8cf3` is complete. The accepted changes
are applied to the paper. R1–R15 below retain the original requests and reasoning
as history; the status notes supersede conflicting claims, including earlier
amendments. Completion of this editorial pass does not close the modeling work.

The adopted design uses a flared winding, an 11 T peak and a retained 5 T exit,
with a 660 m³ bag. The 12 T expansion and winding calculations remain reference
results. Expansion-frame efficiency is distinct from the ship-frame efficiency
used in the fleet calculation. Water radiation accounting uses integrated
in-nozzle emission; the absorbed liner load remains unresolved.

Remaining companion questions and calculations:

- What fraction of overtake pulses falls below the relevant closing-speed
  thresholds, and what fleet-growth benefit would pulse-by-pulse loading provide?
  P23's objective and existing fixed-per-leg policy are answered below.
- How does expansion-frame momentum map to ship-frame efficiency, including
  reversal on the head-on leg?
- Rerun geometry, field and expansion calculations for the corrected bag and
  adopted 11 T peak; assess regrading the full profile, including the exit field.
- Resolve the post-snowplow mass distribution, wall interaction and absorbed
  radiation before replacing liner loads or ablation budgets.
- Compute argon equation of state, expansion, radiation and conductivity before
  assigning it new nozzle efficiencies or fleet-growth results.

These are recorded follow-ups. No request has been sent to either companion
repository.

## P23 follow-up: mission objective and loading policy clarified

Accepted in the paper review. The existing `aim_is_all_you_need` calculation at
`b4ddcf0` supplies the objective and loading policy that P23 asks about.

- `src/two_wave_growth.py:price_chain` maximizes the product of cycle growth
  factors over the flown chain, using one departure slug ratio across the cycles.
- `src/two_leg_nozzle_sweep.py:price_chain_two_leg` chooses separate growth-push
  and departure ratios. Its objective sums logarithms of cycle growth, equivalent
  to maximizing compounded growth, subject to ignition and launch-return bounds.
  Each leg's ratio is held fixed across the cycles.
- Neither calculation optimizes a pulse-by-pulse loading schedule. Such a schedule
  has not been priced or adopted in this review.

The chemistry-only gross-momentum optimum is a different question. Holding other
loss factors fixed and using the paper's `E_a = 50.9 MJ/kg`, its momentum factor
is `sqrt((1+k) - 2 E_a (1+k)^2/w^2)`. At 45.58 km/s this peaks at
`k = w^2/(4 E_a) - 1 = 9.20401`. The reference 8.52 is 0.224927% below that
maximum; moving from 8.52 to 5.2 reduces gross momentum by 7.812997%. These are
analytic sensitivities, not a new fleet run or a change to the flown loading.

The paper now states this distinction. The objective question is answered from
the existing source; the value of a varying loading schedule remains open. The
separate requests for the fraction of overtake pulses at low closing speeds and
for expansion-frame versus ship-frame efficiency accounting are not closed by
this clarification. No request has been sent to either companion repository.

---

## R1. P2's `eta_geom` is lumped, and the two terms it omits both cut the same way

> **Superseded by the reviewed fluid-expansion and frame accounting.** The
> single-particle magnetic-moment estimates below are retired, as are the earlier
> amendment's claims that argon clears the cold leg. The modeled `eta_exp` is mean
> axial speed divided by RMS speed in the initial plume frame, not the full
> ship-frame `eta_geom` or `eta_jet`. Geometry and divergence still matter; neither
> the historical station-weighted levels nor the amendment's numbers establish
> fleet performance.

> **AMENDED 2026-09-04, later the same day. Read this box before the item.**
>
> The 0.48--0.64 below is computed in **your `mu`-conservation framework**, and we no longer
> think that framework applies. `mu = v_perp^2/2B` is a single-particle invariant, and
> `jet.py`'s own docstring lists "the expansion is collisionless enough for `mu` to mean
> anything" among its assumptions. **The Knudsen number violates it**: `Kn` = 5e-8 in the bag,
> 4e-7 at the magnet exit, 1e-6 at an extension exit. The paper's `CONTEXT.md` already says
> "mean free path ~1 um against a 3 m bore ... this is a continuum fluid". A parcel collides
> millions of times crossing the bore.
>
> **The right model is a de Laval nozzle with magnetic walls**, which is the paper's own
> "walled by field rather than fenced by it" and needs no hardware change, since at
> `beta` = 0.013--0.073 the field exceeds plasma pressure 15--75x and *is* the wall. Then
> `eta_geom = cos(theta)/sqrt(1 + 3/(gamma M^2))`, giving **0.767** with no extension and
> **0.928--0.958** with R11's. **The binding term is divergence, not speed spread.**
>
> Also see **R13**: `eta_chem` = 0.731/0.910 is a **water** figure, and the paper's argon slug
> pays no such toll. The cold-leg shortfall this item reports is a chemistry problem, not a
> nozzle one.
>
> The *structure* of the criticism below stands, and it is the reason the correction was found:
> P2 lumps one area ratio over mass that is spread along the column, and it counts conversion
> without the radial spread that causes it. What changes is the arithmetic that replaces it.
> Probe: `todos/framework.py`.

**Priority: highest. It moves P2's headline number.**

`jet.py:alpha_after_expansion` applies one `area_ratio` to the whole plume, so every gram is
credited with the full 20 T to 5 T fall. Two corrections, both downward.

**Station weighting.** `mu` is a *local* invariant. The merged fireball is the 23 m column
itself, filling the bore, so a parcel born at `z` sits in `B(z)` and can only fall to `B_exit`.
Its own ratio is `B(z)/B_exit`, not 4. Against P6's own fit `B = 19.80 z^-0.4405`:

| `z` | 1 m | 3 m | 6 m | 12 m | 23 m |
| --- | ---: | ---: | ---: | ---: | ---: |
| local `A/A*` | 3.98 | 2.45 | 1.81 | 1.33 | 1.00 |
| `alpha` | 0.771 | 0.628 | 0.495 | 0.315 | 0.088 |

Mass-weighted `<alpha>` = 0.345, not 0.772. That alone takes `eta_geom` from 0.70--0.88 to
0.45--0.57.

**The divergence term.** `mu` conversion turns gyration into motion *along the field line*, and
a line that drops fourfold in strength has, by flux conservation, fanned to twice the radius. So
the converted motion is itself tilted off-axis and the axial momentum is `v_par cos(theta)`:

    eta_geom ~ < sqrt(alpha_par) cos(theta) >,   tan(theta) = (r/2)|d ln B/dz|

`jet.py` models the numerator only. **This is why the flare has an optimum rather than being
monotonic in `A/A*`**, which is the standard magnetic-nozzle result and is worth carrying in
`jet.py`'s docstring, since the module currently states the opposite ("the deeper the flare the
more complete the conversion").

**With both terms, at the flown grading and a bore that accommodates every tube.** P3 puts
detachment at 1.44--2.00 exit radii, so that window is the answer; the 0.95-radii row is the
unreachable optimum, shown only to locate the peak:

| detachment | `<cos theta>` | `eta_geom` | `eta_jet` cold | `eta_jet` hot |
| --- | ---: | ---: | ---: | ---: |
| exit plane | 1.000 | 0.452--0.567 | 0.331--0.414 | 0.412--0.516 |
| 0.95 exit radii (*optimum, not reachable*) | 0.79 | 0.527--0.660 | 0.385--0.482 | 0.480--0.601 |
| **1.44 exit radii (P3 low)** | **0.703** | **0.513--0.643** | **0.375--0.470** | **0.467--0.585** |
| **2.00 exit radii (P3 high)** | **0.632** | **0.483--0.605** | **0.353--0.442** | **0.439--0.551** |

**What this does to P2's conclusion.** The mechanism stands and the paper will state it. The
bound does not: `eta_geom` = **0.48--0.64** across P3's detachment window clears `sec:mass_interest`'s forward-thrust floor of
`1/sqrt(1+k)` = 0.324 comfortably, but does **not** reach the 0.775 the growth tables sweep to.
So "where the chain misses, it is `eta_chem` doing it" does not hold. The nozzle is still
missing too, and `eta_geom` is bounded rather than cleared.

**Status of our figures.** Paper-side probes, first order: paraxial field (`B_r = -(r/2)
dB_z/dz`, evaluated out to 6 m against a 3.5 m coil), uniform mass in the bore, one detachment
surface for all streamlines. The tilt formula itself is exact given flux conservation; the weak
step is using the on-axis `B(z)` for an off-axis tube, and since off-axis field is weaker in a
diverging region **the real tubes probably fan somewhat more, so 0.48--0.64 is more likely
generous than harsh.** Probes: `todos/station_weighted_alpha.py`, `todos/fluxtube.py`.

---

## R2. P7 is decided: the winding flares. `eq:bore_from_length` was never a magnet contour

> **Field-line check answered by P16, accepted in the paper review.** In the
> 48-coil, 12 T capped reference calculation, no sampled paths cross the flared
> winding boundary. ADR-0011 records the uniform-column launch assumption and
> vacuum-field model. This is not an actual liner-impact mass fraction or an
> 11 T rerun. Current bag geometry is ADR-0014's 660 m³; current peak is 11 T
> under ADR-0013. The text below records the earlier design and request.

Recorded in `docs/adr/0011`, as amended by `docs/adr/0012`. The winding follows the plume's
bounding flux tube, `r(z) = r_bag sqrt(B_chamber/B(z))` plus clearance. At ADR-0012's 12 T cap
that is **3.50 m at the chamber to 5.17 m at the throat, a mean half-angle of about 4 degrees,
at 1.18x conductor** against the original straight winding at the uncapped field (500 A figures
4.4 t and 7.2 t become 5.2 t and 8.5 t; the "under about 8 t" floor becomes about 9.4 t; the
flare exit is 10.3 m across).

**The cap and the flare pull against each other, and the cap wins.** A lower chamber field
expands the bounding tube less. This item first reported 6.50 m and 1.50x on the uncapped 20 T
profile; ADR-0011's own amendment supersedes those, so **ignore 6.50 m and 1.50x if you have
them from an earlier copy.**

The contradiction dissolves rather than resolving. `eq:bore_from_length` was introduced to size
**the bag**, and the paper then silently reused the same `r` as the solenoid radius. **The bag
stays a 3.00 m by 23.8 m cylinder of 672.9 m³ and sits inside the flare rather than filling
it** (R14), so the volume-to-bore relation is untouched and only the conductor term inherits
the flare.

**What we would like confirmed:** the flux-tube accounting against a real field solve rather
than our paraxial one, since `field.py` already has the winding machinery P8 used.

---

## R3. Regrading the column field to buy back `eta_geom` is self-defeating

> **Superseded by P13 and the adopted P18/P19 field decision.** The
> magnetic-moment efficiency levels and their claimed ranking below are retired.
> The fluid calculation improves modeled expansion efficiency when the reference
> peak falls from 20 T to 12 T. The adopted peak is now 11 T with a retained 5 T
> exit; no new full-profile efficiency or hardware-mass result was computed.

Recorded so nobody re-derives it, in the same spirit as your P9.

`A/A*` is one ratio read two ways: `alpha_exit = 1 - (1 - alpha_0) B_exit/B_start` and
`r_exit/r_start = sqrt(B_start/B_exit)`. **Conversion cannot be bought without radial spread,
because they are the same number.** Holding the exit at 5 T (P9 forbids lowering it) and raising
the column field instead:

| profile | field energy | virial structure | plume missing a 3.5 m winding | `eta_geom` |
| --- | ---: | ---: | ---: | ---: |
| flown 20/12/9/5 T | 1.00x | 10--30 t | 12.9% | 0.53--0.66 |
| flat 12 T | 1.99x | 20--60 t | 38.9% | 0.60--0.75 |
| flat 20 T | 4.92x | 49--148 t | **58.2%** | 0.67--0.83 |

The third row buys a 26% better nozzle by throwing 58% of the propellant at the coils, and the
middle row already reaches the 37--112 t of structure ADR-0009 refused. Probe:
`todos/regrade_full.py`.

_Two caveats on the table, neither of which touches the conclusion._ The `eta_geom` column is
built on `mu` conservation, which R1's amendment retires; read it as a ranking rather than as
levels. And "flown" now means ADR-0012's capped profile rather than the 20 T nose, which does
not move the argument, because the lever being refused here is *raising* the column field.

---

## R4. Your deferred N7 is mispriced, and it is now the most valuable run on the list

> **Partially answered; the post-snowplow state remains open.** The
> station-weighted magnetic-moment efficiencies and factor-of-two-to-three claim
> below are retired. Mass location still matters for geometry and wall loading.
> P16 uses uniform column-volume starting points for field traces; it does not
> reconstruct the actual merged plume or provide a liner-impact mass fraction.

The deferred table rates the rod-resolved snowplow merge by what it buys for `f_d`, which is
worth about 3% on the reflection baseline. **The same run produces the mass-versus-station
profile at the end of the plow, and that is worth a factor of 2 to 3 on `eta_geom`:**

| where the plow leaves the mass | `eta_geom` | `eta_jet` cold | vs floor 0.324 |
| --- | ---: | ---: | --- |
| all at the 20 T entry | 0.70--0.88 | 0.51--0.64 | clears |
| uniform along the column | 0.45--0.57 | 0.33--0.41 | clears, thin |
| all at the 5 T throat | 0.24--0.30 | 0.17--0.22 | **fails** |

And the geometry says the plow runs *downhill*. The paper has the projectile entering the far
end (line 1187) with the field strongest there, so the plow travels from 20 T toward 5 T and
concentrates mass at the **weak** end. **The uniform row is the optimistic bracket, not the
pessimistic one.** What stops the bottom row from being the answer is that the shocked layer
vents backward at its own 21.1 km/s sound speed while the front advances, and that the merged
centre of mass drifts at only `w/(1+k)`. Where between those two the mass actually lands is the
run we need.

---

## R5. Your deferred N3 liner fraction has a first-order answer, and it is not 2.3%

> **Geometric part answered by P16, accepted in the paper review.** The companion
> field trace gives 17% of sampled paths crossing a straight 3.50 m winding at
> the original 20 T profile, 14% at the 12 T cap, and none for the capped flare.
> These supersede the paraxial clearance estimates below. They do not determine
> kilograms striking the liner: the post-snowplow mass distribution and wall
> interaction remain unresolved. No ablation budget is replaced by these fractions.

Flux-tube accounting against a straight 3.5 m winding, uniform mass in the bore:

| `z0` | 1 m | 3 m | 6 m | 12 m | 23 m |
| --- | ---: | ---: | ---: | ---: | ---: |
| widest tube that clears | 1.75 m | 2.23 m | 2.60 m | 3.02 m | 3.02 m |
| that station's mass clearing | 33.8% | 54.8% | 74.3% | 100% | 100% |

**12.9% of the plume misses the winding, about 27 kg/pulse against the 4.9 kg/pulse the ablation
budget books, a factor of 6.** This is geometry, not a wall interaction, so it needs none of the
machinery your deferred table costs (no prescribed-inflow BC, no immersed wall, no table EOS).

_Updated for ADR-0012's cap and R14's bag._ The table above is the uncapped 20 T profile on the
old 23 m bag. Flattening the chamber field expands the tubes born there less, so more of them
clear a straight winding: **11.6%, about 25 kg/pulse, 5.0x the booking** at the 12 T cap on the
23.8 m bag, and 8.8% if R9 buys the 9 T shelf. **The conclusion is unchanged and the number is
not 2.3%.** Probe: `todos/fluxtube_capped.py`, which reproduces the 12.9% above on its original
inputs before re-running.
**With the R2 flare the geometric load goes to zero**, which is the main reason the flare wins.
The 4.9 kg booking then has to be justified by something other than flux-tube geometry, and we
would still like the wall-interaction run eventually.

---

## R6. P5 credits the near-Sun transfer to our ask alone. The paper makes it too

P5 says "The paper never makes that transfer; the ask did." `templateArxiv.tex` line 773, in the
opacity discussion, states the gate flat with no near-Sun qualifier:

> `sec:minimum_nozzle` sets the number that calculation has to return. Radiative escape has to
> stay below about a tenth of a percent for the magnetic nozzle to remain a passive structure.

So P5 is a **required edit rather than a clarification**, and it has two sites, not one.
**Both are now fixed** (2026-09-04). The gate is attached to the near-Sun burn at each, the
Jupiter chain is given its own, and while we were there the sky fraction and the sheddable
ceiling were corrected as well: see R12 and the note in P5's own item that `1500`\,K is not the
temperature of the surface that takes the flash.

---

## R7. `throat` means opposite ends in the two repositories

> **Superseded by P22, accepted in the paper review.** Both repositories now use
> `chamber` for the strong-field end and `exit` for the downstream opening.
> `throat` is reserved for the sonic station, at the chamber in the expansion
> model. The companion's radius constant is now `CHAMBER_RADIUS`. The paper's
> hardware descriptions and CONTEXT glossary have been corrected. The proposal
> below records the earlier convention and is no longer operative.

| | this repo | `puffsat_impact_simulation` |
| --- | --- | --- |
| **throat** | the downstream **exit**, where the plume leaves at 5 T (paper line 1129, "a strong field at the chamber and a weak one at the throat"; `CONTEXT.md` 1654 uses throat and exit interchangeably) | the upstream station where `A/A*` = 1, at 20 T (`expansion.THROAT_RADIUS` = 3.0 m) |

P3's "`M_A` rises from 0.12--0.22 at the throat to 0.35--0.58 at the exit" is therefore
unreadable from the paper side, since both ends are called the throat here. **We are keeping
the paper's usage** (throat = exit) because it is load-bearing in `sec:two_leg_nozzle`'s
hardware description. Suggest the sim repo rename `THROAT_RADIUS` to `CHAMBER_RADIUS`, or that
both repos adopt **chamber** (20 T end) and **throat** (5 T end) throughout.

---

## R8. What happens when sub-Alfvénic plasma is forced against a wall?

> **Architecture preference updated by P14.** The paper prefers a magnetic
> extension. The handback does not establish that every physical bell is
> impossible, nor solve plasma-wall interaction. The historical thermal-survival
> claims and efficiency levels below are not accepted design results. Wall
> interaction remains a modeling question, but no longer blocks the paper's
> statement of the magnetic-extension option.

**This is your own second open question, and it is now load-bearing.** Your deferred section
raises it as a curiosity:

> If a physical diverging nozzle takes over downstream, the plasma does work against field lines
> that want to curve back, currents into the wall, reaction forces on the last coil. Real MHD,
> not modelled here.

A staged nozzle is now the paper's leading candidate for recovering the divergence loss of R1, so
the answer decides whether that architecture exists. **Nothing goes into the paper until this
lands.**

**This item is the paper's critical path. Three things block on it** (user's calls, 2026-09-04):

1. **P2's wording.** Whether `eta_geom` is stated at R1's 0.48--0.64 or at whatever a bell returns.
2. **P3's magnetic-drag question.** The paper retires magnetic drag from `eta_geom` on the strength
   of the `M_A` number P3 corrects. Hoyt's magnetic drag and R1's divergence term are the same
   physics (plume following diverging field lines and losing axial momentum), so if the plume stays
   field-guided the term was never retired and costs `<cos theta>` = 0.63--0.70. **But a physical
   bell sets exhaust direction mechanically, in which case the retirement is genuine after all.**
   The paper cannot say which until R8 lands.
3. **The staged nozzle itself.**

**R11 may make this item unnecessary**, and should be read first. It gets the bell's entire
benefit (setting exhaust direction so the plume detaches while still pointed the right way) from
a magnetic flare past the bag, with **no wall for plasma to push against**. If R11 holds, R8 is
moot. If R11 fails, R8 is the only route left to the divergence loss.

**A cheap partial, if the full MHD is out of reach.** Your deferred note says this is "real MHD,
not modelled here", and we would rather have a third of the answer than none. The favourable
argument is that a wall keeps `rho` up, which lowers `v_A = B/sqrt(mu0 rho)` and raises `M_A`. That
is testable in the **existing quasi-1D machinery**: impose a prescribed wall contour in place of
free expansion and recompute `M_A(z)`. **If constraining the plume moves the `M_A` = 1 crossing
inside the bell, the wall is turning plasma the field has already released and the hard MHD
question never arises.** That is a boundary condition, not a new solver.


### The architecture being tested

The magnet stops at `A/A*` = 4, where the collision needs it and where P9 showed it must stay. A
**physical bell** then takes over outside the winding and provides the rest of the expansion,
with no field to weaken and no coil to protect.

**Why a wall is thermally free here, which is the part that makes it worth asking about.** Pulses
are ~1 ms at 2 Hz, so the duty cycle is 0.2% and the time-averaged flux is 500x below peak.
Pyrolytic graphite conducts at 1700 W/m/K along its sheets, so a 1 ms pulse penetrates 1 mm and
the surface spike from 44.6 MW/m² is **31 K**. Steady-state balance is the wrong model and
overstates the load by about three orders of magnitude.

| bell radius | plume expansion | `T` frozen | `T` equilibrium | graphite survives? |
| ---: | ---: | ---: | ---: | --- |
| 6.03 m (magnet exit) | 1.00x | 5296 K | 16224 K | frozen yes, **equilibrium no** |
| **7.0 m** | 1.16x | 3930 K | 12039 K | **both** |
| 8.5 m | 1.41x | 2665 K | 8165 K | both |
| 12.3 m | 2.04x | 1273 K | 3899 K | both |

Steady baseline plus the 1 ms transient, against graphite's 3900 K. Probe:
`todos/staged2.py`.

### The state at the handoff, from your own numbers

| quantity | value | source |
| --- | ---: | --- |
| `M_A` at the magnet exit | 0.35--0.58 | your P3 |
| `beta` at the magnet exit | 0.013--0.073 | your P3 |
| exit field | 5 T, falling as `R^-3` beyond the last coil | paper `sec:needle_through_fog` |
| plume speed | 10.8--22 km/s | paper `sec:jet_efficiency` |
| `T` at the exit plane | 5296 K frozen, 16224 K equilibrium | your P5 |

**The plume is sub-Alfvénic and low-beta when it meets the wall.** That is the whole difficulty:
the field is energetically dominant and the flow is too slow to break away from it, so a wall in
that region is pushing against the field rather than against free plasma.

### What is wanted

1. **Does the flow attach to the wall or stand off it?** Magnetic pressure against dynamic
   pressure at the wall, along the bell contour.
2. **Currents driven into the wall, and the reaction on the last coil.** Sign matters: does it
   subtract from thrust, and by how much?
3. **Does the wall move detachment?** There is a favourable argument that it does. Constraining
   the plume keeps `rho` up, which lowers `v_A = B/sqrt(mu0 rho)` and raises `M_A`, so a bell
   might detach the flow sooner than free expansion does. That is a sentence, not a calculation,
   and it is the crux.
4. **`eta_geom` with the bell**, against the **0.53--0.66** the field-only case gives (R1). The
   loss the bell is meant to recover is divergence: `<cos theta>` = 0.70--0.79, against a directed
   bound near 0.88. **If a bell recovers most of it, `eta_geom` reaches the 0.775 the growth
   tables sweep to, which nothing else we have tried reaches.**
5. **Wall erosion** at 10--22 km/s grazing incidence, over the eleven flown cycles.

### What would settle it

Whether the paper can carry a staged nozzle at all. If the wall fights the field, the idea dies
and `eta_geom` stays at R1's 0.53--0.66, short of the swept target. If the wall turns free plasma,
the largest remaining loss term in the chain is recoverable by structure that is thermally almost
free.

### Lifts

The divergence term in R1, and the second open question in your own deferred section.

---

## R9. How fast does the snowplow front spread, and where does it first touch the wall?

> **Answered within the prescribed front model by P18/P19.** At a constant
> 3.50 m wall, the adopted faster-spread case first contacts at 3.83 m and demands
> 10.95 T, rounded to an 11 T peak. The sound-speed-only case gives 7.29 m and
> 8.25 T and is not adopted. A flared liner at or outside 3.50 m makes this a
> conservative contact bound within that model. Its bag-area cap builds in swept
> mass independence; lateral magnetic feedback is not resolved. See ADR-0013.

**Cheap, and it is worth 3 T of peak field.**

**Why.** ADR-0012 caps the nozzle's peak field by observing that the field's job at the chamber
is wall standoff, and the front does not reach the wall for the first several metres. **The
station where it first touches sets the cap.** The paper's own bracket moves that station a long
way:

| spreading speed | half-angle | wall contact | profile asks there |
| --- | ---: | ---: | ---: |
| sound speed, 21.1 km/s (paper's choice) | 24.9 deg | **6.0 m** | **9.0 T** |
| 1.9x sound speed (paper's own upper bracket) | 41.3 deg | **3.26 m** | **11.8 T** |

`sec:needle_through_fog` takes the sound speed and calls it the conservative choice, which it is
**for the coupling argument**: a slower-spreading front sweeps less mass and understates `k`. For
the field cap it runs the other way, because a faster front reaches the wall sooner and needs the
field there. **The same assumption is conservative for one conclusion and anti-conservative for
the other**, which is worth flagging in its own right.

We have adopted the safe end, 12 T. The 9 T end is worth having.

**What is wanted.** From the snowplow model, the front's radius against axial station,
`r_front(z)`, for the flown geometry, and the station where it first reaches the 3.02 m bore
wall. A single curve per leg. If the model resolves it, the shocked layer's actual lateral vent
speed against its sound speed is the underlying number.

**What would settle it.** Whether the peak field is 9 T or 12 T, and with it:

| | 9 T | 12 T |
| --- | ---: | ---: |
| field energy | 0.75x | 0.88x |
| virial structure, hot pulse | 7--22 t | 9--27 t |
| conductor | 0.90x | 0.96x |

**Lifts.** ADR-0012's conditional, and the remaining half of P6.

---

## R10. P8 counts minima when what matters is their depth, and P1 sets the threshold

> **Superseded by P17, accepted in the paper review.** The collisionless
> pitch-angle threshold below is retired. The fluid criterion compares local
> contraction with the area change allowed by the local Mach number. The tested
> reference sweep passes at 12 coils for the straight winding and 18 for the
> flared 12 T winding, with the binding region near the chamber. These are sampled
> reference results, not an 11 T rerun or a general coil-count guarantee.

**Not a disagreement with P8's sweep, a disagreement with its pass criterion.**

P8 reports whether an off-axis `|B|` minimum **exists**, and concludes ">= 36 coils". But a
magnetic trap only holds what its mirror ratio can hold. A particle is trapped when
`sin^2(theta) > 1/R`, so the threshold is `R > 1/sin^2(theta)`, and **your own P1 sets that
number**:

| plume | `alpha` | `sin^2(theta)` | traps once `R` > |
| --- | ---: | ---: | ---: |
| isotropic, as `eq:reflection_baseline` assumed | 0.333 | 0.667 | **1.50** |
| **the measured column (P1)** | **0.088** | **0.912** | **1.096** |

**P1 and P8 interact and neither notices.** A mirror traps perpendicular motion, so the pancake
P1 found is trapped by a mirror **five times weaker** than an isotropic plume would need. Your
12-coil row, `R` = 1.36, traps the flown plume comfortably while an isotropic one would walk out.

The correction runs both ways, and mostly in your favour. A shallow minimum is not a failure.
On our own crude re-run against ADR-0011's flared, ADR-0012-capped winding, the 18-coil case
shows one minimum at **`R` = 1.023, below the 1.096 threshold**, so it traps nothing, and 24
coils is clean outright.

**Our coil model is cruder than yours** (per-coil currents set by a rough local-field match rather
than your `field.py` winding solve), so **take the criterion and not our coil count.** What is
wanted is your own P8 sweep re-run with two changes:

1. **Report the mirror ratio of each minimum, not just its existence**, and pass anything below
   `1/(1 - alpha)` = 1.096.
2. **Run it on the current winding**, which is no longer the one P8 assumed: flared 3.50 m to
   5.17 m (ADR-0011 as amended) and capped at 12 T (ADR-0012). Bigger coils downstream smooth
   more, so the binding station has moved to the chamber.

**A caveat that cuts the other way, and it is yours:** the flat 12 T shelf the cap introduces has
**no background gradient** to swamp ripple, so minima will appear there that the old steep chamber
profile suppressed. We believe they are far too shallow to matter (`R` - 1 of order 1e-4), but a
flat region is exactly where the depth criterion has to be applied rather than assumed.

**Lifts.** P8's coil-count requirement, and the connection between P1 and P8.

---

## R11. Reduce the field at the throat by moving the throat downstream. **This may retire R8.**

> **Updated by P14 and P18/P19, accepted in the paper review.** The
> 10.9 m, 15° magnetic extension reaches the model's release condition at 75 km/s,
> but not at 45.58 km/s. Modeled `eta_exp` is 0.89–0.96 and 0.86–0.92,
> respectively; these expansion-frame values do not establish ship-frame fleet
> performance. The 56.3 km/s efficiency-target crossover is not a detachment
> threshold. The retained 5 T exit was derived from bag-referenced standoff,
> not an independent collision constraint; full-profile regrading remains open.
> The blanket clearance claims below are superseded.

**Priority: highest of the open items. It is the only thing we have found that clears the
paper's own 0.775 target.**

**What P9 forbade, and what it did not.** P9 is right that one static field cannot be strong for
the collision and weak for the expansion **at the same station**, so flaring the existing 23 m
harder drops the field where the snowplow is still at the wall, and the front lands on the liner.
**But past the bag the front has stopped sweeping mass and its pressure is falling, so a section
downstream of z = 23 m never has to stand off a collision.** The 5 T at the exit is a collision
requirement. Nothing beyond the bag inherits it.

Note that the field is already **15--75x over-strength for the expansion** at the exit (that is
your own `beta` = 0.013--0.073). It is 5 T because the collision needs 5 T there.

**What it takes.** `M_A` = 1 arrives sooner than expected, because `M_A = M sqrt(gamma/2)
sqrt(beta)` climbs on both factors as the flare opens:

| leg | area needed | extension at 15 deg | exit radius | exit field | total magnet | conductor |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| hot, favourable | 2.63x | 10.9 m | 7.6 m | 1.89 T | 34 m | 1.32x |
| hot, pessimistic | 2.90x | 12.3 m | 8.0 m | 1.72 T | 35 m | 1.35x |
| cold, favourable | 5.60x | 23.9 m | 11.1 m | 0.89 T | 47 m | 1.54x |
| **cold, pessimistic (binds)** | **7.45x** | **30.3 m** | **12.8 m** | **0.67 T** | **53 m** | **1.61x** |

**Peak field stays 12 T.** The extension is cheap per metre because its field is under 2 T. The
3x spread between legs is driven entirely by your `beta` range, so narrowing that narrows this.

**What it buys, and it is not more conversion.** `alpha` barely moves (0.86 against 0.91). The
gain is **where** detachment happens:

| | `<cos theta>` | `eta_geom` | `eta_jet` hot | vs the swept 0.775 |
| --- | ---: | ---: | ---: | --- |
| free fanning to detachment (today, R1) | 0.665 | 0.51--0.63 | 0.46--0.58 | misses |
| **extension at 15 deg** | **0.983** | **0.72--0.91** | **0.66--0.83** | **clears** |

Today the plume detaches by fanning freely along field lines spreading at 40--50 degrees, so two
thirds of its momentum ends up off-axis. An extension reaches `M_A` = 1 **inside a controlled
flare**, releasing the plume while it still points the right way.

**Why this may retire R8.** The physical bell was wanted for exactly one thing: to set exhaust
direction mechanically and recover the divergence loss. **A controlled magnetic flare does the
same with no wall**, so the sub-Alfvenic-wall question never arises. It also **restores the
paper's original claim that detachment happens inside the nozzle** (`sec:jet_efficiency`), which
P3 corrected. The claim was right; only the number was wrong, and the fix is the design the
corrected number points to.

### What is wanted

1. **`M_A(z)` through a prescribed extension, on both legs, with your solver** rather than our
   1-D isentropic area--Mach relation. Where does the crossing actually land?
2. **Is the collision front contained past the bag?** By P9's own `r_front/r_bore =
   beta^(1/2 gamma)`, the front runs `beta` = 1.38 at the extension exit and wants about 1 m of
   winding clearance over the plume tube (included in the conductor column above). Whether the
   front is still a coherent front that far out is a question only the model can answer.
3. **`eta_geom` through the extension**, against R1's 0.48--0.64.
4. **Narrow `beta`**, since it sets the 3x spread between an 11 m add-on and a 30 m one.

### What would settle it

Whether the paper carries a 34 m nozzle, a 53 m nozzle, or neither. **If it holds, `eta_jet`
clears the swept target for the first time in this exercise, R8 is unnecessary, and P3's
correction turns into a design change rather than a retraction.** If it fails, `eta_geom` stays
at R1's 0.48--0.64 and R8 becomes the only route left.

### Status of our figures

Paper-side, first order, and cruder than R1's: 1-D isentropic area--Mach with a cone-average
`<cos theta> = (1 + cos theta_max)/2` rather than a flux-tube integral. Probes:
`todos/extension.py`, `todos/extension2.py`.

### Lifts

`sec:jet_efficiency`'s detachment claim, P3, P9's conditional, R1's divergence term, and possibly
R8 entirely.

---

## R12. We need `phi`, the share of the pulse's radiation emitted before the plume clears the exit

> **Answered by P21; accounting correction accepted in the paper review.** Use
> its integrated in-nozzle emitted energy directly, without another `phi` factor.
> These are original 4:1 water expansion results, not an adopted-nozzle or argon
> rerun. At 238 kg/pulse and 2 Hz, the maximum is 5.73 GW emitted, not absorbed
> liner power. Its own 56.53 km/s dissipated pulse energy gives 8.0%, not the
> 4.55% obtained using the 75 km/s denominator. Liner temperature and shield count
> do not follow from this integral alone. The text below records the original ask.

**Cheap: it is a quadrature over a file you already have.**

**Why.** R5 and our P4 work correct the liner's solid angle from the bag's "tenth of the sky" to
the bore's **82%** (ADR-0011's flared wall, 631 m^2 against 143 m^2 of open ends). But only
radiation emitted **while the plume is still inside** lands on the wall. Transit is a few
milliseconds and the plume radiates for far longer downstream, into nothing. **Every corrected
figure we have carries `phi` as a multiplier, and we cannot pin it from this side.** Your P5
quotes `t_rad/t` = 2.7 to 29 over the cooling history, which says radiation is spread through the
expansion rather than dumped at the start, so `phi` is likely well below 1. That is not a number.

**What is wanted.** From `data/results/cooling_history.csv`, the fraction of total radiated energy
emitted before the plume's leading edge passes the exit plane, per leg and per branch (frozen and
equilibrium). One number each.

**What it decides.** Four things, and the last is hardware:

| quantity | at `phi` = 0.2 | at `phi` = 1.0 |
| --- | ---: | ---: |
| liner load, hot 3.6% branch | 0.66 GW | 3.32 GW |
| against the 8.28 GW graphite ceiling | 0.08x | 0.40x |
| liner equilibrium temperature | 2076 K | 3105 K |
| **refractory shields needed in the liner/shell gap** | **none** | **3** |

On the equilibrium branch it is sharper still: `phi` = 0.2 wants 2 shields, `phi` = 0.5 wants 5,
and `phi` = 1.0 puts the liner itself at **4300 K, past graphite's 3900 K**, which is the only
case in this whole exercise where the passive-structure claim actually fails.

**Lifts.** The liner load in P4, the gate margin in P5, the ablation booking, and the shield stack
`sec:watering_it_down` will have to specify.

---

## R13. Everything on both sides has been computed for a water slug. `sec:watering_it_down` has an argon option that removes the binding constraint

> **Argon modeling remains open.** Argon removes water's molecular
> bond-dissociation term, but its ionization, recombination and radiative losses
> must be accounted for in its own plume history. No argon equation-of-state,
> expansion, radiation or conductivity calculation was imported in this review.
> The automatic `eta_chem = 1`, `eta_jet = eta_geom` and cold-leg clearance claims
> below are superseded. The paper's growth tables have not been recomputed for
> argon.

**Raised by the user, 2026-09-04, and it changes which quantity binds.**

`jet.py` charges `eta_chem` = 0.731 cold and 0.910 hot, our R1 inherited those, and your solved
expansion is water chemistry throughout. **The paper's argon slug pays neither toll**
(`sec:watering_it_down`, line 1074):

> A bare atom has no bonds to break, so the \SI{50.9}{\mega\joule\per\kilogram} goes away and so
> does the toll `eq:eta_chem` charges for it.

And the paper's `CONTEXT.md` is explicit that argon's **ionisation** is not a frozen toll either:
three-body electron-ion recombination goes as `n_e^2` with `alpha ~ T_e^-4.5`, giving nanoseconds
at 0.32 kg/m^3 against a ~100 us expansion, so the energy returns **inside the nozzle**.

**So `eta_chem` -> ~1 for argon, and `eta_jet` = `eta_geom` directly.**

| nozzle | `eta_geom` | water cold | water hot | **argon, both legs** |
| --- | ---: | ---: | ---: | ---: |
| no extension | 0.767 | 0.561 | 0.698 | **0.767** |
| extension 2.63x (10.9 m) | 0.928 | 0.678 | 0.844 | **0.928** |
| extension 7.45x (30.3 m) | 0.958 | 0.700 | 0.871 | **0.958** |

**The line that matters comes before any nozzle exists:**

    water, cold leg   eta_jet <= 0.731   -- below the paper's own 0.775 target
    water, hot leg    eta_jet <= 0.910
    argon, both legs  eta_jet <= 1.000

**The cold-leg shortfall in R1 and R11 is a water problem, not a nozzle problem.** No nozzle
reaches 0.775 on a 45.58 km/s water pulse, because the dissociation toll caps it at 0.731 first.
The paper says as much in the same passage: "Both of argon's gains therefore land on the leg where
water is weakest." **With argon the binding cold leg clears on the short 10.9 m extension**, and
R11's 30.3 m case is not needed.

### What is wanted

1. **`eta_chem` for argon, stated.** The paper argues the toll vanishes but prints no number, and
   the growth tables are charged from `eq:eta_chem`, which is water's.
2. **The argon plume's temperature and ionisation history.** 25 mol/kg against dissociated water's
   166, so the same energy has a sixth as many particles to share it. Further ionisation stages
   buffer the rise, so it is not the naive sixfold, but nobody has computed where it lands.
3. **The radiated share for argon**, against `tab:bag_sizing`'s 1.0--3.6% for water. **This is the
   one that could take the gain back.** Radiated power goes as `T^4`, and that share multiplies
   every liner-load and gate figure in R12: the shield count, the ablation booking, and P5's
   margin. A hotter plume may swap a chemical constraint for a thermal one.
4. **The field leak for argon**, against `tab:bag_state`'s 2.54% on the cold leg. Should improve:
   more ionisation, better `Rm`, and no recombination to wait for.

### What would settle it

Whether the growth tables should be recharged at `eta_chem` ~ 1, which moves every entry in
`tab:mass_interest_growth`, and whether R11's extension needs to be 10.9 m or 30.3 m.

### Lifts

The `eta_chem` half of R1 and R11, `eq:eta_chem`'s applicability, and the caption of
`tab:mass_interest_growth`, which states its chemical factor as "between 0.78 and 0.91 across the
rows that grow" without saying that is a water figure.

---

## R14. Column length and bag volume resolve in your favour. We adopt 23.8 m and 672.9 m³

> **Superseded 2026-09-05 by P20, accepted in the paper review.** The bag is now
> 660 m³ at aspect ratio four: length 23.7789 m, radius 2.97236 m, density
> 0.322727 kg/m³. [ADR-0014](adr/0014-bag-volume-fixes-the-column-geometry.md)
> records the rerun and its provenance. The historical adoption below explains
> the reply P20 corrects. The impact simulation's geometry artifacts have not been rerun.

Your answer document lists the column length as unreconciled and says to pick one. **We pick
yours**, and the paper now flies it end to end.

The paper *stated* 23 m and 660 m³, which give a 3.022 m bore and a 28.70 m² cross-section. The
prose around those statements *quoted* a 3.0 m bore, a 28 m² cross-section, and an aspect ratio
of 4. Those quoted figures are not roundings of the stated pair. They are your 23.8 m and
672.9 m³:

| | paper as stated | paper as quoted | sim, 23.8 m / 672.9 m³ |
| --- | ---: | ---: | ---: |
| bore | 3.022 m | "3.0 m" | **3.000 m** |
| cross-section | 28.70 m² | "28 m²" | **28.27 m²** |
| aspect `l/2r` | 3.81 | "4" | **3.97** |

**Three independent round figures the paper already prints match your pair, and none of them
match its own stated pair.** So the disagreement was internal to the paper and worth about 2% in
volume. Adopting yours fixes it in one move, rather than forcing a choice about which quoted
figure to break.

**What changed in the paper.** `tab:axial_bag`'s sweep volume goes from 660 m³ to 672.9 m³ and
every row is recomputed on it. The design row becomes 23.8 m at a 3.00 m bore with 449 m² of
membrane, against the 23 m / 3.02 m / 437 m² it printed before. The straggling "23 m" in the
needle-through-fog paragraph becomes 23.8 m, and the areal density the rod meets goes from
7.4 to 7.5 kg/m². Bag density is now 213/672.9 = 0.3165 kg/m³, still 0.32 to two figures, so
nothing quoting 0.32 moves. Also **`k` = 8.52, not 8.5** (213/25), with 8.5 kept as the round
figure.

**What we owe you, and it is a real one.** `tab:axial_bag` is generated by `make bag-state` in
`aim_is_all_you_need`, and we recomputed it **by hand** from the model its own caption states,
validating first by reproducing all five printed rows at 660 m³ before re-emitting at 672.9 m³
(`todos/bag_geometry_converge.py`). The generator has **not** been rerun, so the paper's table
and its generator now disagree. That sits alongside the `tab:bag_state` recompute already owed
for the ice-enthalpy defects (`todos/bag_state_recompute_2026-09-03.md`). **Both want one pass.**

**Nothing here is a physics claim about your run.** We are adopting your geometry because it is
self-consistent and ours was not. If your 23.8 m came from something we should be matching more
carefully than three round numbers, say so and we will re-derive rather than adopt.

---

## R15. Which surface is the standoff requirement written against, the liner or the bag bore?

> **Answered by P19 and accepted in the paper review.** ADR-0013 now adopts
> the liner criterion and an 11 T peak, using P18's constant 3.50 m contact
> surface as a conservative bound within its prescribed model. Existing 12 T
> winding and expansion results remain reference calculations. P19 also confirms
> that 5 T is bag-referenced standoff; whole-profile regrading remains deferred.
> The text below records the original request.

**Priority: high, and cheap to answer. It is one line of your existing geometry, not a run.**

Recorded as `docs/adr/0013`, which is **proposed rather than accepted** and waits on this item.

**The question behind it.** Asked paper-side whether a flare or a hybrid nozzle could buy a peak
field under ADR-0012's 12 T cap. The hybrid half answers itself and needs nothing from you: the
shelf height is the standoff demand at the station where the front first touches the wall, so the
peak is set upstream of anything a bell or a magnetic extension can reach. R8 and R11 cannot
lower it. **The flare half turns entirely on which surface "the wall" means, and that is yours to
settle.**

**What we found.** ADR-0012's cap table reads "wall at 3.02 m" at every station, which is
`eq:bore_from_length`'s bag bore. ADR-0011 puts the liner at 3.50 m flaring to 5.17 m. Reading
the same flown profile at the contact station against the liner instead:

| spreading | wall | contact | flown profile there |
| --- | --- | ---: | ---: |
| 1.9x bracket (the one that forced 12 T) | bag bore 3.02 m | 3.27 m | 11.75 T |
| **same, against the liner** | **3.50 m, flared** | **4.14 m** | **10.59 T** |
| sound speed | bag bore 3.02 m | 6.18 m | 8.87 T |
| **same, against the liner** | **3.50 m, flared** | **8.50 m** | **7.71 T** |

**ADR-0012 already answers this against itself.** Its own text says the field's job is *"wall
standoff. The field is there to keep plasma off the liner."* The table directly beneath that
sentence measures to 3.02 m. So the correction does not need a new argument, only a decision about
which of ADR-0012's two statements is the operative one.

**Our reading is that the liner is the right surface**, because the bag is 12 um of polyethylene
that vaporises in the collision and stands nothing off, and because the rest of this repository
already treats the liner as the wall (R12's 82% sky fraction and the 631 m^2 radiating area are
both taken over ADR-0011's flared bore). ADR-0012 is the one place still using the bag bore, and
it was written in the same session as ADR-0011 without picking up its flare. **We would rather
have you confirm that than adopt it on our own reading**, because it changes an accepted ADR.

### The two questions

1. **Is the standoff requirement written against the liner or against the mist column?** If the
   front has to be held inside the mist it is still sweeping, so that the coupling survives, then
   the bag bore is right, ADR-0012 stands as written, and ADR-0013 is void. If the requirement is
   only that plasma not reach the graphite, the liner is right. **This decides the whole item.**
2. **Does `k` = 7.2 survive the front expanding into the clearance gap?** The mist is inside the
   3.00 m bag and the bag does not flare, so expanding past it dilutes pressure without reducing
   swept mass. We read that as neutral to favourable. It is unverified, and it is the thing that
   would make question 1 come out the other way.

### A third question, only if the first two go our way

Does the standoff demand scale as `1/r` at fixed station? Nothing on either side has tested it.
ADR-0012's table varies `z` at fixed `r`, and our `1/r` comes from `p ~ E/V` with `V ~ r^2 z`.

It matters because it is the difference between a small correction and a large one. **Reading the
flown profile at a corrected contact station needs no radial scaling at all** and gives 10.6 T,
which is the version ADR-0013 proposes. Letting the whole profile follow the flared bore needs
`1/r` and gives **8.44 T**, with `A/A*` improving from 2.40 to 2.94 because the exit demand falls
faster than the peak. **We are not asking for that one yet**, because it drops the exit to 2.87 T
against P9's 5 T, and P9 calls the 5 T exit a collision requirement rather than a standoff one.
If P9's 5 T is in fact a standoff number evaluated at a 3.02 m bore, say so, and the larger
version comes back on the table.

### What would settle it

Question 1 is a statement of what your standoff criterion means, not a run. Question 2 is the
mass-versus-station profile at the end of the plow, which **R4 already asks you for** on other
grounds. Nothing new is being requested.

### Lifts

ADR-0013's conditional status, and with it about 1 T off the binding bracket and 1.3 T off the
sound-speed case, at no hardware cost. Also the conductor pricing in ADR-0011: if the field is
standoff-limited then tape runs as the integral of `B r` while demand runs as `B ~ 1/r`, the
product is bore-independent, and **the 1.18x to 1.50x we charged the flare is too harsh.** That
one is ours to correct, but it only bites if the liner is the wall.
