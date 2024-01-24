# EPyT-C - Fully independent multi-species reactive transport modelling extension for EPyT (EPANET-Python) toolkit

An open-source Python package for modeling water quality in water distribution systems.

# EPyT (EPANET-Python) toolkit
EPyT is an open-source software, initially developed by the KIOS Research and Innovation Center of Excellence, University of Cyprus, operating within the Python environment for providing a PYTHON programming interface for the latest version of EPANET (Rossman et al., 2020). It calls EPANET as a shared object and employs an Object-Oriented approach for interfacing EPANET with PYTHON.


# Water quality modeling extensions of EPyT-C

Though EPyT can be employed for performing water quality analysis, which comes within the scope of EPANET 2.2, it does not have any multi-species reactive-transport (MSRT) modeling capability in its current form. A fully independent water quality modeling extension, EPyT-C (in which C stands for contaminant), is developed toward this limitation. The source code of EPyT-C calls EPyT and employs the hydraulic solver of EPANET 2.2 for performing hydraulic simulation, which the in-built water quality solver then utilizes for performing MSRT modeling.
	
 The default modules of EPyT-C conceptualize scientific knowledge about the physical, physicochemical, and biochemical exchanges concerning water quality, mathematize them as partial differential equations (PDE), and numerically solve them to simulate the spatiotemporal distribution of complex water quality parameters in WDS. EPyT-C employs the numerical method initially presented by (Tzatchkov et al., 2002), which solves the advective-reactive equations by combining the explicit method of characteristics and the fourth-order Runge-Kutta method.

## EPyT-C is now equipped with four MSRT modules.

|     EPyT-C module    |    Water quality parameters considered and their units     |    Processes considered within the pipe domain    |
|    ---------------   |    ---------------                                         |    ---------------                                |
|    Chlorine decay and Trihalomethanes formation               |    Bulk phase: (1) chlorine (mg/L); (2) total organic carbon, TOC (mg/L); and (3) trihalomethanes, THMs (ug/L).                                                     |    (1) chlorine - TOC reaction leading to chlorine decay, TOC degradation, and THMs formation; (2) mass-transfer of chlorine from bulk to wall phase; and (3) wall reactions of chlorine leading to its decay.                                           |
|    Bacterial regrowth               |    Bulk phase: (1) chlorine (mg/L); (2) recalcitrant dissolved organic carbon, RDOC (mg/L); (3) biodegradable DOC, BDOC (mg/L); (4) free living bacteria, FLB (CFU/L); and (5) free dead bacteria, FDB (cells/L).                                                     |    (1) chlorine - RDOC reaction leading to chlorine decay and RDOC degradation; (2) chlorine - BDOC reaction leading to chlorine decay and BDOC degradation; (3) mass-transfer of chlorine from bulk to wall phase; and (4) wall reactions of chlorine leading to its decay; (5) bacterial growth and subsequent BDOC utilization; (6) bacterial mortality and FDB formation; and (7) FDB cell lysis and BDOC contribution.                                            |
|    Arsenite oxidation and arsenate attachment/detachment               |    Bulk phase: (1) aqueous arsenite (mg/L); (2) aqueous arsenate (mg/L); (3) aqueous arsenic (mg/L); (4) residual chlorine (mg/L); and (5) TOC (mg/L). Wall phase: (1) adsorbed arsenate (mg/m<sup>2</sup>).|    (1) chlorine - TOC reaction leading to chlorine decay, TOC degradation, and THMs formation; (2) mass-transfer of chlorine from bulk to wall phase; (3) wall reactions of chlorine leading to its decay; (4) chlorine – aqueous arsenite reaction leading to arsenite oxidation to arsenate and subsequent chlorine decay; (5) adsorption/ desorption of arsenate within the bulk-wall phase interface.  |
|    Perfluorooctanoic acid formation               |    Bulk phase: (1) chlorine (mg/L); (2) TOC (mg/L); (3) perfluoro octaneamido betaine, PFOAB (ng/L); (4) perfluoro octaneamido ammonium salt, PFOAAmS (ng/L); and perfluorooctanoic acid, PFOA (ng/L).                                                     |    (1) chlorine - TOC reaction leading to chlorine decay, TOC degradation, and THMs formation; (2) mass-transfer of chlorine from bulk to wall phase; (3) wall reactions of chlorine leading to its decay; (4) chlorine - PFOAB reaction leading to chlorine decay, PFOAB degradation, and PFOA formation; and (5) chlorine - PFOAAmS reaction leading to chlorine decay, PFOAAmS degradation, and PFOA formation. | 

# Flexibilities

EPyT-C offers the following flexibilities, making it a handy tool for research and industry:
- Allows time-series variations in the input values for the water quality parameters at the sources (reservoirs and booster nodes).
- Customize the random fluctuations in the input values for the water quality parameters at the sources.
- Customize the perturbations in the reaction rate coefficient values.
- Customize the outputs and export the data as Excel files or other formats.
- Customize the numerical accuracy by altering the model parameters (time step, velocity tolerance, etc.).
- Control the computational efficiency by adjusting the accuracy of the numerical solutions.

# Installation

To install EPyT-C:
> pip install epyt_c
    
Alternatively, the sources for EPyT-C can be downloaded from the GitHub repo. You can clone the public repository: 
> https://github.com/grabhijith/EPyT-C

# Dependencies
- EPyT 
- NumPy 1.2.6
- Pandas 2.1.3
- XlsxWriter 3.1.9

# References
Rossman, L.A., Woo, H., Tryby, M., Shang, F., Janke, R., Haxton, T., 2020. Epanet 2.2 User ’s Manual, USEPA. Cincinnati, Ohio.

Tzatchkov, V.G., Aldama, A.A., Arreguin, F.I., 2002. Advection-Dispersion-Reaction Modeling in Water Distribution Networks. J. Water Resour. Plan. Manag. 128, 334–342. https://doi.org/10.1061/(asce)0733-9496(2002)128:5(334)

# Contact

**Gopinbathan R Abhijith** - abhijith@iitk.ac.in

**Avi Ostfeld** - ostfeld@technion.ac.il

# Credits 

The **Smart Water Infrastructure Laboratory**, **Indian Institute of Technology Kanpur** and **Technion Israel Institute of Technology** jointly created this package.
