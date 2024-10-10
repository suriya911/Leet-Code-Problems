import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = np.where((employees['employee_id'] % 2 == 1) & (employees['name'].str[0] != 'M'), employees['salary'], 0)
    return employees[['employee_id', 'bonus']].sort_values(by = 'employee_id')