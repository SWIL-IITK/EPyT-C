from main import epyt_c

epyt_c.module = "MSRT-1"
epyt_c.maximum_iterations_required = 50
epyt_c.simulation_period_days = 10
epyt_c.reservoir_quality_matrix = [[1, 0.56, 0], [1, 3.55, 0]]
epyt_c.reservoir_quality_pattern = "rand"
epyt_c.reservoir_quality_pattern_random_variability = 0.1
epyt_c.injection_nodes_index = [16, 61]
epyt_c.injection_nodes_quality_matrix = [[1, 0, 0], [1, 0, 0]]
epyt_c.injection_node_quality_pattern = "rand"
epyt_c.injection_node_quality_pattern_random_variability = 0.1
epyt_c.exe()
