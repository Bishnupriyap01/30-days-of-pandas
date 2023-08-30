#https://leetcode.com/problems/second-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    unique_salaries = employee['salary'].drop_duplicates()
    #sort in desc order and get 2nd highest salary
    second_highest = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None
    if second_highest is None:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    result_df = pd.DataFrame({'SecondHighestSalary':[second_highest]})

    return result_df
