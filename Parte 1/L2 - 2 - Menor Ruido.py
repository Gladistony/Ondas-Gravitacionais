from gwpy.timeseries import TimeSeries
from gwosc.datasets import event_gps
import pylab as plt

gps = event_gps('GW190412')
ldata = TimeSeries.fetch_open_data('L1', int(gps)-512, int(gps)+512, cache=True)
lasd = ldata.asd(fftlength=4, method="median")

gps2 = event_gps('GW150914')
ldata2 = TimeSeries.fetch_open_data('L1', int(gps2)-512, int(gps2)+512, cache=True)
lasd2 = ldata2.asd(fftlength=4, method="median")

plt.loglog(lasd, label = 'GW190412')
plt.loglog(lasd2,label = 'GW150914')
plt.legend()
plt.xlim(10,2000)
plt.savefig('L2 - 2 - Menor Ruido.png')