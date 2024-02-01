import os
from os import getcwd
import hydra
from run_epyt_c import RunEpytc

class epyt_c:

    # def __init__(self, module, maximum_iterations_required, network_name, simulation_period_days, simulation_time_step, base_period_days,
    #          minimum_pipe_flow_velocity, reservoir_quality_matrix, reservoir_quality_pattern, reservoir_quality_pattern_random_variability, reservoir_injection_pattern, reservoir_injection_pattern_random_variability, reservoir_injection_start_time, reservoir_injection_end_time, reservoir_injection_input_value, injection_nodes_index, injection_nodes_quality_matrix, injection_node_quality_pattern, injection_node_quality_pattern_random_variability, injection_node_injection_pattern, injection_node_injection_pattern_random_variability, injection_node_injection_start_time, injection_node_injection_end_time, injection_node_injection_input_value, hyd_wq_sync_option):
    print(
        """
    EPyT is an open-source software operating within the Python environment to
    provide a programming interface for the latest version of EPANET 2.2.
    It calls EPANET a shared object and employs an Object-Oriented approach for
    interfacing EPANET with Python.

    Though EPyT can be employed for performing single-species water quality
    analysis, which comes within the scope of EPANET 2.2, it lacks
    multi-species reactive-transport (MSRT) modeling capability in its current
    form. In other words, EPyT can only analyze one water quality parameter at
    a time. Consequently, the water quality modeling compartment of EPyT needs
    to be improved to solve several real-world problems concerning water quality
    variations during delivery via water distribution systems (WDS). A fully
    independent water quality modeling extension, EPyT-C, is developed in this
    direction.

    EPyT-C is a  joint initiative by Indian Institute of Technology Kanpur and
    Technion Israel Institute of Technology.

    The source code of EPyT-C calls EPyT and employs the hydraulic solver of
    EPANET 2.2 for performing hydraulic simulation, which the in-built water
    quality solver then utilizes for performing MSRT modeling. Based on the
    module selected for WDS analysis, EPyT-C evolves partial differential
    equations and ordinary differential equations governing the propagation
    and formation/ degradation of the corresponding water quality parameters
    within the distribution network realm. Once the governing equations
    (advective-reactive equations) are framed, the numerical method that
    involves the explicit method of characteristics and the fourth-order
    Runge-Kutta method is applied to derive numerical solutions - spatiotemporal
    distribution of complex water quality parameters in WDS.
    """
    )

    module = "MSRT-2"

    network = "Net3.inp"
    sys_folder = os.path.join(getcwd(), "epyt_c")
    network_folder = os.path.join(sys_folder, "Networks")
    network_name = os.path.join(network_folder, network)

    maximum_iterations_required = 1

    simulation_period_days = 1

    """***************************************************************************************************************************
    INPUT (5)
    Time step in seconds for water quality simulation"""

    simulation_time_step = 300

    """***************************************************************************************************************************
    INPUT (6)
    Base time cycle (1 day is default)"""

    base_period_days = 1

    """***************************************************************************************************************************
    INPUT (7)
    Minimum velocity (m/s) inside pipes considered for stagnancy (1e-4 is default)"""

    minimum_pipe_flow_velocity = 1e-4
    """***************************************************************************************************************************
    INPUT (8)
    Specifying source water quality - only bulk water quality parameters
    Format: [[Bulk paramater 1 for Reservoir 1, Bulk paramater 2 for Reservoir 1, ..., Bulk paramater m for Reservoir 1], \
        ....., [Bulk paramater 1 for Reservoir n, Bulk paramater 2 for Reservoir n, ..., Bulk paramater m for Reservoir n]]
    m - number of bulk parameters, n = number of reservoirs"""

    reservoir_quality_matrix = [[0, 0, 0], [0, 0, 0]]

    """***************************************************************************************************************************
    INPUT (9)
    Specify the type of variation in reservoir water quality
    Two options - 'none' and 'rand'
    'none' - no variation; 'rand' - random variations"""

    reservoir_quality_pattern = "none"

    """***************************************************************************************************************************
    INPUT (10)
    Specify the range (%) of random variation in reservoir water quality
    For example - 0.1 denotes +/- 10% random variation in the input values per iteration"""

    reservoir_quality_pattern_random_variability = 0

    """***************************************************************************************************************************
    INPUT (11)
    Specify the type of pattern for reservoir water quality
    Three options - 'none' , 'rand' , and 'specific'
    'none' - no variation; 'rand' - random variations'
    'specific' - can specify user-defined pattern"""

    reservoir_injection_pattern = "none"

    """***************************************************************************************************************************
    INPUT (12)
    Specify the range (%) of random variation in reservoir water quality pattern
    For example - 0.1 denotes +/- 10% random variation in the pattern inputs per iteration"""

    reservoir_injection_pattern_random_variability = 0

    """***************************************************************************************************************************
    INPUT (13)
    Specify the start time for the 'specific' reservoir water quality pattern
    Format: [[Start time for Reservoir 1], [Start time for Reservoir 2], ..., [Start time for Reservoir n]]
    n = number of reservoirs
    For 'none' and 'rand' cases, input can be of the form: [[]]
    """

    reservoir_injection_start_time = [[]]

    """***************************************************************************************************************************
    INPUT (14)
    Specify the end time for the 'specific' reservoir water quality pattern
    Format: [[End time for Reservoir 1], [End time for Reservoir 2], ..., [End time for Reservoir n]]
    n = number of reservoirs
    For 'none' and 'rand' cases, input can be of the form: [[]]
    """
    reservoir_injection_end_time = [[]]

    """***************************************************************************************************************************
    INPUT (15)
    Specify the input value for the 'specific' reservoir water quality pattern. The typical value is 1
    Format: [[Value for Reservoir 1], [Value for Reservoir 2], ..., [Value for Reservoir n]]
    n = number of reservoirs
    For 'none' and 'rand' cases, input can be of the form: [[]]
    """
    reservoir_injection_input_value = [[]]

    """***************************************************************************************************************************
    INPUT (16)
    Specify indices of injection nodes (if any)
    Format: [Injection node 1 index, Injection node 2 index, ..., Injection node n index]
    n = number of injection nodes"""

    injection_nodes_index = []

    """***************************************************************************************************************************
    INPUT (17)
    Specify water quality (only bulk water quality parameters) in injection nodes (if any)
    Format: [[Bulk paramater 1 for Injection node 1, Bulk paramater 2 for Injection node 1, ..., Bulk paramater m for Injection node 1], \
        ....., [Bulk paramater 1 for Injection node n, Bulk paramater 2 for Injection node n, ..., Bulk paramater m for Injection node n]]
    m - number of bulk parameters, n = number of injection nodes"""

    injection_nodes_quality_matrix = [[]]

    """***************************************************************************************************************************
    INPUT (18)
    Specify the type of variation in injection node water quality
    Two options - 'none' and 'rand'
    'none' - no variation; 'rand' - random variations"""
    injection_node_quality_pattern = "none"

    """***************************************************************************************************************************
    INPUT (19)
    Specify the range (%) of random variation in injection node water quality
    For example - 0.1 denotes +/- 10% random variation in the input values per iteration"""
    injection_node_quality_pattern_random_variability = 0

    """***************************************************************************************************************************
    INPUT (20)
    Specify the type of pattern for injection node water quality
    Three options - 'none' , 'rand' , and 'specific'
    'none' - no variation; 'rand' - random variations'
    'specific' - can specify user-defined pattern"""

    injection_node_injection_pattern = "none"

    """***************************************************************************************************************************
    INPUT (21)
    Specify the range (%) of random variation in injection node water quality pattern
    For example - 0.1 denotes +/- 10% random variation in the pattern inputs per iteration"""

    injection_node_injection_pattern_random_variability = 0

    """***************************************************************************************************************************
    INPUT (22)
    Specify the start time for the 'specific' injection node water quality pattern
    Format: [[Start time for Injection node 1], [Start time for Injection node 2], ..., [Start time for Injection node n]]
    n = number of injection nodes
    For 'none' and 'rand' cases, input can be of the form: [[]]
    """

    injection_node_injection_start_time = [[]]

    """***************************************************************************************************************************
    INPUT (23)
    Specify the end time for the 'specific' injection node water quality pattern
    Format: [[End time for Injection node 1], [End time for Injection node 2], ..., [End time for Injection node n]]
    n = number of injection nodes
    For 'none' and 'rand' cases, input can be of the form: [[]]
    """
    injection_node_injection_end_time = [[]]

    """***************************************************************************************************************************
    INPUT (24)
    Specify the input value for the 'specific' injection node water quality pattern. The typical value is 1
    Format: [[Value for Injection node 1], [Value for Injection node 2], ..., [Value for Injection node n]]
    n = number of injection nodes
    For 'none' and 'rand' cases, input can be of the form: [[]]
    """
    injection_node_injection_input_value = [[]]

    """***************************************************************************************************************************
    INPUT (25)
    Specify the type of hydraulic analysis data to be used for water quality simulation
    Two options - steady & dynamic
    steady - converged hydraulic data for water quality simulation
    dynamic - diverged hydraulic data for water quality simulation"""

    hyd_wq_sync_option = "steady"

def ExecuteEpytc(epyt_c: epyt_c):
    print("EPyT-C loaded for execution...")
    RunEpytc(epyt_c)
