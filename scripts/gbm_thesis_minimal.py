# Minimal GBM simulator (plain Python, no external libraries)
# MU and SIGMA must be ANNUALIZED in decimal.
# - MU: paste the value printed as mu_for_sim by scripts/estimate_mu_thesis.py
# - SIGMA: paste the annualized volatility from scripts/estimate_sigma_thesis.py

# --- inputs you can change ---
NUM_DAYS = 252
SIGMA = 0.8            # e.g., 0.67 if annualized from your sigma script
MU = 0.15              # e.g., 0.23 (mu_for_sim from your mu script)
INITIAL_PRICE = 30000.0
NUM_SIMULATIONS = 200
SEED = 42
# -----------------------------

import math
import random

random.seed(SEED)
dt = 1.0 / NUM_DAYS
t = list(range(NUM_DAYS + 1))  # 0..NUM_DAYS

# deterministic drift-only path: K(t) = S0 * exp(MU * t * dt)
K = [INITIAL_PRICE * math.exp(MU * (k * dt)) for k in t]

# Monte Carlo GBM paths (same formula as your MATLAB loop)
paths = []
for _ in range(NUM_SIMULATIONS):
    s = INITIAL_PRICE
    path = [s]
    for _ in range(NUM_DAYS):
        Z = random.gauss(0.0, 1.0)  # ~ N(0,1)
        inc = (MU - 0.5 * SIGMA * SIGMA) * dt + SIGMA * math.sqrt(dt) * Z
        s = s * math.exp(inc)
        path.append(s)
    paths.append(path)

# simple confirmation output
print("simulated paths:", len(paths), "points per path:", len(paths[0]))
print("final K:", K[-1])
print("MU (annual):", MU, "SIGMA (annual):", SIGMA)
