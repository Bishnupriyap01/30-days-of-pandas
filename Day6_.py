#https://leetcode.com/problems/calculate-special-bonus/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
   #create new bonus column with default value 0
   employees['bonus'] = 0 

   #calculate bonus. based on conditions
   employees.loc[(employees['employee_id'] % 2 != 0) & (~employees['name'].str.startswith('M')), 'bonus'] = employees['salary']

   #select only required colum in result df and sort the result table by emp_id in asc order 
   result_df = employees[['employee_id','bonus']].sort_values(by='employee_id', ascending = True)

   return result_df
