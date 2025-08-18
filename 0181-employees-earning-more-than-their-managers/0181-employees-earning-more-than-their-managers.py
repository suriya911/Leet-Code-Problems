import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee, how='left', left_on='managerId',right_on='id')

    filtered = df.query('salary_x>salary_y')

    result = pd.DataFrame({'Employee':filtered['name_x']})

    return result