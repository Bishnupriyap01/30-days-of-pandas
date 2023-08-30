#https://leetcode.com/problems/delete-duplicate-emails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    #sort the rows based on id (Ascending order)
    person.sort_values(by='id', ascending=True,inplace=True)
    #Drop the duplicates based on email.
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    #inplace__changes the default behaviour such that the operation on the dataframe doesn't return anything
