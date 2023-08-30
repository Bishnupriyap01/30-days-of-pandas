#https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Merge the two tables on the 'id' column using a left join
    merged = employees.merge(employee_uni, on='id', how='left')
    
    # Return the result table with the 'unique_id' column
    result = merged[['unique_id','name']]
    
    return result
