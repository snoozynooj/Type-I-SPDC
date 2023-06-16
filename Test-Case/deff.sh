#!/bin/bash
input="database"
#for folders in $list1;do
while IFS= read -r line
do
    echo $line > result
    cif=$(awk '{print $1}' result)
    crystaltype=$(awk '{print $2}' result)
    bandgap=$(awk '{print $3}' result)
    signal=$(awk '{print $4}' result)

    cp autophasematching.py.bak $cif-autophasematching.py
    sed -i "s/FILE/$cif/" $cif-autophasematching.py
    sed -i "s/bandgap/$bandgap/" $cif-autophasematching.py
    sed -i "s/PUMP/$signal/" $cif-autophasematching.py
    echo "$cif $bandgap $signal"
    python $cif-autophasematching.py > $cif-Count.txt &
#    python $cif-autophasematching.py  
done < "$input"
#rm *-au*
#rm *-G2*
