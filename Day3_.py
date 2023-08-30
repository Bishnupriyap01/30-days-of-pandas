#https://leetcode.com/problems/customers-who-never-order/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
  # select customer whose id is present in the orders df and then naegate them (~) to get which customers has't ordered.
  customers_df = customers[~customers['id'].isin(orders['customerId'])]
#build df to print only name of customers and cahnge column name to customers
  result_df = customers_df[['name']].rename(columns={'name':'Customers'})
  
  return result_df
