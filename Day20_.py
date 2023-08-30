#https://leetcode.com/problems/game-play-analysis-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    #Sort the DataFrame by player_id and event_date
    activity = activity.sort_values(by=['player_id', 'event_date'])

    # Group by player_id and select the minimum event_date for each player
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    result.rename(columns={'event_date': 'first_login'}, inplace=True)

    return result

    
    
