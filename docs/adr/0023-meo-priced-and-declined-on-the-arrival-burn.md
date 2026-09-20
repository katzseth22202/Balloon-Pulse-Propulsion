# Medium Earth orbit is priced and declined on the arrival burn, not on radiation or battery mass

Status: accepted (2026-09-20 grill). Recorded because a later reader will ask why a section
that sends a data center 1.5 million km out skips the obvious middle ground, where the round
trip to Earth is 147 ms instead of 10 seconds.

Medium Earth orbit is the strongest objection to a libration-point site, and the section used
to leave it unanswered. It wins the latency comparison outright. It also takes most of the
deterrence the section buys with distance, because a vertical lob to 22,000 km needs
9.84 km/s against 11.01 km/s for escape, which on solid propellant at 250 s is 14 times the
low-orbit mass ratio against escape's 22. An unanswered reader closes that gap themselves and
concludes the paper overshot.

The objection was priced rather than waved off, and two of the three obvious rebuttals were
rejected in the process.

**The eclipse battery does not decide it.** No orbit above about 5,974 km altitude can be
sun-synchronous, because the J2 nodal drift that holds a dawn-dusk plane on the terminator
falls off as roughly `a^(-7/2)` and at 22,000 km supplies 0.054 deg/day against the
0.9856 deg/day the Sun demands. So a medium orbit carries a 56-minute eclipse 114 times a
year, and a 5 GW cluster riding it needs about 31,000 t of battery at 200 Wh/kg pack and 80%
depth of discharge. That is a large number in isolation. It is only 2.8 times what the
dawn-dusk low-orbit baseline already needs for its 20-minute eclipse, and in a paper whose
thesis is that delivered mass gets cheap it reads as a quote rather than a refusal.

**Radiation does not lead it.** 22,000 km sits at 4.45 Earth radii, inside the outer electron
belt that peaks between 4 and 5, which both distant sites clear. That much `li2019vanallen`
will carry, and it is already cited at line 707. It will not carry a dose figure, and no MEO
dose source is in `references.bib`. Printing rad/year at MEO would need a citation that clears
the bar, so the belt is stated qualitatively and does not decide the case.

**The arrival burn decides it.** The arrival burn is the delta-V a payload supplies itself at
its destination, beyond the perigee push PuffSats deliver at the 200 km interception altitude.

| Destination | Arrival burn | Propellant at Isp 320 s |
|---|---|---|
| Sun-Earth L1 halo insertion | 30 m/s | 1.0% |
| LEO 650 km, perigee raise after aerobraking | 140 m/s | 4.4% |
| Earth-Moon L4/L5 (line 693) | 180 m/s | 5.6% |
| **MEO 22,000 km** | **1,449 m/s** | **37.0%** |

Sun-Earth L1 is cheaper to arrive at than low orbit, by 4.7 times. Every input is already
printed in the paper, so the comparison needs no new source and a reader can check it with a
calculator.

The section states the shape of that curve, not just the point, because the burn is not
monotonic. Arrival is cheap only where the air stops you or where gravity has already stopped
you, and the middle of the range gives neither, so the burn peaks at 32,300 km altitude where
apogee is 5.88 times perigee. Medium orbit is therefore near the worst altitude available
rather than merely worse than the two endpoints. Showing the point alone invites the reader to
propose 40,000 km, or 80,000 km, which is where the grill went before the curve was computed.

## Consequences

- A high circular orbit at 80,000 km escapes the belts, needs no battery (6.7 eclipses a year,
  99.92% availability) and answers Earth in 534 ms, but still costs 1,340 m/s to arrive at. It
  is covered by the trough argument and is not named as a site.
- The latency concession is deliberate. MEO does win it, and the section's own argument is
  that the target customers tolerate Earth-customer latency, so winning it buys little.
- Do not re-open this on the 31,000 t battery figure. It was computed, compared against the
  low-orbit baseline, and judged a price rather than a disqualifier.
