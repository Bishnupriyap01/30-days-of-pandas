#https://leetcode.com/problems/nth-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary = employee['salary'].drop_duplicates()
    #desc order
    sorted_salaries = unique_salary.sort_values(ascending=False)

    if N > len(sorted_salaries):
        return pd.DataFrame({'Nth Highest Salary' : [None]})

    nth_highest = sorted_salaries.iloc[N-1]

    return pd.DataFrame({'Nth Highest Salary' : [nth_highest]})
