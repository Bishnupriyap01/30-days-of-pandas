#https://leetcode.com/problems/rank-scores/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores.sort_values(by='score', ascending=False)
    #assign lowest rank to highest rank
    #`method=dense' `assigns same rank to equal values without skipping ranks`
    df['rank'] = df['score'].rank(method='dense', ascending=False)
    return df[['score','rank']]


