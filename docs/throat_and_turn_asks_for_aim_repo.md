# A wider throat, and the Earth turn on the flown chain: asks for `aim_is_all_you_need`

Raised 2026-10-13, applying aim `9ade857` (`docs/orbit_turn_for_parent.md`, ADRs 0045, 0049,
0052, 0053) to the paper. **Written to be copied verbatim into `katzseth22202/aim_is_all_you_need`**,
so it repeats context the paper repo already has. Register items **S24-S25** (S24's impulse waits on **S26**, asked of the impact sim),
`docs/deferred_to_companion_repos.md`.

Same ground rules as your own handbacks: neither document is the source of truth; if a number
here looks wrong, say so rather than working around it.

**What the paper did already.** It takes item 2 of `orbit_turn_for_parent.md` (Earth turns the
vehicle through head-on) and the arrival-angle half of item 1 (only one mirror is visible; 164.5
deg on the circular 3S return). It prints 164.5 with the circular model named, keeps the 2S
160.6 as the chain's figure, and cites S25 below for both. It does **not** adopt a wider throat,
the miss-safety floor (item 3), recycling (item 7), slush (item 8) or the pulse-rate framing
(item 9) yet. Item 1's efficiency point (a pulsed chamber gets about `1/sqrt(gamma)` of a steady
NTR's exhaust at the same temperature) changes no number the paper prints, because
`eq:eta_isp` already budgets internal energy, so the paper leaves it alone.

---

## S24. Price a wider throat for the survivable methane chamber

### The parent's first reading, and why it was incomplete

The parent first argued against a wider throat. At a fixed exit, a wider throat is a smaller area
ratio, and a smaller area ratio returns less of the energy held in broken bonds. The paper's own
`tab:wall_pairing_doubling` shows the cost: methane falls from 762-777 s at A/A* 300 to 612-623 s
at A/A* 14. Your ADR 0049 makes the same point the other way round: the wide throat only came free
at 3000 K, where hydrogen holds about 2% of its energy in bonds, and ADR 0052 shows that chamber
does not grow.

Seth's objection is that the bulged chamber is a different gas. **Your S20 answer** (sim `79e40d9`,
recorded 2026-10-08) found that at the 212 m^3 chamber's lower density more of the methane is
dissociated and ionized, so each kilogram holds 115-120 MJ at 7000 K against 93 MJ in the 20 m^3
sphere. And the survivable chamber's solved AR 300 efficiency, eta 0.539, matches the sphere's
0.538 (`survivable_chamber_for_parent.md` item 3). So the nozzle returned the larger bond store
at least as well as before. If you concluded anywhere that recombination *improved* in the bulged
chamber, please point to it; the parent found only these two results.

### What has never been varied

**Both of ADR 0044's nozzles share one throat.** AR 100 is a 13.0 m exit and AR 300 a 22.5 m
exit, both over the 1.33 m^2 throat (`pi 6.5^2 / 1.33 = 99.8`, `pi 11.25^2 / 1.33 = 299`). Both
fly 2 Hz. So "AR 300 beats AR 100 by 0.28 yr" is a statement about the exit, not the throat. The
throat is the one knob that sets the pulse rate, and no row has moved it.

ADR 0053's blowdown goes as `V / (A* a)`. Doubling the throat to 2.66 m^2 halves the time to fill
pressure, from 278-336 ms to **139-168 ms**. A 250 ms period then leaves **82-111 ms** for the
films, plug, fill and lock, against 164-222 ms at 2 Hz now. Your hydrocode ask puts doubling the
rate at about 10% in growth per cycle, mostly through a burn that falls from 24-37 min to about
12-19 min.

There are two ways to widen the throat, and they pay in different currencies:

| option | throat | exit | A/A* | what it costs |
|---|---:|---:|---:|---|
| (a) same exit, lower ratio | 2.66 m^2 | 22.5 m | 150 | bond energy not returned |
| (b) same ratio, larger exit | 2.66 m^2 | 31.9 m | 300 | extension ~29.5 t against 14.7 t (your 2.19 t scaled by exit area, as ADR 0044 did) |
| (c) smaller chamber, same throat | 1.33 m^2 | 22.5 m | 300 | the wall at 106 or 53 m^3 (ADR 0053; open with the impact sim) |

