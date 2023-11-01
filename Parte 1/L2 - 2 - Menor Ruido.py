from gwpy.timeseries import TimeSeries
from gwosc.datasets import event_gps
import pylab as plt

EVENTO1 = "GW190412"
EVENTO2 = "GW150914"
#Coletar dados do primeiro evento
gps = event_gps(EVENTO1)
ldata = TimeSeries.fetch_open_data('L1', int(gps)-512, int(gps)+512, cache=True)
lasd = ldata.asd(fftlength=4, method="median")
print("Dados do evento", EVENTO1,"coletados com sucesso!")
#Coletar dados do segundo evento
gps2 = event_gps(EVENTO2)
ldata2 = TimeSeries.fetch_open_data('L1', int(gps2)-512, int(gps2)+512, cache=True)
lasd2 = ldata2.asd(fftlength=4, method="median")
print("Dados do evento", EVENTO2,"coletados com sucesso!")
#Criar grafico com os dados
plt.loglog(lasd, label = EVENTO1)
plt.loglog(lasd2,label = EVENTO2)
plt.legend()
plt.xlim(10,2000)
print("Grafico gerado com sucesso!")
#Salvar infomações em arquivo
plt.savefig('L2 - 2 - Menor Ruido.png')
print("Arquivo salvo com sucesso!")