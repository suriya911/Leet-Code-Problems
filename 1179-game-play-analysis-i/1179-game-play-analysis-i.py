import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].agg(min).reset_index()

    first_login = first_login.rename(columns={'event_date':'first_login'})

    return first_login