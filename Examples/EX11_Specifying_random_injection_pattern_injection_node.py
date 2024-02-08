# Importing EPyT-C
from epyt_c.main_epytc import create_epytc, execute_epytc
import os

print(
    """  EPyT-C Example 11

   This example contains:
    Import EPyT-C.
    Specify the INP file name of the network to be simulated.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source nodes.
    Specify the injection node.
    Add water quality parameter input values for the injection node.
    Specify a random pattern for water quality input values for the injection
    node over time.
    Specify the range (%) of random variations in the water quality values for
    the injection node over time.
    Run EPyT-C for water quality analysis.

        The results are saved as .XLSX files by default.

"""
)

# create an epytc_class instace
epytc = create_epytc()

# Specify the network name
epytc.network_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "epyt_c", "Networks", "Net3.inp")

# Specify the simulation period (days)
epytc.simulation_period_days = 1

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
To specify random variations over time, use the following code:"""

epytc.injection_node_injection_pattern = "rand"

"""Random variations to the water water quality values for the injection node
over time has been now specified."""

"""The defualt range (%) of variations specified for water quality values for
the injection node over time is 0.
To specify a value for the range, use the following code:"""

epytc.injection_node_injection_pattern_random_variability = 0.1

"""+/-10% random variations to the water water quality values for the injection
node over time has been now specified."""

# Executing EPyT-C
execute_epytc(epytc)
