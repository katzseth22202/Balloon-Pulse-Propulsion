# Survivable departure chamber: the charge per pulse, owed by `puffsat_impact_simulation`

**Answered 2026-10-08, sim `79e40d9`: the 117 kg is a 7000 K charge.** The reasoning below
assumed a fixed gas composition. At 0.55 kg/m^3 more of the methane is dissociated and ionized,
so a kilogram holds 115-120 MJ at 7000 K. Kept as the record of the question. Its first fix
printed "0.28 kg/m^3, ~46 bar"; sim `2491d15` corrected the row to ~0.55 kg/m^3 and ~95 bar.

Raised 2026-10-08, after `aim_is_all_you_need` @ `a45604d` answered S17
(`docs/survivable_chamber_for_parent.md`, its ADR 0044). **Written to be copied verbatim into
`katzseth22202/puffsat_impact_simulation`**, so it repeats context the paper repo already has.
Register item **S20**, `docs/deferred_to_companion_repos.md`. It joins S18 (the hydrogen
chamber) and S19 (gate, convergence, wall heat at 94 bar) from the same batch.

Same ground rules as before: neither document is the source of truth. If the reasoning here is
wrong, say so.

## S20. Is 117 kg of charge and plug per 5 kg pulse the intended charge, and at what temperature?

**Where the number comes from.** Your chamber note, `docs/walled_nozzle_chamber_blast.md` §3h,
gives the chosen configuration's carried mass as "~117 kg charge and plug (a 20 kg plug)", with
the basis "`near_term` at 106 m^3 x2". The same note says to keep the methane chamber at 7000 K
(§1 and §5: "10,000 K does not pay; keep 7000 K").

**Why that looks inconsistent.** The aim repo flagged it, and two hand checks agree:

| | sphere (the ledger's old chamber) | bulged chamber (§3h) |
|---|---|---|
| rod, impact energy at 75 km/s | 2.5 kg, 7.03 GJ | 5 kg, 14.06 GJ |
| charge + plug per pulse | 68.8 + 4.4 = 73.2 kg | 117 kg (97 + 20) |
| per rod kilogram (`k + P`) | 29.3 | 23.4 |
| impact energy per kilogram carried | 96 MJ/kg | 120 MJ/kg (+25%) |
| chamber, pressure | 20 m^3, 496 bar | 212 m^3, ~94 bar |
| pressure at the sphere's temperature, scaling `p ~ m/V` | | 75 bar |

The energy check says the charge takes 25% more energy per kilogram than the sphere's 7000 K
charge did. The pressure check says the same thing independently: at the sphere's temperature
and composition the bulged chamber would sit at about 75 bar, not 94. Read as an ideal gas,
94 bar is about 8,800 K. That reading ignores dissociation and ionization, so take the
temperature as rough, but both checks give the same +25%. Holding 7000 K would need
`k + P` = 29.3, about **146 kg** per 5 kg pulse.

**What the aim repo did with it.** It took 117 kg as given. With the gate charged, it
reproduces your 906 / 971 kN s (AR 100 / 300) at eta 0.488 / 0.539, effective Isp 788 / 845 s.
The AR 300 eta matches the sphere's solved 0.538, so the chamber law carries over. The ledger
rows are therefore consistent with your impulse figures. The open question is whether those
figures are for the chamber we meant.

**Wanted:**

1. Confirm which is intended: 117 kg at a hotter charge, or about 146 kg at 7000 K. If 117 kg,
   state the charge temperature in the bulged chamber.
2. **If 7000 K (~146 kg):** the net impulse per pulse at AR 100 and AR 300, head-on debit taken,
   and the pitch per pulse at that state.
3. **If hotter (~117 kg):** the wall heat and pitch at that temperature. The 3.5-24 kg pitch
   band was scaled from the 20 m^3 wall heat at 7000 K, and radiation rises as `T^4`, so the
   high edge is the number most exposed. Also say whether §5's reason for keeping 7000 K
   ("counting pitch it is no better per kilogram") still holds for this chamber.
4. Either way, the plug's share: is the 20 kg frozen methane plug (`P` = 4 per rod kilogram)
   heated as charge, or does it carry less of the energy than the gas?

**What moves.** The paper now prints the aim repo's rows built on 117 kg and 906 / 971 kN s,
with the 117 kg and its source stated in the text and this ask cited as open. A changed charge,
impulse or pitch goes back through `aim_is_all_you_need` as a rerun of S17
(`make survivable-chamber`, ~5 min). The direction is not obvious: more charge at 7000 K gives
more impulse per pulse but a lower Isp. So the paper does not guess which way the doubling time
moves.
