#problem link _ https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# Write a solution to find the ids of products that are both low fat and recyclable.

# Return the result table in any order.

# The result format is in the following example.

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
  product_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] =='Y')]
  result_df = product_df[['product_id']]
  return result_df
