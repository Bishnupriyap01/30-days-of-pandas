#https://leetcode.com/problems/immediate-food-delivery-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    #Calculate the count of immediate orders
    immediate_count = delivery[delivery['order_date'] == delivery   ['customer_pref_delivery_date']].shape[0]

    #calculate the total count of orders
    total_orders = delivery.shape[0]

    #calculate the percentange of immediate orders
    immediate_percentage = (immediate_count / total_orders) * 100

    #create a dataframe to store the result 
    result_df = pd.DataFrame({'immediate_percentage': [round(immediate_percentage, 2)]})

    return result_df

    #shape[80,90] =enables us to obtain the shape of a DataFrame. number or columns androw  and shape[0] = count 
    #round(count, precision) = rounds the count





