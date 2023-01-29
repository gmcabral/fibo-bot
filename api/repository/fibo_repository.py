import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from binance.client import Client
from dateutil.rrule import *
from datetime import date
from flask import jsonify
from models.fibo import Fibo

class FiboRepository:

    def __init__(self) -> None:
        pass

    def get_current_levels(self, symbol):
        today = date.today()
        symbol = symbol.upper()
        df = self.getdata(symbol, str(today))
        sl, entry, tp = self.get_levels(today, df)
        fibo = Fibo(symbol, entry=entry, take_profit=tp, stop_loss=sl)
        return jsonify(fibo.to_dict())

    def getdata(self, symbol, start):
        client = Client()
        print(symbol)
        frame = pd.DataFrame(client.get_historical_klines(symbol, '1h', start))
        frame = frame.iloc[:,:6]
        frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
        frame.set_index('Time', inplace=True)
        frame.index = pd.to_datetime(frame.index, unit='ms')
        frame.Close = frame.Close.astype(float)
        frame.Low = frame.Low.astype(float)
        return frame

    def get_levels(self, day, df):
        values = [-0.618, 0.618, 1.618]
        series = df.loc[day:][1:2].squeeze()
        diff = float(series.High) - float(series.Low)
        levels = [series.Low + i * diff for i in values]
        return levels
