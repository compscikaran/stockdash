import pandas as pd
import datetime as dt
pd.core.common.is_list_like = pd.api.types.is_list_like
from pandas_datareader import data


def get_stock_value(stock):
    start = dt.datetime(2010, 1, 1)
    end = dt.datetime.now()
    df = data.get_data_quandl(stock, start, end)
    values = list(df['Close'])
    labels = list(df.index)
    return values, labels
