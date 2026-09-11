# Prefer escape delivery with a periapsis disposal reserve

Status: accepted, 2026-09-11. Supersedes [ADR-0017](0017-near-term-disposal-with-high-apogee-staging.md).

Recommend Earth escape for near-term Earth-delivery PuffSats. Pay for inward
injection at the top of a long staging ellipse so the payload encounter occurs
at 200 km periapsis with horizontal inflow. The user prefers this delivery cost
to the expected cost of oblique pulse momentum and routine atmospheric disposal
of dry hardware. Removing downkick alone does not recover the forward impulse
lost to obliquity; the full economic comparison remains uncomputed.

The working Earth-only example starts from an ellipse with 200 km perigee altitude
and an apogee radius of 1,000,000 km from Earth's centre. An approximately
0.95 km/s inward injection gives a vacuum encounter speed 5 m/s above local
escape, corresponding to about 332 m/s hyperbolic excess. The coast after injection
is about 8.4 days. This is delivery propulsion, outside the cold-gas guidance budget.

After detachment and clearance of the rocket, each functioning hardware package
spends a reserved 10 m/s prograde near periapsis. Before drag and release losses,
the local margin becomes 15 m/s and hyperbolic excess becomes about 575 m/s.
Each detached package needs its own reserve and burn capability. Inbound drag
uses the intact PuffSat's mass and area; outbound drag uses the remnant's.

Successful injection establishes the initial escape trajectory even if the unit
subsequently fails. Failure before injection leaves a bound orbit whose 200 km
perigee guarantees neither escape nor prompt reentry. The user accepts injection
as part of normal delivery; the earlier requirement for passive atmospheric
disposal after any complete failure is superseded. Breakup fragments remain a
separate residual risk. Remote-ocean targeting applies to deliberate contingency
reentries. Successful escape removes routine dry-hardware reentry from the nominal
cycle, without eliminating environmental accounting for failures or propulsion material.

Choose encounter timing and orbital plane together to obtain the desired outgoing
solar orbit. Escape along or against Earth's solar motion changes the orbital
period, but does not establish a numerical re-encounter probability. Solar and
lunar perturbations matter at the staging distance. Thermal and delivery attitudes
can agree when the closing velocity is perpendicular to the Sun-line; outgoing
escape direction alone does not ensure this, because Earth bends the trajectory
by about 84–87 degrees between periapsis velocity and outgoing asymptotic velocity.

The existing 150,000 km guidance simulation and bound-orbit fare calculation
remain reference cases, explicitly distinguished from this delivery route. Their
numerical results do not include the new injection or establish its mission cost.


For spacecraft launches with flexible dates, retain planetary returns as an
alternative to direct delivery. A loaded PuffSat can burn at its first Earth
periapsis toward Venus or Mars and deliver on a later return. In an ideal
coplanar transfer estimate, starting 5 m/s above escape at 200 km takes about
274 m/s for Venus or 382 m/s for Mars. These are first-pass injection costs,
not a solved return trajectory. An illustrative 8 km/s Earth-return excess
would give 13.61 km/s at 200 km, about 2.60 km/s above the direct stream.
The paper does not claim that a 300 m/s burn produces that return excess;
flyby limits and Earth re-intercept phasing remain part of the trajectory solve.
Scheduled intercity flights retain the direct route.


The Moon is also a candidate for a partial assist: use its flyby to reshape the
outer arc and reduce a powered return correction, rather than assuming it can
reverse a near-escape outbound trajectory by itself. This is a timing-dependent
alternative, not a solved saving or a replacement for the escape recommendation.
The roughly 98 m/s disposal burn quoted for a lunar-distance bound ellipse is
only a comparison; a real flyby changes the return energy. A bound-return variant
would need active disposal after delivery and would lose passive escape on failure.
