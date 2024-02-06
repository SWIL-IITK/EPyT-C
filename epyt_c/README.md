# The default values used for EPyT-C along with explanation

## INPUT (1)
Currently, EPyT-C is equipped with four mult-species reactive-transport (MSRT) modules:
    MSRT-1: Chlorine decay and trihalomethanes formation module ('chlorine_decay_thms_formation')
    MSRT-2: Bacterial regrowth module ('bacterial_regrowth')
    MSRT-3: Arsenite oxidation and arsenate attachment/detachment module ('arsenite_oxidation_arsenate_attachment_detachment')
    MSRT-4: Perfluorooctanoic acid formation module ('pfas_formation')
Specify the MSRT module index

module = 'MSRT-1'

## INPUT (2)
Specify the network name

network_name = os.path.join("..", "epyt_c", "Networks", "Net3.inp")

## INPUT (3)
Number of iterations

maximum_iterations_required = 1

## INPUT (4)
Number of days for which water quality needs to be simulated

simulation_period_days = 1

## INPUT (5)
Time step in seconds for water quality simulation

simulation_time_step = 300

## INPUT (6)
Base time cycle (1 day is default)

base_period_days = 1

## INPUT (7)
Minimum velocity (m/s) inside pipes considered for stagnancy (1e-4 is default)

minimum_pipe_flow_velcoity = 1e-4;

## INPUT (8)
Specifying source water quality - only bulk water quality parameters
Format: [[Bulk paramater 1 for Reservoir 1, Bulk paramater 2 for Reservoir 1, ..., Bulk paramater m for Reservoir 1], \
    ....., [Bulk paramater 1 for Reservoir n, Bulk paramater 2 for Reservoir n, ..., Bulk paramater m for Reservoir n]]
m - number of bulk parameters, n = number of reservoirs

reservoir_quality_matrix = [[0, 0, 0], [0, 0, 0]]

## INPUT (9)
Specify the type of variation in reservoir water quality
Two options - 'none' and 'rand'
'none' - no variation; 'rand' - random variations

reservoir_quality_pattern = 'none'

## INPUT (10)
Specify the range (%) of random variation in reservoir water quality
For example - 0.1 denotes +/- 10% random variation in the input values per iteration

reservoir_quality_pattern_random_variability = 0

## INPUT (11)
Specify the type of pattern for reservoir water quality
Three options - 'none' , 'rand' , and 'specific'
'none' - no variation; 'rand' - random variations'
'specific' - can specify user-defined pattern

reservoir_injection_pattern = 'none'

## INPUT (12)
Specify the range (%) of random variation in reservoir water quality pattern
For example - 0.1 denotes +/- 10% random variation in the pattern inputs per iteration

reservoir_injection_pattern_random_variability = 0

## INPUT (13)
Specify the start time for the 'specific' reservoir water quality pattern
Format: [[Start time for Reservoir 1], [Start time for Reservoir 2], ..., [Start time for Reservoir n]]
n = number of reservoirs
For 'none' and 'rand' cases, input can be of the form: [[]]


reservoir_injection_start_time = [[]]

## INPUT (14)
Specify the end time for the 'specific' reservoir water quality pattern
Format: [[End time for Reservoir 1], [End time for Reservoir 2], ..., [End time for Reservoir n]]
n = number of reservoirs
For 'none' and 'rand' cases, input can be of the form: [[]]

reservoir_injection_end_time = [[]]

## INPUT (15)
Specify the input value for the 'specific' reservoir water quality pattern. The typical value is 1
Format: [[Value for Reservoir 1], [Value for Reservoir 2], ..., [Value for Reservoir n]]
n = number of reservoirs
For 'none' and 'rand' cases, input can be of the form: [[]]

reservoir_injection_input_value = [[]]

## INPUT (16)
Specify indices of injection nodes (if any)
Format: [Injection node 1 index, Injection node 2 index, ..., Injection node n index]
n = number of injection nodes

injection_nodes_index = []

## INPUT (17)
Specify water quality (only bulk water quality parameters) in injection nodes (if any)
Format: [[Bulk paramater 1 for Injection node 1, Bulk paramater 2 for Injection node 1, ..., Bulk paramater m for Injection node 1], \
    ....., [Bulk paramater 1 for Injection node n, Bulk paramater 2 for Injection node n, ..., Bulk paramater m for Injection node n]]
m - number of bulk parameters, n = number of injection nodes

injection_nodes_quality_matrix = [[]]

## INPUT (18)
Specify the type of variation in injection node water quality
Two options - 'none' and 'rand'
'none' - no variation; 'rand' - random variations
injection_node_quality_pattern = 'none'

## INPUT (19)
Specify the range (%) of random variation in injection node water quality
For example - 0.1 denotes +/- 10% random variation in the input values per iteration
injection_node_quality_pattern_random_variability = 0

## INPUT (20)
Specify the type of pattern for injection node water quality
Three options - 'none' , 'rand' , and 'specific'
'none' - no variation; 'rand' - random variations'
'specific' - can specify user-defined pattern

injection_node_injection_pattern = 'none'

## INPUT (21)
Specify the range (%) of random variation in injection node water quality pattern
For example - 0.1 denotes +/- 10% random variation in the pattern inputs per iteration

injection_node_injection_pattern_random_variability = 0

## INPUT (22)
Specify the start time for the 'specific' injection node water quality pattern
Format: [[Start time for Injection node 1], [Start time for Injection node 2], ..., [Start time for Injection node n]]
n = number of injection nodes
For 'none' and 'rand' cases, input can be of the form: [[]]


injection_node_injection_start_time = [[]]

## INPUT (23)
Specify the end time for the 'specific' injection node water quality pattern
Format: [[End time for Injection node 1], [End time for Injection node 2], ..., [End time for Injection node n]]
n = number of injection nodes
For 'none' and 'rand' cases, input can be of the form: [[]]

injection_node_injection_end_time = [[]]

## INPUT (24)
Specify the input value for the 'specific' injection node water quality pattern. The typical value is 1
Format: [[Value for Injection node 1], [Value for Injection node 2], ..., [Value for Injection node n]]
n = number of injection nodes
For 'none' and 'rand' cases, input can be of the form: [[]]

injection_node_injection_input_value = [[]]

## INPUT (25)
Specify the type of hydraulic analysis data to be used for water quality simulation
Two options - steady & dynamic
steady - converged hydraulic data for water quality simulation
dynamic - diverged hydraulic data for water quality simulation

hyd_wq_sync_option = 'steady'