from gwosc.datasets import query_events
selection = query_events(select=["network-matched-filter-snr >= 30"])
print(len(selection))