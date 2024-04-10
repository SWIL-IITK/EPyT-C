import os
from epyt_c import create_epytc, execute_epytc

epytc = create_epytc()

# Enter the full path to the INP file below after 'r'
root = os.path.dirname(os.path.realpath(__file__))
network_name = os.path.join(root, "Networks", "Net1.inp")

epytc.network_name = network_name
execute_epytc(epytc)
