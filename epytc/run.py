from sys import exit
from .functions import fn
import os
from os import getcwd
import math
import numpy as np
import pandas as pd
import copy
import time
from epyt import epanet

def run_epytc(epytc):
    """Runs the simulation using the data from the epytc object

    :param epytc: epytc object
    :type epytc: epytc_class
    """
    if epytc.module == "MSRT-1":
        from .chlorine_decay_thms_formation import module
    elif epytc.module == "MSRT-2":
        from .bacterial_regrowth import module
    elif epytc.module == "MSRT-3":
        from .arsenite_oxidation_arsenate_attachment_detachment import module
    elif epytc.module == "MSRT-4":
        from .pfas_formation import module

    start_time = time.time()
    # Display MSRT module details
    module.details()
    # Input data
    wq_max_iteration = epytc.maximum_iterations_required
    wq_sim_days = epytc.simulation_period_days
    wq_sim_time_step_s = epytc.simulation_time_step
    base_time_cycle_day = epytc.base_period_days
    total_wq_steps = int(((wq_sim_days * 24 * 3600) / wq_sim_time_step_s) + 1)
    base_time_cycle_s = base_time_cycle_day * 24 * 3600
    Tolerable_u = epytc.minimum_pipe_flow_velocity
    reservoir_quality_input = epytc.reservoir_quality_matrix
    reservoir_quality_pattern = epytc.reservoir_quality_pattern
    reservoir_quality_pattern_rand_var = (
        epytc.reservoir_quality_pattern_random_variability
    )
    reservoir_injection_pattern = epytc.reservoir_injection_pattern
    reservoir_injection_pattern_rand_var = (
        epytc.reservoir_injection_pattern_random_variability
    )
    reservoir_injection_start_time = epytc.reservoir_injection_start_time
    reservoir_injection_end_time = epytc.reservoir_injection_end_time
    reservoir_injection_input_val = epytc.reservoir_injection_input_value
    index_injection_nodes = epytc.injection_nodes_index
    injection_nodes_quality_mat = epytc.injection_nodes_quality_matrix
    injection_node_quality_pattern = epytc.injection_node_quality_pattern
    injection_node_quality_pattern_rand_var = (
        epytc.injection_node_quality_pattern_random_variability
    )
    injection_node_injection_pattern = epytc.injection_node_injection_pattern
    injection_node_injection_pattern_rand_var = (
        epytc.injection_node_injection_pattern_random_variability
    )
    injection_node_injection_start_time = epytc.injection_node_injection_start_time
    injection_node_injection_end_time = epytc.injection_node_injection_end_time
    injection_node_injection_input_val = epytc.injection_node_injection_input_value
    sync_option = epytc.hyd_wq_sync_option
    # Load network
    d = epanet(epytc.network_name)
    # Creating variables
    num_nodes = fn.network(d)[0]
    num_links = fn.network(d)[1]
    num_reservoirs = fn.network(d)[2]
    num_tanks = fn.network(d)[3]
    num_pumps = fn.network(d)[4]
    num_valves = fn.network(d)[5]
    name_nodes = fn.network(d)[6]
    name_links = fn.network(d)[7]
    index_reservoirs = fn.network(d)[8]
    index_tanks = fn.network(d)[9]
    index_pumps = fn.network(d)[10]
    index_valves = fn.network(d)[11]
    unit = fn.network(d)[12]
    link_connectivity_array = fn.network(d)[13]
    connectivity_mat = fn.network(d)[14]
    length_links = fn.network(d)[15]
    diameter_links = fn.network(d)[16]
    start_node_mat = fn.network(d)[17]
    end_node_mat = fn.network(d)[18]
    num_omitted_nodes = fn.network(d)[19]
    index_omitted_nodes = fn.network(d)[20]
    num_omitted_links = fn.network(d)[21]
    index_omitted_links = fn.network(d)[22]
    wq_parameter_num = module.species()[0]
    bulk_wq_parameter_num = module.species()[1]
    wall_wq_parameter_num = module.species()[2]
    num_variables = module.species()[3]
    # Displaying relevant information
    fn.reservoir_names(num_reservoirs, name_nodes, index_reservoirs)
    fn.tank_names(num_tanks, name_nodes, index_tanks)
    fn.pump_names(num_pumps, num_valves, name_links)
    fn.valve_names(num_valves, name_links)
    fn.simulation_info(
        wq_max_iteration, wq_sim_days, wq_sim_time_step_s, total_wq_steps
    )
    fn.msrt_info(wq_parameter_num, bulk_wq_parameter_num, wall_wq_parameter_num)
    fn.omitted_nodes(num_omitted_nodes, name_nodes, index_omitted_nodes)
    fn.omitted_links(num_omitted_links, name_links, index_omitted_links)
    # Getting the values of MSRT module variables
    variable_values_mat = module.variables(wq_max_iteration, num_variables)
    # Getting the quality characteristics of reservoir(s)
    reservoir_quality = module.reservoir_quality(
        d,
        wq_max_iteration,
        reservoir_quality_input,
        reservoir_quality_pattern,
        reservoir_quality_pattern_rand_var,
    )
    # Getting the quality characteristics of reservoir(s)
    injection_quality = module.injection_quality(
        wq_max_iteration,
        index_injection_nodes,
        injection_nodes_quality_mat,
        injection_node_quality_pattern,
        injection_node_quality_pattern_rand_var,
    )
    wq_iteration_count = 1
    # Start of water quality simulation
    while wq_iteration_count <= wq_max_iteration:
        print(
            "Water quality simulation (Iteration %d) is starting..."
            % (wq_iteration_count)
        )
        # Hydraulic simulation Module
        # Number of seconds for which hydraulics is simulated
        h_sim_s = d.getTimeSimulationDuration()
        if h_sim_s < (wq_sim_days * 24 * 3600):
            d.setTimeSimulationDuration(wq_sim_days * 24 * 3600)
            print(
                "Hydraulic analysis simulation period (changed to): %d days"
                % (wq_sim_days)
            )
        else:
            print(
                "Hydraulic analysis simulation period: %d days"
                % (h_sim_s / (24 * 3600))
            )
        # Storing hydraulic time step in seconds
        h_sim_time_step_s = d.getTimeHydraulicStep()
        print("Time period for hydraulic analysis: %d seconds" % (h_sim_time_step_s))
        # EPANET analysis
        d.setQualityType("age")
        H = d.getComputedHydraulicTimeSeries()
        Q = d.getComputedQualityTimeSeries()
        print("Analysis with EPANET completed...")
        print("Information successfully stored.")
        # Interpreting hydraulic analysis report
        total_h_steps_reported = len(H.Time)
        total_h_steps_expected = int(
            (d.getTimeSimulationDuration() / h_sim_time_step_s) + 1
        )
        h_ratio_report = (total_h_steps_reported - 1) / (total_h_steps_expected - 1)
        # Filter uneven timesteps
        filter_steps_mat = fn.time_filter(
            H, h_ratio_report, total_h_steps_reported, h_sim_time_step_s
        )
        H.Time = fn.time_data(H.Time, filter_steps_mat)
        H.Velocity = fn.velocity_data(H.Velocity, filter_steps_mat, unit)
        H.Demand = fn.demand_data(H.Demand, filter_steps_mat, unit)
        H.Flow = fn.flow_data(H.Flow, filter_steps_mat, unit)
        H.TankVolume = fn.tank_volume_data(H.TankVolume, filter_steps_mat, unit)
        # Creating temporary storage matrices
        link_conc_data_points_mat = np.zeros((total_wq_steps, num_links))
        link_segments_width_mat = np.zeros((total_wq_steps, num_links))
        link_flow_velocity_mat = np.zeros((total_wq_steps, num_links))
        link_flow_Reynolds_num_mat = np.zeros((total_wq_steps, num_links))
        tank_flow_volume_mat = np.zeros((total_wq_steps, num_tanks))
        # Getting the maximum number of link grid points required
        link_conc_data_points_max = fn.maximum_segments(
            Tolerable_u, wq_sim_time_step_s, length_links, H.Velocity
        )
        link_conc_array_a = np.zeros(
            (wq_parameter_num, link_conc_data_points_max, num_links)
        )
        link_conc_array = np.zeros(
            (wq_parameter_num, link_conc_data_points_max, num_links)
        )
        node_conc_array_a = np.zeros((bulk_wq_parameter_num, total_wq_steps, num_nodes))
        node_conc_array = np.zeros((bulk_wq_parameter_num, total_wq_steps, num_nodes))
        # Reservoir water quality
        reservoir_quality_mat = np.zeros((num_reservoirs, bulk_wq_parameter_num))
        for x in range(num_reservoirs):
            reservoir_quality_mat[x] = reservoir_quality[x][wq_iteration_count - 1]
        # Injection node(s) water quality
        injection_quality_mat = np.zeros(
            (len(index_injection_nodes), bulk_wq_parameter_num)
        )
        for x in range(len(index_injection_nodes)):
            injection_quality_mat[x] = injection_quality[x][wq_iteration_count - 1]
        # Storing the initial condition for all nodes
        node_conc_initial_mat = np.zeros((num_nodes, bulk_wq_parameter_num))
        for x in range(num_reservoirs):
            node_conc_initial_mat[index_reservoirs[x] - 1] = reservoir_quality_mat[x]
        for x in range(len(index_injection_nodes)):
            for sp in range(bulk_wq_parameter_num):
                if injection_quality[x][wq_iteration_count - 1][sp] != 0:
                    node_conc_initial_mat[index_injection_nodes[x] - 1][sp] = (
                        injection_quality[x][wq_iteration_count - 1][sp]
                    )
        # Storing the initial condition for all links
        link_conc_initial_mat = np.zeros((num_links, wall_wq_parameter_num))
        print("Water quality simulation started...")
        wq_time = 0
        wq_step = 0
        reservoir_pattern = module.reservoir_pattern(
            d,
            base_time_cycle_day,
            reservoir_injection_pattern,
            reservoir_injection_pattern_rand_var,
            reservoir_injection_start_time,
            reservoir_injection_end_time,
            reservoir_injection_input_val,
        )
        injection_pattern = module.injection_pattern(
            d,
            base_time_cycle_day,
            index_injection_nodes,
            injection_node_injection_pattern,
            injection_node_injection_pattern_rand_var,
            injection_node_injection_start_time,
            injection_node_injection_end_time,
            injection_node_injection_input_val,
        )
        while wq_time <= wq_sim_days * 24 * 3600:
            print(
                "Water quality simulation step (Iteration {}/ {}): {} (/ {})".format(
                    wq_iteration_count, wq_max_iteration, wq_step + 1, total_wq_steps
                )
            )
            wq_step += 1
            time_cycle_count = math.ceil(
                (wq_time / (base_time_cycle_day * 24 * 3600)) / 1
            )

            # Synchronizing hydraulic and water quality information
            if wq_time == 0:
                h_step_expected = 0
            sync_out = fn.sync_time(
                d,
                H,
                wq_time,
                total_h_steps_expected,
                base_time_cycle_s,
                h_sim_time_step_s,
                time_cycle_count,
                base_time_cycle_day,
                wq_sim_time_step_s,
                h_step_expected,
                sync_option,
                reservoir_pattern,
            )
            h_step = sync_out[0]
            h_step_expected = sync_out[1]
            reservoir_pattern_step = sync_out[2]
            injection_pattern_step = sync_out[3]
            # Lagrangian stage
            count_links_lagrangian = 0
            link_flow_velocity_time_step = H.Velocity[h_step]
            link_flow_rate_time_step = H.Flow[h_step]
            link_flow_rate_prev_time_step = H.Flow[h_step - 1]
            for p in range(num_links):
                if index_omitted_links.count(p + 1) > 0:
                    count_links_lagrangian += 0
                else:
                    count_links_lagrangian += 1
                    nodes_connecting_link = d.getLinkNodesIndex(p + 1)
                    # Getting the flow velocity of link
                    link_flow_velocity = abs(link_flow_velocity_time_step[p])
                    # Getting the flow rate inside link
                    link_flow_rate = link_flow_rate_time_step[p]
                    # Getting the flow rate inside link for previous time step
                    link_flow_rate_prev = link_flow_rate_prev_time_step[p]

                    if index_pumps.count(p + 1) > 0 or index_valves.count(p + 1) > 0:
                        length_links[p] = fn.minimum_link_length(
                            total_h_steps_expected,
                            wq_sim_time_step_s,
                            Tolerable_u,
                            H.Velocity,
                        )
                        diameter_links[p] = fn.minimum_link_diameter(
                            num_links, num_pumps, num_valves, diameter_links
                        )
                    elif link_flow_velocity > 0 and link_flow_velocity < Tolerable_u:
                        link_flow_velocity = 0
                    if length_links[p] != 0:
                        # Getting the number of segments into which a link is divided
                        if link_flow_velocity > 0:
                            link_segments_num = math.floor(
                                length_links[p]
                                / (link_flow_velocity * wq_sim_time_step_s)
                            )
                        else:
                            link_segments_num = 0
                        if link_segments_num <= 1:
                            link_segments_num = 2
                        elif link_segments_num > (link_conc_data_points_max - 1):
                            link_segments_num = link_conc_data_points_max - 1
                        # Getting the width of the segments into which a link is divided
                        link_segments_width = length_links[p] / link_segments_num
                        link_segments_width_mat[wq_step - 1][p] = link_segments_width
                        link_conc_data_points_mat[wq_step - 1][p] = (
                            link_segments_num + 1
                        )
                        # Checking for reservoir connected to a link
                        start_node = nodes_connecting_link[0]
                        if start_node in index_reservoirs:
                            for sp in range(bulk_wq_parameter_num):
                                if wq_step == 1:
                                    link_conc_array_a[sp][0][p] = reservoir_quality_mat[
                                        index_reservoirs.index(start_node)
                                    ][sp]
                                else:
                                    link_conc_array_a[sp][0][p] = (
                                        reservoir_quality_mat[
                                            index_reservoirs.index(start_node)
                                        ][sp]
                                        * reservoir_pattern[
                                            index_reservoirs.index(start_node)
                                        ][reservoir_pattern_step - 1][sp]
                                    )
                        elif start_node in index_injection_nodes:
                            for sp in range(bulk_wq_parameter_num):
                                if (
                                    injection_quality_mat[
                                        index_injection_nodes.index(start_node)
                                    ][sp]
                                    != 0
                                ):
                                    if wq_step == 1:
                                        link_conc_array_a[sp][0][p] = (
                                            injection_quality_mat[
                                                index_injection_nodes.index(start_node)
                                            ][sp]
                                        )
                                    else:
                                        link_conc_array_a[sp][0][p] = (
                                            injection_quality_mat[
                                                index_injection_nodes.index(start_node)
                                            ][sp]
                                            * injection_pattern[
                                                index_injection_nodes.index(start_node)
                                            ][injection_pattern_step - 1][sp]
                                        )
                        # Calculating the distance of grid points from rear end of a link
                        segment_time_step_mat = np.zeros((link_segments_num + 1, 1))
                        segment_prev_time_step_mat = np.zeros(
                            (int(link_conc_data_points_mat[wq_step - 2][p]), 1)
                        )
                        for i in range(1, link_segments_num + 1):
                            segment_time_step_mat[i][0] = (
                                segment_time_step_mat[i - 1][0] + link_segments_width
                            )

                        # Calculating the distance of grid points from rear end of a link for previous time step
                        if wq_step == 1:
                            segment_prev_time_step_mat = segment_time_step_mat
                        else:
                            for i in range(
                                1, int(link_conc_data_points_mat[wq_step - 2][p])
                            ):
                                segment_prev_time_step_mat[i][0] = (
                                    segment_prev_time_step_mat[i - 1][0]
                                    + link_segments_width_mat[wq_step - 2][p]
                                )
                        # Application of method of characteristics
                        alpha_mat = np.zeros((link_segments_num + 1, 1))
                        if (
                            wq_step == 1
                            or h_step == h_step_expected
                            or np.sign(link_flow_rate) == np.sign(link_flow_rate_prev)
                        ):
                            first_grid = 1
                            last_grid = link_segments_num + 1
                        else:
                            first_grid = 0
                            last_grid = link_segments_num
                        for i in range(first_grid, last_grid):
                            if (
                                wq_step == 1
                                or h_step == h_step_expected
                                or np.sign(link_flow_rate)
                                == np.sign(link_flow_rate_prev)
                            ):
                                alpha_mat[i][0] = segment_time_step_mat[i][0] - (
                                    link_flow_velocity * wq_sim_time_step_s
                                )
                            else:
                                alpha_mat[i][0] = segment_time_step_mat[i][0] + (
                                    link_flow_velocity * wq_sim_time_step_s
                                )
                            if alpha_mat[i][0] < 0:
                                alpha_mat[i][0] = 0
                            elif alpha_mat[i][0] > length_links[p]:
                                alpha_mat[i][0] = length_links[p]
                            if wq_step == 1:
                                ratio_segment = alpha_mat[i][0] / link_segments_width
                            else:
                                ratio_segment = (
                                    alpha_mat[i][0]
                                    / link_segments_width_mat[wq_step - 2][p]
                                )
                            prev_grid = math.floor(ratio_segment)
                            if prev_grid <= 0:
                                prev_grid = 0
                            next_grid = math.ceil(ratio_segment)
                            if next_grid >= link_segments_num + 1:
                                next_grid = link_segments_num + 1
                            elif next_grid == 0:
                                next_grid = 1
                            for sp in range(bulk_wq_parameter_num):
                                if prev_grid == next_grid:
                                    if (
                                        index_pumps.count(p + 1) > 0
                                        or index_valves.count(p + 1) > 0
                                    ):
                                        link_conc_array_a[sp][i][p] = link_conc_array_a[
                                            sp
                                        ][0][p]
                                    else:
                                        prev_grid -= 1
                                        link_conc_array_a[sp][i][p] = link_conc_array[
                                            sp
                                        ][prev_grid][p]
                                elif wq_step == 1:
                                    link_conc_array_a[sp][i][p] = link_conc_array[sp][
                                        prev_grid
                                    ][p] + (
                                        (
                                            link_conc_array[sp][next_grid][p]
                                            - link_conc_array[sp][prev_grid][p]
                                        )
                                        / link_segments_width
                                    ) * (
                                        alpha_mat[i][0]
                                        - segment_prev_time_step_mat[prev_grid][0]
                                    )
                                else:
                                    link_conc_array_a[sp][i][p] = link_conc_array[sp][
                                        prev_grid
                                    ][p] + (
                                        (
                                            link_conc_array[sp][next_grid][p]
                                            - link_conc_array[sp][prev_grid][p]
                                        )
                                        / link_segments_width_mat[wq_step - 2][p]
                                    ) * (
                                        alpha_mat[i][0]
                                        - segment_prev_time_step_mat[prev_grid][0]
                                    )
                            if (
                                index_pumps.count(p + 1) == 0
                                and index_valves.count(p + 1) == 0
                            ):
                                delta = module.pipe_reaction(
                                    wq_sim_time_step_s,
                                    p,
                                    i,
                                    link_flow_velocity,
                                    diameter_links[p],
                                    length_links[p],
                                    link_segments_width,
                                    variable_values_mat[wq_iteration_count - 1],
                                    link_conc_array_a,
                                )
                                for sp in range(wq_parameter_num):
                                    link_conc_array_a[sp][i][p] = (
                                        link_conc_array_a[sp][i][p] + delta[sp]
                                    )
                        link_conc_array_a[link_conc_array_a < 0] = 0
            if count_links_lagrangian != (num_links - num_omitted_links):
                print("Error in Lagrangian stage dedicated to pipes!")
                exit()
            count_nodes_lagrangian = 0
            node_demand_time_step = H.Demand[h_step]
            tank_flow_volume_time_step = H.TankVolume[h_step]
            for n in range(num_nodes):
                if index_omitted_nodes.count(n + 1) > 0:
                    count_nodes_lagrangian += 0
                else:
                    count_nodes_lagrangian += 1
                    flag_reservoir = 0
                    # Getting the demand of node
                    node_demand = node_demand_time_step[n]

                    if index_reservoirs.count(n + 1) > 0:
                        # Checking for reservoir
                        flag_reservoir = 1
                        for sp in range(bulk_wq_parameter_num):
                            if wq_step == 1:
                                node_conc_array_a[sp][wq_step - 1][n] = (
                                    reservoir_quality_mat[
                                        index_reservoirs.index(n + 1)
                                    ][sp]
                                )
                            else:
                                node_conc_array_a[sp][wq_step - 1][n] = (
                                    reservoir_quality_mat[
                                        index_reservoirs.index(n + 1)
                                    ][sp]
                                    * reservoir_pattern[index_reservoirs.index(n + 1)][
                                        reservoir_pattern_step - 1
                                    ][sp]
                                )
                    elif index_tanks.count(n + 1) > 0:
                        # Checking for tank
                        t = index_tanks.index(n + 1)
                        # Getting tank volume
                        tank_flow_volume = tank_flow_volume_time_step[n]
                        tank_flow_volume_mat[wq_step - 1][t] = tank_flow_volume
                        tank_flow_volume_prev = tank_flow_volume_mat[wq_step - 2][t]
                        links_connecting_to_node = fn.incoming_links(n, end_node_mat)
                        links_connecting_from_node = fn.outgoing_links(
                            n, start_node_mat
                        )
                        num_incoming_links = len(links_connecting_to_node)
                        num_outgoing_links = len(links_connecting_from_node)
                        mass_incoming_mat = np.zeros((bulk_wq_parameter_num, 1))
                        tank_outflow = 0
                        for i in range(num_incoming_links):
                            incoming_link = links_connecting_to_node[i]
                            if index_omitted_links.count(incoming_link + 1) > 0:
                                break
                            else:
                                link_flow_rate = link_flow_rate_time_step[incoming_link]
                                if link_flow_rate >= 0:
                                    pos = int(
                                        link_conc_data_points_mat[wq_step - 1][
                                            incoming_link
                                        ]
                                        - 1
                                    )
                                    for sp in range(bulk_wq_parameter_num):
                                        mass_incoming_mat[sp][0] = (
                                            mass_incoming_mat[sp][0]
                                            + abs(link_flow_rate)
                                            * link_conc_array_a[sp][pos][incoming_link]
                                        )
                                else:
                                    tank_outflow = tank_outflow + abs(link_flow_rate)
                        for o in range(num_outgoing_links):
                            outgoing_link = links_connecting_from_node[o]
                            if index_omitted_links.count(outgoing_link + 1) > 0:
                                break
                            else:
                                link_flow_rate = link_flow_rate_time_step[outgoing_link]
                                if link_flow_rate < 0:
                                    pos = 0
                                    for sp in range(bulk_wq_parameter_num):
                                        mass_incoming_mat[sp][0] = (
                                            mass_incoming_mat[sp][0]
                                            + abs(link_flow_rate)
                                            * link_conc_array_a[sp][pos][outgoing_link]
                                        )
                                else:
                                    tank_outflow = tank_outflow + abs(link_flow_rate)
                        for sp in range(bulk_wq_parameter_num):
                            if wq_step == 1:
                                tank_flow_volume_prev = tank_flow_volume
                                tank_initial_conc = node_conc_initial_mat[n][sp]
                            else:
                                tank_initial_conc = node_conc_array_a[sp][wq_step - 2][
                                    n
                                ]
                            # CSTR model
                            node_conc_array_a[sp][wq_step - 1][n] = (
                                tank_flow_volume_prev * tank_initial_conc
                                + mass_incoming_mat[sp][0] * wq_sim_time_step_s
                            ) / (tank_flow_volume + tank_outflow * wq_sim_time_step_s)
                        # Reactions
                        delta = module.tank_reaction(
                            wq_sim_time_step_s,
                            wq_step,
                            n,
                            tank_flow_volume_prev,
                            tank_flow_volume,
                            variable_values_mat[wq_iteration_count - 1],
                            node_conc_initial_mat,
                            node_conc_array_a,
                        )
                        for sp in range(bulk_wq_parameter_num):
                            node_conc_array_a[sp][wq_step - 1][n] = (
                                node_conc_array_a[sp][wq_step - 1][n] + delta[sp]
                            )

                        # Check for injection node
                        for sp in range(bulk_wq_parameter_num):
                            if (
                                index_injection_nodes.count(n + 1) > 0
                                and injection_quality_mat[
                                    index_injection_nodes.index(n + 1)
                                ][sp]
                                != 0
                            ):
                                if wq_step == 1:
                                    node_conc_array_a[sp][wq_step - 1][n] = (
                                        injection_quality_mat[
                                            index_injection_nodes.index(n + 1)
                                        ][sp]
                                    )
                                else:
                                    node_conc_array_a[sp][wq_step - 1][n] = (
                                        injection_quality_mat[
                                            index_injection_nodes.index(n + 1)
                                        ][sp]
                                        * injection_pattern[
                                            index_injection_nodes.index(n + 1)
                                        ][injection_pattern_step - 1][sp]
                                    )
                        node_conc_array_a[node_conc_array_a < 0] = 0
                    else:
                        node_outflow = abs(node_demand)
                        links_connecting_to_node = fn.incoming_links(n, end_node_mat)
                        links_connecting_from_node = fn.outgoing_links(
                            n, start_node_mat
                        )
                        num_incoming_links = len(links_connecting_to_node)
                        num_outgoing_links = len(links_connecting_from_node)
                        incoming_flow = 0
                        outgoing_flow = 0
                        mass_incoming_mat = np.zeros((bulk_wq_parameter_num, 1))
                        for i in range(num_incoming_links):
                            incoming_link = links_connecting_to_node[i]
                            if index_omitted_links.count(incoming_link + 1) > 0:
                                break
                            else:
                                link_flow_rate = link_flow_rate_time_step[incoming_link]
                                if link_flow_rate >= 0:
                                    pos = (
                                        int(
                                            link_conc_data_points_mat[wq_step - 1][
                                                incoming_link
                                            ]
                                        )
                                        - 1
                                    )
                                    for sp in range(bulk_wq_parameter_num):
                                        mass_incoming_mat[sp][0] = (
                                            mass_incoming_mat[sp][0]
                                            + abs(link_flow_rate)
                                            * link_conc_array_a[sp][pos][incoming_link]
                                        )
                                else:
                                    outgoing_flow = outgoing_flow + abs(link_flow_rate)
                        for o in range(num_outgoing_links):
                            outgoing_link = links_connecting_from_node[o]
                            if index_omitted_links.count(outgoing_link + 1) > 0:
                                break
                            else:
                                link_flow_rate = link_flow_rate_time_step[outgoing_link]
                                if link_flow_rate < 0:
                                    pos = (
                                        int(
                                            link_conc_data_points_mat[wq_step - 1][
                                                outgoing_link
                                            ]
                                        )
                                        - 1
                                    )
                                    for sp in range(bulk_wq_parameter_num):
                                        mass_incoming_mat[sp][0] = (
                                            mass_incoming_mat[sp][0]
                                            + abs(link_flow_rate)
                                            * link_conc_array_a[sp][pos][outgoing_link]
                                        )
                                else:
                                    outgoing_flow = outgoing_flow + abs(link_flow_rate)
                        total_outflow = node_outflow + outgoing_flow
                        if total_outflow == 0:
                            for sp in range(bulk_wq_parameter_num):
                                node_conc_array_a[sp][wq_step - 1][n] = 0
                        else:
                            for sp in range(bulk_wq_parameter_num):
                                node_conc_array_a[sp][wq_step - 1][n] = (
                                    mass_incoming_mat[sp][0] / total_outflow
                                )

                        # Check for injection node
                        for sp in range(bulk_wq_parameter_num):
                            if (
                                index_injection_nodes.count(n + 1) > 0
                                and injection_quality_mat[
                                    index_injection_nodes.index(n + 1)
                                ][sp]
                                != 0
                            ):
                                if wq_step == 1:
                                    node_conc_array_a[sp][wq_step - 1][n] = (
                                        injection_quality_mat[
                                            index_injection_nodes.index(n + 1)
                                        ][sp]
                                    )
                                else:
                                    node_conc_array_a[sp][wq_step - 1][n] = (
                                        injection_quality_mat[
                                            index_injection_nodes.index(n + 1)
                                        ][sp]
                                        * injection_pattern[
                                            index_injection_nodes.index(n + 1)
                                        ][injection_pattern_step - 1][sp]
                                    )
                    if flag_reservoir == 0:
                        for i in range(num_incoming_links):
                            incoming_link = links_connecting_to_node[i]
                            if index_omitted_links.count(incoming_link + 1) > 0:
                                break
                            else:
                                link_flow_rate = link_flow_rate_time_step[incoming_link]
                                if link_flow_rate >= 0:
                                    pos = (
                                        int(
                                            link_conc_data_points_mat[wq_step - 1][
                                                incoming_link
                                            ]
                                        )
                                        - 1
                                    )
                                else:
                                    pos = 0

                                for sp in range(bulk_wq_parameter_num):
                                    link_conc_array_a[sp][pos][incoming_link] = (
                                        node_conc_array_a[sp][wq_step - 1][n]
                                    )
                        for o in range(num_outgoing_links):
                            outgoing_link = links_connecting_from_node[o]
                            if index_omitted_links.count(outgoing_link + 1) > 0:
                                break
                            else:
                                link_flow_rate = link_flow_rate_time_step[outgoing_link]
                                if link_flow_rate >= 0:
                                    pos = 0
                                else:
                                    pos = (
                                        int(
                                            link_conc_data_points_mat[wq_step - 1][
                                                outgoing_link
                                            ]
                                        )
                                        - 1
                                    )

                                for sp in range(bulk_wq_parameter_num):
                                    link_conc_array_a[sp][pos][outgoing_link] = (
                                        node_conc_array_a[sp][wq_step - 1][n]
                                    )
            if count_nodes_lagrangian != (num_nodes - num_omitted_nodes):
                print("Error in Lagrangian stage dedicated to nodes!")
                exit()
            link_conc_array = copy.deepcopy(link_conc_array_a)
            node_conc_array = copy.deepcopy(node_conc_array_a)
            wq_time += wq_sim_time_step_s
        print(
            "Water quality simulation (Iteration %d) completed." % (wq_iteration_count)
        )
        # Creating folder to save simulation results
        folder_name = "Results_Iteration" + str(wq_iteration_count)
        path = os.path.join(getcwd(), folder_name)
        if os.path.exists(path):
            print(
                "Output folder already exists in the directory. No new folder created."
            )
        else:
            os.makedirs(path)
        # Reporting the water quality simulation results
        reporting_time_cycle_s = wq_sim_days * 24 * 3600
        reporting_time_steps = (reporting_time_cycle_s / wq_sim_time_step_s) + 1
        reporting_step_start = total_wq_steps - reporting_time_steps
        reporting_step_end = total_wq_steps
        node_conc_report = np.zeros(
            (bulk_wq_parameter_num, int(reporting_time_steps), num_nodes)
        )
        for sp in range(bulk_wq_parameter_num):
            node_conc_report[sp] = node_conc_array[sp][
                int(reporting_step_start) : int(reporting_step_end) + 1
            ]
        time_mat = np.zeros((int(reporting_time_steps), 1))
        for t in range(int(reporting_time_steps)):
            time_mat[t] = (t * wq_sim_time_step_s) / 3600
        data_time = pd.DataFrame(time_mat)
        # Printing the time versus node concentration as Excel
        file_path1 = os.path.join(path, "Time versus node_concentration.xlsx")
        w1 = pd.ExcelWriter(file_path1, engine="xlsxwriter")
        for sp in range(bulk_wq_parameter_num):
            data_conc = pd.DataFrame(node_conc_report[sp])
            data = pd.concat([data_time, data_conc], axis=1)
            data.to_excel(w1, sheet_name="Bulk parameter " + str(sp + 1))
        data_water_age = pd.DataFrame(
            Q.NodeQuality[int(reporting_step_start) : int(reporting_step_end) + 1]
        )
        data_water_age_out = pd.concat([data_time, data_water_age], axis=1)
        data_water_age_out.to_excel(w1, sheet_name="Water age")
        w1.close()
        print("Excel files created.")
        wq_iteration_count += 1
    file_path2 = "Quality Input values.xlsx"
    w2 = pd.ExcelWriter(file_path2, engine="xlsxwriter")
    for i in range(num_reservoirs):
        data_source_quality = pd.DataFrame(reservoir_quality[i])
        data_source_quality.to_excel(w2, sheet_name="Source Quality " + str(i + 1))
    if len(injection_quality) != 0:
        for i in range(len(injection_quality)):
            data_injection_quality = pd.DataFrame(injection_quality[i])
            data_injection_quality.to_excel(
                w2, sheet_name="Injection Quality " + str(i + 1)
            )
    data_para = pd.DataFrame(variable_values_mat)
    data_para.to_excel(w2, sheet_name="Parameter values")
    w2.close()
    print("Anlysis completed...")
    print("Simulation time in seconds is %f" % (time.time() - start_time))
    exit()
