# Importing EPyT-C
from ..epyt_c.main_epytc import create_epytc, execute_epytc

print(
    """  EPyT-C Example 1

   This example contains:
    Import EPyT-C.
    Add water quality parameter input values for the source nodes.
    Run EPyT-C for water quality analysis.

        The results are saved as .XLSX files by default.

"""
)

""" The default .INP file for EPyT-C is Net3.inp with two source nodes
(River and Lake). Thus, the default input for water quality at the source
nodes is [[0, 0, 0], [0, 0, 0]] corresponding to the default MSRT module
Chlorine decay and trihalomethanes formation module
('chlorine_decay_thms_formation', i.e., MSRT-1).

To change the water quality at the source nodes, use the following code:"""

# create an epytc_class with default values
epytc = create_epytc()
epytc.reservoir_quality_matrix = [[1, 2, 40], [1, 2, 40]]

"""The bulk water quality parameters (Chlorine, TOC, and THMs) at the two
source nodes are now changed to 1 mg/L, 2 mg/L, and 40 ug/L, respectively."""

# Executing EPyT-C
execute_epytc(epytc)
