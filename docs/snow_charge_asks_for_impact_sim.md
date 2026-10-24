# Water or argon snow as the charge, on all three plates: ask S60 (for `puffsat_impact_simulation`)

Raised 2026-10-24 against sim `2992448` and aim `7ce7628`. **Written to be copied verbatim into
`katzseth22202/puffsat_impact_simulation`**, so it repeats context the paper repo already has.
Register entry: S60 in `docs/deferred_to_companion_repos.md`. It widens S49 item 6 (water snow as
the departure charge, still open) to every plate and to argon.

Same ground rules as your own handbacks. Neither document is the source of truth. If a premise
here is wrong, say so rather than working around it.

## The question (Seth, 2026-10-24)

What happens if the charge is water snow or argon snow instead of polyethylene? The snow rides in
a thin bag, probably polyethylene film, to hold its shape. The bag may also hold some of the gas
from the snow-making, as long as the bulk density stays low. If snow is too slow to make, a bag of
water and bubbles might do. This is for all three plates: the growth push, the departure bowl and
the Sun bowl.

Seth's reasons:

- **Debris.** A lost ice charge sublimes. A lost polyethylene one stays until drag or atomic oxygen
  removes it.
- **Launch and storage.** Water launches as a dense liquid and can be made into snow in flight.
  Snow-making is mature technology for water, less so for argon.

Seth's premise: *good coupling comes from a denser impactor striking a less dense charge, with the
charge's bubbles or pores collapsing in the shock.* He expects the energy physics to resemble
polyethylene foam's, and wants that checked.

## Two effects of density, pulling opposite ways (please confirm or correct)

The parent's record supports the premise for **heating**:

- **Dense into light puts the heat in the light body.** The paper's pass-through pusher
  (`sec:pass_through_pusher`): a dense disk plowing through a ~10 kg/m^3 lattice acts as a
  snowplow, and the heat of each swept kilogram's sudden stop stays in the lattice. The disk is
  only squeezed.
