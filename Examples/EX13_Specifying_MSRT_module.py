# Importing EPyT-C
from main import epyt_c

print(
    """  EPyT-C Example 13

   This example contains:
    Import EPyT-C.
    Specify the MSRT module.
    Add water quality parameter input values for the source nodes.
    Run EPyT-C for water quality analysis.
    
        The results are saved as .XLSX files by default.
    
"""
)

"""Currently, EPyT-C is equipped with four mult-species reactive-transport (MSRT) modules:
MSRT-1: Chlorine decay and trihalomethanes formation module 
('chlorine_decay_thms_formation')
MSRT-2: Bacterial regrowth module ('bacterial_regrowth')
MSRT-3: Arsenite oxidation and arsenate attachment/detachment module 
('arsenite_oxidation_arsenate_attachment_detachment')
MSRT-4:P Perfluorooctanoic formation module ('pfas_formation')

The default module for EPyT-C is Chlorine decay and trihalomethanes formation 
module ('chlorine_decay_thms_formation', i.e., MSRT-1).

To change to the Bacterial regrowth MSRT module ('bacterial_regrowth'), use the
following code:"""

epyt_c.module = "MSRT-2"

"""To specify the water quality at the source nodes, use the following code:"""

epyt_c.reservoir_quality_matrix = [[1, 2, 0.8, 0.1, 1e6], [1, 2, 0.8, 0.1, 1e6]]

"""The bulk water quality parameters (Chlorine, TOC, BDOC, FLB, and FDB) at the 
two source nodes are now changed to 1 mg/L, 2 mg/L, 0.8 mg/L, 0.1 CFU/L, and
1e6 cells/L, respectively, corresponding to the MSRT module selected."""

# Executing EPyT-C
epyt_c.exe()
