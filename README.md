# Type-I-SPDC
A different folder is for calculating different things.
## **Phase_Matching + G2 + Photon_Count** 
This folder is all about producing phase-matching angles, $G^{(2)}$ and photon count. There is a file called the ***database*** which has information about all the crystals used in this study. 

Description of database file: 
- Column 1: Name of crystals
- Column 2: Type of crystal
- Column 3: Band gap of the crystal
- Column 4: Signal wavelength for SPDC

After you run deff.sh file, it will produce three files corresponding to the crystal. For example, if the crystal name is RATDAS01, it will produce the following files.

**1: RATDAS01-Count.txt**

nx(w), ny(w), nz(w), nx(2w), ny(2w), nz(2w)

1.545739 1.553462 1.611269 1.564891 1.573036 1.634139

Optimum phase matching: 142.5 29.8 0.533167931611107

Crystal: Positive biaxial

Photon Count: 4258840.787977502 s^-1 mW^-1 mm^-1

Correlation time: 1.1923320604724541e-14 s

**2: RATDAS01-phasematching-deff.csv** - This file has all the possible phase-matching angles and d<sub>eff</sub> at those angles. Column 1, Column 2, and Column 3 represent $d_{eff}$, $\theta$, and $\phi$. 

**3: RATDAS01-G2.csv** - This file can be used to plot $G^{(2)}$. Column 1 is \tau (c) and Column 2 is $G^{(2)}$ ($\tau / \tau_o$)
