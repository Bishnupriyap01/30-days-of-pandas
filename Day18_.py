#https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            'category': ['High Salary', 'Average Salary', 'Low Salary'],
            'accounts_count': [
                
                accounts[accounts.income > 50000].shape[0],
                accounts[(accounts.income>= 20000) & (accounts.income <= 50000)].shape[0],
                accounts[accounts.income < 20000].shape[0],

            ],
        }#dict
    )
