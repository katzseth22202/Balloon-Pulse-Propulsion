# Recombination rates in the bulged chamber's nozzle: owed by `puffsat_impact_simulation`

Raised 2026-10-13, alongside S24 to `aim_is_all_you_need`
(`docs/throat_and_turn_asks_for_aim_repo.md`). **Written to be copied verbatim into
`katzseth22202/puffsat_impact_simulation`**, so it repeats context the paper repo already has.
Register item **S26**, `docs/deferred_to_companion_repos.md`.

Same ground rules as before: neither document is the source of truth; if a number here looks
wrong, say so rather than working around it.

---

## S26. Solve the nozzle with finite reaction rates at the bulged chamber's density

### Why it is asked

The survivable methane chamber empties too slowly for more than 2 Hz (aim ADR 0053). Blowdown
goes as `V / (A* a)`, and the exit does not enter it. So a wider throat with a proportionally
wider exit should empty faster at the same area ratio. Doubling the 1.33 m^2 throat to 2.66 m^2
halves the time to fill pressure, from 278-336 ms to 139-168 ms. At A/A* 300 that needs a
31.9 m exit. S24 asks the aim repo to fly it through the ledger. What the aim repo cannot supply
is whether the nozzle still returns the energy held in broken bonds.

Your S20 answer is why that matters. At the bulged chamber's ~0.55 kg/m^3 the charge holds
115-120 MJ/kg at 7000 K, against 93 MJ/kg in the 20 m^3 sphere, because the thinner gas is more
dissociated. That larger bond store becomes thrust only if the fragments rejoin in the nozzle.
Rejoining is mostly three-body recombination, so its rate goes roughly as density squared.

The sphere's charge was 68.8 kg in 20 m^3, about 3.4 kg/m^3. The bulged chamber is about 6.3
times thinner, so recombination runs about **40 times slower** at the same point in the
expansion. At a fixed area ratio the nozzle passes through the same density ratios. Doubling the
throat at a fixed area ratio lengthens the nozzle by `sqrt(2)`, so the gas gets about 1.4 times
longer at each density. That does not close a factor of 40, unless recombination is fast enough
that the sphere had time to spare.

### What the paper prints now

`tab:nozzle_area_ratio` reports methane's eta between two limits: carbon frozen at its chamber
state, the floor, and carbon in equilibrium. Its "bond energy recovered" is computed at
equilibrium. The 0.669 chemistry ceiling the aim ledger uses (52% of the bond share returned at
A/A* 300) is the equilibrium figure. No finite-rate solve exists. The bulged chamber's net impulse,
906 / 971 kN s at A/A* 100 / 300 (your section 3h, eta 0.488 / 0.539), does not say which limit
it took.

### Wanted

1. **Which limit is 0.539?** Say whether the bulged chamber's 971 kN s at A/A* 300 assumes
   equilibrium, frozen, or something between.
2. **A finite-rate expansion.** Quasi-1D is enough. Solve the bulged chamber's peak state
   (7000 K, ~0.55 kg/m^3, ~94 bar) through A/A* 300 with finite-rate carbon and hydrogen
   recombination, for three nozzles:
   - today's 1.33 m^2 throat, 22.5 m exit;
   - (a) a 2.66 m^2 throat on the same 22.5 m exit, A/A* 150;
   - (b) a 2.66 m^2 throat on a 31.9 m exit, A/A* 300.
   Report eta and the share of the bond energy returned, beside the equilibrium and frozen
   values for the same nozzle.
3. **The sphere, for calibration.** The same finite-rate solve for the 20 m^3 sphere's state
   (~3.4 kg/m^3, 496 bar) at A/A* 300. If it lands near equilibrium and the bulged chamber does
   not, the density is the cause.
4. **The wall angle.** State the divergence half-angle or contour, since nozzle length and so
   residence time follow from it. A longer, slower-opening nozzle is a separate lever on the same
   rate question. Say if it is worth a row.

The paper will not print a wider throat until this and S24 land.
