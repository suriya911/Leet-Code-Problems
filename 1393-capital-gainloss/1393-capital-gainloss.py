import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    stocks.loc[stocks['operation']=='Buy', 'price'] = -stocks['price']
    stocks = stocks.groupby('stock_name')['price'].sum().reset_index(name='capital_gain_loss')
    return stocks