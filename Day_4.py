#https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.loc[
        views['author_id'] == views['viewer_id'], ['author_id']
    ].drop_duplicates().rename(columns={
        'author_id': 'id',
    }).sort_values(
        by=['id'],
    )
