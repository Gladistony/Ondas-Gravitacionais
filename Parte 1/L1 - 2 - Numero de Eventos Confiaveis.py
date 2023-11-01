from gwosc import datasets
from gwosc.datasets import run_segment
GWTC3_events = datasets.find_datasets(type='events', catalog='GWTC-3-confident', segment=run_segment('O3b_16KHZ_R1'))
print("Total de eventos registrados que são confiaveis:",len(GWTC3_events))