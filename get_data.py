import pandas as pd
from decouple import config

from alpha_vantage.timeseries import TimeSeries

# Download stock data
ticker = 'GOOGL'
keys = config('KEYS')
time = TimeSeries(key=keys, output_format='pandas')
data, metadata = time.get_intraday(symbol=ticker, interval='1min', outputsize='full')
data.to_csv('google_stock_data.csv')

