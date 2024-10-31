import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    second=employee.salary.sort_values().drop_duplicates()
    if len(second)<= 1 :
        return pd.DataFrame({"SecondHighestSalary": [None]})

    high=second.iloc[-2]
    return pd.DataFrame({"SecondHighestSalary": [high]})