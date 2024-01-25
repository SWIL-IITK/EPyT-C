print(
    """  EPyT-C Example 5

   This example contains:
    Import EPyT-C.
    Specify the INP file name of the network to be simulated.
    Specify the number of Monte Carlo simulations to be performed.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source nodes.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
"""
)

# Importing EPyT-C
from main import epyt_c

# Specify the network name
epyt_c.network_name = epyt_c.network_folder + "Net3.inp"

"""The default number of simulations in EPyT-C is 1.
To specify the number of Monte Carlo simulations, use the following code:"""

epyt_c.maximum_iterations_required = 50

"""The number of simulations is now changed to 50"""

# Specify the simulation period (days)
epyt_c.simulation_period_days = 10

# Specify the simulation time step (seconds)
epyt_c.simulation_time_step = 300

# Add water quality at the source nodes
epyt_c.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

# Executing EPyT-C
epyt_c.exe()
