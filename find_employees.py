import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    em=employee.merge(employee,left_on="managerId",right_on="id",suffixes=("","_mgr"))
    return em[em['salary']>em['salary_mgr']][['name']].rename(columns={'name':'Employee'})
