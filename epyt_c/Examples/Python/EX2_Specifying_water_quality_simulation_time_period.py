print("""  EPyT-C Example 2

   This example contains:
    Import EPyT-C.
    Specify the number of days for which water quality needs to be simulated.
    Add water quality parameter input values for the source nodes.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
""")

# Importing EPyT-C
from main import epyt_c

'''The default simulation period for EPyT-C is 1 day.
To change the simulation period for EPyT-C, use the following code:'''

epyt_c.simulation_period_days = 10

''' The number of days for which water quality needs to be simulated is now
changed to 10 days.'''

# Add water quality at the source nodes
epyt_c.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

# Executing EPyT-C
epyt_c.exe()