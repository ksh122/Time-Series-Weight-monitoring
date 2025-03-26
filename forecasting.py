import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_weight(df, days=7):
    """Forecasts weight for the next 7 days using Exponential Smoothing."""
    model = ExponentialSmoothing(df["imputed_weight"], trend="add", seasonal="add", seasonal_periods=7)
    fitted_model = model.fit()
    future_dates = pd.date_range(start=df["date"].max() + pd.Timedelta(days=1), periods=days)
    forecast = fitted_model.forecast(steps=days)
    return pd.DataFrame({"date": future_dates, "forecasted_weight": forecast})