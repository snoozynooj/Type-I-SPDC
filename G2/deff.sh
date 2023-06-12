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

    cp G2.py.bak $cif-G2.py
    sed -i "s/FILE/$cif/" $cif-G2.py
    sed -i "s/bandgap/$bandgap/" $cif-G2.py
    sed -i "s/PUMP/$signal/" $cif-G2.py
#    echo "$cif $bandgap $signal"
    python $cif-G2.py > $cif-NP.txt &
#    python $cif-G2.py 
done < "$input"

