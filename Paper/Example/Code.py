from epyt_c.main_epytc import create_epytc, execute_epytc

epytc = create_epytc()
epytc.module = "MSRT-1"
epytc.maximum_iterations_required = 50
epytc.simulation_period_days = 10
epytc.reservoir_quality_matrix = [[1, 0.56, 0], [1, 3.55, 0]]
epytc.reservoir_quality_pattern = "rand"
epytc.reservoir_quality_pattern_random_variability = 0.1
epytc.injection_nodes_index = [16, 61]
epytc.injection_nodes_quality_matrix = [[1, 0, 0], [1, 0, 0]]
epytc.injection_node_quality_pattern = "rand"
epytc.injection_node_quality_pattern_random_variability = 0.1

execute_epytc(epytc)