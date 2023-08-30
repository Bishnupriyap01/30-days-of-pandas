#https://leetcode.com/problems/find-users-with-valid-e-mails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_email_df = users[users['mail'].str.match(r'^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return valid_email_df
