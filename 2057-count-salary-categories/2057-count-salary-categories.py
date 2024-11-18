import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    df = accounts
    low = len(df[df['income'] < 20000])
    avrg = len(df[(df['income'] >= 20000) & (df['income'] <= 50000)])
    high = len(df[df['income'] > 50000])
    df_new = pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'], 'accounts_count': [low, avrg, high]})
    return df_new