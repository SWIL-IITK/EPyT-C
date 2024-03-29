# Bacterial regrowth module
# Reactive species (bulk) - Chlorine (mg-Cl/L), RDOC (mg-C/L), BDOC (mg-C/L), free living bacteria (CFU/L)
# free dead bacteria (cells/L)
# Reactive species (wall) - ''

import math
import random
import numpy as np


class module:
    # Display modulde details
    def details():
        print("Bacterial regrowth module loaded.")
        print("Reactive species (bulk):")
        print("Chlorine (mg-Cl/L)\nTOC (mg-C/L)\nBDOC (mg-C/L)\nFLB (CFU/L)\nFDB (cells/L)")

    # Getting basic details of the network
    def network(d):
        network_info = [
            d.getNodeCount(),
            d.getLinkCount(),
            d.getNodeReservoirCount(),
            d.getNodeTankCount(),
            d.getLinkPumpCount(),
            d.getLinkValveCount(),
            d.getNodeNameID(),
            d.getLinkNameID(),
            d.getNodeReservoirIndex(),
            d.getNodeTankIndex(),
        ]
        index_pumps = []
        for x in range(
            d.getLinkCount() - (d.getLinkPumpCount() + d.getLinkValveCount()),
            len(d.getLinkNameID()) - d.getLinkValveCount(),
        ):
            index_pumps.append(x + 1)
        network_info.append(index_pumps)
        index_valves = []
        for x in range(d.getLinkCount() - d.getLinkValveCount(), len(d.getLinkNameID())):
            index_valves.append(x + 1)
        network_info.append(index_valves)
        network_info.extend(
            [
                d.getFlowUnits(),
                d.getNodesConnectingLinksIndex(),
                d.getConnectivityMatrix(),
            ]
        )
        # Conversion of GPM units to SI units
        if d.getFlowUnits() == "GPM":
            network_info.append(0.3048 * d.getLinkLength())
            network_info.append(25.4 * d.getLinkDiameter())
        else:
            network_info.extend([d.getLinkLength(), d.getLinkDiameter()])
        start_node_matrix = []
        end_node_matrix = []
        for x in range(d.getLinkCount()):
            var1 = d.getNodesConnectingLinksIndex()[x][0]
            var2 = d.getNodesConnectingLinksIndex()[x][1]
            start_node_matrix.append(var1)
            end_node_matrix.append(var2)
        network_info.extend([start_node_matrix, end_node_matrix])
        # Number of nodes omitted for analysis, if any
        number_omitted_nodes = 0
        # Index of omitted nodes
        index_omitted_nodes = []
        # Number of links omitted for analysis, if any
        number_omitted_links = 0
        # Index of omitted nodes
        index_omitted_links = []
        network_info.extend(
            [
                number_omitted_nodes,
                index_omitted_nodes,
                number_omitted_links,
                index_omitted_links,
            ]
        )
        return network_info

    # Defining the species information of the MSRT module selected
    def species():
        msrt_info = []
        number_water_quality_parameters = 5
        msrt_info.append(number_water_quality_parameters)
        number_bulk_water_quality_parameters = 5
        msrt_info.append(number_bulk_water_quality_parameters)
        number_wall_water_quality_parameters = 0
        msrt_info.append(number_wall_water_quality_parameters)
        number_model_variables = 19
        msrt_info.append(number_model_variables)
        msrt_info = [
            number_water_quality_parameters,
            number_bulk_water_quality_parameters,
            number_wall_water_quality_parameters,
            number_model_variables,
        ]
        return msrt_info

    # Defining zero order reaction
    def zero_order_reaction(num1):
        # num1 - water quality time step
        delta_zero_order = num1
        return delta_zero_order

    # Defining first order reaction
    def first_order_reaction(num1, num2, num3):
        # num1 - reaction rate constant; num2 - concentration value; num3 - water quality time step
        m1 = num1 * num1
        m2 = num1 * (num2 + (num3 / 4) * m1)
        m3 = num1 * (num2 + (num3 / 4) * m2)
        m4 = num1 * (num2 + (num3 / 2) * m3)
        delta_first_order = (num3 / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
        return delta_first_order

    # Defining Reynolds number
    def Reynolds_number(num1, num2, num3):
        # num1 - pipe flow velocity (m/s); num2 - pipe diameter (mm); num3 - kinematic viscosity of water (sq.m/s)
        num4 = num2 * 1e-3
        reynolds_num = (num1 * num4) / num3
        return reynolds_num

    # Defining Schmidt number
    def Schmidt_number(num1, num2):
        # num1 - kinematic viscosity of water (sq.m/s); num2 - molecular diffusivity of bulk species (sq.m/s)
        schmidt_num = num1 / num2
        return schmidt_num

    # Defining Sherwood number
    def Sherwood_number(num1, num2, num3, num4):
        # num1 - Reynolds number; num2 - Schmidt number; num3 - pipe diameter (mm); num4 - pipe length (m)
        num5 = num3 * 1e-3
        if num1 < 2300:
            sherwood_num = 0.023 * (num1**0.83) * (num2**0.33)
        else:
            sherwood_num = 3.65 + (
                (0.0668 * (num5 / num4) * num1 * num2)
                / (1 + 0.04 * ((num5 / num4) * num1 * num2) ** (2 / 3))
            )
        return sherwood_num

    # Defining Mass transfer coefficient
    def mass_transfer_coefficient(num1, num2, num3):
        # num1 - Sherwood number; num2 - molecular diffusivity of bulk species (sq.m/s); num3 - pipe diameter (mm)
        num4 = num3 * 1e-3
        kf_value = num1 * (num2 / num4)
        return kf_value

    # Defining Hydrauic mean radius
    def hydraulic_mean_radius(num1):
        # num1 - pipe diameter (mm)
        num2 = num1 * 1e-3
        rh_value = num2 / 4
        return rh_value

    # Defining variables of the MSRT module
    def variables(num1, num2):
        # num1 - number of iterations; num2 - number of variables
        variable_mat = np.zeros((num1, num2))
        # Temperature (degree Celsius)
        temperature_mean = 25
        temperature_var = 0.5
        # Rate constant (chlorine - TOC reaction) (L/mg-C/s)
        kbNC_lower = 2.19e4
        kbNC_upper = 3.81e4
        kbNC_mean = 3e4
        # Rate constant (chlorine wall reaction) (m/s)
        kwC_lower = 1.04e-7
        kwC_upper = 1.43e-5
        kwC_mean = 1.22e-6
        # Reaction yield constant (chlorine - TOC reaction) (mg-C/ mg-Cl)
        YN_upper = 0.15
        YN_lower = 2.50
        YN_mean = 0.61
        # Specific growth rate of bacteria (1/s)
        umax_lower = 3.6e-6
        umax_upper = 8.5e-4
        umax_mean = 5.5e-5
        # Half-saturation constant for bacteria (mg-C/L)
        Ks_lower = 0.05
        Ks_upper = 1.20
        Ks_mean = 0.24
        # Inactivation constant for bacteria (L/mg-Cl)
        kin_mean = 0.5
        kin_var = 10
        # Mortality rate constant for bacteria (1/s)
        kd_mean = 5.83e-6
        kd_var = 1e-5
        # Chlorine-induced mortality rate constant for bacteria (L/mg-Cl/s)
        kcd_mean = 1.47e-4
        kcd_var = 1e-3
        # Lysis rate constant for dead bacteria (1/s)
        klys_mean = 3.06e-6
        klys_var = 1e-5
        # Yield coefficient for bacteria
        Y_lower = 0.007
        Y_upper = 1.5
        Y_mean = 0.102
        # Organic carbon fraction of bacterial cell
        a_mean = 2.2e-9
        a_var = 1e-8
        # BDOC supplementation by dead bacteria
        b_mean = 0.46
        b_var = 1.5
        # Molecular diffusivity of chlorine (sq.m/s)
        Dm_chlorine = 12.5e-10
        # Molecular diffusivity of RDOC (sq.m/s)
        Dm_rdoc_lower = 7.8e-10
        Dm_rdoc_upper = 11.5e-10
        Dm_rdoc_mean = 9.65e-10
        # Molecular diffusivity of BDOC (sq.m/s)
        Dm_bdoc_lower = 6.7e-10
        Dm_bdoc_upper = 12.1e-10
        Dm_bdoc_mean = 9.4e-10
        # Molecular diffusivity of FLB (sq.m/s)
        Dm_flb_lower = 8e-10
        Dm_flb_upper = 34e-10
        Dm_flb_mean = 21e-10
        # Molecular diffusivity of FDB (sq.m/s)
        Dm_fdb = 1e-13
        # Kinematic viscosity of water (sq.m/s)
        nu_water = 9.31e-7
        if num1 == 1:
            variable_mat[num1 - 1][0] = temperature_mean
            variable_mat[num1 - 1][1] = kbNC_mean * math.exp(-6050 / (temperature_mean + 273))
            variable_mat[num1 - 1][2] = kwC_mean
            variable_mat[num1 - 1][3] = YN_mean
            variable_mat[num1 - 1][4] = math.log(umax_mean)
            variable_mat[num1 - 1][5] = Ks_mean
            variable_mat[num1 - 1][6] = kin_mean
            variable_mat[num1 - 1][7] = kd_mean
            variable_mat[num1 - 1][8] = kcd_mean
            variable_mat[num1 - 1][9] = klys_mean
            variable_mat[num1 - 1][10] = math.log(Y_mean)
            variable_mat[num1 - 1][11] = a_mean
            variable_mat[num1 - 1][12] = b_mean
            variable_mat[num1 - 1][13] = Dm_chlorine
            variable_mat[num1 - 1][14] = Dm_rdoc_mean
            variable_mat[num1 - 1][15] = Dm_bdoc_mean
            variable_mat[num1 - 1][16] = Dm_flb_mean
            variable_mat[num1 - 1][17] = Dm_fdb
            variable_mat[num1 - 1][18] = nu_water
        else:
            for x in range(num1):
                variable_mat[x][0] = (1 - temperature_var) * temperature_mean + (
                    2 * temperature_var * temperature_mean
                ) * random.uniform(0, 1)
                variable_mat[x][1] = random.uniform(kbNC_lower, kbNC_upper) * math.exp(
                    -6050 / ((variable_mat[x][0]) + 273)
                )
                variable_mat[x][2] = random.uniform(kwC_lower, kwC_upper)
                variable_mat[x][3] = random.uniform(YN_lower, YN_upper)
                variable_mat[x][4] = random.uniform(math.log(umax_lower), math.log(umax_upper))
                variable_mat[x][5] = random.uniform(math.log(Ks_lower), math.log(Ks_upper))
                variable_mat[x][6] = np.mod(np.abs(np.random.normal(kin_mean, kin_var)), 10 * kin_mean)
                variable_mat[x][7] = np.mod(np.abs(np.random.normal(kd_mean, kd_var)), 1e3 * kd_mean)
                variable_mat[x][8] = np.mod(np.abs(np.random.normal(kcd_mean, kcd_var)), 1e3 * kcd_mean)
                variable_mat[x][9] = np.mod(np.abs(np.random.normal(klys_mean, klys_var)), 1e3 * klys_mean)
                variable_mat[x][10] = random.uniform(math.log(Y_lower), math.log(Y_upper))
                variable_mat[x][11] = np.abs(np.random.normal(a_mean, a_var))
                variable_mat[x][12] = np.abs(np.random.normal(b_mean, b_var))
                variable_mat[x][13] = Dm_chlorine
                variable_mat[x][14] = random.uniform(Dm_rdoc_lower, Dm_rdoc_upper)
                variable_mat[x][15] = random.uniform(Dm_bdoc_lower, Dm_bdoc_upper)
                variable_mat[x][16] = random.uniform(Dm_flb_lower, Dm_flb_upper)
                variable_mat[x][17] = Dm_fdb
                variable_mat[x][18] = nu_water
        return variable_mat

    # Defining pipe reactions for the MSRT model selected
    def pipe_reaction(num1, num2, num3, num4, num5, num6, num7, arr1, arr2):
        # num1 - water quality time step;num2 - pipe number; num3- grid number;
        # num4 - pipe flow velocity (m/s); num5 - pipe diameter (mm); num6 - pipe length; num7 - width of link segment (m)
        # arr1 - matrix of variables; arr2 = array of pipe concentration
        T = arr1[0]
        kbNC = arr1[1]
        kwC = arr1[2]
        YN = arr1[3]
        umax = math.exp(arr1[4]) * math.exp(-((37 - T) / 30) ** 2)
        Ks = math.exp(arr1[5])
        kin = arr1[6]
        kd = arr1[7]
        kcd = arr1[8]
        klys = arr1[9]
        Y = math.exp(arr1[10])
        a = arr1[11]
        b = arr1[12]
        Dm_chlorine = arr1[13]
        nu_water = arr1[18]

        KbNC = kbNC * arr2[1][num3][num2]
        KbSC = kbNC * arr2[2][num3][num2]
        Re = module.Reynolds_number(num4, num5, nu_water)
        Sc_chlorine = module.Schmidt_number(nu_water, Dm_chlorine)
        Sh_chlorine = module.Sherwood_number(Re, Sc_chlorine, num5, num6)
        kfC = module.mass_transfer_coefficient(Sh_chlorine, Dm_chlorine, num5)
        rh = module.hydraulic_mean_radius(num5)
        KwC = (kwC * kfC) / ((kwC + kfC) * rh)
        if (arr2[0][num3][num2] > 0) and (1.4985 * (arr2[2][num3][num2] / arr2[0][num3][num2]) - 0.4) > 0:
            YS = 1.4985 * (arr2[2][num3][num2] / arr2[0][num3][num2]) - 0.4
        else:
            YS = 0
        u = umax * (arr2[2][num3][num2] / (Ks + arr2[2][num3][num2])) * math.exp(-kin * arr2[0][num3][num2])
        Kd = kd + (kcd * arr2[0][num3][num2])

        # Reactions within pipe
        delta_chlorine_rdoc_reac_pipe = module.first_order_reaction(KbNC, arr2[0][num3][num2], num1)
        delta_chlorine_bdoc_reac_pipe = module.first_order_reaction(KbSC, arr2[0][num3][num2], num1)
        delta_chlorine_wall_reac_pipe = module.first_order_reaction(KwC, arr2[0][num3][num2], num1)
        delta_rdoc_chlorine_reac_pipe = YN * delta_chlorine_rdoc_reac_pipe
        delta_bdoc_chlorine_reac_pipe = YS * delta_chlorine_bdoc_reac_pipe
        delta_bacteria_regrowth_pipe = module.first_order_reaction(u, arr2[3][num3][num2], num1)
        delta_bacteria_death_pipe = module.first_order_reaction(Kd, arr2[3][num3][num2], num1)
        delta_bacteria_lysis_pipe = module.first_order_reaction(klys, arr2[4][num3][num2], num1)
        delta_bdoc_consumption_pipe = (a / Y) * delta_bacteria_regrowth_pipe
        delta_bdoc_lysis_pipe = b * 1e-9 * delta_bacteria_lysis_pipe

        net_delta_chlorine_reac = (
            -delta_chlorine_rdoc_reac_pipe - delta_chlorine_bdoc_reac_pipe - delta_chlorine_wall_reac_pipe
        )
        net_delta_rdoc_reac = -delta_rdoc_chlorine_reac_pipe
        net_delta_bdoc_reac = (
            -delta_bdoc_chlorine_reac_pipe - delta_bdoc_consumption_pipe + delta_bdoc_lysis_pipe
        )
        net_delta_flb_reac = delta_bacteria_regrowth_pipe - delta_bacteria_death_pipe
        net_delta_fdb_reac = delta_bacteria_death_pipe - delta_bacteria_lysis_pipe

        delta_mat = [
            net_delta_chlorine_reac,
            net_delta_rdoc_reac,
            net_delta_bdoc_reac,
            net_delta_flb_reac,
            net_delta_fdb_reac,
        ]
        return delta_mat

    # Defining tank reactions for the MSRT model selected
    def tank_reaction(num1, num2, num3, num4, num5, arr1, arr2, arr3):
        # num1 - water quality time step; num2 - water quality step, num3 - tank number;
        # num4 - tank volume in the previous time step; num5 - tank volume in the present time step;
        # arr1 - matrix of variables; arr2 = initial water quality condition array; arr3 - array of tank concentration
        kbNC = arr1[1]
        YN = arr1[3]
        umax = arr1[4]
        Ks = arr1[5]
        kin = arr1[6]
        kd = arr1[7]
        kcd = arr1[8]
        klys = arr1[9]
        Y = arr1[10]
        a = arr1[11]
        b = arr1[12]

        if num2 == 1:
            tank_chlorine_conc = arr2[num3][0]
            tank_rdoc_conc = arr2[num3][1]
            tank_bdoc_conc = arr2[num3][2]
            tank_flb_conc = arr2[num3][3]
            tank_fdb_conc = arr2[num3][4]
        else:
            tank_chlorine_conc = arr3[0][num2 - 1][num3]
            tank_rdoc_conc = arr3[1][num2 - 1][num3]
            tank_bdoc_conc = arr3[2][num2 - 1][num3]
            tank_flb_conc = arr3[3][num2 - 1][num3]
            tank_fdb_conc = arr3[4][num2 - 1][num3]

        KbNC = kbNC * tank_rdoc_conc
        KbSC = kbNC * tank_bdoc_conc
        if (tank_chlorine_conc > 0) and (1.4985 * (tank_bdoc_conc / tank_chlorine_conc) - 0.4) > 0:
            YS = 1.4985 * (tank_bdoc_conc / tank_chlorine_conc) - 0.4
        else:
            YS = 0
        u = umax * (tank_bdoc_conc / (Ks + tank_bdoc_conc)) * math.exp(-kin * tank_chlorine_conc)
        Kd = kd + (kcd * tank_chlorine_conc)

        # Reactions within tank
        delta_chlorine_rdoc_reac_tank = (num4 / num5) * module.first_order_reaction(
            KbNC, tank_chlorine_conc, num1
        )
        delta_chlorine_bdoc_reac_tank = (num4 / num5) * module.first_order_reaction(
            KbSC, tank_chlorine_conc, num1
        )
        delta_rdoc_chlorine_reac_tank = YN * delta_chlorine_rdoc_reac_tank
        delta_bdoc_chlorine_reac_tank = YS * delta_chlorine_bdoc_reac_tank
        delta_bacteria_regrowth_tank = (num4 / num5) * module.first_order_reaction(u, tank_flb_conc, num1)
        delta_bacteria_death_tank = (num4 / num5) * module.first_order_reaction(Kd, tank_flb_conc, num1)
        delta_bacteria_lysis_tank = (num4 / num5) * module.first_order_reaction(klys, tank_fdb_conc, num1)
        delta_bdoc_consumption_tank = (a / Y) * delta_bacteria_regrowth_tank
        delta_bdoc_lysis_tank = b * 1e-9 * delta_bacteria_lysis_tank

        net_delta_chlorine_reac = -delta_chlorine_rdoc_reac_tank - delta_chlorine_bdoc_reac_tank
        net_delta_rdoc_reac = -delta_rdoc_chlorine_reac_tank
        net_delta_bdoc_reac = (
            -delta_bdoc_chlorine_reac_tank - delta_bdoc_consumption_tank + delta_bdoc_lysis_tank
        )
        net_delta_flb_reac = delta_bacteria_regrowth_tank - delta_bacteria_death_tank
        net_delta_fdb_reac = delta_bacteria_death_tank - delta_bacteria_lysis_tank

        delta_mat = [
            net_delta_chlorine_reac,
            net_delta_rdoc_reac,
            net_delta_bdoc_reac,
            net_delta_flb_reac,
            net_delta_fdb_reac,
        ]
        return delta_mat

    # Defining source quality at the reservoir(s)
    def reservoir_quality(d, num1, arr1, str1, num2):
        # num1 - number of iterations; arr1 - source water quality input
        # str1 - input value for pattern; num2 - percentage variation in the random pattern
        num_reservoirs = module.network(d)[2]
        num_bulk_parameters = module.species()[1]
        if len(arr1) == num_reservoirs:
            if len(arr1[0]) == num_bulk_parameters:
                print("Reservoir quality updated.")
            else:
                print("Reservoir quality input error.")
                exit()
        reservoir_quality = np.zeros((num_reservoirs, num1, num_bulk_parameters))
        # Input
        # 'none' - constant values; 'rand' - randomly varying values
        input = str1
        rand_vary = num2  # percentage variation
        if input == "none":
            for x in range(num_reservoirs):
                reservoir_quality[x] = arr1[x]
        elif input == "rand":
            if num1 == 1:
                mat_min = arr1
                mat_max = arr1
            else:
                mat_min = np.multiply(arr1, (1 - rand_vary))
                mat_max = np.multiply(arr1, (1 + rand_vary))
            for x in range(num_reservoirs):
                for y in range(num_bulk_parameters):
                    z = 0
                    while z < num1:
                        reservoir_quality[x][z][y] = random.uniform(mat_min[x][y], mat_max[x][y])
                        z += 1
        return reservoir_quality

    # Defining source quality pattern for the reservoir(s)
    def reservoir_pattern(d, num1, str1, num2, arr1, arr2, arr3):
        # num1 - base time in days # str1 - input value for pattern; num2 - percentage variation in the random pattern
        # arr1 - reservoir injection start time steps; arr2 - reservoir injection stop time steps
        # arr3 - reservoir injection input value
        num_reservoirs = module.network(d)[2]
        num_bulk_parameters = module.species()[1]
        h_time = d.getTimeHydraulicStep()
        pattern_steps = int(num1 * 24 * 3600 / h_time)
        pattern_mat = np.zeros((num_reservoirs, pattern_steps, num_bulk_parameters))
        # Input
        # 'none' - constant pattern; 'rand' - random variations; 'specific - specify pattern
        input = str1
        rand_vary = num2  # percentage variation
        if input == "none":
            pattern_mat = np.add(pattern_mat, 1)
        elif input == "rand":
            for x in range(num_reservoirs):
                for y in range(num_bulk_parameters):
                    z = 0
                    while z < pattern_steps:
                        pattern_mat[x][z][y] = random.uniform(1 - rand_vary, 1 + rand_vary)
                        z += 1
        elif input == "specific":
            start_step_mat = arr1
            end_step_mat = arr2
            val_input = arr3
            if len(start_step_mat) == num_reservoirs and len(end_step_mat) == num_reservoirs:
                if len(start_step_mat[0]) <= pattern_steps and len(end_step_mat[0]) <= pattern_steps:
                    for x in range(num_reservoirs):
                        for y in range(len(start_step_mat[x])):
                            pattern_mat[x][start_step_mat[x][y] : end_step_mat[x][y]] = val_input[x][y]
            else:
                exit()
        return pattern_mat

    # Defining quality at the injection node(s)
    def injection_quality(num1, arr1, arr2, str1, num2):
        # num1 - number of iterations; arr1 - matrix of injection nodes indices; arr2 - matrix of injection nodes quality
        # str1 - input value for pattern; num2 - percentage variation in the random pattern
        num_injection_nodes = len(arr1)
        num_bulk_parameters = module.species()[1]
        if len(arr2) == num_injection_nodes:
            if len(arr2[0]) == num_bulk_parameters:
                print("Reservoir quality updated.")
            else:
                print("Injection node quality input error.")
                exit()
        injection_quality = np.zeros((num_injection_nodes, num1, num_bulk_parameters))
        print("Injection nodes quality updated.")
        # Input
        # 'none' - constant values; 'rand' - randomly varying values
        input = str1
        rand_vary = num2  # percentage variation
        if input == "none":
            for x in range(num_injection_nodes):
                injection_quality[x] = arr2[x]
        elif input == "rand":
            if num1 == 1:
                mat_min = arr2
                mat_max = arr2
            else:
                mat_min = np.multiply(arr2, (1 - rand_vary))
                mat_max = np.multiply(arr2, (1 + rand_vary))
            for x in range(num_injection_nodes):
                for y in range(num_bulk_parameters):
                    z = 0
                    while z < num1:
                        injection_quality[x][z][y] = random.uniform(mat_min[x][y], mat_max[x][y])
                        z += 1
        return injection_quality

    # Defining injection pattern for the injection node(s)
    def injection_pattern(d, num1, arr1, str1, num2, arr2, arr3, arr4):
        # num1 - base time in days; arr1 - matrix of injection nodes indices
        # str1 - input value for pattern; num2 - percentage variation in the random pattern
        # arr2 - injection node injection start time steps; arr3 - injection node injection stop time steps
        # arr4 - injection node injection input value
        num_injection_nodes = len(arr1)
        num_bulk_parameters = module.species()[1]
        h_time = d.getTimeHydraulicStep()
        pattern_steps = int(num1 * 24 * 3600 / h_time)
        inj_pattern_mat = np.zeros((num_injection_nodes, pattern_steps, num_bulk_parameters))
        # Input
        # 'none' - constant pattern; 'rand' - random variations; 'specific - specify pattern
        input = str1
        rand_vary = num2  # percentage variation
        if input == "none":
            inj_pattern_mat = np.add(inj_pattern_mat, 1)
        elif input == "rand":
            for x in range(num_injection_nodes):
                for y in range(num_bulk_parameters):
                    z = 0
                    while z < pattern_steps:
                        inj_pattern_mat[x][z][y] = random.uniform(1 - rand_vary, 1 + rand_vary)
                        z += 1
        elif input == "specific":
            start_step_mat = arr2
            end_step_mat = arr3
            val_input = arr4
            if len(start_step_mat) == num_injection_nodes and len(end_step_mat) == num_injection_nodes:
                if len(start_step_mat[0]) <= pattern_steps and len(end_step_mat[0]) <= pattern_steps:
                    for x in range(num_injection_nodes):
                        for y in range(len(start_step_mat[x])):
                            inj_pattern_mat[x][start_step_mat[x][y] : end_step_mat[x][y]] = val_input[x][y]
            else:
                exit()
        return inj_pattern_mat
