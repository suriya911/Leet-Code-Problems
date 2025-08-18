import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df=person.loc[person.duplicated('email')==True]
    result = df[['email']].drop_duplicates(keep='first')
    return result