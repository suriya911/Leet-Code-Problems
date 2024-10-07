import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'id':sorted(views.loc[views['author_id']==views['viewer_id']]['author_id'].unique())})