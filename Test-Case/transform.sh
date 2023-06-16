
#!/bin/bash
cp BIBO.csv  BIBOtemp.csv
sed -i "s/X/P/g" BIBOtemp.csv
sed -i "s/Y/Q/g" BIBOtemp.csv
sed -i "s/Z/R/g" BIBOtemp.csv
sed -i "s/P/X/g" BIBOtemp.csv
sed -i "s/Q/Z/g" BIBOtemp.csv
sed -i "s/R/Y/g" BIBOtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/BIBOtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > BIBO.csv1
rm BIBOtemp.csv

