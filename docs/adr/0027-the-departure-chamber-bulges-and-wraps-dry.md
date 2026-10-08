# The departure chamber bulges at its plug and wraps dry; the plate face takes an alumina barrier

Status: accepted (2026-10-08). Amends the near-term chamber of `sec:methane_7000_near_term` and
ADR 0025's plate face. Paper: `sec:chamber_shape`, `sec:dry_wrap_wall`, `sec:one_chamber`,
`sec:chamber_assembly`, `sec:chamber_wall_tests` (new); `sec:material_chamber_plug`,
`sec:steel_chamber_service`, `sec:carbon_overwrap`, `sec:rod_2p5kg`, `sec:port_gate`,
`sec:methane_7000_near_term`, `sec:spray_cup_skirt`, `sec:spray_cup_pressure`,
`sec:growth_ledger`, `sec:heat_shield_bill`; `fig:chamber_bulge` (new), `fig:methane_wall_detail`,
`fig:plate_stack`; `tab:dry_wrap_zones`, `tab:one_chamber` (new).

## Context

`puffsat_impact_simulation` @ `69d1f40` solved the blast inside the near-term methane chamber
with the rod and plug as material (its `docs/walled_nozzle_chamber_blast.md`), and the plate
face's fatigue, spall and hydrogen exposure (`docs/argon_plate_owed_to_companions.md` P10/P12,
`docs/spray_plate_fatigue_and_spall.md`). The 4.4 kg plug sends a 5-6 GPa hammer into the nose;
the stopped rod is a line blast, `p ~ (E/L)/R^2`, that no cushion softens; the paper's bonded
overwrap peels under the spike everywhere; solid Cr-Mo cracks in hydrogen at the plug band in
30-660 pulses. The paper's 100 t / 630-780-pulse departure disagreed with the ledger's 500-600 t
stacks.

## Decision

1. **Rewrite in place** (author's choice over a superseding subsection or a hold). Superseded
   designs shrink to a sentence on why they failed.
2. **Chamber:** domed head r 1.4 m, bulge to r 3.0 m at the plug (z 1.4-2.8 m, opened over 0.5 m,
   closed by a 3 m taper), 12 deg cone; 106 m^3 per 2.5 kg of rod. Plug: 10 kg frozen methane in a
   polyethylene can per 2.5 kg of rod. Wall: 10 mm Cr-Mo shell under a dry Kevlar 49 wrap, alumina
   film under the pitch as defense in depth. Fallback: maraging 300 band behind the barrier at
   r 2.6 m.
3. **One 5 kg chamber at 2 Hz** (the companion's 2026-10-08 decision, accepted): 212 m^3, 48.2 t
   wall, 53-63 t hardware, 500-600 t stacks, 2000-2650 pulses, +3-5% finite-burn loss.
4. **Methane is the proposed chamber; hydrogen is unverified** (author's choice). Hydrogen's
   centred spike is ~2.95 GPa and its wall has not been run with the bulge or wrap (S18).
5. **Ledger and cost tables are flagged, not changed** (author's choice) until S17 lands. Landed 2026-10-08; see ADR 0028. The
   business-case hydrogen-first ordering is left for that pass.
6. **Plate face:** maraging 300 only (K_Ic 66.5 vs 33); the merge is a structural requirement
   (failed merge detected and stopped within a few pulses; face rise >= one ~10 us round trip);
   sub-micron alumina barrier on floor and skirt liner; A-286 / NASA-HR1 / 718 as the fallback at
   the cost of fault tolerance.
7. **New citations**, where the companion gave none: Levchuk 2004 and Nemanic 2019 (alumina
   barrier), Mescheryakov 2017 (maraging spall), Lin 1954 (line blast), Kinney & Graham 1985
   (cube-root scaling), Gourdin 1989 (ring expansion), Rogers Commission 1986 (segmented SRM
   joints). Kevlar 49's 2.4% break from the existing DuPont guide entry.

## Consequences

- `sec:port_gate` now says the gate's case is open in the bulged chamber (open-port leak ~2%).
- `fig:chamber_bulge` is generated from the companion's contour (`simulations/chamber_bulge/gen_bulge.py`; volume reproduces 106.05 m^3).
- Asks S17 (aim: ledger with the new chamber, methane headline), S18 (impact sim: hydrogen wall),
  S19 (impact sim: gate, convergence, wall heat) go back to the companions.
