# Importing EPyT-C
from epyt_c.main_epytc import create_epytc, execute_epytc

print(
    """  EPyT-C Example 15

   This example contains:
    Import EPyT-C.
    Add water quality parameter input values for the source nodes.
    Specify the minimum velocity (m/s) for stagnancy.
    Specify the type of hydraulic analysis data to be used for water quality
    simulation.
    Run EPyT-C for water quality analysis.

        The results are saved as .XLSX files by default.

"""
)

# create an epytc_class instace
epytc=create_epytc()

# Specify the simulation period (days)
epytc.simulation_period_days = 10

# Add water quality at the source nodes
epytc.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

"""EPyT-C considers a minimum velocity value for pipes, below which the flow is
assumed as stagnant. By default, this value is assumed as 1e-4 m/s. To change
this value, the following code can be used:"""

epytc.minimum_pipe_flow_velcoity = 1e-2

""" The minimum pipe flow velocity considered for stagnancy is now increased
to 1e-2 m/s. It may be noted that this affects the accuracy of the water
quality model predictions."""

# Executing EPyT-C
execute_epytc(epytc)
