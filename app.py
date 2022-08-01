import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from pandas.plotting import scatter_matrix
from tracemalloc import start
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

today = datetime.datetime.today()
start_date = today - datetime.timedelta(days=90)
print(cg.get_price('solana', 'usd'))
print(start_date.strftime('%d-%m-%Y'))
data = cg.get_coin_market_chart_by_id("solana", "usd", 90)

prices = []
dates = []

i = 91

for d in data['prices']:
  prices.append(d[1])
  date = today - datetime.timedelta(days=i)
  dates.append(date.strftime('%d-%m-%Y'))
  i -= 1

print(dates)
fig = go.Figure(data=go.Scatter(x=dates,y=prices, mode='lines'))
fig.show()