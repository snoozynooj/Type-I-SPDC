# Type-I-SPDC
Different folder is for calculating different things.
## **2d-Map-deff** 
This folder will is all about produce d_eff map for any given biaxial crystals as function of theta (0 to 180) and phi (0 to 360). A file name called database in this folder have all the information about the crystals which is required by deff.sh file.
Description of database file:
Column 1 : Name of crystals
Column 2 : Type of crystal
Column 3 : Band gap of the crystal
Column 4 : Signal wavelength for SPDC

After you run deff.sh file, it will produce *.csv files corresponding to the crystal and *-result file. For example
### TAKRIJ-2dmap.csv
Column 1 is deff value in pm/V, Coulmn 2 is theta value and Column 3 is phi value
### TAKRIJ-result
omega 1064 2omega 532.0 

1.585116 1.611625 1.687287 1.601634 1.628612 1.712148
Max 135.0 317.0 0.127683535317773
Min 45.0 137.0 -0.127683535317773
True
