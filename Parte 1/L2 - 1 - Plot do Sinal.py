from gwpy.timeseries import TimeSeries
from gwosc.datasets import event_gps
from matplotlib import pyplot as plt

gps = event_gps('GW190412')
segment = (int(gps)-5, int(gps)+5)
hdata = TimeSeries.fetch_open_data('H1', *segment, verbose=True)
plt.plot(hdata)
plt.savefig('L2 - 1 - Plot do Sinal.png')