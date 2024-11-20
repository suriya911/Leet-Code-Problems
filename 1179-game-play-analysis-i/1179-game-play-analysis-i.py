import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = activity.groupby('player_id')['event_date'].min().reset_index()
    
    first_login.columns = ['player_id', 'first_login']
    
    return first_login