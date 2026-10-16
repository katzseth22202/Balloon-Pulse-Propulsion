# The solar-dive charge pusher in the paper: asks for `aim_is_all_you_need`

Raised 2026-10-16, while the paper adopts aim `127162f` (ADR 0072,
`docs/solar_dive_cycle_reply_for_sim.md`) as its lead growth cycle. **Written to be copied verbatim
into `katzseth22202/aim_is_all_you_need`**, so it repeats context the paper repo already has.
Register items start at **S27** (`docs/deferred_to_companion_repos.md`).

Same ground rules as your own handbacks: neither document is the source of truth. If a number
here looks wrong, say so rather than working around it.

**What the paper is doing.** It makes the solar-dive charge pusher the headline growth cycle, and
moves every finance table (chamber and methalox rows included) to ADR 0072's gated rNPV with 15
synodic periods of growth. `make solar-dive` was re-run in the sandbox at `127162f` and reproduces
the headline exactly (3.60 / 4.92 per 3S; $88 / $104 and $63 / $67 break-even). The paper will
print each depth's own seed price: $1297 / $4993 per kg at 9.86 R_sun, and $1423 / $5559 at
4 R_sun. ADR 0072's note gives only the first pair.

---

## S27. Charge the apoapsis methalox stage's engine and tanks

`fly_unit` step 3 (`src/solar_dive_growth.py:742`) burns 0.237 km/s of methalox at apoapsis
(0.211 at 4 R_sun). Almost all of it turns the orbit from the push axis to the thrust axis. Only
0.003 km/s is the 400 -> 600 km periapsis raise. That is 68.5 t (66.6 t) per departure-wave
unit, about 6% of the pushed stack. `lines["methalox"]` charges the propellant at $0.20/kg, but
no engine, tanks, pressurant or feed system is charged anywhere in the module (`grep -i
'raptor\|engine\|tank'` finds nothing).

The paper is going to say the loop needs "no new kind of nozzle": the only engine is a flown
methalox stage making a small turn in quiet orbit. It needs that stage priced, so the claim is
not made on an uncharged line.

Wanted:
1. The stage's dry mass (engine, tanks, structure) per unit, with its source. One sea-level or
   vacuum Raptor is the obvious first case; a smaller engine sized to the burn is the second.
2. Whether it is expended with the unit or recovered, and its price on the Estimate and
   Pessimistic books.
3. A deep-space correction reserve on the departing ship, which ADR 0072 also leaves uncharged.
   30-50 m/s of methalox on the ~640 t ship is ~5-8.5 t. The paper now gives it a second job: its
   methane is the buffer spray for an Earth-side abort (see the impact sim's ask on bare-sheet hits).
4. The headline re-run with the stage and the reserve charged: growth, doubling and both
   break-evens at both depths.

## S28. Can the push wave's aim shrink the apoapsis turn?

Nearly all of S27's burn is the rotation between the push wave's axis and the departure's
thrust axis. ADR 0072's push-wave route is solved on three knobs (excess, aim, climb-out excess)
against the clock, the Earth intercept and Jupiter's phase. Was the turn angle a cost in that
solve, or was the route solved first and the turn paid afterwards? If it was not in the
objective, what does the growth optimum look like once it is, and how small can the turn get
before Jupiter's phase or the Earth intercept binds? This is a curiosity. The paper does not
wait on it.

## S29. Does a smaller seed work?

`value_design` hard-codes the seed as one launch unit's departing ships: 676 t at 9.86 R_sun and
798 t at 4 R_sun, which is 4.4-5.0 and 5.7-6.6 stripped Starships, or $0.88-3.37B and
$1.14-4.44B of launch. (These come from `fly_unit`, `balance` and `seed_payload` at the
headline knobs. The paper's scratch reproduces your break-evens exactly. Please confirm them.)

Apart from the attrition and plate-batch learning curves, the ledger is linear in seed size. So
the break-even should barely move if the seed is cut, and the fleet should just reach a given
tonnage one or two cycles later. Wanted:
1. Is anything in the loop indivisible below one 1500 t launch unit (a minimum plate, a minimum
   wave that still arrives as one usable pulse, the carrier)?
2. The headline at both depths with a 1-ship and a 2-ship seed (about 150 and 300 t): break-even
   on both ends, the up-front bill, and the years until the fleet matches today's harvest.
3. The seed's dollars per fleet kg on the dear seed beside the cheap one in the report. ADR 0072
   prints only $21 / $7. The dear ends are $80 / $25.

## S32. A pessimistic book for the solar dive

`SolarDivePrices` has only `ESTIMATE`. The paper has always printed every architecture on an
Estimate and a Pessimistic book (`tab:delivery_ledger`, `tab:growth_prices`). For now it prints
the solar dive's two worst single levers in its place: the lob at $50/kg ($125 / $101 steady,
$166 / $116 dear) and the 20 g cap ($77 / $58 steady, $155 dear at 9.86 R_sun). Wanted: a
Pessimistic `SolarDivePrices` that sets every line at its evidenced worst at once, as
`growth_cost.PESSIMISTIC` does for the chamber. The paper would carry it as a labelled row. That
covers the plates at the spray cup's full curve with no learning, disks at $2000/kg or more,
avionics and shade at the dear end, polyethylene at fibre rather than resin prices, and the lob
at $53.2. Then the headline and the child's rows on it.

