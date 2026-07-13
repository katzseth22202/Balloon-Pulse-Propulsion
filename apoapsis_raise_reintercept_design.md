# Apoapsis-Raise Earth Re-Intercept — Design Document

**Status:** Locked design point for further iteration. The apoapsis SEP burn's impulsive approximation is now verified against a finite-thrust propagation (see §3).
**Date:** 2026-07-13
**Author context:** Seth Katz (paper author). Distilled from a grilling session exploring whether a high-speed Earth flyby is reachable without ISRU, gravity assists, or a close solar approach, as a candidate addition to `sec:earth_reintercept` in `templateArxiv.tex`.
**Intended home:** this paper repo, likely as a fourth phasing option alongside the two-impulse loop, single-impulse resonant dive, and gravity-assist return already in `sec:earth_reintercept`. Not yet folded into the paper text.

---

## 1. Purpose

Check whether a projectile can leave Earth, coast to a modest heliocentric apoapsis, take a single retrograde burn there, and fall back to intercept Earth at a closing speed useful for the PuffSat mass-doubling cascade, without:

- ISRU (no mined propellant along the way),
- a gravity assist (no trajectory-bending flyby of Earth, Venus, or Jupiter),
- a close solar approach (nothing near the 4–10 solar-radii dives of `sec:no_isru_rocket`).

This is a candidate **cheaper, simpler alternative for early bootstrapping**, before the PuffSat network is mature enough to support the deep-dive phasing options. It trades collision energy (25–35 km/s vs. 150+ km/s Earth-crossing speeds) for a much smaller total Δv budget and no solar-proximity engineering.

## 2. Trajectory shape

Three steps, all in-plane (no inclination change), patched-conic, impulsive-burn approximation:

