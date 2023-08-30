#https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    result = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()
    
    return result[result['timestamp']>=3][['actor_id', 'director_id']]
