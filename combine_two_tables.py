import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
   df=pd.merge(left=person,right=address,on='personId',how='left')[['firstName','lastName','city','state']]  # LEFT JOIN to keep all persons even if address is missing
   return df
