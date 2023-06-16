
#!/bin/bash
cp RATDAS01.csv  RATDAS01temp.csv
sed -i "s/X/P/g" RATDAS01temp.csv
sed -i "s/Y/Q/g" RATDAS01temp.csv
sed -i "s/Z/R/g" RATDAS01temp.csv
sed -i "s/P/X/g" RATDAS01temp.csv
sed -i "s/Q/Z/g" RATDAS01temp.csv
sed -i "s/R/Y/g" RATDAS01temp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/RATDAS01temp/g" arrange1.f90
gfortran arrange1.f90
./a.out > RATDAS01.csv1
rm RATDAS01temp.csv

cp TAKRIJ.csv    TAKRIJtemp.csv
sed -i "s/X/P/g" TAKRIJtemp.csv
sed -i "s/Y/Q/g" TAKRIJtemp.csv
sed -i "s/Z/R/g" TAKRIJtemp.csv
sed -i "s/P/X/g" TAKRIJtemp.csv
sed -i "s/Q/Z/g" TAKRIJtemp.csv
sed -i "s/R/Y/g" TAKRIJtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/TAKRIJtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > TAKRIJ.csv1
rm TAKRIJtemp.csv


cp LASPZN.csv    LASPZNtemp.csv
sed -i "s/X/P/g" LASPZNtemp.csv
sed -i "s/Y/Q/g" LASPZNtemp.csv
sed -i "s/Z/R/g" LASPZNtemp.csv
sed -i "s/P/X/g" LASPZNtemp.csv
sed -i "s/Q/Y/g" LASPZNtemp.csv
sed -i "s/R/Z/g" LASPZNtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/LASPZNtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > LASPZN.csv1
rm LASPZNtemp.csv

cp OFUWIV.csv    OFUWIVtemp.csv
sed -i "s/X/P/g" OFUWIVtemp.csv
sed -i "s/Y/Q/g" OFUWIVtemp.csv
sed -i "s/Z/R/g" OFUWIVtemp.csv
sed -i "s/P/Y/g" OFUWIVtemp.csv
sed -i "s/Q/Z/g" OFUWIVtemp.csv
sed -i "s/R/X/g" OFUWIVtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/OFUWIVtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > OFUWIV.csv1
rm OFUWIVtemp.csv


cp FIRZIP.csv    FIRZIPtemp.csv
sed -i "s/X/P/g" FIRZIPtemp.csv
sed -i "s/Y/Q/g" FIRZIPtemp.csv
sed -i "s/Z/R/g" FIRZIPtemp.csv
sed -i "s/P/X/g" FIRZIPtemp.csv
sed -i "s/Q/Z/g" FIRZIPtemp.csv
sed -i "s/R/Y/g" FIRZIPtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/FIRZIPtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > FIRZIP.csv1
rm FIRZIPtemp.csv

cp FIPWUY.csv    FIPWUYtemp.csv
sed -i "s/X/P/g" FIPWUYtemp.csv
sed -i "s/Y/Q/g" FIPWUYtemp.csv
sed -i "s/Z/R/g" FIPWUYtemp.csv
sed -i "s/P/Y/g" FIPWUYtemp.csv
sed -i "s/Q/X/g" FIPWUYtemp.csv
sed -i "s/R/Z/g" FIPWUYtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/FIPWUYtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > FIPWUY.csv1
rm FIPWUYtemp.csv

cp PODREH.csv    PODREHtemp.csv
sed -i "s/X/P/g" PODREHtemp.csv
sed -i "s/Y/Q/g" PODREHtemp.csv
sed -i "s/Z/R/g" PODREHtemp.csv
sed -i "s/P/Y/g" PODREHtemp.csv
sed -i "s/Q/Z/g" PODREHtemp.csv
sed -i "s/R/X/g" PODREHtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/PODREHtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > PODREH.csv1
rm PODREHtemp.csv

cp RUVBAN.csv    RUVBANtemp.csv
sed -i "s/X/P/g" RUVBANtemp.csv
sed -i "s/Y/Q/g" RUVBANtemp.csv
sed -i "s/Z/R/g" RUVBANtemp.csv
sed -i "s/P/Z/g" RUVBANtemp.csv
sed -i "s/Q/X/g" RUVBANtemp.csv
sed -i "s/R/Y/g" RUVBANtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/RUVBANtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > RUVBAN.csv1
rm RUVBANtemp.csv

cp MUYGOE.csv    MUYGOEtemp.csv
sed -i "s/X/P/g" MUYGOEtemp.csv
sed -i "s/Y/Q/g" MUYGOEtemp.csv
sed -i "s/Z/R/g" MUYGOEtemp.csv
sed -i "s/P/Y/g" MUYGOEtemp.csv
sed -i "s/Q/X/g" MUYGOEtemp.csv
sed -i "s/R/Z/g" MUYGOEtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/MUYGOEtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > MUYGOE.csv1
rm MUYGOEtemp.csv

cp NELWUY.csv    NELWUYtemp.csv
sed -i "s/X/P/g" NELWUYtemp.csv
sed -i "s/Y/Q/g" NELWUYtemp.csv
sed -i "s/Z/R/g" NELWUYtemp.csv
sed -i "s/P/Y/g" NELWUYtemp.csv
sed -i "s/Q/Z/g" NELWUYtemp.csv
sed -i "s/R/X/g" NELWUYtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/NELWUYtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > NELWUY.csv1
rm NELWUYtemp.csv
