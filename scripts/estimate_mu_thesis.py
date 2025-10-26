# Estimate μ from last 3 months of daily log-returns and compute the annualized value for simulator

import numpy as np
import pandas as pd
import yfinance as yf

data = yf.download('BTC-USD', start="2023-01-01", end="2025-01-01", progress=False)
data['Log_Ret'] = np.log(data['Close'] / data['Close'].shift(1)) * 100

last_3_months = data.loc[data.index > (data.index[-1] - pd.DateOffset(months=3))]
mu_daily = last_3_months['Log_Ret'].mean() / 100  # daily mean (decimal)

# Keep these equal to simulator settings
NUM_DAYS = 252
SIGMA = 0.8

mu_for_sim = mu_daily * NUM_DAYS + 0.5 * SIGMA * SIGMA  # annualized μ for GBM

print(mu_daily)     # daily μ (decimal)
print(mu_for_sim)   # annualized μ for simulator

