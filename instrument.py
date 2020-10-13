import pandas as pd
from os import path
from instrumentData import *

class Instrument:
    """
    A class for storing the price data of a particular tradeable instrument.
    symbol : "XBTUSD"
    candle_size: "1d", "1h"
    timespan: int (x) where 0 < x < 1001
    """
    def __init__(self, symbol, candle_size, timespan):

        file = "{0}-{1}-{2}.csv".format(symbol, candle_size, timespan)
        if path.exists(file):
            self._data = pd.read_csv(file)
        else:
            self._data = InstrumentData("XBTUSD").getCandles(candle_size, count)
    
        # data keys: timestamp,symbol,open,high,low,close,trades,volume,
        #               vwap,lastSize,turnover,homeNotional,foreignNotional


    def getOpen(self, day:int):
        return self._data['open'][day]

    def getClose(self, day:int):
        return self._data['close'][day]

    def getHigh(self, day:int):
        return self_data['high'][day]

    def getLow(self, day:int):
        return self._data['low'][day]

    def getVol(self, day:int):
        return self._data['volume'][day]
        

test = Instrument('XBTUSD', '1d', 1000)

print(test._data.keys())

    


