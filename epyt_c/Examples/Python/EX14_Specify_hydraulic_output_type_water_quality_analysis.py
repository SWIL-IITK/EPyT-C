print("""  EPyT-C Example 14

   This example contains:
    Import EPyT-C.
    Add water quality parameter input values for the source nodes.
    Specify the type of hydraulic analysis data to be used for water quality 
    simulation.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
""")

# Importing EPyT-C
from main import epyt_c

# Specify the simulation period (days)
epyt_c.simulation_period_days = 10

# Add water quality at the source nodes
epyt_c.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

'''EPyT-C performs the hydraulic simulation first for a simulation
period greater (if specified) than or equal to the water quality simulation
perid. By default, the hydraulic analysis output corresponding to the last base 
time cycle (converged results) are then applied for water quality simulation.
If this needs to be bypassed, the following code can be used:'''

epyt_c.hyd_wq_sync_option = 'dynamic'

# Executing EPyT-C
epyt_c.exe()