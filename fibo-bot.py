import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from binance.client import Client
from dateutil.rrule import *
from datetime import date

client = Client()

def getdata(symbol, start):
    frame = pd.DataFrame(client.get_historical_klines(symbol, '1h', start))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame.set_index('Time', inplace=True)
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame.Close = frame.Close.astype(float)
    frame.Low = frame.Low.astype(float)
    return frame

def get_levels(day, df):
    values = [-0.618, 0.618, 1.618]
    series = df.loc[day:][1:2].squeeze()
    diff = float(series.High) - float(series.Low)
    levels = [series.Low + i * diff for i in values]
    return levels


day = '2023-01-23'
df = getdata('BTCUSDT', day)
print(df.head())
series = df.loc[day:][1:2].squeeze()
diff_ = float(series.High) - float(series.Low)
ratios_ = [-0.618, 0.618, 1.618]
levels_ = [i * diff_ + series.Close for i in ratios_]
sl, entry, tp = get_levels(day, df)
day_one = df.loc[day:][:25]
day_one['price'] = day_one.Open.shift(-1)
# print(series)
# print(day_one)
print(levels_)
in_position = False
for index, row in day_one.iterrows():
    #entry condition
    if not in_position and row.Close >= entry:
        print('Buy price: ' + str(row.price))
        in_position = True
    #buy/sell condition
    if in_position:
        if float(row.Close) >= float(tp) or float(row.Close) <= float(sl) or row.price is None:#str(index) >= str("23:00:00"):
            print('Sell price: ' + str(row.price))
            print('Close price: ' + str(row.Close))
            print('SL: ' + str(sl))
            print('TP: ' + str(tp))
            print(index)
            in_position = False
            break




plt.axhline(y = levels_[0], color = 'k', linestyle = '-')
plt.axhline(y = levels_[1], color = 'g', linestyle = '-')
plt.axhline(y = levels_[2], color = 'b', linestyle = '-')


plt.plot(df.loc[day:][:25].Close)
plt.show()


def fibo_bot():
    buys, sells = [], []
    trade_dates = []
    df = getdata('BTCUSDT', '2023-01-24')
    df['price'] = df.Open.shift(-1)
    dates = np.unique(df.index.date)
    in_position = False
    for date in dates:
        for index, row in df[date:][2:].iterrows():
            if not in_position:
                sl, entry, tp = get_levels(date, df)
                if row.Close >= entry:
                    buys.append(row.price)
                    trade_dates.append(date)
                    in_position = True
            if in_position:
                if row.Close >= tp or row.Close <= sl:
                    sells.append(row.price)
                    in_position = False
                    break
    trades = pd.DataFrame([buys, sells])
    trades.columns = trade_dates
    trades.index = ['Buy', 'Sell']
    trades = trades.T
    trades['PnL'] = trades.Sell.astype(float) - trades.Buy.astype(float)
    trades['PnL_rel'] = trades.PnL.astype(float) / trades.Buy.astype(float)
    print((trades.PnL_rel.astype(float) + 1).cumprod())

