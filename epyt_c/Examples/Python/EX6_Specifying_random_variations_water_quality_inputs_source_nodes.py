print("""  EPyT-C Example 6

   This example contains:
    Import EPyT-C.
    Specify the INP file name of the network to be simulated.
    Specify the number of Monte Carlo simulations to be performed.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source nodes.
    Specify the type of variations in the water quality values for the source 
    nodes over iterations.
    Specify the range (%) of random variations in the water quality values for
    the source nodes over iterations.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
""")

# Importing EPyT-C
from main import epyt_c

# Specify the network name
epyt_c.network_name = epyt_c.network_folder + 'Net3.inp'

# Sspecify the number of simulations
epyt_c.maximum_iterations_required = 50

# Specify the simulation period (days)
epyt_c.simulation_period_days = 10

# Specify the simulation time step (seconds)
epyt_c.simulation_time_step = 300

# Add water quality at the source nodes
epyt_c.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

'''By default, no variations is specified for water quality values for the 
source nodes over iterations.
To specify random variations, use the following code:'''

epyt_c.reservoir_quality_pattern = 'rand'

'''Random variations to the water water quality values for the source nodes 
over iterations has been now specified.'''

'''The defualt range (%) of variations specified for water quality values for 
the source nodes over iterations is 0.
To specify a value for the range, use the following code:'''

epyt_c.reservoir_quality_pattern_random_variability = 0.25

'''+/-25% random variations to the water water quality values for the source 
nodes over iterations has been now specified.'''

# Executing EPyT-C
epyt_c.exe()