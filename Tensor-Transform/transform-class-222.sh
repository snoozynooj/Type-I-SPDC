
#!/bin/bash
cp ECIHIK.csv  ECIHIKtemp.csv
sed -i "s/X/P/g" ECIHIKtemp.csv
sed -i "s/Y/Q/g" ECIHIKtemp.csv
sed -i "s/Z/R/g" ECIHIKtemp.csv
sed -i "s/P/Z/g" ECIHIKtemp.csv
sed -i "s/Q/X/g" ECIHIKtemp.csv
sed -i "s/R/Y/g" ECIHIKtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/ECIHIKtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > ECIHIK.csv1
rm ECIHIKtemp.csv

cp EWUSIZ.csv    EWUSIZtemp.csv
sed -i "s/X/P/g" EWUSIZtemp.csv
sed -i "s/Y/Q/g" EWUSIZtemp.csv
sed -i "s/Z/R/g" EWUSIZtemp.csv
sed -i "s/P/Z/g" EWUSIZtemp.csv
sed -i "s/Q/Y/g" EWUSIZtemp.csv
sed -i "s/R/X/g" EWUSIZtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/EWUSIZtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > EWUSIZ.csv1
rm EWUSIZtemp.csv


cp NIBRUN.csv    NIBRUNtemp.csv
sed -i "s/X/P/g" NIBRUNtemp.csv
sed -i "s/Y/Q/g" NIBRUNtemp.csv
sed -i "s/Z/R/g" NIBRUNtemp.csv
sed -i "s/P/X/g" NIBRUNtemp.csv
sed -i "s/Q/Y/g" NIBRUNtemp.csv
sed -i "s/R/Z/g" NIBRUNtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/NIBRUNtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > NIBRUN.csv1
rm NIBRUNtemp.csv

cp NIBSAU.csv    NIBSAUtemp.csv
sed -i "s/X/P/g" NIBSAUtemp.csv
sed -i "s/Y/Q/g" NIBSAUtemp.csv
sed -i "s/Z/R/g" NIBSAUtemp.csv
sed -i "s/P/X/g" NIBSAUtemp.csv
sed -i "s/Q/Y/g" NIBSAUtemp.csv
sed -i "s/R/Z/g" NIBSAUtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/NIBSAUtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > NIBSAU.csv1
rm NIBSAUtemp.csv


cp VAHWOS01.csv    VAHWOS01temp.csv
sed -i "s/X/P/g" VAHWOS01temp.csv
sed -i "s/Y/Q/g" VAHWOS01temp.csv
sed -i "s/Z/R/g" VAHWOS01temp.csv
sed -i "s/P/X/g" VAHWOS01temp.csv
sed -i "s/Q/Y/g" VAHWOS01temp.csv
sed -i "s/R/Z/g" VAHWOS01temp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/VAHWOS01temp/g" arrange1.f90
gfortran arrange1.f90
./a.out > VAHWOS01.csv1
rm VAHWOS01temp.csv

cp ODIVON.csv    ODIVONtemp.csv
sed -i "s/X/P/g" ODIVONtemp.csv
sed -i "s/Y/Q/g" ODIVONtemp.csv
sed -i "s/Z/R/g" ODIVONtemp.csv
sed -i "s/P/Z/g" ODIVONtemp.csv
sed -i "s/Q/X/g" ODIVONtemp.csv
sed -i "s/R/Y/g" ODIVONtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/ODIVONtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > ODIVON.csv1
rm ODIVONtemp.csv

cp WOVPAB.csv    WOVPABtemp.csv
sed -i "s/X/P/g" WOVPABtemp.csv
sed -i "s/Y/Q/g" WOVPABtemp.csv
sed -i "s/Z/R/g" WOVPABtemp.csv
sed -i "s/P/X/g" WOVPABtemp.csv
sed -i "s/Q/Z/g" WOVPABtemp.csv
sed -i "s/R/Y/g" WOVPABtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/WOVPABtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > WOVPAB.csv1
rm WOVPABtemp.csv

cp DOYBEY.csv    DOYBEYtemp.csv
sed -i "s/X/P/g" DOYBEYtemp.csv
sed -i "s/Y/Q/g" DOYBEYtemp.csv
sed -i "s/Z/R/g" DOYBEYtemp.csv
sed -i "s/P/Z/g" DOYBEYtemp.csv
sed -i "s/Q/Y/g" DOYBEYtemp.csv
sed -i "s/R/X/g" DOYBEYtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/DOYBEYtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > DOYBEY.csv1
rm DOYBEYtemp.csv

cp JUKVEQ02.csv    JUKVEQ02temp.csv
sed -i "s/X/P/g" JUKVEQ02temp.csv
sed -i "s/Y/Q/g" JUKVEQ02temp.csv
sed -i "s/Z/R/g" JUKVEQ02temp.csv
sed -i "s/P/Z/g" JUKVEQ02temp.csv
sed -i "s/Q/X/g" JUKVEQ02temp.csv
sed -i "s/R/Y/g" JUKVEQ02temp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/JUKVEQ02temp/g" arrange1.f90
gfortran arrange1.f90
./a.out > JUKVEQ02.csv1
rm JUKVEQ02temp.csv

cp WOVPEF.csv    WOVPEFtemp.csv
sed -i "s/X/P/g" WOVPEFtemp.csv
sed -i "s/Y/Q/g" WOVPEFtemp.csv
sed -i "s/Z/R/g" WOVPEFtemp.csv
sed -i "s/P/Z/g" WOVPEFtemp.csv
sed -i "s/Q/X/g" WOVPEFtemp.csv
sed -i "s/R/Y/g" WOVPEFtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/WOVPEFtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > WOVPEF.csv1
rm WOVPEFtemp.csv


cp XISBUX.csv    XISBUXtemp.csv
sed -i "s/X/P/g" XISBUXtemp.csv
sed -i "s/Y/Q/g" XISBUXtemp.csv
sed -i "s/Z/R/g" XISBUXtemp.csv
sed -i "s/P/Y/g" XISBUXtemp.csv
sed -i "s/Q/Z/g" XISBUXtemp.csv
sed -i "s/R/X/g" XISBUXtemp.csv
cp arrange.f90.bak arrange1.f90
sed -i "s/FILE/XISBUXtemp/g" arrange1.f90
gfortran arrange1.f90
./a.out > XISBUX.csv1
rm XISBUXtemp.csv
