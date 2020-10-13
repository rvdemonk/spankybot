# bitmex spanky 
import bitmex
from market import Instrument
import matplotlib.pyplot as plt
import time
from config import *



client = bitmex.bitmex()

xbt = Instrument(client, 'XBTUSD')

start = time.time()
XBTd = xbt.getCandles('1d', 900)
end = time.time()

close = list(XBTd['close'])
close.reverse()

print('{0} seconds'.format(end-start))

plt.plot(close)
plt.show()





