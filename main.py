import pandas as pd
from data_processing import preprocess_data
from forecasting import forecast_weight

# Load data
df = pd.read_csv("user_weights.csv")
df = preprocess_data(df)

# Forecast next 7 days
forecast_df = forecast_weight(df)
print(forecast_df)