1. **Depart Earth.** Start at 200 km altitude already moving at local escape velocity (`v_esc(200km) = 11.01 km/s`, C3 = 0, matching the interception-altitude convention already used elsewhere in the paper). A methalox burn at this point (Oberth maneuver, deep in Earth's well) adds Δv₁, raising the heliocentric orbit to a chosen aphelion Q with perihelion pinned at Earth's 1 AU.
2. **Retrograde burn at apoapsis.** At heliocentric distance Q, a second burn (argon solar-electric, purely tangential, retrograde) removes Δv₂ of tangential speed. This lowers the new orbit's semi-major axis and perihelion; Q remains an apsis of the new orbit since the burn has no radial component.
3. **Fall and intercept Earth.** The craft falls back inward on the new ellipse. It is intercepted at Earth (1 AU) during this inbound leg — the trajectory is truncated there. Any hypothetical continuation toward a lower perihelion is irrelevant; the craft never reaches it because the pusher plate consumes it at Earth.

All burns are assumed purely tangential; Earth's own orbit is treated as circular at 1 AU, 29.78 km/s.

## 3. Resolved decisions

**Success metric — closest-approach speed, not v∞.**
"Twice Earth's escape velocity" is measured as the local speed at 200 km altitude during the Earth encounter, `v_close200 = sqrt(v_inf_arrival^2 + v_esc200^2)`. This is a natural Oberth-style boost from passing close to Earth, not a trajectory-bending gravity assist, so it doesn't conflict with excluding gravity assists as a mission-design tool.

**Phasing — closed by tuning Q and Δv₂, not by extra loops.**
The literal nominal inputs (Q=3.0 AU, Δv₂=3.0 km/s) clear the speed bar but miss Earth's position by ~100° of heliocentric longitude. Phasing is closed by root-solving for (Q, Δv₂) pairs where the craft's total swept angle matches Earth's angular advance over the same transit time (mod 360°), the same method `sec:earth_reintercept` uses for the single-impulse resonant dive. Multiple resonances exist; we did not rely on waiting through extra heliocentric periods.

**No perihelion floor.**
Earlier concern about the post-burn orbit's implied perihelion (as low as ~0.46–0.50 AU in some solutions) is moot. The craft is intercepted at 1 AU; it never continues toward the Sun. "Without close solar approaches" is satisfied by construction, not by a distance constraint on an orbit the craft never completes.

**Role — early-bootstrap alternative, not a replacement.**
This sits alongside, not instead of, the existing `sec:earth_reintercept` options. Present it as a lower-Δv, lower-complexity, lower-closing-speed fourth option.

**Speed bar vs. cadence — the 2× bar is a design constraint, not the optimization target.**
A faster-cycling resonance exists that *misses* 2× escape velocity but still grows mass faster per year. We kept the 2× bar as a hard constraint per Seth's direction rather than dropping it, and searched for the best cadence subject to it.

**Aphelion is phasing-locked near 2.26 AU; the SEP budget sets closing speed, not orbit size.**
Raising Δv₂ does not shrink the orbit. Across the full single-pass search (Q ∈ [1.05, 3.2] AU, transit ≤ 4 yr), the only phasing-exact Earth intercept sits at Q ≈ 2.26 AU for both Δv₂ = 4 and 5 km/s, because the swept-angle-versus-time balance that closes phasing is dominated by the long leg-1 arc, which the apoapsis kick barely perturbs. The 2× closing-speed bar on its own would allow a sub-2-AU aphelion (down to ~1.74 AU at Δv₂ = 5 km/s), but no sub-2-AU solution also intercepts Earth. The only nearby phasing feature below 2 AU is an anti-phased (~180°) miss near Q ≈ 1.65 AU.

**Impulsive SEP burn verified against a finite-thrust propagation.**
A 2D finite-thrust integration (constant thrust, mass loss by the rocket equation, thrust held anti-velocity, burn centered on apoapsis) was compared to the instantaneous kick. A 60–90 day burn reproduces the impulsive result to within 0.3–0.7% in closest-approach speed, about 1 day in transit time, ~0.005 AU in the truncated perihelion, and under 1° in phasing. A 180-day burn stays within 2.8% on closing speed. The agreement holds because apoapsis is the slowest part of the orbit, so a 90-day burn sweeps only ~10° of true anomaly, and the velocity stays almost purely tangential across that arc, keeping anti-velocity thrust near-optimal throughout. Centering the burn on apoapsis is the one requirement. A burn that instead starts at apoapsis shifts the effective impulse time by about half the burn duration and throws phasing off by ~16° for a 90-day burn, which is then removed by centering the burn or by re-solving Q with the extended burn modeled.

**Collision debris is a reduced concern.**
Every PuffSat arrives well above Earth's escape velocity. The hyperbolic excess at SOI entry is 21.4 km/s and the close-approach speed at 200 km is 24.06 km/s, against an 11.01 km/s escape velocity. Fragments from the pusher-plate collision carry close to this bulk velocity, so all but those scattered by more than roughly 13 km/s in the collision leave Earth on hyperbolic paths rather than settling into bound orbits. Earth's gravity then deflects the departing spray, and on most approach geometries it is thrown into heliocentric orbits inclined off the ecliptic rather than back into Earth's orbital plane, so it does not linger where the next inbound PuffSats fly. Bound near-Earth orbital debris, the Kessler-type hazard, is therefore unlikely to accumulate from these encounters. A minority of fragments can still be scattered below escape speed, so near-Earth plate operations are not debris-free, only far less debris-prone than the raw collision energy would suggest.

**Positioning in the paper.**
Present this as the near-term, buildable member of the `sec:earth_reintercept` family, in the same comparison as the two-impulse loop, single-impulse resonant dive, and gravity-assist return, and distinguished as the only one that needs no gravity assist, no solar dive, and no second off-Earth boost node. The conclusion lists it as the near-term bootstrap option, stated honestly against the main solar-dive scenario: roughly 6× lower closing speed (24 vs. ~150 km/s) and about 3× slower to a millionfold (~54 vs. ~17 yr), in exchange for only ~5.2 km/s of onboard Δv from two flight-proven propulsion types and none of the solar-proximity thermal and dust engineering. Pair "easiest to build" with "slowest and f-contingent" wherever it appears, so it reads as the demonstrator that the solar-dive scenario is the prize beyond, not as the headline result.

## 4. Locked design point

Searched Q ∈ [2.0, 3.0] AU, Δv₂ ∈ [0.2, 4.0] km/s (SEP budget capped at 4 km/s), for phasing-exact solutions (residual < 0.3°) with total transit time ≤ 4 yr and `v_close200 ≥ 2×v_esc200`. The optimum sits at the Δv₂ = 4.0 km/s boundary — spending the full SEP budget helps — with Q root-solved for exact phasing.

| Quantity | Value |
|---|---|
| Aphelion Q | **2.258 AU** |
| Leg-1 semi-major axis a₁ | 1.629 AU |
| Step 1 burn Δv₁ (methalox, 380s Isp, at 200 km) | **1.202 km/s** |
| Methalox mass fraction retained | 0.724 |
| Step 2 burn Δv₂ (argon SEP, 2000s Isp, at apoapsis) | **4.000 km/s** (full budget) |
| SEP mass fraction retained | 0.816 |
| Combined dry-mass fraction reaching Earth | **0.591** |
| Implied perihelion of the (truncated) new orbit | 0.460 AU — not reached, see §3 |
| v∞ at SOI-entry (before Earth's well) | 21.394 km/s |
| **Closest-approach speed at 200 km (v_close200)** | **24.060 km/s** |
| 2× escape-velocity target | 22.017 km/s |
| Margin over target | 2.04 km/s (9.3%) |
| **Total transit time (Earth to Earth)** | **1.692 yr** |
| Phasing residual | 0.036° |
| Mass cap: 4-yr cycle | satisfied with 2.3 yr to spare |

## 5. Economics

Uses `eq:PuffSat_ratio` from `sec:PuffSat_ratio_approximation`: `m_r/m_p = 2f / ln(v_p/(v_p - v_rf))`, with fudge factor f = 0.8, v_ri = 0, v_rf = 11.0 km/s (Earth escape velocity, matching the departure condition for the next cycle), v_p = v_close200 = 24.06 km/s.

| Quantity | Value |
|---|---|
| m_r / m_p (new payload pushed to escape per kg of returning PuffSat) | 2.619 |
| **Net growth per cycle** | **1.5469× (+54.7%)** |
| **Cycle time** | **1.692 yr** |
| Cycles to a millionfold | 31.7 |
| **Time to a millionfold** | **≈53.6 years** |
| Doublings per year | 0.372 |

For comparison, the paper's existing solar-dive two-impulse loop reaches a millionfold in ~17 years. This design is roughly **3× slower**, in exchange for ~5.2 km/s of total onboard-propellant Δv (vs. 24–37 km/s of PuffSat-boost impulse for the dive options) and no solar-proximity thermal/dust engineering. Both the growth factor and the millionfold time assume f = 0.8 carries over to 24 km/s, which is the load-bearing caveat for the economics (see §7).

## 6. Comparison to existing `sec:earth_reintercept` options

| Method | Closing speed | Cycle time | Millionfold | Needs |
|---|---|---|---|---|
| Two-impulse phasing loop (dive) | ~150 km/s | ~0.86 yr | ~17 yr | second PuffSat boost node off Earth |
| Single-impulse resonant dive | ~150 km/s | ~0.85–0.89 yr | slower than 17 yr (lower doubling factor) | only Earth boost node; heavier boost (~37.5 km/s) |
| Gravity-assist resonant return | ~150 km/s | ~1–2 yr | constrained by flyby timing | Venus/Earth flyby availability |
| **Apoapsis-raise re-intercept (this doc)** | **24.06 km/s** | **1.69 yr** | **~54 yr** | only onboard propellant (methalox + argon SEP); no solar dive, no gravity assist, no network node |

## 7. Open items / caveats for iteration

- **Low-thrust SEP burn, impulsive approximation now verified (see §3).** Burn duration is not a binding constraint. Assuming lightweight mirrors concentrate the dilute sunlight at 2.26 AU (flux there is 19.5% of 1 AU, so about 5× concentration restores one sun on the cells, within flown concentrator ratios) onto panels delivering ~1 kW/kg of array-level specific power, the 4 km/s argon burn finishes in days to a few weeks. Even at a conservative 100 W/kg system specific power it finishes in ~1–2 months, inside the range where the finite-burn check agrees with the impulsive result and small against the 2.3-yr schedule margin. The 1 kW/kg figure is defensible as a collector/array number (ultralight membrane optics feeding concentrated cells), not as a full power-and-propulsion system number, since the PPU and radiators alone cap the system near a few hundred W/kg. Burn timing is insensitive to which of these holds.
- **The 4 km/s SEP budget is load-bearing, and was kept deliberately.** Pushing past it helps. At Δv₂ = 5 km/s the same phasing resonance (the aphelion moves only 2.258 → 2.264 AU, since phasing is anchored by the leg-1 half-period rather than the apoapsis kick) gives a 26.34 km/s closing speed and reaches a millionfold in ~45.5 yr instead of 53.6 yr, at the cost of a deeper 0.37 AU truncated perihelion and a lower 0.775 argon mass fraction. We kept 4 km/s to preserve this option's role as the lowest-closing-speed, gentlest-perihelion member of the `sec:earth_reintercept` set. The 5 km/s point is on file if a faster cascade is wanted later.
- **Splitting the departure burn was checked and gives only a marginal gain, so the locked point keeps the single methalox impulse.** Offloading the last ~700 m/s of the apoapsis-raise from the methalox Oberth burn to argon near the 1 AU perihelion lifts the combined dry fraction from 0.591 to 0.615 and trims the millionfold from ~53.6 to ~49.0 yr (about 9%). It helps at all because the methalox Oberth leverage here is only ~2.3× (v∞ = 5.28 km/s is already a large fraction of the 12 km/s local speed), while argon's Isp edge is 5.26×, so argon costs ~0.44× the propellant mass of methalox per unit apoapsis-raise. The cap near 700 m/s is set by the brief perihelion pass, not by power (that outbound burn needs only ~2.6 W/kg). Idealized as impulsive at perihelion; the real 2-month smear costs a few percent, so read ~49 yr as a slight floor. Marginal enough to leave out of the headline design point.
- **HET plus mirror hardware mass at 100 W/kg does not move the headline.** Sized by the 4 km/s apoapsis burn over 90 days (η ≈ 0.5), the power-and-thruster hardware is ~9% of the vehicle at apoapsis, about 11% of the mass arriving at Earth. It stays inside the existing ~0.59 dry fraction rather than adding to it, because the rocket-equation dry fraction is independent of what the dry mass is made of, and the returning PuffSat hits the plate as a unit, so its hardware delivers collision momentum like any other mass. The millionfold time is essentially unchanged. Only a parasitic accounting, where the hardware does not collide and must be preserved, would push it to ~74 yr, and that is the wrong model for a cascade that consumes each PuffSat every cycle. The real cost of 100 W/kg versus 1 kW/kg is engineering, roughly 9–14% of the vehicle as deployable arrays and mirrors to finish the burn inside the 60–90 day impulsive-valid window, not cascade speed. One qualifier: low-density membrane optics may couple momentum a little worse than dense mass, which folds back into the f caveat above.
- **Burn direction idealization.** Both burns are assumed purely tangential. Real departure-asymptote geometry (patched-conic matching at Earth's SOI) may require a small non-tangential component; not yet checked against a full three-body or high-fidelity patched-conic model.
- **f = 0.8 fudge factor reused from the existing collision framework**, not re-derived for this lower closing-speed regime, and it gates only part of the result. The orbital numbers stand on their own. The 24.06 km/s closing speed, the ~5.2 km/s onboard Δv, and the 1.69 yr cycle come from the trajectory and the finite-thrust check, with no dependence on f. What rides on f is the economics: the +54.7% growth per cycle and the ~54 yr millionfold both come from `eq:PuffSat_ratio` with f = 0.8. The existing appendix notes f "varies with the relative PuffSat-rocket velocity", and 24 km/s carries roughly 1/40 the specific collision energy of the 150+ km/s regime f was calibrated against, so f could shift materially. Until the impact sim covers this regime, treat the trajectory as firm and the doubling economics as provisional.
- **The apoapsis-raise technique may also cut the injection Δv for the main solar-dive scenario (qualitative, unquantified).** Sending a fresh round from 1 AU down to a 4 R☉ perihelion by one retrograde impulse near Earth is expensive, because it means killing most of Earth's ~30 km/s orbital motion at 1 AU (the 24–37 km/s of PuffSat-boost impulse the dive options assume). Raising apoapsis first and then lowering perihelion from that high apoapsis, the bi-elliptic idea, costs less total impulse for a perihelion this extreme, because at a large apoapsis Q the orbital speed is low, so the burn that drops perihelion to 4 R☉ there is small. The connection to this document is direct. The returning hypervelocity PuffSats reach 1 AU moving almost purely radially outward (only a few km/s of their ~150 km/s is tangential), and a radial-outward collision kick is exactly what raises apoapsis. So the expensive first phase is close to a free byproduct of the collision, and only the small apoapsis burn need be paid for, which lowers the mass fraction (or PuffSat-boost impulse) needed to launch each new round. Three caveats. Raising apoapsis is the automatic part, not cancelling the velocity; a purely radial kick cannot bring perihelion below ~0.5 AU on its own, so the angular-momentum-killing burn at apoapsis is still required, only small. The payoff is contingent on how efficiently the PuffSat magnetic nozzle couples that outward momentum into the payload, mirroring the f caveat above. And the large apoapsis excursion lengthens the cycle, trading doubling rate for Δv. No numbers yet; flagged for the same impact and orbital pass that revisits f.
- **Not yet reconciled with the companion calculations repo** (`katzseth22202/aim_is_all_you_need`). All numbers above come from an ad hoc script in this session, not yet ported to tested code there. This includes the split-departure and hardware-mass figures in the two bullets just above. Port them to the calc repo first, then cite that repo when this lands in the paper.
- **Placement resolved (see §3), layout detail still open.** This lands as the near-term option in the conclusion and as the low-infrastructure member of the `sec:earth_reintercept` comparison. Still open is whether it gets its own subsection or a short appendix.
- **Add a row to `tab:mass_scenarios` for this scenario.** The row scores the collision that boosts the next cycle, matching the table's existing columns: Rocket Final Velocity ~11.0 km/s (0 to Earth escape at the 200 km interception altitude, matching §5's v_rf; ≈11.2 km/s at the surface), PuffSat Velocity 24.06 km/s (the closing speed v_close200), Rocket Initial Velocity 0, and Rocket/PuffSat Mass Ratio 2.62 (`eq:PuffSat_ratio` at f = 0.8). The Scenario cell should describe the apoapsis-raise Earth re-intercept as the lowest-closing-speed member of the set and `\autoref` the section we write for it. Leave the `\autoref` target unresolved until that section exists, then point the row at it.

## 8. Methodology notes (for reproducing the numbers)

- Units: AU and years, with `mu_sun = 4*pi^2 AU^3/yr^2` so that Earth's circular speed at 1 AU is exactly `2*pi AU/yr = 29.78 km/s`.
- `mu_earth = 398600.4418 km^3/s^2`, 200 km altitude → `r = 6578.137 km`, `v_esc200 = sqrt(2*mu_earth/r) = 11.0086 km/s`.
- Leg 1: purely tangential injection at r=1 AU with aphelion Q fixes `a1=(1+Q)/2`; `v_p1 = sqrt(mu_sun*(2/1 - 1/a1))`; `v_inf1 = v_p1 - v_E`; `Δv1` found via Oberth relation `v1_local = sqrt(v_inf1^2 + v_esc200^2)`, `Δv1 = v1_local - v_esc200`.
- Leg 2: at r=Q, tangential speed before burn `va1 = h1/Q` where `h1 = 1*v_p1`; after burn `va2 = va1 - Δv2` (AU/yr); new orbit elements from vis-viva/angular-momentum at (r=Q, v_r=0, v_t=va2); true anomaly and time-since-periapsis via the standard eccentric-anomaly relations to find the inbound r=1 AU crossing.
- Phasing residual: `(total_swept_angle - 360*total_time_yr) mod 360`, minimized over (Q, Δv2).
- Arrival relative velocity: craft's (radial, tangential) velocity at the 1 AU crossing minus Earth's (0, 29.78 km/s); `v_close200` adds the 200 km Oberth boost the same way as departure.
- Rocket-equation mass fractions: `exp(-Δv/(Isp*g0))`, `g0 = 9.80665 m/s²`.
- PuffSat-to-rocket ratio: `eq:PuffSat_ratio` from `sec:PuffSat_ratio_approximation`, `m_r/m_p = 2f/ln(v_p/(v_p-v_rf))`.
