'''
EPyT is an open-source software operating within the Python environment to provide a programming interface for the latest version of EPANET 2.2. 
It calls EPANET a shared object and employs an Object-Oriented approach for interfacing EPANET with Python. 
Though EPyT can be employed for performing single-species water quality analysis, which comes within the scope of EPANET 2.2, 
it lacks multi-species reactive-transport modeling capability in its current form. 
In other words, EPyT can only analyze one water quality parameter at a time. 
Consequently, the water quality modeling compartment of EPyT needs to be improved to solve several real-world problems concerning 
water quality variations during delivery via water distribution systems (WDS). 
A fully independent water quality modeling extension, EPyT-C, is developed in this direction

EPyT-C is a  joint initiative by Indian Institute of Technology Kanpur and Technion Irael Institute of Technology.

The source code of EPyT-C calls EPyT and employs the hydraulic solver of EPANET 2.2 for performing hydraulic simulation, 
which the in-built water quality solver then utilizes for performing MSRT modeling. Based on the module selected for WDS analysis, 
EPyT-C evolves partial differential equations and ordinary differential equations  governing the propagation and 
formation/ degradation of the corresponding water quality parameters within the distribution network realm. 
Once the governing equations (advective-reactive equations) are framed, the numerical method that involves the explicit method of 
characteristics and the fourth-order Runge-Kutta method is applied to derive numerical solutions 
- spatiotemporal distribution of complex water quality parameters in WDS.
'''

from os import getcwd

