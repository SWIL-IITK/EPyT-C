print("""  EPyT-C Example 3

   This example contains:
    Import EPyT-C.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source nodes.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
""")

# Importing EPyT-C
from main import epyt_c

# Specify the simulation period (days)
epyt_c.simulation_period_days = 5

'''The default simulation time step for EPyT-C is 300 seconds.
To change the simulation time step for EPyT-C, use the following code:'''

epyt_c.simulation_time_step = 150

''' The time step in seconds for water quality simulation is now changed to
150 seconds.'''

# Add water quality at the source nodes
epyt_c.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

# Executing EPyT-C
epyt_c.exe()