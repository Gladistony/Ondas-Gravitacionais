from gwosc.datasets import run_segment
O2 = run_segment('O2_4KHZ_R1')
print('O2 start and stop gps: ', O2)
time_seconds = O2[1] - O2[0]
month_seconds = 30 * 24 * 3600
print('months in O2:', time_seconds / month_seconds)