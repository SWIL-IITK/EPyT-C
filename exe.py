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
        '''INPUT
        Currently, EPyT-C is equipped with four mult-species reactive-transport (MSRT) modules:
            MSRT-1: Chlorine decay and trihalomethanes formation module ('chlorine_decay_thms_formation')
            MSRT-2: Bacterial regrowth module ('bacterial_regrowth')
            MSRT-3: Arsenite oxidation and arsenate attachment/detachment module ('arsenite_oxidation_arsenate_attachment_detachment')
            MSRT-4:P Perfluorooctanoic formation module ('pfas_formation')
        Specify the MSRT module index'''
        module = 'MSRT-4'
        
        '''INPUT
        Specify the network name'''
        network_name = getcwd() + '\\epyt_c\\Networks\\Net3.inp'
        
        '''INPUT
        Number of iterations'''
        maximum_iterations_required = 1
        
        '''INPUT'''
        # Number of days for which water quality needs to be simulated
        simulation_period_days = 10
        
        '''INPUT
        Time step in seconds for water quality simulation
        '''
        simulation_time_step = 300
        
        ''''INPUT
        Base time cycle (1 day is default)'''
        base_period_days = 1
        
        '''INPUT
        Minimum velocity (m/s) allowed inside pipes (1e-4 is default)'''
        minimum_pipe_flow_velcoity = 1e-4;
        
        '''INPUT
        Specifying source water quality - only bulk water quality parameters
        Format: [[Bulk paramater 1 for Reservoir 1, Bulk paramater 2 for Reservoir 1, ..., Bulk paramater m for Reservoir 1], \
            ....., [Bulk paramater 1 for Reservoir n, Bulk paramater 2 for Reservoir n, ..., Bulk paramater m for Reservoir n]]
        m - number of bulk parameters, n = number of reservoirs'''
        reservoir_quality_mat = [[1, 2, 40, 40, 0], [1, 2, 40, 40, 0]]
        
        '''INPUT
        Specify indices of injection nodes (if any)
        Format: [[Injection node 1 index, Injection node 2 index, ..., Injection node n index]]
        n = number of injection nodes'''
        injection_nodes_index = []
        
        '''INPUT
        Specify water quality (only bulk water quality parameters) in injection nodes (if any)
        Format: [[Bulk paramater 1 for Injection node 1, Bulk paramater 2 for Injection node 1, ..., Bulk paramater m for Injection node 1], \
            ....., [Bulk paramater 1 for Injection node n, Bulk paramater 2 for Injection node n, ..., Bulk paramater m for Injection node n]]
        m - number of bulk parameters, n = number of injection nodes'''
        injection_nodes_quality_mat = [[]]
        
        
        '''INPUT
        Specifying the type of hydraulic analysis data to be used for water quality simulation
        Two options - steady & dynamic
        steady - converged hydraulic data for water quality simulation
        dynamic - diverged hydraulic data for water quality simulation'''
        hyd_wq_sync_opt = "steady"
        
        
        input_info = [module, network_name, maximum_iterations_required, simulation_period_days, simulation_time_step, base_period_days,\
                      int(((simulation_period_days * 24 * 3600)/ simulation_time_step) + 1), base_period_days * 24 * 3600, minimum_pipe_flow_velcoity,\
                          reservoir_quality_mat, injection_nodes_index, injection_nodes_quality_mat, hyd_wq_sync_opt]
        
        return input_info
    
exec(open('epyt_c.py').read())
