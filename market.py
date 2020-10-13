# module for analysing market 
import bitmex
import pandas as pd
import csv
from config import *


class Instrument(object):
    """
    Class for the purpose of interacting with data from Bitmex instruments on.
    """
    def __init__(self, client, symbol):
        self._client = client
        self._symbol = symbol 

    def getCandles(self, timeframe, count):
        """Time interval to bucket by. Available options: [1m,5m,1h,1d]
            count: the number of candles
            symbol: 'XBTUSD', 
            Returns a pandas dataframe.
        """
        candles = pd.DataFrame(self._client.Trade.Trade_getBucketed(
            binSize=timeframe,
            symbol=self._symbol,
            count=count,
            reverse=True).result()[0])
        return pd.DataFrame(candles)

    def exportcsv(self, timeframe, count, compression=None):
        """
        Valid compression types are ['infer', None, 'bz2', 'gzip', 'xz', 'zip']
        """
        if compression:
            compression_opts = dict(method='zip', archive_name='out.csv') 
        df = self.getCandles(timeframe, count)
        filename = "{0}-{1}-{2}".format(self._symbol, timeframe, count)
        df.to_csv('{0}.csv'.format(filename), index=False, compression=compression)



