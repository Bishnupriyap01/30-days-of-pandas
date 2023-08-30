import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
  #searching in data frame big countries
  big_countries_df = world[(world['area'] >= 3000000 ) | (world['population'] >= 25000000)]
  # selecting required columns to display
  result_df = big_countries_df [['name', 'population', 'area']]

  return result_df
  
