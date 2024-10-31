import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.sort_values('salary', ascending = False)[['salary']].drop_duplicates()
    if employee['salary'].nunique() < 2:
        salary = pd.DataFrame({'SecondHighestSalary':[pd.NA]})
    else:
        p=result.iloc[1]['salary']
        salary = pd.DataFrame({"SecondHighestSalary":[p]})

    return salary