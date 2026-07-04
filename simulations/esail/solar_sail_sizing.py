"""Solar sail sizing for pushing a PuffSat at electric-sail accelerations.

Photon pressure at 1 AU on a perfect reflector at normal incidence is
2 * S / c with S = 1361 W/m^2, about 9.08 uN/m^2. With a realistic
optical efficiency of ~0.88 (McInnes 1999, Solar Sailing, Springer)
the usable figure is ~8.0 uN/m^2. Characteristic acceleration a_c for
sail area A, sail system areal density sigma, and payload mass m_pay:

    a_c = eta * P * A / (sigma * A + m_pay)

Solving for A shows a hard ceiling: a bare sail (m_pay = 0) reaches
1 mm/s^2 only if sigma < eta * P / a_c, about 8 g/m^2. Flown systems:
LightSail 2 was 32 m^2 at 5 kg total (~160 g/m^2, Spencer et al. 2021,
doi:10.1016/j.asr.2020.06.029); IKAROS was 196 m^2 at 315 kg
(Tsuda et al. 2011, doi:10.1016/j.actaastro.2011.06.005).
"""
S = 1361.0            # solar constant, W/m^2
C = 2.99792458e8      # speed of light, m/s
ETA = 0.88            # realistic optical efficiency
P = ETA * 2 * S / C   # usable photon pressure at 1 AU, N/m^2

M_PAY = 25.0          # PuffSat payload mass, kg
A_C = 1e-3            # target characteristic acceleration, m/s^2

print(f"usable photon pressure at 1 AU: {P * 1e6:.2f} uN/m^2")
print(f"areal-density ceiling for {A_C * 1e3:.0f} mm/s^2 (bare sail): "
      f"{P / A_C * 1e3:.1f} g/m^2\n")

for sigma_g in (3.0, 4.0, 5.0):
    sigma = sigma_g * 1e-3                       # kg/m^2
    denom = P - A_C * sigma
    if denom <= 0:
        print(f"sigma = {sigma_g} g/m^2: infeasible")
        continue
    A = A_C * M_PAY / denom
    side = A**0.5
    m_sail = sigma * A
    print(f"sigma = {sigma_g} g/m^2: area {A:7.0f} m^2 "
          f"({side:.0f} m square), sail mass {m_sail:5.1f} kg, "
          f"total {m_sail + M_PAY:5.1f} kg")
