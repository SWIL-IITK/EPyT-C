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

# Importing EPyT-C
from main import epyt_c

# Specify the simulation period (days)
epyt_c.simulation_period_days = 10

# Add water quality at the source nodes
epyt_c.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

"""EPyT-C considers a minimum velocity value for pipes, below which the flow is
assumed as stagnant. By default, this value is assumed as 1e-4 m/s. To change
this value, the following code can be used:"""

epyt_c.minimum_pipe_flow_velcoity = 1e-2

""" The minimum pipe flow velocity considered for stagnancy is now increased
to 1e-2 m/s. It may be noted that this affects the accuracy of the water 
quality model predictions."""

# Executing EPyT-C
epyt_c.exe()
