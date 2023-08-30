#https://leetcode.com/problems/rearrange-products-table/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(
        products, id_vars='product_id', var_name='store', value_name='price'
    ).dropna()

    # pd.melt =>is used to change the DataFrame format from wide to long. It's used to create a specific format of the DataFrame object where one or more columns work as identifiers.
    #The dropna() method removes the rows that contains NULL values
    #id_vars-tuple, list, or ndarray, optional Column(s) to use as identifier variables.
    #var_name=Name to use for the ‘variable’ column. If None it uses
    #value_name = scalar, default ‘value’Name to use for the ‘value’ column.

