import pandas as pd
from numpy import where

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks.price *= where(stocks.operation=='Buy',-1,1)
    return (stocks.groupby('stock_name')['price'].sum().reset_index(name = 'capital_gain_loss'))