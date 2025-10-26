# Minimal GBM simulator + plot
# MU and SIGMA are annualized (decimal). Replace them with values from estimator scripts.

# --- inputs you can change ---
NUM_DAYS = 252
SIGMA = 0.8
MU = 0.15
INITIAL_PRICE = 30000.0
NUM_SIMULATIONS = 200
SEED = 42
# -----------------------------

import math
import random
import matplotlib.pyplot as plt

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

print("simulated paths:", len(paths), "points per path:", len(paths[0]))
print("final K:", K[-1])
print("MU (annual):", MU, "SIGMA (annual):", SIGMA)

# plot and save
for p in paths:
    plt.plot(t, p, linewidth=0.9)
plt.plot(t, K, "k", linewidth=1.5)
plt.xlabel("Days")
plt.ylabel("Bitcoin Price")
plt.title("Geometric Brownian Motion — Bitcoin (Python)")
plt.tight_layout()
plt.savefig("gbm_paths.png", dpi=150)
print("Saved gbm_paths.png")
