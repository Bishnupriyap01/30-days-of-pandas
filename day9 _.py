#https://leetcode.com/problems/patients-with-a-condition/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    dia_patient_df = patients[patients['conditions'].str.contains(r'\bDIAB1')]
    result_df = dia_patient_df[['patient_id', 'patient_name', 'conditions']]
    return result_df
