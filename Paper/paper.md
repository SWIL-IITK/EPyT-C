---
title: 'EPyT-C: A Python package for water quality modeling in water distribution systems'
tags:
  - Python
  - EPANET
  - Water distribution
  - Water quality
  - Chlorine
  - Bacteria
authors:
  - name: Gopinathan R. Abhijith
    corresponding: true
    orcid: 0000-0002-7390-7848
    affiliation: 1
  - name: G Jaykrishnan
    orcid: 0000-0002-2225-0866
    affiliation: 2
  - name: Avi Ostfeld
    orcid: 0000-0001-9112-6079
    affiliation: 3
affiliations:
 - name: Department of Civil Engineering, Indian Institute of Technology Kanpur, Kanpur, UP, India
   index: 1
 - name: Faculty of Data and Decision Sciences, Technion - Israel Institute of Technology, Haifa, Israel
   index: 2
 - name: Faculty of Civil and Environmental Engineering, Technion - Israel Institute of Technology, Haifa, Israel
   index: 3
date: 24 January 2024
bibliography: paper.bib

---

# Summary

Water distribution systems (WDS) comprise numerous components, such as reservoirs, tanks, pipes, and hydraulic control elements. Arguably, being one of the most critical infrastructures of every society, they are vulnerable to accidents, attacks, and related drinking water quality-associated public health risks owing to their spatial spread and accessibility. Computer-based tools that simulate water quality variations in WDS are functional solutions for monitoring WDS integrity. This paper presents EPyT-C (in which C stands for contaminant), a Python-based package allowing the simulation of the transport and fate of multiple water quality parameters in WDS. EPyT-C constitute in-built modules that conceptualize the scientific understanding of the physical, physicochemical, and biochemical interactions concerning water quality parameters within the distribution network realm, mathematize them as one-dimensional advective-reactive equations, and numerically solve them to emulate the spatiotemporal distribution of the quality of water delivered via WDS. 

# Statement of need

Generally, computer-based water quality simulation tools for WDS built on mathematical models depict the time-series behavior of water quality parameters within the WDS. EPANET-MSX [@shang2007] has become the de-facto WDS water quality modeling tool due to its direct collaboration with EPANET 2.0 [@rossman2000], the most commonly used software package for WDS modeling. Nevertheless, two challenges are encountered while using EPANET-MSX for WDS water quality modeling. They are (a) the conceptualization of the physical, physicochemical, and biochemical interactions between water quality parameters and (b) the evolution of scientific depictions (generating mathematical expressions) of these interactions. In addition, owing to its complex user interface, the EPANET-MSX application requires programming knowledge. To overcome these limitations of the EPANET-MSX application, [@abhijith2022a] have built EPANET-C, which comprises in-built function directories integrating all the input information required for executing EPANET-MSX. EPANET-C also simplified EPANET-MSX execution by providing a simple command-line MATLAB interface with an exhaustive set of instructions. 

However, EPANET-C, utilizing EPANET-MSX solver for solving advective-reactive equations, can be quite computationally intensive when solving stiff equations [@abhijith2021]. Also, EPANET-C is based on MATLAB, a commercial numeric computing environment. If available in Python, a user-friendly and more portable open-source language, such a simulation tool could become accessible to the scientific community and water supply managers. This paper presents EPyT-C, an open-source umbrella WDS water quality modeling tool based on the recently developed EPANET-Python Toolkit (EPyT) to help researchers and practitioners in the WDS analysis domain. Users are welcome to further develop, improve, and extend these open-source scripts. Above and beyond, further modifications will be added to enhance the capability of EPyT-C to simulate the fate and transport of numerous water quality parameters and to introduce the effects of dispersion in WDS water quality modeling.

# Functionality

EPyT is an open-source software, initially developed by the KIOS Research and Innovation Center of Excellence, University of Cyprus, operating within the Python environment to provide a programming interface for the latest version of EPANET 2.2 [@rossman2020]. It calls EPANET a shared object and employs an Object-Oriented approach for interfacing EPANET with Python. Though EPyT can be employed for performing single-species water quality analysis, which comes within the scope of EPANET 2.2, it lacks multi-species reactive-transport modeling capability in its current form. In other words, EPyT can only analyze one water quality parameter at a time. Consequently, the water quality modeling compartment of EPyT needs to be improved to solve several real-world problems concerning water quality variations during delivery via WDS. A fully independent water quality modeling extension, EPyT-C, is developed in this direction. EPyT-C employs the hydraulic solver of EPANET 2.2 for performing hydraulic simulation, which the in-built water quality solver then utilizes for performing MSRT modeling. The conceptual framework of EPyT-C is described in Figure 1.

