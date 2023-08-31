#Problem link _ https://leetcode.com/problems/big-countries/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
#595. Big Countries
#A country is big if:

# it has an area of at least three million (i.e., 3000000 km2), or
# it has a population of at least twenty-five million (i.e., 25000000).
# Write a solution to find the name, population, and area of the big countries.

# Return the result table in any order.

# The result format is in the following example.



import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
  #searching in data frame big countries
  big_countries_df = world[(world['area'] >= 3000000 ) | (world['population'] >= 25000000)]
  # selecting required columns to display
  result_df = big_countries_df [['name', 'population', 'area']]

  return result_df
  
