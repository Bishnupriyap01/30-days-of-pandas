#https://leetcode.com/problems/classes-more-than-5-students/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    grouped = courses.groupby(['class'])['student'].count().reset_index()

    result = grouped[grouped['student'] >= 5]

    return result[['class']]
