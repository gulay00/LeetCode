import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.groupby('player_id', as_index=False)['event_date'].min()
    return activity[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})
