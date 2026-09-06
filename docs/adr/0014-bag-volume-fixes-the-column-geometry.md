# The 660 m³ bag volume fixes the column dimensions

Status: accepted (2026-09-05, P20 reviewed with Seth). Supersedes R14's adoption
of 672.9 m³ and the bag-dimension amendment in ADR-0011. This decision concerns
the bag geometry; the winding and wall-standoff decisions remain separate.

## Decision

Use 660 m³ and an aspect ratio `length / (2 radius) = 4`. The paper's cylindrical
volume relation gives:

| Quantity | Value used in calculations | Printed value |
| --- | ---: | ---: |
| Volume | 660 m³ | 660 m³ |
| Length | 23.7788773 m | 23.78 m |
| Radius | 2.97235966 m | 2.972 m |
| Cross-section | 27.7557259 m² | 27.76 m² |
| Mean density, 213 kg slug | 0.322727273 kg/m³ | 0.323 kg/m³ |
| Axial areal density | 7.67409221 kg/m² | 7.7 kg/m² |

The impact simulation's 23.8 m field length and 3.0 m chamber radius were
separately rounded inputs. Treating them as an exact pair created the 672.9 m³
volume. Its handback P20 restores the volume and derives the dimensions from it.
The cross-section rounds to 27.76 m² using the unrounded dimensions; the
handback's 27.75 m² came from rounded inputs.

The film estimate retains the existing capsule model, while bore sizing uses
the cylindrical volume approximation. This distinction is stated in the table
caption. No exact capsule-volume solve is substituted for that approximation.

## Dependent quantities

`simulations/bag_geometry.py` evaluates the existing water model at the explicit
new volume. It first reproduces the upstream results at 672.9291464 m³. It keeps
the ice-melting gate and the published heating inputs from `aim_is_all_you_need`
at `b4ddcf0`; no cooling-history, opacity, or conductivity inputs are regenerated.

| Quantity | Previous geometry | Corrected geometry |
| --- | ---: | ---: |
| Design membrane area | 448.619 m² | 444.092 m² |
| Earth pressure film, design column | 6.162 kg | 6.173 kg |
| Plugged Earth pressure film, design column | 4.447 kg | 4.455 kg |
| 12.7 µm handling film, design column | 5.242 kg | 5.189 kg |
| Earth mist temperature | 315.873 K | 316.267 K |
| Earth mist pressure | 8.519 kPa | 8.696 kPa |
| Jupiter mist temperature | 278.697 K | 278.831 K |
| Jupiter mist pressure | 0.9053 kPa | 0.9137 kPa |
| Reversal field, existing 56 km/s example | 7.547 T | 7.621 T |
| Compact-front swept ratio, existing sound-speed interpolation | 7.07195 | 7.08525 |

The pressure film does not scale with volume. Its mass follows `F x T` at fixed
slug mass and film material. Changing volume acts through the saturation state
and the shape factor. The compact/full-bore growth comparison still rounds to
99.7% / 92% of the optimum under the existing mission assumptions.

The argon flash check uses the appendix's constant-enthalpy model: triple point
83.81 K and 68.891 kPa, molar mass 39.948 g/mol, sublimation 7.71 kJ/mol, fusion
29.7 kJ/kg, and solid heat capacity 525 J/(kg K). At 660 m³ it gives 60.125 K,
vapour fraction 0.21831, and 0.88168 kPa. The 450–600 J/(kg K) sensitivity bracket
still rounds to 0.3 K and vapour fraction 0.210–0.227. These are thermodynamic
flash estimates, not an argon plume simulation.

## Provenance and reproduction

- `puffsat_impact_simulation` at `6fe8cf3`, `docs/nozzle_replies_answered.md`, P20,
  and its ADR-0042 supply the geometry correction.
- `aim_is_all_you_need` at `b4ddcf0` supplies `src/bag_state.py` and
  `src/nozzle_geometry.py`. The reproduction passes explicit volume, density,
  and arrival fraction; it changes no upstream files.
- Using that checkout's Python environment and dependencies, run from this
  paper repository:

```bash
python simulations/bag_geometry.py --calculations-repo /path/to/aim_is_all_you_need --include-growth
```

The script emits the original and corrected values, including all rows of
`tab:axial_bag`, both columns of `tab:bag_state`, and the plug cases. The optional
growth check uses the companion's default eleven-cycle schedule, geometric
efficiency 1.0, plate factor 0.8, and fixed compact/full-bore slug ratios.

N8's request to rerun at 0.3165 kg/m³ is withdrawn. The restored density rounds
to the simulation's 0.323 kg/m³. The impact simulation's expansion and winding
artifacts still use a 3.0 m chamber radius and 23.8 m field length; they have not
been rerun at the corrected dimensions. Their input geometry is stated with
the paper's expansion discussion. The appendix's cylindrical liner/cooling
examples retain their own 3 m reference radius; changing the bag does not resize
the liner.
