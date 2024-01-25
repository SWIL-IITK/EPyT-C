print(
    """  EPyT-C Example 4

   This example contains:
    Import EPyT-C.
    Specify the INP file name of the network to be simulated.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source node.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
"""
)

# Importing EPyT-C
from main import epyt_c

"""The default .INP file for EPyT-C is Net3.inp, and is stored in the folder
'EPyT-C\\Networks'. To change the .INP file, use the following code:"""

epyt_c.network_name = epyt_c.network_folder + "Net1.inp"

"""The network for water quality simulation is now changed to Net1.inp."""

# Specify the simulation period (days)
epyt_c.simulation_period_days = 10

# Specify the simulation time step (seconds)
epyt_c.simulation_time_step = 300

# Add water quality at the source node
epyt_c.reservoir_quality_matrix = [[1, 2, 40]]

# Executing EPyT-C
epyt_c.exe()
