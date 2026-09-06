"""Recompute the paper's P20 bag geometry and dependent quantities.

Run with the Python environment of an aim_is_all_you_need checkout::

    python simulations/bag_geometry.py --calculations-repo /path/to/aim_is_all_you_need

The required upstream revision is b4ddcf0. Its BagState model is evaluated with
an explicit volume; no upstream files or cached simulation artifacts are changed.
Dependencies are the checkout's astropy/numpy/scipy environment.

Geometry follows the paper's cylindrical volume approximation and its capsule
film model. The water calculation preserves the published heating inputs and
solved ice-melting gate. In particular, film mass is never multiplied by a volume
ratio. The historical geometry is reproduced before evaluating 660 m^3 at aspect
ratio four. Output is JSON, including source revision and both sets of results.
"""

from __future__ import annotations

import argparse
import importlib
import json
import math
from pathlib import Path
import subprocess
import sys


def argon_flash(volume: float, heat_capacity: float = 525.0) -> dict[str, float]:
    """Solve eq:argon_flash with the appendix's constant-enthalpy model.

    SI inputs: 83.81 K, 68.891 kPa at the triple point, 7.71 kJ/mol
    sublimation, 29.7 kJ/kg fusion, and 39.948 g/mol. The heat capacity is
    the midpoint of the paper's 450--600 J/(kg K) bracket.
    """
    gas_constant, molar_mass = 8.314462618, 0.039948
    triple_temperature, triple_pressure = 83.81, 68891.0
    sublimation_molar, fusion = 7710.0, 29700.0
    sublimation = sublimation_molar / molar_mass
    lower, upper = 40.0, triple_temperature
    for _ in range(100):
        temperature = (lower + upper) / 2
        fraction = (fusion + heat_capacity * (triple_temperature - temperature)) / sublimation
        pressure = triple_pressure * math.exp(
            -sublimation_molar / gas_constant * (1 / temperature - 1 / triple_temperature)
        )
        gas_pressure = fraction * 213.0 / volume * gas_constant * temperature / molar_mass
        if pressure > gas_pressure:
            upper = temperature
        else:
            lower = temperature
    return {"temperature_K": temperature, "vapour_fraction": fraction, "pressure_Pa": pressure}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--calculations-repo", type=Path, required=True)
    parser.add_argument("--include-growth", action="store_true", help="Recheck the quoted compact/full-bore growth comparison.")
    args = parser.parse_args()
    repo = args.calculations_repo.resolve()
    revision = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    if not revision.startswith("b4ddcf0"):
        parser.error("Use aim_is_all_you_need revision b4ddcf0 to reproduce these inputs.")
    subprocess.run(["git", "-C", str(repo), "diff", "--exit-code", "HEAD", "--", "src"], check=True)
    sys.path.insert(0, str(repo))
    from astropy import units as u

    bag = importlib.import_module("src.bag_state")
    nozzle = importlib.import_module("src.nozzle_geometry")

    def state(volume: float, location: str, factor: float = 1.5, plug: float = 0.0) -> dict[str, float]:
        solved = bag.BagState(
            leak_fraction=bag.SOLVED_LEAK_FRACTIONS["equilibrium"][bag.TABLE_CLOSING_SPEED],
            stored_energy=bag.table_stored_energy(),
            storage=location,
            shape_factor=factor,
            plug_mass=plug * u.kg,
            bag_volume=volume * u.m**3,
        )
        return {
            "waste_MJ_per_kg": solved.waste_heat.to_value(u.MJ / u.kg),
            "warming_MJ_per_kg": solved.warming.to_value(u.MJ / u.kg),
            "boiling_MJ_per_kg": solved.boiling.to_value(u.MJ / u.kg),
            "vapour_fraction": solved.vapour_fraction,
            "vapour_kg": solved.vapour_mass.to_value(u.kg),
            "temperature_K": solved.mist_temperature.to_value(u.K),
            "pressure_kPa": solved.mist_pressure.to_value(u.kPa),
            "film_kg": solved.film_mass.to_value(u.kg),
            "film_percent": 100 * solved.film_fraction,
        }

    def evaluate(volume: float, length: float) -> dict:
        radius = math.sqrt(volume / (math.pi * length))
        sphere_radius = (3 * volume / (4 * math.pi)) ** (1 / 3)
        lengths = [2 * sphere_radius, 16.0, length, 32.0, 50.0]
        rows = []
        for index, ell in enumerate(lengths):
            r = sphere_radius if index == 0 else math.sqrt(volume / (math.pi * ell))
            barrel = ell - 2 * r
            factor = (2 * barrel + 2 * r) / (barrel + 4 * r / 3)
            area = 2 * math.pi * r * ell
            rows.append({
                "length_m": ell, "radius_m": r,
                "conductor_ratio": r * ell / (2 * sphere_radius**2),
                "shape_factor": factor, "area_m2": area,
                "pressure_film_kg": state(volume, "earth", factor)["film_kg"],
                "cold_pressure_film_kg": state(volume, "jupiter", factor)["film_kg"],
                "handling_kg": [area * gauge * 920 for gauge in (6e-6, 25e-6)],
                "handling_12_7_um_kg": area * 12.7e-6 * 920,
            })
        # Only process-local parameters change. Pass the density and arrival
        # fraction explicitly, since upstream defaults describe its old bag.
        saved = nozzle.BORE_RADIUS, nozzle.COLUMN_LENGTH
        try:
            nozzle.BORE_RADIUS, nozzle.COLUMN_LENGTH = radius, length
            coupling = nozzle.self_consistent_slug_ratio(
                arrival_fraction=0.15 / radius, slug_density=213 / volume
            )
            full_bore = nozzle.full_bore_slug_ratio(slug_density=213 / volume)
        finally:
            nozzle.BORE_RADIUS, nozzle.COLUMN_LENGTH = saved
        assert math.isclose(full_bore, 213 / 25, rel_tol=1e-12)
        pulse_momentum = 25 * 56000
        merged_mass = 238.0
        drift = pulse_momentum / merged_mass
        dissipated_energy = 0.5 * 25 * 56000**2 - 0.5 * merged_mass * drift**2
        reversal_pressure = (0.2 * dissipated_energy + merged_mass * drift**2) / volume
        return {
            "volume_m3": volume, "length_m": length, "radius_m": radius,
            "aspect_ratio": length / (2 * radius), "cross_section_m2": math.pi * radius**2,
            "density_kg_m3": 213 / volume, "areal_density_kg_m2": 213 * length / volume,
            "rows": rows,
            "water": {location: state(volume, location) for location in ("jupiter", "earth")},
            "plugged_water": {
                location: state(volume, location, rows[2]["shape_factor"], 37.5)
                for location in ("jupiter", "earth")
            },
            "compact_coupling_k": coupling, "full_bore_k": full_bore,
            "reversal_pressure_MPa": reversal_pressure / 1e6,
            "reversal_field_T": math.sqrt(2 * 4e-7 * math.pi * reversal_pressure),
            "argon": {str(cp): argon_flash(volume, cp) for cp in (450.0, 525.0, 600.0)},
        }

    original = evaluate(bag.BAG_VOLUME.to_value(u.m**3), bag.FLOWN_COLUMN_LENGTH.to_value(u.m))
    # Reproduce the upstream generator before changing its input volume.
    for location in ("jupiter", "earth"):
        expected = bag.paper_bag_state(location)
        assert math.isclose(original["water"][location]["film_kg"], expected.film_mass.to_value(u.kg), rel_tol=1e-12)
    for row in original["rows"]:
        ell = row["length_m"] * u.m
        assert math.isclose(row["area_m2"], bag.bag_surface_area(ell).to_value(u.m**2), rel_tol=1e-12)
        assert math.isclose(row["shape_factor"], bag.shape_factor(ell), rel_tol=1e-12)
    corrected_radius = (660.0 / (8 * math.pi)) ** (1 / 3)
    corrected = evaluate(660.0, 8 * corrected_radius)
    assert math.isclose(corrected["aspect_ratio"], 4.0, rel_tol=1e-12)
    result = {"upstream_commit": revision, "original": original, "corrected": corrected}
    if args.include_growth:
        growth = importlib.import_module("src.two_wave_growth")
        cycles = growth.adaptive_two_wave_cycles()
        optimum = growth.price_chain(cycles, 1.0, 0.8, geometric_efficiency=1.0)
        result["growth_comparison"] = {
            "optimum_k": optimum.slug_ratio,
            "geometric_efficiency": 1.0,
            "plate_fudge": 0.8,
            "fraction_of_optimum": {
                name: growth.price_chain(
                    cycles, 1.0, 0.8, slug_ratio=k, geometric_efficiency=1.0
                ).total_growth / optimum.total_growth
                for name, k in {
                    "original_compact": original["compact_coupling_k"],
                    "corrected_compact": corrected["compact_coupling_k"],
                    "full_bore": corrected["full_bore_k"],
                }.items()
            },
        }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
