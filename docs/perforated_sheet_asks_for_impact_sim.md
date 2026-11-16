# A perforated Kapton sheet on the fast growth wave: ask S64 (for `puffsat_impact_simulation`)

Raised 2026-11-16 against sim `1eb4115` (Result 24, ADR-0075) and paper `f47fef4`.
**Written to be copied verbatim into `katzseth22202/puffsat_impact_simulation`.** Register entry:
S64 in `docs/deferred_to_companion_repos.md`. Companion ask on the Sun disk: S65,
`docs/penetrating_sun_disk_asks_for_impact_sim.md`.

Same ground rules as your own handbacks. If a premise here is wrong, say so rather than working
around it.

## Why

Seth asked whether the growth sheet would couple or mix better as a grid of thicker strands that
cuts deeper into the charge. The parent's scratch says coupling is not where a grid could pay.
Above about 75 km/s every layer of the charge is vaporized many times over, momentum is
conserved whatever the shape, and millimetre structure has some 100 us to wash out before the
fireball reaches a plate 2 m away. Geometry moves only the losses.

Heating is where a grid could pay. Kapton's window at the fast returns is set by the earlier
pulses' gas (Results on the backward plume and the Kapton band): at 208 km/s a 33 um sheet sits
against a 28 um heat floor and a 54 um load ceiling on maraging steel, so the ledger flies carbon
fabric at $100/kg above 140 km/s. That costs $19 dear at Parker's depth on the all-carbon
sensitivity ($156 to $175). The plume is free-molecular at the sheet, so a strand takes heat only
on its own projected face. A perforated sheet with the same mean areal density but fill fraction
`f` puts `1/f` times the thermal mass behind each square metre of exposed face.

The gain is capped by conduction. Kapton's diffusivity is about 7.8e-8 m^2/s, so over the 0.1-0.2 s
the dose arrives in, heat reaches only 90-125 um into the face. A 70 um film heats through, but a
strand much thicker than ~120 um does not. The parent therefore expects the face to cool by about
2x, not `1/f`. That is the number this ask wants.

Parent scratch for the push charge (k ~ 7, 0.70 kg/m^2 polyethylene, 0.73 mm thick) with
Birkhoff's `L sqrt(rho_p / rho_t)` penetration (ratio 1.22):

| strand / web | fill `f` | penetration, share of charge | pitch |
|---|---|---|---|
| 70 um film | 1.00 | 0.12 | n/a |
| 0.25 mm | 0.28 | 0.42 | 0.9 mm |
| 0.35 mm | 0.20 | 0.58 | 1.75 mm |
| 0.45 mm | 0.16 | 0.75 | 2.9 mm |

The sheet would be a laser-perforated film, not a knotted net, since crossings double the
thickness and punch through the charge from 0.35 mm up.

## Ask

1. **Face temperature.** On the computed backward plume at 137, 158 and 208 km/s, at the slowest
   spread run, give the peak face temperature of a perforated Kapton sheet at fills of 0.2, 0.3
   and 0.5. Use the same mean areal density as the flown film at each speed, with 1-D conduction
   into the web. Does any fill keep Kapton under its 400 C rating at 208 km/s, and with what
   margin?
2. **Plate load.** Does the face's peak load stay set by the mean areal density (the
   `sigma v^2` ceiling), or do the strands print on the plate at a 2 m standoff? One planar or
   2-D run at 0.2-0.3 fill with web pitch resolved is enough to say which.
3. **Coupling.** The overtake law for the perforated sheet against the flat film at the same mean
   areal density, at 99 and 137 km/s. The parent expects within 1%. If it is not, say why.
4. **Radiation above 130 km/s.** If the code's radiating model can see it, compare the hot
   channels' radiative loss against the film's. Otherwise say it is outside the model.
5. **If a web holds at 208 km/s,** state the thickest one that still passes item 2, so aim can
   price Kapton across the fast rows in place of carbon fabric.

## Outcome

If items 1-2 come back with a working fill at 208 km/s, aim reprices the fast-return rows with
Kapton, and the paper replaces the carbon-fabric step above 140 km/s with a perforated sheet.
If the face gains only ~2x and still fails, the paper says so in one sentence beside the carbon
veil. The headline at 99 km/s does not wait on this.