class inp():
    def info():
        '''***************************************************************************************************************************
        INPUT (1)
        Currently, EPyT-C is equipped with four mult-species reactive-transport (MSRT) modules:
            MSRT-1: Chlorine decay and trihalomethanes formation module ('chlorine_decay_thms_formation')
            MSRT-2: Bacterial regrowth module ('bacterial_regrowth')
            MSRT-3: Arsenite oxidation and arsenate attachment/detachment module ('arsenite_oxidation_arsenate_attachment_detachment')
            MSRT-4:P Perfluorooctanoic formation module ('pfas_formation')
        Specify the MSRT module index'''
        
        module = 'MSRT-1'
        
        '''***************************************************************************************************************************
        INPUT (2)
        Specify the network name'''
        
        network_name = getcwd() + '\\epyt_c\\Networks\\Net3.inp'
        
        '''***************************************************************************************************************************
        INPUT (3)
        Number of iterations'''
        
        maximum_iterations_required = 1
        
        '''***************************************************************************************************************************
        INPUT (4)
        Number of days for which water quality needs to be simulated'''
        
        simulation_period_days = 1
        
        '''***************************************************************************************************************************
        INPUT (5)
        Time step in seconds for water quality simulation'''
        
        simulation_time_step = 300
        
        '''***************************************************************************************************************************
        INPUT (6)
        Base time cycle (1 day is default)'''
        
        base_period_days = 1
        
        '''***************************************************************************************************************************
        INPUT (7)
        Minimum velocity (m/s) allowed inside pipes (1e-4 is default)'''
        
        minimum_pipe_flow_velcoity = 1e-4;
        
        '''***************************************************************************************************************************
        INPUT (8)
        Specifying source water quality - only bulk water quality parameters
        Format: [[Bulk paramater 1 for Reservoir 1, Bulk paramater 2 for Reservoir 1, ..., Bulk paramater m for Reservoir 1], \
            ....., [Bulk paramater 1 for Reservoir n, Bulk paramater 2 for Reservoir n, ..., Bulk paramater m for Reservoir n]]
        m - number of bulk parameters, n = number of reservoirs'''
        
        reservoir_quality_mat = [[1, 2, 20], [1, 2, 20]]
        
        '''***************************************************************************************************************************
        INPUT (9)
        Specify the type of variation in reservoir water quality
        Two options - 'none' and 'rand'
        'none' - no variation; 'rand' - random variations'''
        
        reservoir_quality_pattern = 'none'
        
        '''***************************************************************************************************************************
        INPUT (10)
        Specify the range (%) of random variation in reservoir water quality
        For example - 0.1 denotes +/- 10% random variation in the input values per iteration'''
        
        reservoir_quality_pattern_rand_var = 0
        
        '''***************************************************************************************************************************
        INPUT (11)
        Specify the type of pattern for reservoir water quality
        Three options - 'none' , 'rand' , and 'specific'
        'none' - no variation; 'rand' - random variations' 
        'specific' - can specify user-defined pattern'''
        
        reservoir_injection_pattern = 'none'
        
        '''***************************************************************************************************************************
        INPUT (12)
        Specify the range (%) of random variation in reservoir water quality pattern
        For example - 0.1 denotes +/- 10% random variation in the pattern inputs per iteration'''
        
        reservoir_injection_pattern_rand_var = 0
        
        '''***************************************************************************************************************************
        INPUT (13)
        Specify the start time for the 'specific' reservoir water quality pattern
        Format: [[Start time step for Reservoir 1], [Start time step for Reservoir 2], ..., [Start time step for Reservoir n]]
        n = number of reservoirs
        For 'none' and 'rand' cases, input can be of the form: [[]]
        '''
        
        reservoir_injection_start_time = [[]]
        
        '''***************************************************************************************************************************
        INPUT (14)
        Specify the end time for the 'specific' reservoir water quality pattern
        Format: [[End time step for Reservoir 1], [End time step for Reservoir 2], ..., [End time step for Reservoir n]]
        n = number of reservoirs
        For 'none' and 'rand' cases, input can be of the form: [[]]
        '''
        reservoir_injection_end_time = [[]]
        
        '''***************************************************************************************************************************
        INPUT (15)
        Specify the input value for the 'specific' reservoir water quality pattern. The typical value is 1
        Format: [[Value for Reservoir 1], [Value for Reservoir 2], ..., [Value for Reservoir n]]
        n = number of reservoirs
        For 'none' and 'rand' cases, input can be of the form: [[]]
        '''
        reservoir_injection_input_val = [[]]
        
        '''***************************************************************************************************************************
        INPUT (16)
        Specify indices of injection nodes (if any)
        Format: [[Injection node 1 index, Injection node 2 index, ..., Injection node n index]]
        n = number of injection nodes'''
        
        injection_nodes_index = []
        
        '''***************************************************************************************************************************
        INPUT (17)
        Specify water quality (only bulk water quality parameters) in injection nodes (if any)
        Format: [[Bulk paramater 1 for Injection node 1, Bulk paramater 2 for Injection node 1, ..., Bulk paramater m for Injection node 1], \
            ....., [Bulk paramater 1 for Injection node n, Bulk paramater 2 for Injection node n, ..., Bulk paramater m for Injection node n]]
        m - number of bulk parameters, n = number of injection nodes'''
        
        injection_nodes_quality_mat = [[]]
        
        '''***************************************************************************************************************************
        INPUT (18)
        Specify the type of variation in injection node water quality
        Two options - 'none' and 'rand'
        'none' - no variation; 'rand' - random variations'''
        injection_node_quality_pattern = 'rand'
        
        '''***************************************************************************************************************************
        INPUT (19)
        Specify the range (%) of random variation in injection node water quality
        For example - 0.1 denotes +/- 10% random variation in the input values per iteration'''
        injection_node_quality_pattern_rand_var = 0.5
        
        '''***************************************************************************************************************************
        INPUT (20)
        Specify the type of pattern for injection node water quality
        Three options - 'none' , 'rand' , and 'specific'
        'none' - no variation; 'rand' - random variations' 
        'specific' - can specify user-defined pattern'''
        
        injection_node_injection_pattern = 'none'
        
        '''***************************************************************************************************************************
        INPUT (21)
        Specify the range (%) of random variation in injection node water quality pattern
        For example - 0.1 denotes +/- 10% random variation in the pattern inputs per iteration'''
        
        injection_node_injection_pattern_rand_var = 0
        
        '''***************************************************************************************************************************
        INPUT (22)
        Specify the start time for the 'specific' injection node water quality pattern
        Format: [[Start time step for Injection node 1], [Start time step for Injection node 2], ..., [Start time step for Injection node n]]
        n = number of injection nodes
        For 'none' and 'rand' cases, input can be of the form: [[]]
        '''
        
        injection_node_injection_start_time = [[]]
        
        '''***************************************************************************************************************************
        INPUT (23)
        Specify the end time for the 'specific' injection node water quality pattern
        Format: [[End time step for Injection node 1], [End time step for Injection node 2], ..., [End time step for Injection node n]]
        n = number of injection nodes
        For 'none' and 'rand' cases, input can be of the form: [[]]
        '''
        injection_node_injection_end_time = [[]]
        
        '''***************************************************************************************************************************
        INPUT (24)
        Specify the input value for the 'specific' injection node water quality pattern. The typical value is 1
        Format: [[Value for Injection node 1], [Value for Injection node 2], ..., [Value for Injection node n]]
        n = number of injection nodes
        For 'none' and 'rand' cases, input can be of the form: [[]]
        '''
        injection_node_injection_input_val = [[]]
        
        '''***************************************************************************************************************************
        INPUT (25)
        Specifying the type of hydraulic analysis data to be used for water quality simulation
        Two options - steady & dynamic
        steady - converged hydraulic data for water quality simulation
        dynamic - diverged hydraulic data for water quality simulation'''
        
        hyd_wq_sync_opt = "steady"
        
        '''***************************************************************************************************************************
        '''
            
        input_info = [module, network_name, maximum_iterations_required, simulation_period_days, simulation_time_step, base_period_days,\
                      int(((simulation_period_days * 24 * 3600)/ simulation_time_step) + 1), base_period_days * 24 * 3600, minimum_pipe_flow_velcoity,\
                          reservoir_quality_mat, reservoir_quality_pattern, reservoir_quality_pattern_rand_var, reservoir_injection_pattern, reservoir_injection_pattern_rand_var, \
                              reservoir_injection_start_time, reservoir_injection_end_time, reservoir_injection_input_val, \
                                  injection_nodes_index, injection_nodes_quality_mat, injection_node_quality_pattern, injection_node_quality_pattern_rand_var,\
                                      injection_node_injection_pattern, injection_node_injection_pattern_rand_var, injection_node_injection_start_time, \
                                          injection_node_injection_end_time, injection_node_injection_input_val, hyd_wq_sync_opt]
        
        return input_info
    
exec(open('epyt_c.py').read())
