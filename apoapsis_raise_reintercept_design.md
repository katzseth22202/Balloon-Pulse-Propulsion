# Apoapsis-Raise Earth Re-Intercept — Design Document

**Status:** Locked design point for further iteration
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

For comparison, the paper's existing solar-dive two-impulse loop reaches a millionfold in ~17 years. This design is roughly **3× slower**, in exchange for ~5.2 km/s of total onboard-propellant Δv (vs. 24–37 km/s of PuffSat-boost impulse for the dive options) and no solar-proximity thermal/dust engineering.

## 6. Comparison to existing `sec:earth_reintercept` options

| Method | Closing speed | Cycle time | Millionfold | Needs |
|---|---|---|---|---|
| Two-impulse phasing loop (dive) | ~150 km/s | ~0.86 yr | ~17 yr | second PuffSat boost node off Earth |
| Single-impulse resonant dive | ~150 km/s | ~0.85–0.89 yr | slower than 17 yr (lower doubling factor) | only Earth boost node; heavier boost (~37.5 km/s) |
| Gravity-assist resonant return | ~150 km/s | ~1–2 yr | constrained by flyby timing | Venus/Earth flyby availability |
| **Apoapsis-raise re-intercept (this doc)** | **24.06 km/s** | **1.69 yr** | **~54 yr** | only onboard propellant (methalox + argon SEP); no solar dive, no gravity assist, no network node |

## 7. Open items / caveats for iteration

- **Low-thrust SEP burn approximated as instantaneous.** A real 2–3 month argon SEP burn sweeps only ~7–10° of true anomaly out of the ~250° total trip, and it happens during the slowest part of the orbit (near apoapsis), so the impulsive approximation is likely reasonable to first order. Not yet checked against a real low-thrust propagation; the precise Q needed for exact phasing could shift slightly once the burn is modeled as extended rather than a point kick.
- **Is 4 km/s a hard SEP ceiling, or a placeholder?** The optimum sits exactly at the boundary of the searched Δv₂ range. Worth checking whether pushing past 4 km/s continues to help, and if so by how much, before treating 4 km/s as load-bearing.
- **Burn direction idealization.** Both burns are assumed purely tangential. Real departure-asymptote geometry (patched-conic matching at Earth's SOI) may require a small non-tangential component; not yet checked against a full three-body or high-fidelity patched-conic model.
- **f = 0.8 fudge factor reused from the existing collision framework**, not re-derived for this lower closing-speed regime. The existing appendix notes f "varies with the relative PuffSat-rocket velocity" — worth checking whether 0.8 still holds at 24 km/s vs. the 150+ km/s regime it was calibrated against.
- **Not yet reconciled with the companion calculations repo** (`katzseth22202/aim_is_all_you_need`). All numbers above come from an ad hoc script in this session, not yet ported to tested code there.
- **Not yet decided:** where this lands in `templateArxiv.tex` (new subsection of `sec:earth_reintercept`, or its own appendix), and whether `tab:mass_scenarios` gets a new row.

## 8. Methodology notes (for reproducing the numbers)

- Units: AU and years, with `mu_sun = 4*pi^2 AU^3/yr^2` so that Earth's circular speed at 1 AU is exactly `2*pi AU/yr = 29.78 km/s`.
- `mu_earth = 398600.4418 km^3/s^2`, 200 km altitude → `r = 6578.137 km`, `v_esc200 = sqrt(2*mu_earth/r) = 11.0086 km/s`.
- Leg 1: purely tangential injection at r=1 AU with aphelion Q fixes `a1=(1+Q)/2`; `v_p1 = sqrt(mu_sun*(2/1 - 1/a1))`; `v_inf1 = v_p1 - v_E`; `Δv1` found via Oberth relation `v1_local = sqrt(v_inf1^2 + v_esc200^2)`, `Δv1 = v1_local - v_esc200`.
- Leg 2: at r=Q, tangential speed before burn `va1 = h1/Q` where `h1 = 1*v_p1`; after burn `va2 = va1 - Δv2` (AU/yr); new orbit elements from vis-viva/angular-momentum at (r=Q, v_r=0, v_t=va2); true anomaly and time-since-periapsis via the standard eccentric-anomaly relations to find the inbound r=1 AU crossing.
- Phasing residual: `(total_swept_angle - 360*total_time_yr) mod 360`, minimized over (Q, Δv2).
- Arrival relative velocity: craft's (radial, tangential) velocity at the 1 AU crossing minus Earth's (0, 29.78 km/s); `v_close200` adds the 200 km Oberth boost the same way as departure.
- Rocket-equation mass fractions: `exp(-Δv/(Isp*g0))`, `g0 = 9.80665 m/s²`.
- PuffSat-to-rocket ratio: `eq:PuffSat_ratio` from `sec:PuffSat_ratio_approximation`, `m_r/m_p = 2f/ln(v_p/(v_p-v_rf))`.
