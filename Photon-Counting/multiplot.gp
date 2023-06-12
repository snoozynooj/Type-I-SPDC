set ylabel "Free energy (kJ/mol)"  tc rgb "black"
set yrange [0:180]
set xrange [0:360]
set xtics 40 tc rgb "black"
set ytics 30 tc rgb "black"
set cbtics tc rgb "black"
set border lw 2 lc rgb "black" 
set terminal postscript eps enhanced color solid background rgb 'white' "Helvetica" 32 size 7,5
set xlabel "z" tc rgb "black"
set ylabel "Free energy (kJ/mol)" tc rgb "black"
#set cblabel "Free energy (kJ/mol)" tc rgb "black"
set palette rgb 33,13,10
#set grid
set key out horiz  font ",26" tc rgb "black"
set cblabel "d_{eff} (pm/V)" tc rgb "black"
set xlabel "{/Symbol f} (^o)"  offset 2,0,0 tc rgb "black"
set ylabel "{/Symbol q} (^o)" offset 2,0,0  tc rgb "black"

set output "222.eps"

plot  "ECIHIK-1.csv"    u 3:2 w p lw 0.1  lc rgb "#277DA1"  t "ECIHIK", \
      "EWUSIZ-1.csv"    u 3:2 w p lw 0.1  lc rgb "#F9C74F"  t "EWUSIZ", \
      "NIBRUN-1.csv"    u 3:2 w p lw 0.1  lc rgb "#F3722C"  t "NIBRUN", \
      "NIBSAU-1.csv"    u 3:2 w p lw 0.1  lc rgb "#F94144"  t "NIBSAU", \
      "VAHWOS01-1.csv"  u 3:2 w p lw 0.1  lc rgb "#43AA8B"  t "VAHWOS01", \
      "ODIVON-1.csv"    u 3:2 w p lw 0.1  lc rgb "#40E0D0"  t "ODIVON", \
      "WOVPAB-1.csv"    u 3:2 w p lw 0.1  lc rgb "#4D908E"  t "WOVPAB", \
      "DOYBEY-1.csv"    u 3:2 w p lw 0.1  lc rgb "#90BE6D"  t "DOYBEY", \
      "JUKVEQ02-1.csv"  u 3:2 w p lw 0.1  lc rgb "#F9C74F"  t "JUKVEQ02", \
      "WOVPEF-1.csv"    u 3:2 w p lw 0.1  lc rgb "#FFFF00"  t "WOVPEF", \
      "XISBUX-1.csv"    u 3:2 w p lw 0.1  lc rgb "#800000"  t "XISBUX"  

set yrange [-1.2:1.2]
set xrange [0:180]
set xtics 30 tc rgb "black"
set ytics 0.3 tc rgb "black"
set ylabel "d_{eff} (pm/V)"
set xlabel "{/Symbol q} (^o)"
plot  "ECIHIK-1.csv"    u 2:1 w p lw 0.1  lc rgb "#277DA1"  t "ECIHIK", \
      "EWUSIZ-1.csv"    u 2:1 w p lw 0.1  lc rgb "#F9C74F"  t "EWUSIZ", \
      "NIBRUN-1.csv"    u 2:1 w p lw 0.1  lc rgb "#F3722C"  t "NIBRUN", \
      "NIBSAU-1.csv"    u 2:1 w p lw 0.1  lc rgb "#F94144"  t "NIBSAU", \
      "VAHWOS01-1.csv"  u 2:1 w p lw 0.1  lc rgb "#43AA8B"  t "VAHWOS01", \
      "ODIVON-1.csv"    u 2:1 w p lw 0.1  lc rgb "#40E0D0"  t "ODIVON", \
      "WOVPAB-1.csv"    u 2:1 w p lw 0.1  lc rgb "#4D908E"  t "WOVPAB", \
      "DOYBEY-1.csv"    u 2:1 w p lw 0.1  lc rgb "#90BE6D"  t "DOYBEY", \
      "JUKVEQ02-1.csv"  u 2:1 w p lw 0.1  lc rgb "#F9C74F"  t "JUKVEQ02", \
      "WOVPEF-1.csv"    u 2:1 w p lw 0.1  lc rgb "#FFFF00"  t "WOVPEF", \
      "XISBUX-1.csv"    u 2:1 w p lw 0.1  lc rgb "#800000"  t "XISBUX"  

set xlabel "{/Symbol f} (^o)"
set ylabel "{/Symbol q} (^o)"
set yrange [0:180]
set xrange [0:360]
set xtics 40 tc rgb "black"
set ytics 30 tc rgb "black"
plot "HONCOF-1.csv"   u 3:2 w p  lw 1 lt 7 lc rgb "#277DA1" t "HONCOF", \
     "DIFKOS-1.csv"   u 3:2 w p  lw 1 lt 7 lc rgb "#43AA8B" t "DIFKOS", \
     "FEHJIN-1.csv"   u 3:2 w p  lw 1 lt 7 lc rgb "#4D908E" t "FEHJIN", \
     "VEKNEH-1.csv"   u 3:2 w p  lw 1 lt 7 lc rgb "#90BE6D" t "VEKNEH", \
     "IVAZUA01-1.csv" u 3:2 w p  lw 1 lt 7 lc rgb "#F9C74F" t "IVAZUA01", \
     "FIQGEU-1.csv"   u 3:2 w p  lw 1 lt 7 lc rgb "#FIQGEU" t "FIQGEU", \
     "NUYWUA-1.csv"   u 3:2 w p  lw 1 lt 7 lc rgb "#F3722C" t "NUYWUA", \
     "OXUNUR-1.csv"   u 3:2 w p  lw 1 lt 7 lc rgb "#F94144" t "OXUNUR"

