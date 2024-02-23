import os
from epyt_c.main_epytc import create_epytc, execute_epytc
epytc = create_epytc()
# Enter the full path to the INP file below after 'r'
path_name = r"C:\Users\Abhijith\Documents\GitHub\EPyT-C\Networks\Net3.inp"
epytc.network_name = os.path.normpath(path_name)
execute_epytc(epytc)
