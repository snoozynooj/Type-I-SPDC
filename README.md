# Type-I-SPDC
Different folder is for calculating different things.
## **2d-Map-deff** 
This folder will is all about produce d_eff map for any given biaxial crystals as function of theta (0 to 180) and phi (0 to 360). A file name called database in this folder have all the information about the crystals which is required by deff.sh file.
Description of database file:
Column 1 : Name of crystals
Column 2 : Type of crystal
Column 3 : Band gap of the crystal
Column 4 : Signal wavelength for SPDC

After you run deff.sh file, it will produce *.csv files corresponding to the crystal. For example
### TAKRIJ-2dmap.csv
Column 1 is deff value in pm/V, Coulmn 2 is theta value and Column 3 is phi value
1.76799997000000e-8 0.0 0.0
1.69511053422187e-8 0.0 1.0
1.61875481514561e-8 0.0 2.0
1.53909433938836e-8 0.0 3.0
1.45629934681548e-8 0.0 4.0
1.37054833857782e-8 0.0 5.0
1.28202760260607e-8 0.0 6.0
1.19093071785802e-8 0.0 7.0
1.09745803867329e-8 0.0 8.0
