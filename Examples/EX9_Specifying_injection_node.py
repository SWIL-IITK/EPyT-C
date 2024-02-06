# Importing EPyT-C
from epyt_c.main_epytc import create_epytc, execute_epytc
import os

print(
    """  EPyT-C Example 9

   This example contains:
    Import EPyT-C.
    Specify the INP file name of the network to be simulated.
    Specify the number of days for which water quality needs to be simulated.
    Specify the time step in seconds for water quality simulation.
    Add water quality parameter input values for the source nodes.
    Specify the injection node.
    Add water quality parameter input values for the injection node.

    Run EPyT-C for water quality analysis.

        The results are saved as .XLSX files by default.

"""
)

# create an epytc_class instace
epytc=create_epytc()

# Specify the network name
epytc.network_name = os.path.join("..","epyt_c","Networks","Net3.inp")

# Specify the simulation period (days)
epytc.simulation_period_days = 10

# Specify the simulation time step (seconds)
epytc.simulation_time_step = 300

# Add water quality at the source nodes
epytc.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

"""By default, no injection node is specified in EPyT-C. To specify injection
node, use the following code:"""

epytc.injection_nodes_index = [21]

"""The junction '121' with index 21 is now specified as the injection node."""

"""To specify the water quality at the injection node, use the following
code:"""

epytc.injection_nodes_quality_matrix = [[2, 0, 0]]


"""It is now specified that at injection node, i.e., junction '121', the
chlorine concentration will be always 2 mg/L. In other words, junction '121'
acts like like a booster node for chloirne."""


# Executing EPyT-C
execute_epytc(epytc)
