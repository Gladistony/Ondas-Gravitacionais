from gwosc.datasets import run_segment
O2 = run_segment('O2_4KHZ_R1')
print('Hora de inicio e fim do O2 (Formato de GPS): ', O2)
time_seconds = O2[1] - O2[0]
month_seconds = 30 * 24 * 3600
print('Total de meses que durou o O2:', time_seconds / month_seconds)