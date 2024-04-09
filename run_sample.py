import os
from epyt_c import create_epytc, execute_epytc

epytc = create_epytc()

# Enter the full path to the INP file below after 'r'
path_name = r"/Users/jaykrishnang/Documents/Technion/civil/EPyT-C/Networks/Net1.inp"

epytc.network_name = os.path.normpath(path_name)
execute_epytc(epytc)
