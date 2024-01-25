print(
    """  EPyT-C Example 8

   This example contains:
    Import EPyT-C.
    Specify the INP file name of the network to be simulated.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source nodes.
    Specify the injection node.
    Add water quality parameter input values for the injection node.
    Specify a user-defined pattern for water quality input values for the 
    injection node over time.
    Specify the starting time for the injection corresponding to the injection 
    node.
    Specify the ending time for the injection corresponding to the injection
    node.
    Specify the value for the injection pattern corresponding to the injection
    node.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
"""
)

# Importing EPyT-C
from main import epyt_c

# Specify the network name
epyt_c.network_name = epyt_c.network_folder + "Net3.inp"

# Specify the simulation period (days)
epyt_c.simulation_period_days = 10

# Specify the simulation time step (seconds)
epyt_c.simulation_time_step = 300

# Add water quality at the source nodes
epyt_c.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

"""By default, no variations is specified for water quality values for the 
source nodes over time.
To specify a user-defined temporal pattern for injection, use the following 
code:"""

epyt_c.reservoir_injection_pattern = "specific"

"""For specifying a user-defined temporal pattern, the start and end time need
to be specified."""

"""To specify the starting time, use the following code:"""

epyt_c.reservoir_injection_start_time = [[12], [0]]

"""It is now specified that the injection for the first source node (River) 
will commence at the 13th hour every day, and the same for the second source 
node (Lake) will start at the 1st hour. It may be noted that the base 
time period is selected as 1 day (by default). To change the base time period,
the following code may be used: 
    epyt_c.base_period_days = N, where N is in days
    """

"""To specify the ending time, use the following code:"""

epyt_c.reservoir_injection_end_time = [[23], [11]]

"""It is now specified that the injections for the first source node (River) 
will end at the 24th hour while the same for the second source node (Lake) will 
end at the 12th hour every day."""

"""To specify the value for the injection pattern, use the following code:"""

epyt_c.reservoir_injection_input_value = [[1], [1]]

"""It is now specified that the value for the injection patterns is 1 for both
source nodes."""

# Executing EPyT-C
epyt_c.exe()
