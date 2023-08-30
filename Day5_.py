#https://leetcode.com/problems/invalid-tweets/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    # Filter rows where the length of contect is > 15
    invalid_df = tweets[tweets['content'].str.len() > 15]

    #select only the tweet_id column from invalid_df
    result_df = invalid_df[['tweet_id']]

    return result_df
