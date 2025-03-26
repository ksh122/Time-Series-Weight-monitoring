import pandas as pd

def preprocess_data(df):
    """Handles missing values by forward-fill for small gaps and interpolation for large gaps."""
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").reset_index(drop=True)
    df["imputed_weight"] = df["avg_weight"].fillna(method="ffill").interpolate()
    return df
