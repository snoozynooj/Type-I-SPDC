
#!/bin/bash
cp ECIWAO.csv  ECIWAOtemp.csv
sed -i "s/X/P/g" ECIWAOtemp.csv
sed -i "s/Y/Q/g" ECIWAOtemp.csv
sed -i "s/Z/R/g" ECIWAOtemp.csv
sed -i "s/P/Y/g" ECIWAOtemp.csv
sed -i "s/Q/X/g" ECIWAOtemp.csv
sed -i "s/R/Z/g" ECIWAOtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/ECIWAOtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > ECIWAO.csv1
rm ECIWAOtemp.csv

cp AQOROP.csv    AQOROPtemp.csv
sed -i "s/X/P/g" AQOROPtemp.csv
sed -i "s/Y/Q/g" AQOROPtemp.csv
sed -i "s/Z/R/g" AQOROPtemp.csv
sed -i "s/P/Z/g" AQOROPtemp.csv
sed -i "s/Q/Y/g" AQOROPtemp.csv
sed -i "s/R/X/g" AQOROPtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/AQOROPtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > AQOROP.csv1
rm AQOROPtemp.csv


cp KOMMII.csv    KOMMIItemp.csv
sed -i "s/X/P/g" KOMMIItemp.csv
sed -i "s/Y/Q/g" KOMMIItemp.csv
sed -i "s/Z/R/g" KOMMIItemp.csv
sed -i "s/P/X/g" KOMMIItemp.csv
sed -i "s/Q/Y/g" KOMMIItemp.csv
sed -i "s/R/Z/g" KOMMIItemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/KOMMIItemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > KOMMII.csv1
rm KOMMIItemp.csv

cp SEYVIC.csv    SEYVICtemp.csv
sed -i "s/X/P/g" SEYVICtemp.csv
sed -i "s/Y/Q/g" SEYVICtemp.csv
sed -i "s/Z/R/g" SEYVICtemp.csv
sed -i "s/P/Y/g" SEYVICtemp.csv
sed -i "s/Q/Z/g" SEYVICtemp.csv
sed -i "s/R/X/g" SEYVICtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/SEYVICtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > SEYVIC.csv1
rm SEYVICtemp.csv


cp MOFTIL.csv    MOFTILtemp.csv
sed -i "s/X/P/g" MOFTILtemp.csv
sed -i "s/Y/Q/g" MOFTILtemp.csv
sed -i "s/Z/R/g" MOFTILtemp.csv
sed -i "s/P/Z/g" MOFTILtemp.csv
sed -i "s/Q/Y/g" MOFTILtemp.csv
sed -i "s/R/X/g" MOFTILtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/MOFTILtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > MOFTIL.csv1
rm MOFTILtemp.csv

cp IDOGIR.csv    IDOGIRtemp.csv
sed -i "s/X/P/g" IDOGIRtemp.csv
sed -i "s/Y/Q/g" IDOGIRtemp.csv
sed -i "s/Z/R/g" IDOGIRtemp.csv
sed -i "s/P/Z/g" IDOGIRtemp.csv
sed -i "s/Q/Y/g" IDOGIRtemp.csv
sed -i "s/R/X/g" IDOGIRtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/IDOGIRtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > IDOGIR.csv1
rm IDOGIRtemp.csv

cp RUBDOI.csv    RUBDOItemp.csv
sed -i "s/X/P/g" RUBDOItemp.csv
sed -i "s/Y/Q/g" RUBDOItemp.csv
sed -i "s/Z/R/g" RUBDOItemp.csv
sed -i "s/P/Z/g" RUBDOItemp.csv
sed -i "s/Q/Y/g" RUBDOItemp.csv
sed -i "s/R/X/g" RUBDOItemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/RUBDOItemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > RUBDOI.csv1
rm RUBDOItemp.csv

