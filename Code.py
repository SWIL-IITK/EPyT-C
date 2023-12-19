from main import epyt_c

epyt_c.module = 'MSRT-4'
epyt_c.simulation_period_days = 2
epyt_c.reservoir_quality_matrix = [[1, 2, 40, 40, 0], [1, 2, 40, 40, 0]]

epyt_c.exe()