<figure>
<figcaption align = "center"><b>Figure 1</b>. Conceptual framework of EPyT-C.</figcaption>
<img src="Figure 1.png" width="1024"/>
</figure>

In its current form, EPyT-C comprises four in-built modules - the 'Chlorine decay and Trihalomethanes formation' module, the 'Bacterial regrowth' module, the 'Arsenite oxidation and arsenate attachment/detachment' module, and the 'Perfluorooctanoic acid formation' module. The details of the four modules (number and characteristics of water quality parameters, the type of reactions considered) are detailed in Table 1. Based on the module selected for WDS analysis, EPyT-C evolves governing (partial differential and ordinary differential) equations emulating the propagation and formation/ degradation of the corresponding water quality parameters within the distribution network realm. Once the governing equations (one-dimensional advective-reactive equations) are framed, the numerical method that involves the explicit method of characteristics and the fourth-order Runge-Kutta method, initially presented by [@tzatchkov2002], is applied to derive numerical solutions - spatiotemporal distribution of complex water quality parameters in WDS.

Insert Table 1 here.

|     EPyT-C module    |    Water quality parameters considered and their units     |    Processes considered within the pipe domain    |
|    ---------------   |    ---------------                                         |    ---------------                                |
|    Chlorine decay and Trihalomethanes formation               |    Bulk phase: (1) chlorine (mg/L); (2) total organic carbon, TOC (mg/L); and (3) trihalomethanes, THMs (ug/L).                                                     |    (1) chlorine - TOC reaction leading to chlorine decay, TOC degradation, and THMs formation; (2) mass-transfer of chlorine from bulk to wall phase; and (3) wall reactions of chlorine leading to its decay.                                           |
|    Bacterial regrowth               |    Bulk phase: (1) chlorine (mg/L); (2) recalcitrant dissolved organic carbon, RDOC (mg/L); (3) biodegradable DOC, BDOC (mg/L); (4) free living bacteria, FLB (CFU/L); and (5) free dead bacteria, FDB (cells/L).                                                     |    (1) chlorine - RDOC reaction leading to chlorine decay and RDOC degradation; (2) chlorine - BDOC reaction leading to chlorine decay and BDOC degradation; (3) mass-transfer of chlorine from bulk to wall phase; and (4) wall reactions of chlorine leading to its decay; (5) bacterial growth and subsequent BDOC utilization; (6) bacterial mortality and FDB formation; and (7) FDB cell lysis and BDOC contribution.                                            | |
|    Arsenite oxidation and arsenate attachment/detachment               |    Bulk phase: (1) aqueous arsenite (mg/L); (2) aqueous arsenate (mg/L); (3) aqueous arsenic (mg/L); (4) residual chlorine (mg/L); and (5) TOC (mg/L).
Wall phase: (1) adsorbed arsenate (mg/m2).
                                                     |    (1) chlorine - TOC reaction leading to chlorine decay, TOC degradation, and THMs formation; (2) mass-transfer of chlorine from bulk to wall phase; (3) wall reactions of chlorine leading to its decay; (4) chlorine – aqueous arsenite reaction leading to arsenite oxidation to arsenate and subsequent chlorine decay; (5) adsorption/ desorption of arsenate within the bulk-wall phase interface.                                             | |
|    Perfluorooctanoic acid formation               |    Bulk phase: (1) chlorine (mg/L); (2) TOC (mg/L); (3) perfluoro octaneamido betaine, PFOAB (ng/L); (4) perfluoro octaneamido ammonium salt, PFOAAmS (ng/L); and perfluorooctanoic acid, PFOA (ng/L).                                                     |    (1) chlorine - TOC reaction leading to chlorine decay, TOC degradation, and THMs formation; (2) mass-transfer of chlorine from bulk to wall phase; (3) wall reactions of chlorine leading to its decay; (4) chlorine - PFOAB reaction leading to chlorine decay, PFOAB degradation, and PFOA formation; and (5) chlorine - PFOAAmS reaction leading to chlorine decay, PFOAAmS degradation, and PFOA formation.                                            | |

EPyT-C offers the following flexibilities, making it a handy tool for research and industry:
1. Allows time-series variations in the input values for the water quality parameters at the sources (reservoirs and booster nodes).
2. Customize the random fluctuations in the input values for the water quality parameters at the sources.
3. Customize the perturbations in the reaction rate coefficient values.
4. Customize the outputs and export the data as Excel files or other formats.
5. Customize the numerical accuracy by altering the model parameters (time step, velocity tolerance, etc.).
6. Control the computational efficiency by adjusting the accuracy of the numerical solutions.

# Example