set yrange [-1.2:1.2]
set xrange [0:180]
set xtics 30 tc rgb "black"
set ytics 0.3 tc rgb "black"
set ylabel "d_{eff} (pm/V)"
set xlabel "{/Symbol q} (^o)"
plot "HONCOF-1.csv"   u 2:1 w p  lw 1 lt 7 lc rgb "#277DA1" t "HONCOF", \
     "DIFKOS-1.csv"   u 2:1 w p  lw 1 lt 7 lc rgb "#43AA8B" t "DIFKOS", \
     "FEHJIN-1.csv"   u 2:1 w p  lw 1 lt 7 lc rgb "#4D908E" t "FEHJIN", \
     "VEKNEH-1.csv"   u 2:1 w p  lw 1 lt 7 lc rgb "#90BE6D" t "VEKNEH", \
     "IVAZUA01-1.csv" u 2:1 w p  lw 1 lt 7 lc rgb "#F9C74F" t "IVAZUA01", \
     "FIQGEU-1.csv"   u 2:1 w p  lw 1 lt 7 lc rgb "#FIQGEU" t "FIQGEU", \
     "NUYWUA-1.csv"   u 2:1 w p  lw 1 lt 7 lc rgb "#F3722C" t "NUYWUA", \
     "OXUNUR-1.csv"   u 2:1 w p  lw 1 lt 7 lc rgb "#F94144" t "OXUNUR"



set xlabel "{/Symbol f} (^o)"
set ylabel "{/Symbol q} (^o)"
set xrange [0:360]
set yrange [0:180]
set xtics 40 tc rgb "black"
set ytics 30 tc rgb "black"
plot "RATDAS01-1.csv" u 3:2 w  p  lw 1 lt 7 lc rgb "#277DA1" t "RATDAS01", \
     "TAKRIJ-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#43AA8B" t "TAKRIJ", \
     "FIPWUY-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#4D908E" t "FIPWUY", \
     "LASPZN-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#90BE6D" t "LASPZN", \
     "FIRZIP-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#F9C74F" t "FIRZIP", \
     "PODREH-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#F9C74F" t "PODREH", \
     "RUVBAN-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#F3722C" t "RUVBAN", \
     "OFUWIV-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#F94144" t "OFUWIV", \
     "MUYGOE-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#AE2012" t "MUYGOE", \
     "NELWUY-1.csv"   u 3:2 w  p  lw 1 lt 7 lc rgb "#001219" t "NELWUY"

set xrange [0:180]
set yrange [-1.2:1.2]
set xtics 30 tc rgb "black"
set ytics 0.3 tc rgb "black"
set ylabel "d_{eff} (pm/V)"
set xlabel "{/Symbol q} (^o)"
plot "RATDAS01-1.csv" u 2:1 w  p  lw 1 lt 7 lc rgb "#277DA1" t "RATDAS01", \
     "TAKRIJ-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#43AA8B" t "TAKRIJ", \
     "FIPWUY-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#4D908E" t "FIPWUY", \
     "LASPZN-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#90BE6D" t "LASPZN", \
     "FIRZIP-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#F9C74F" t "FIRZIP", \
     "PODREH-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#F9C74F" t "PODREH", \
     "RUVBAN-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#F3722C" t "RUVBAN", \
     "OFUWIV-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#F94144" t "OFUWIV", \
     "MUYGOE-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#AE2012" t "MUYGOE", \
     "NELWUY-1.csv"   u 2:1 w  p  lw 1 lt 7 lc rgb "#001219" t "NELWUY"


set xlabel "{/Symbol f} (^o)"
set ylabel "{/Symbol q} (^o)"
set xrange [0:360]
set yrange [0:180]
set xtics 40 tc rgb "black"
set ytics 30 tc rgb "black"
plot "AQOROP-1.csv"   u 3:2 w  p  lw 1 lt 6 lc rgb "#FF0000" t "AQOROP", \
     "KOMMII-1.csv"   u 3:2 w  p  lw 1 lt 6 lc rgb "#008000" t "KOMMII", \
     "MOFTIL-1.csv"   u 3:2 w  p  lw 1 lt 6 lc rgb "#0000FF" t "MOFTIL", \
     "IDOGIR-1.csv"   u 3:2 w  p  lw 1 lt 6 lc rgb "#FF7F50" t "IDOGIR", \
     "RUBDOI-1.csv"   u 3:2 w  p  lw 1 lt 6 lc rgb "#40E0D0" t "RUBDOI", \
     "SEYVIC-1.csv"   u 3:2 w  p  lw 1 lt 6 lc rgb "#6495ED" t "SEYVIC"

set yrange [-10:10]
set xrange [0:180]
set xtics 20 tc rgb "black"
set ytics 5 tc rgb "black"
set ylabel "d_{eff} (pm/V)"
set xlabel "{/Symbol q} (^o)"
plot "AQOROP-1.csv"   u 2:1 w  p  lw 1 lt 6 lc rgb "#FF0000" t "AQOROP", \
     "KOMMII-1.csv"   u 2:1 w  p  lw 1 lt 6 lc rgb "#008000" t "KOMMII", \
     "MOFTIL-1.csv"   u 2:1 w  p  lw 1 lt 6 lc rgb "#0000FF" t "MOFTIL", \
     "IDOGIR-1.csv"   u 2:1 w  p  lw 1 lt 6 lc rgb "#FF7F50" t "IDOGIR", \
     "RUBDOI-1.csv"   u 2:1 w  p  lw 1 lt 6 lc rgb "#40E0D0" t "RUBDOI", \
     "SEYVIC-1.csv"   u 2:1 w  p  lw 1 lt 6 lc rgb "#6495ED" t "SEYVIC"
