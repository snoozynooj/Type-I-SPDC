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

    cp deffmap.py.bak $cif-deffmap.py
    sed -i "s/FILE/$cif/" $cif-deffmap.py
    sed -i "s/bandgap/$bandgap/" $cif-deffmap.py
    sed -i "s/PUMP/$signal/" $cif-deffmap.py
    echo "$cif $bandgap $signal"
    python $cif-deffmap.py > $cif-result  &
done < "$input"

