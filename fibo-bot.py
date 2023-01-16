import pandas as pd
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
    return frame

def get_levels(day, df):
    values = [-0.618, 0.618, 1.618]
    series = df.loc[day:][1:2].squeeze()
    diff = float(series.High) - float(series.Low)
    levels = [series.Close + i * diff for i in values]
    return levels


df = getdata('BTCUSDT', '2023-01-02')
day = '2023-01-02'
series = df.loc[day:][1:2].squeeze()
diff_ = float(series.High) - float(series.Low)
ratios_ = [-0.618, 0.618, 1.618]
levels_ = [i * diff_ + series.Close for i in ratios_]
sl, entry, tp = get_levels('2023-01-02', df)
day_one = df.loc[day:][:25]
day_one['price'] = day_one.Open.shift(-1)
print(day_one)
print(levels_)
in_position = False
for index, row in day_one.iterrows():
    #entry condition
    if not in_position and row.Close >= entry:
        print(row.price)
        in_position = True
    #buy/sell condition
    if in_position:
        if row.Close >= tp or row.Close <= sl:
            print(row.price)
            print('Close price: ' + str(row.Close))
            in_position = False
            break



plt.axhline(y = levels_[0], color = 'k', linestyle = '-')
plt.axhline(y = levels_[1], color = 'g', linestyle = '-')
plt.axhline(y = levels_[2], color = 'b', linestyle = '-')


plt.plot(df.loc[day:][:25].Close)
plt.show()



def fibo_backtest():
    months = [day.isoformat() for day in rrule(MONTHLY, dtstart=date(2022, 1, 1), until=date.today())]
    start_date = date(2023, 1, 1)
    days = [day.isoformat() for day in rrule(DAILY, dtstart=start_date, until=date.today())]
    df = getdata('BTCUSDT', str(start_date))
    for day in days:
        sl, entry, tp = get_levels(day, df)
        day_one = df.loc[day:][:25]
        day_one['price'] = day_one.Open.shift(-1) 
        in_position = False
        wallet_count = 0
        for index, row in day_one.iterrows():
            #entry condition
            if not in_position and row.Close >= entry:
                print('Entry price: ' + str(row.price))
                in_position = True
                entry_price = row.price
            #buy/sell condition
            if in_position:
                if row.Close >= tp or row.Close <= sl:
                    print('Exit price: ' + str(row.price))
                    in_position = False
                    wallet_count = wallet_count + (float(row.price) - float(entry_price))
                    print ('Wallet: ' + str(wallet_count))
                    break



