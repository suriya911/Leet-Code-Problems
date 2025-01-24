import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    count = courses.groupby(by='class').count().reset_index()
    return count[count['student']>=5][['class']]