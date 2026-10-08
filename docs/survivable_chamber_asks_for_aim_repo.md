# Survivable departure chamber: recompute owed by `aim_is_all_you_need`

Raised 2026-10-08, applying `puffsat_impact_simulation` @ `69d1f40` (its chamber note
`docs/walled_nozzle_chamber_blast.md` §1, §3e-§3h, §5, and the plate handoff P10/P12) to the
paper. **Written to be copied verbatim into `katzseth22202/aim_is_all_you_need`**, so it repeats
context the paper repo already has. Register items **S17-S18**, `docs/deferred_to_companion_repos.md`.
Paper-side record: `docs/adr/0027-the-departure-chamber-bulges-and-wraps-dry.md`.

**What the paper did already.** It describes the new chamber (`sec:chamber_shape`,
`sec:dry_wrap_wall`, `sec:one_chamber`, `tab:one_chamber`). It does **not** change any ledger,
cost or seed number. Every growth and cost table still prices the old chamber, and the text now
says so in `sec:growth_ledger` and `sec:heat_shield_bill`. The author's call: "flag, don't change"
until this recompute lands.

Same ground rules as your own handbacks: neither document is the source of truth; if a number
here looks wrong, say so rather than working around it.

---

## Why the chamber changed

The impact sim solved the blast inside the near-term methane chamber with the rod and plug as
material. The 4.4 kg polyethylene plug lets the merged body hit the nose at 5-6 GPa, and the
stopped rod is a line blast, `p ~ (E/L)/R^2`, that no cushion softens. The bonded carbon overwrap
your ledger charges (19 t methane, 32 t hydrogen per 2.5 kg chamber) delaminates under the spike
everywhere. What survives one departure:

| item | old (ledger now) | new (impact sim §3h, decided 2026-10-08) |
|---|---|---|
| rod per pulse | 2.5 kg | **5 kg** |
| rate | 4 Hz | **2 Hz** (4 Hz cannot refill) |
| chamber | 20 m^3 sphere, 496 bar | **212 m^3 bulged** (r 3.0 m bulge x 2^(1/3)), ~94 bar, throat 1.33 m^2, `V/A*` 160 m |
| plug | 4.4 kg polyethylene foam (`P` = 1.76) | **20 kg frozen methane in a polyethylene can** (`P` = 4 per rod kg); comes out of the charge |
| wall | 19 t bonded overwrap (CH4) | **48.2 t** dry Kevlar 49 over a 10 mm Cr-Mo shell (fallback 68.8 t maraging band) |
| extension | 2.19 t at 8.7 m exit (AR 300) | **4.9 t** (AR 100, 13.0 m) / **14.7 t** (AR 300, 22.5 m), your 2.19 t scaled by exit area |
| carried per pulse | 68.8 kg charge + 4.4 kg plug + 1.4-5.6 kg pitch, per 2.5 kg | **~117 kg** charge + plug, **+3.5-24 kg** pitch, per 5 kg |
| net impulse per pulse | (from eta at 20 m^3) | **906 / 971 kN s** (AR 100 / 300), head-on debit taken |
| effective Isp | 762-777 s (AR 300, gate) | **788 / 845 s** (AR 100 / 300) on charge + plug |
| departing stack | 100 t in `tab:wall_pairing_doubling`; 500-600 t in the ledger | **500-600 t** |
| pulses per departure | 630-780 | **~2,000-2,650** five-kilogram pulses, 16-21 min |
| finite-burn loss | fixed-direction loss scaled by burn time^2 | **+3.1-4.8%** of the 5.43 km/s burn (constant thrust along the velocity, 600 km periapsis, net thrust 1.81-1.94 MN) |

Hardware per stack: ~53-63 t (wall + extension), about a tenth of the stack. Pitch per departure
is 7-60 t between the wall-heat edges.

## S17. Recompute the growth ledger, cost book and seed with the survivable methane chamber

Wanted, in this order:

1. **Methane chamber rows** with the table above: 48.2 t wall, 4.9 / 14.7 t extension, 117 kg
   charge+plug per 5 kg rod, the pitch at both edges (3.5 and 24 kg), Isp_eff 788 / 845 s or the
   eta that reproduces 906 / 971 kN s, 2 Hz, and the finite-burn loss **charged**, not scaled.
   Does the ledger charge a finite-burn loss for the departure at all? The impact sim's note says
   it "does not appear to"; please confirm.
2. **AR 100 against AR 300.** AR 300 is worth ~5% impulse but costs ~10 t more extension and a
   22.5 m exit. Which wins in doubling time?
3. **Redundancy.** One 5 kg chamber (48.2 t) against two 2.5 kg chambers (49.8 t on the same
   0.25 cm history, plus a second extension, port, plug feed and membrane set). The paper takes
   one chamber; confirm the ledger agrees, or say by how much two would lose.
4. **Lead with methane.** The impact sim has not shown the hydrogen chamber's wall survives
   (S18). Keep the hydrogen rows if you like, labeled "wall unverified", but make methane the
   headline in `tab:growth_ledger_doubling`, `tab:growth_ledger_ten_year`, the cost book
   (`tab:growth_prices`, `tab:l1_comparison`, `tab:delivery_ledger`) and the seed tables
   (`tab:seed_return`, `tab:seed_amortization`, `tab:plate_designs_cost`). The paper currently
   headlines "solved hydrogen" in about 14 places; it will reorder those when your rows land.
5. **Make targets** for every new cell, as S11/S14 did.

The rows `tab:wall_pairing_doubling` (100 t, 630-780 pulses, 20 m^3) and
`tab:rod_2p5kg_doubling` can stay as the record of the sphere, or be rerun on the 500-600 t
stack. Say which you prefer.

## S18. Hydrogen chamber at this pulse size (puffsat_impact_simulation, for reference)

Not yours, listed so the two repos see the same register. The impact sim owes: the hydrogen
chamber (5500 K, 818 bar at 20 m^3) run with the rod and plug as material, the bulge and the dry
wrap; and whether a bonded copper liner survives the spike at all. Until then the paper calls the
hydrogen chamber unverified and proposes methane.
