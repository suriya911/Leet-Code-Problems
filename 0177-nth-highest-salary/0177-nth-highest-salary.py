import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique = employee['salary'].drop_duplicates().sort_values(ascending=False)

    if N>len(unique) or N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    Highest_nth = unique.iloc[N-1]

    return pd.DataFrame({f'getNthHighestSalary({N})':[Highest_nth]})