#https://leetcode.com/problems/the-number-of-rich-customers/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    #Filter the DataFrame to include only rows with amount > 0
    rich_customers = store[store['amount'] > 500]

    #Get the number of unique n_unique customer IDs in the filtered DataFrame
    num_rich_customers = rich_customers['customer_id'].nunique() 

    #create a new DataFrame with the result
    result_df = pd.DataFrame({'rich_count': [num_rich_customers]})
    return result_df