To demonstrate the applicability of EPyT-C, an example problem is considered. This idealizes the real-world problem of understanding the effects of booster/ secondary chlorination in WDS. The EPANET Example Network 3 [@rossman2000], which is the adaptation of the North Marin Water District WDS, USA, is considered as the test network. It has 92 demand nodes, with a total base demand of 709.2 L/s and 117 pipes totaling a length of 65.8 km. The water is delivered from two sources (Lake and River) via pumping. The test network also includes three overhead storage tanks. The TOC concentration of the treated water delivered from the water treatment plants (WTPs) associated with the lake and river sources was considered to be 3.55 mg/L and 0.56 mg/L, respectively. The mean chlorine concentration to be maintained at the two WTP outlets was assumed to be 1.0 mg/L. The demand nodes with IDs' 113' and '205' were arbitrarily selected as potential booster nodes, and the booster chlorine loading was selected such that the mean chlorine concentration of water leaving these two nodes would be 1.0 mg/L.
Four cases (A, B, C, and D) were considered to comprehend the suitability of booster chlorination at the two selected booster nodes. Case A corresponds to the base case with no booster chlorination. Under Case B and Case C, demand nodes '113' and '205', respectively, are the only booster nodes. Meanwhile, under Case D, both the nodes ('113' and '205') function as booster nodes. The 'Chlorine decay and Trihalomethanes formation' module of EPyT-C was selected for the analysis. The number of iterations corresponding to each case was set as 50 to comprehend the effects of random variations (±10 %) in the input parameters and the perturbations in the reaction rate coefficients on the model outputs (time series variations of chlorine, TOC, and THMs concentrations at the 92 demand nodes and the three tanks). The simulation time period was kept at 10 days, and the default values of EPyT-C were used for all the other inputs. The codes used for the example problem are provided in the repository.

Figure 2 depicts the variations in the chlorine concentrations at the 92 demand nodes, two source nodes, and the three tanks predicted using the selected module of EPyT-C under the four cases. As can be seen, the variability of chlorine predictions is reasonably high and was significantly caused by the variabilities in the reaction rate coefficients integrated into the simulations using EPyT-C. From Figure 2, we can also perceive the effects of booster chlorination at nodes '113' and '205' on the relative distribution of chlorine in the network. As expected, Case D, considering simultaneous booster chlorination at nodes '113' and '205' has increased the mean chlorine concentration at the remaining 90 demand nodes and the three overhead tanks. Figure 3a is provided to evaluate the percentage of nodes that benefit from the booster chlorination under cases B, C, and D. Under Case A, in the absence of booster chlorination, 71% of the nodes were estimated to have a mean chlorine concentration greater than 0.4 mg/L. Upon booster chlorination at nodes '113' and '205' (Case D), this number increased to 97%, and only one node was found to have a chlorine concentration of less than 0.3 mg/L. The selected module of EPyT-C offers the ability to simulate THMs formation simultaneously with the chlorine decay (and with TOC degradation). Figure 3 also shows that as more chlorine is injected into the system, more THMs (by-products of chlorination that have carcinogenic effects) are formed. Under Case A, over 95% of the nodes get water with THMs concentration of less than 80 µg/L, which is the regulatory limit put forth by the United States Environmental Protection Agency [@usepa2006]. However, under Case D, this value decreased to 84%. Interestingly, this value was much lower under Case C (Figure 3b) when the amount of chlorine injected was lesser relative to Case D. It can be presumed that this incongruity is entirely related to the perturbations in the reaction rate coefficients considered and also because 50 is not the ideal number of iterations to reflect the uncertainties of the reactions concerning chlorine decay and THMs formation [@abhijith2022b].

<figure>
<figcaption align = "center"><b>Figure 2</b>. Predicted distribution of cholorine concentration in the nodes of the test network under the four cases considered. The crimson red circles depict the mean of the average chlorine concentrations predicted at the nodes during the 50 Monte Carlo simulations. The cyan lines show the difference between the minimum and maximum of these average chlorine concentration predictions.</figcaption>
<img src="Figure 2.png" width="1024"/>
</figure>

<figure>
<figcaption align = "center"><b>Figure 3</b>. </b>(a)</b> Percentage of nodes with mean chlorine concentration greater than the reference values and </b>(b)</b> percentage of nodes with mean THMs concentration lesser than the reference values. The reference values are denoted in the abscissa.</figcaption>
<img src="Figure 3.png" width="1024"/>
</figure>

# Conclusion

EPyT-C is a practical tool that can assist the scientific community and water utility managers in examining WDS performance under different operating scenarios. EPyT-C scripts are under continuous development and can be further extended and improved by users and developers for specific applications. Forthcoming works involve advancing EPyT-C modeling capability to simulate dispersive transport.

# Acknowledgements

This research was supported by a grant from the Ministry of Science and Technology of the State of Israel and the Federal Ministry of Education and Research (BMBF), Germany.

# References
