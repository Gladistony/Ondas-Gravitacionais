from gwosc.datasets import query_events
selection = query_events(select=["network-matched-filter-snr >= 30"])
print("Total de eventos com um sinal de ruido maior ou igual a 30:",len(selection))