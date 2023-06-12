set ylabel "Free energy (kJ/mol)"  tc rgb "black"
set yrange [0:180]
set xrange [0:360]
set xtics 40 tc rgb "black"
#set key left tc rgb "black"
set ytics 30 tc rgb "black"
set cbtics tc rgb "black"
set border lw 2 lc rgb "black" 
set terminal postscript eps enhanced color solid background rgb 'white' "Helvetica" 32 size 7,5
set xlabel "z" tc rgb "black"
set ylabel "Free energy (kJ/mol)" tc rgb "black"
#set cblabel "Free energy (kJ/mol)" tc rgb "black"
set palette rgb 33,13,10
set grid
set key out horiz  font ",18" tc rgb "black"
set cblabel "d_{eff} (pm/V)" tc rgb "black"
set xlabel "{/Symbol f} (^o)"  offset 2,0,0 tc rgb "black"
set ylabel "{/Symbol q} (^o)" offset 2,0,0  tc rgb "black"

set output "ECIHIK.eps"
plot "ECIHIK-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/ECIHIK-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "EWUSIZ.eps"
plot "EWUSIZ-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/EWUSIZ-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "NIBRUN.eps"
plot "NIBRUN-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/NIBRUN-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "NIBSAU.eps"
plot "NIBSAU-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/NIBSAU-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "VAHWOS01.eps"
plot "VAHWOS01-2dmap.csv"  u 3:2:($1**1) w image t "", "../Photon-Count/VAHWOS01-1.csv"  u 3:2 w p lw 0.1 lc 8  t ""
set output "ODIVON.eps"
plot "ODIVON-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/ODIVON-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "WOVPAB.eps"
plot "WOVPAB-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/WOVPAB-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "DOYBEY.eps"
plot "DOYBEY-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/DOYBEY-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "JUKVEQ02.eps"
plot "JUKVEQ02-2dmap.csv"  u 3:2:($1**1) w image t "", "../Photon-Count/JUKVEQ02-1.csv" u 3:2 w p lw 0.1 lc 8  t ""
set output "WOVPEF.eps"
plot "WOVPEF-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/WOVPEF-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
set output "XISBUX.eps"
plot "XISBUX-2dmap.csv"    u 3:2:($1**1) w image t "", "../Photon-Count/XISBUX-1.csv"   u 3:2 w p lw 0.1 lc 8  t ""
                                             
                                            





  
