# === Thesis sigma estimator (your original logic, unchanged) ===
# Libraries used in your thesis:
import numpy as np
import pandas as pd
import yfinance as yf
from arch import arch_model

# 1) Download BTC daily data for the chosen period
data = yf.download('BTC-USD', start="2023-01-01", end="2025-01-01")

# 2) Compute daily log-returns and scale to percent (as in your thesis)
data['Log_Ret'] = np.log(data['Close'] / data['Close'].shift(1))
data['Log_Ret'] = data['Log_Ret'] * 100

# 3) Fit GARCH(1,1) on percent log-returns (thesis setup)
model = arch_model(data['Log_Ret'].dropna(), vol='Garch', p=1, q=1)
model_fitted = model.fit()

# 4) Forecast next 30 days of variance and convert to volatility
forecast = model_fitted.forecast(horizon=30)
volatility_forecast = np.sqrt(forecast.variance.values[0, :]) / 10

# 5) Print daily forecast vector and its mean (thesis output)
print(volatility_forecast)
volatility = np.mean(volatility_forecast)
print(f"Volatilità media sui prossimi 30 giorni: {volatility}")
