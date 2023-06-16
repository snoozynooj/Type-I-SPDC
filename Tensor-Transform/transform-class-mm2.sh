
#!/bin/bash
cp HONCOF.csv  HONCOFtemp.csv
sed -i "s/X/P/g" HONCOFtemp.csv
sed -i "s/Y/Q/g" HONCOFtemp.csv
sed -i "s/Z/R/g" HONCOFtemp.csv
sed -i "s/P/X/g" HONCOFtemp.csv
sed -i "s/Q/Y/g" HONCOFtemp.csv
sed -i "s/R/Z/g" HONCOFtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/HONCOFtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > HONCOF.csv1
rm HONCOFtemp.csv

cp DIFKOS.csv    DIFKOStemp.csv
sed -i "s/X/P/g" DIFKOStemp.csv
sed -i "s/Y/Q/g" DIFKOStemp.csv
sed -i "s/Z/R/g" DIFKOStemp.csv
sed -i "s/P/Y/g" DIFKOStemp.csv
sed -i "s/Q/X/g" DIFKOStemp.csv
sed -i "s/R/Z/g" DIFKOStemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/DIFKOStemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > DIFKOS.csv1
rm DIFKOStemp.csv


cp FEHJIN.csv    FEHJINtemp.csv
sed -i "s/X/P/g" FEHJINtemp.csv
sed -i "s/Y/Q/g" FEHJINtemp.csv
sed -i "s/Z/R/g" FEHJINtemp.csv
sed -i "s/P/Y/g" FEHJINtemp.csv
sed -i "s/Q/Z/g" FEHJINtemp.csv
sed -i "s/R/X/g" FEHJINtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/FEHJINtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > FEHJIN.csv1
rm FEHJINtemp.csv

cp VEKNEH.csv    VEKNEHtemp.csv
sed -i "s/X/P/g" VEKNEHtemp.csv
sed -i "s/Y/Q/g" VEKNEHtemp.csv
sed -i "s/Z/R/g" VEKNEHtemp.csv
sed -i "s/P/Y/g" VEKNEHtemp.csv
sed -i "s/Q/X/g" VEKNEHtemp.csv
sed -i "s/R/Z/g" VEKNEHtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/VEKNEHtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > VEKNEH.csv1
rm VEKNEHtemp.csv


cp NUYWUA.csv    NUYWUAtemp.csv
sed -i "s/X/P/g" NUYWUAtemp.csv
sed -i "s/Y/Q/g" NUYWUAtemp.csv
sed -i "s/Z/R/g" NUYWUAtemp.csv
sed -i "s/P/Y/g" NUYWUAtemp.csv
sed -i "s/Q/Z/g" NUYWUAtemp.csv
sed -i "s/R/X/g" NUYWUAtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/NUYWUAtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > NUYWUA.csv1
rm NUYWUAtemp.csv

cp IVAZUA01.csv    IVAZUA01temp.csv
sed -i "s/X/P/g" IVAZUA01temp.csv
sed -i "s/Y/Q/g" IVAZUA01temp.csv
sed -i "s/Z/R/g" IVAZUA01temp.csv
sed -i "s/P/X/g" IVAZUA01temp.csv
sed -i "s/Q/Y/g" IVAZUA01temp.csv
sed -i "s/R/Z/g" IVAZUA01temp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/IVAZUA01temp/g" arrange1.f90
gfortran arrange1.f90
./a.out > IVAZUA01.csv1
rm IVAZUA01temp.csv

cp FIQGEU.csv    FIQGEUtemp.csv
sed -i "s/X/P/g" FIQGEUtemp.csv
sed -i "s/Y/Q/g" FIQGEUtemp.csv
sed -i "s/Z/R/g" FIQGEUtemp.csv
sed -i "s/P/X/g" FIQGEUtemp.csv
sed -i "s/Q/Z/g" FIQGEUtemp.csv
sed -i "s/R/Y/g" FIQGEUtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/FIQGEUtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > FIQGEU.csv1
rm FIQGEUtemp.csv

cp OXUNUR.csv    OXUNURtemp.csv
sed -i "s/X/P/g" OXUNURtemp.csv
sed -i "s/Y/Q/g" OXUNURtemp.csv
sed -i "s/Z/R/g" OXUNURtemp.csv
sed -i "s/P/Z/g" OXUNURtemp.csv
sed -i "s/Q/X/g" OXUNURtemp.csv
sed -i "s/R/Y/g" OXUNURtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/OXUNURtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > OXUNUR.csv1
rm OXUNURtemp.csv


cp LBO.csv       LBOtemp.csv
sed -i "s/X/P/g" LBOtemp.csv
sed -i "s/Y/Q/g" LBOtemp.csv
sed -i "s/Z/R/g" LBOtemp.csv
sed -i "s/P/Y/g" LBOtemp.csv
sed -i "s/Q/Z/g" LBOtemp.csv
sed -i "s/R/X/g" LBOtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/LBOtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > LBO.csv1
rm LBOtemp.csv
