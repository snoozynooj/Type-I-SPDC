set ylabel "Free energy (kJ/mol)"  tc rgb "black"
set yrange [0:180]
set xrange [0:360]
set xtics 45 tc rgb "black"
#set key left tc rgb "black"
set ytics 30 tc rgb "black"
set cbtics tc rgb "black"
set border lw 2 lc rgb "black"
set terminal postscript eps enhanced color solid background rgb 'white' "Helvetica" 32 size 7,6
set palette rgb 33,13,10
#set grid
set key out horiz  font ",32" tc rgb "black"
#set cblabel "d_{eff} (pm/V)" tc rgb "black"
set xlabel "{/Symbol f} (^o)"  offset 2,0,0 tc rgb "black"
set ylabel "{/Symbol q} (^o)" offset 2,0,0  tc rgb "black"

set output "Compare.eps"
set title "Signal = 810 nm, (X, Y, Z -> a, c, b)"
plot "BIBO810-phasematching-deff.csv" u 3:2 w p lw 0.1 lc 7  t "BIBO-Calculated", \
     "BIBOEXP-phasematching-deff.csv" u 3:2 w p lw 0.1 lc 2  t "BIBO-EXP", \