### Why (b) might return more bond energy, not less

Recombination in the nozzle is mostly three-body, so its rate goes roughly as density squared.
That is the catch in S20. The thinner gas holds more energy in bonds and is slower to give it back.
What sets how much comes back is the gas's time in the dense part of the nozzle against the
recombination time. At a fixed area ratio and wall angle, nozzle length scales with throat
diameter. Option (b) therefore gives the flow about `sqrt(2)` = 1.41 times longer at each density
on the way out. It could return more than AR 300 does today. Option (a) cuts the expansion short
and should return less. The parent cannot rank them. The 0.669 ceiling (52% returned at AR 300,
carbon in equilibrium) was set on the sphere's density, and this is a kinetics question.

**Added 2026-10-13: the size of the gap.** The sphere's charge was about 3.4 kg/m^3 and the bulged
chamber's about 0.55, so recombination runs about 40 times slower at the same point in the
expansion. Option (b)'s `sqrt(2)` of extra time does not close that, unless the sphere had time
to spare. Every methane eta the paper prints is a limit, frozen or equilibrium
(`tab:nozzle_area_ratio`), not a finite-rate solve. The rate question belongs to the impact sim
and is asked there as **S26** (`docs/throat_kinetics_asks_for_impact_sim.md` in the paper repo).

### Wanted

1. **The cycle.** ADR 0053's timing table for options (a) and (b) at 2, 3 and 4 Hz: time to fill
   pressure and time left in the period. Say which rates fit.
2. **The impulse.** eta for (a) and (b) comes from S26, not from here. Until it lands, fly both
   options at the two limits, carbon in equilibrium and carbon frozen, scaled from the impact
   sim's A/A* sweep, and label each row with its limit. Do not quote an equilibrium-only row as
   the answer.
3. **The ledger.** Doubling, steady $/kg and break-even for (a) and (b) at every rate that fits,
   behind the spray cup with the film carried, at 24 kg pitch, next to the 2.76 yr / $162 headline.
   Charge the finite-burn loss as ADR 0032 does, integrated, in the fixed direction.
4. **The films.** The throat film carries `pr/(2t)`, so a throat with `sqrt(2)` the radius needs
   `sqrt(2)` the film thickness. Note it if the film's mass or burst timing changes the cycle.
5. **Hydrogen, if cheap.** The 5500 K sphere at 4 Hz has 115 ms left (ADR 0053), which is tight.
   The same `V / A*` scaling would open slack there. One row is enough.

The paper will not print a wider throat until this lands. If neither (a) nor (b) beats the
headline, say so, and the paper will say why in one sentence.

---

## S25. Check the Earth turn on the flown chain, at the chamber's own burns

Your `orbit_turn_for_parent.md` items 1-2 run on the **circular** 3S return, at a 20-minute burn
and the reference loading `k` = 3 (`REFERENCE_SLUG_RATIO`, collimation 0.8, 11 km/s reference
exhaust). The paper's angles came from the flown chain. The paper now prints:

- 164.5 deg on the circular 3S return, labelled as such, in place of the chain's 150.4 deg, which
  used the occulted mirror;
- 160.6 deg for the 2S cycles, from the chain, **not yet checked for occultation**;
- 19.8 to 11.7 deg off head-on over a fixed-direction, periapsis-centered burn, worth 0.3% of
  delivered mass at `k` = 3, and "less at the chamber's own loading".

Wanted:

1. **Visibility on the flown chain.** For each of the eleven flown cycles (seven 2S, four 3S), the
   arrival angle on the visible mirror at the 600 km burn, and whether the other mirror is
   occulted. In particular, does any 2S cycle's 160.6 deg come from an occulted mirror?
2. **The turn at the chamber's burn.** The off-head-on range and the delivered-mass gain over
   exactly head-on, for the survivable methane chamber's 24-37 minute burns at its own `k + P`
   of about 23 (`tab:one_chamber`). The paper says the gain falls with loading. Confirm it, or
   give the number.
3. **The old figures.** The paper used to say head-on "misstates the delivered mass by 0.9% and
   0.5%" (3S, 2S). Say which loading those were at, so the paper can retire or keep the 2S 0.5%.

The miss-safety floor (item 3) is not asked here. The paper has not taken it, and its 7.3% was
run only on the 3000 K model, as your handback says.
