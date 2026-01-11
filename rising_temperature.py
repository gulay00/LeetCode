import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Select days where temperature is higher than the previous day
    weather.sort_values('recordDate', inplace=True)
    return weather[weather['temperature'] > weather['temperature'].shift(1)][['id']]
