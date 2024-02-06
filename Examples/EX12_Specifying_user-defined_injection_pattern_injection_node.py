# Importing EPyT-C
from epyt_c.main_epytc import create_epytc, execute_epytc
import os

print(
    """  EPyT-C Example 12

   This example contains:
    Import EPyT-C.
    Specify the INP file name of the network to be simulated.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source nodes.
    Specify a user-defined pattern for water quality input values for the
    source nodes over time.
    Specify the starting time for the injection corresponding to the source
    nodes.
    Specify the ending time for the injection corresponding to the source
    nodes.
    Specify the value for the injection pattern corresponding to the source
    nodes.
    Run EPyT-C for water quality analysis.

        The results are saved as .XLSX files by default.

"""
)

# create an epytc_class instace
epytc=create_epytc()

# Specify the network name
epytc.network_name = os.path.join("..","epytc","Networks","Net3.inp")

# Specify the simulation period (days)
epytc.simulation_period_days = 10

# Specify the simulation time step (seconds)
epytc.simulation_time_step = 300

# Add water quality at the source nodes
epytc.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

# Specify the injection node
epytc.injection_nodes_index = [21]

# Add water quality at the injection node
epytc.injection_nodes_quality_matrix = [[2, 0, 0]]

"""By default, no variations is specified for water quality values for the
injection node over time.
To specify a user-defined temporal pattern for injection, use the following
code:"""

epytc.injection_node_injection_pattern = "specific"

"""For specifying a user-defined temporal pattern, the start and end time need
to be specified."""

"""To specify the starting time, use the following code:"""

epytc.injection_node_injection_start_time = [[3]]

"""It is now specified that the injection for the injection node (junction 121)
will commence at the 4th hour every day. It may be noted that the base
time period is selected as 1 day (by default)."""

"""To specify the ending time, use the following code:"""

epytc.injection_node_injection_end_time = [[19]]

"""It is now specified that the injection for the injection node (junction 121)
will end at the 20th hour every day."""

"""To specify the value for the injection pattern, use the following code:"""

epytc.injection_node_injection_input_value = [[1]]

"""It is now specified that the value for the injection patterns is 1 for both
source nodes."""

# Executing EPyT-C
execute_epytc(epytc)