- **Pores collapsing heat the shocked material further.** The paper's porous methane plug
  (`sec:needle_through_fog`, citing Zel'dovich and Raizer): a shock that crushes a porous solid
  does extra work closing the voids. At the same pressure the porous material ends up hotter, and
  more of it leaves as vapor rather than as droplets. A snow or froth charge should vaporize more
  completely than solid polyethylene, leaving fewer unvaporized pieces.

Your record limits it through **geometry**:

- `xray_collision_study.md` (the charge pusher). "The disk couples only to the column it crosses:
  at k = 20 it needs ~160 kg/m^2 of polyethylene, 17 cm of solid against 5 m of 30 kg/m^3 foam.
  A long foam column would be a line source exploding sideways." The bowl turns a compact
  fireball at its focus, so the charge must stay compact.
- The methane-faced layered charge (`canted_2d_layers.jsonl`). In the gamma-gas model "only the
  density differs between the layers". A 5x density step moved the canted share by about 1-3%.

So the parent expects a sweet spot. Porous enough to heat and vaporize fully, and dense enough
that the column stays a compact source. Very light foam (30 kg/m^3) is past it. Snow at
300-600 kg/m^3 makes a column 1.6-3 times longer than solid polyethylene (about 17-34 cm at the Sun
bowl, against 11 cm), which may still be compact against a bowl several meters deep. The ask is
where the sweet spot sits on each plate. The gamma-gas model may not capture pore collapse,
since it carries density but not porosity. If so, say what it would take to model it.

## The three closures and their charges

All from aim `7ce7628`'s floored headline at 9.86 R_sun, X 60. The rates are the parent's
division (charge mass over burn time).

| Plate | Impactor | k | Charge per pulse | Rate | Charge form now |
|---|---|---|---|---|---|
| Growth push (and the L1 delivery) | Kapton sheet, ~0.07 kg/m^2, 99 km/s | 6.4 | ~200 kg | 2 Hz, ~400 kg/s over ~16 min | plate-wide sheet, 0.5-0.75 kg/m^2 (0.5-0.8 mm of solid PE) |
| Departure bowl | compact impactor, ~15 kg, 84 km/s at 130 deg | 12.4 | ~190 kg | 1 Hz, ~190 kg/s over 32 min | compact charge at the bowl's focus |
| Sun bowl | 1 kg graphite disk, 0.5 m across, 392 km/s | 20 | ~20 kg | 2 Hz, ~40 kg/s over 0.99 h | compact cylinder, ~11 cm of solid PE |

The bond toll falls hardest on the departure. Take the dissipated energy as 1/2 v^2 k/(1+k) per
impactor kilogram, spread over 1+k kilograms. The departure's merged charge then holds about
245 MJ/kg, and polyethylene's 84 MJ/kg of bonds is about 30% of it. Water's ~51 MJ/kg would be
about 19%. The growth push holds ~570 MJ/kg (PE toll ~13%, water ~8%). The Sun bowl holds
~3.5 GJ/kg (PE toll ~2%). These are parent scratch figures, and they leave out ionization.
aim's "bonds returned" sensitivity is $16 dear at Parker's depth, so water might buy about a
third of that, if snow couples as well as solid polyethylene.

## S60. Wanted

1. **Density as a variable on each plate.** Each plate's push law against charge bulk density, at
   its own impactor, angle and k. Densities: solid PE 950 (the reference), water ice 917, liquid
   water 1000, water snow 300 and 600, a water-and-bubbles froth at ~500, and polyethylene foam at
   the same densities as a material control. If a law is cheaper as a breakpoint than a sweep
   (e.g. "within 2% of solid down to X kg/m^3"), that is enough.
2. **Material at fixed density, and porosity.** Water against polyethylene at the same bulk
   density, so the bond-toll and equation-of-state effect is separated from the density effect.
   Is Seth's "like polyethylene foam" right? Then porosity itself. Does pore collapse raise the
   share of the charge that vaporizes, or the impulse, against a solid of the same areal density?
3. **Argon.** Solid argon (~1620 kg/m^3, denser than PE) and argon snow (~78% solid, 22% vapor by
   mass in a sealed bag at 60 K, from the parent's argon bag, `sec:needle_through_fog`). It has no
   bonds, but it does have ionization. What is its frozen toll at each plate's energy per kilogram,
   and does a monatomic gas expand onto the plate better or worse?
4. **The bag.** Does a polyethylene film of ~0.05 kg/m^2 around the snow change anything? Does the
   gas held inside it (water vapor at ~0.6 kPa, argon at ~0.9 kPa) change anything?
5. **The growth push's geometry.** Its charge is a plate-wide sheet a fraction of a millimeter
   thick. As snow it would be a pillow 1-2.5 mm thick and ~20 m across. Does the push law care
   about that thickness? Would a different charge shape suit a bagged charge better at the same k?
6. **Debris from a missed or failed pulse.** For ice and snow, what pieces leave a charge struck
   off-center, or not struck at all? This is S49 items 5 and 6 for the departure, extended to the
   push.

## Paper-side estimates (not asked of you; context for the ledger)

These are the parent's scratch estimates. aim will price whatever you find.

- **Freezing is fast in vacuum.** A water droplet sprayed into vacuum cools by evaporation. At
  273 K the Hertz-Knudsen flux removes ~1.7 MW/m^2, so a 100 um droplet freezes in roughly
  10-100 ms, and a 1 mm droplet in under a few seconds. About an eighth of the water boils off to
  freeze the rest.
- **Throughput is not the hard part.** 400 kg/s is a few large fire monitors' worth of flow.
- **The heat is.** Water's boil-off cannot stay in a small sealed bag. Saturated vapor at 273 K is
  ~0.005 kg/m^3, so holding 12% of a 200 kg charge as vapor would take ~5000 m^3. Real-time water
  snow must therefore vent ~50 kg/s of steam at the ship during the push. Alternatively the vapor
  must condense on a radiating wall, which at ~260 K rejects ~260 W/m^2. Argon is the exception.
  Sprayed into its sealed bag it flashes to 22% vapor and freezes with nothing vented.
- **Real time is needed only for the push.** The departure charge has the 10 days in the parking
  orbit, which is ~0.4 kg/s. The Sun charge has the ~3-year cruise.
- **The Sun charge's storage.** Behind the shade, snow may melt. A sealed bag of liquid water is
  still a charge, at about solid polyethylene's density, so "snow would not survive the dive"
  (the paper's best case) may only mean the charge becomes water.
- **Compactness at launch.** Solid polyethylene (950 kg/m^3) is already as compact as liquid
  water. The launch argument favors water over polyethylene *foam*, not over solid polyethylene.

Answers from items 1-3 go to aim to reprice the three charges, the toll, the snow-making hardware,
the vented water, and the cryostat for argon.
