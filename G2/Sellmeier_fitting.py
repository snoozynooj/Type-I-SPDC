#CRYSTAl 17 And castep

# Funtion to import and work with the data
from numpy import *
from numpy import genfromtxt
from matplotlib import pyplot as plt
from fractions import Fraction as F

# Import funtion for fitting the sellmeir equation to data

from scipy.optimize import leastsq
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

# Import funtion to plot the results

import matplotlib.pyplot as plt

import sympy as sym
x1=sym.symbols('x1')
c=sym.symbols('c')
# loading data into python
# The scripth I made, used a file with the information of the frecuency in the first raw and the dielectric on that point.
my_data =  genfromtxt('FIRZIP.txt1', delimiter='')
my_data1 = genfromtxt('FIRZIP.txt1', delimiter='')
my_data2 = genfromtxt('FIRZIP.txt1', delimiter='')
def funcSell(x, A, B1, C1, B2, C2):
    return ((A)+(((x**2)*B1)/((x**2)-C1))+(((x**2)*B2)/((x**2)-C2)))

def Sell(x1, A, B1, C1, B2, C2):
    return sym.sqrt(((A)+(((x1**2)*B1)/((x1**2)-C1))+(((x1**2)*B2)/((x1**2)-C2))))
bg=4.0552
x=500
y=1100
z=2000
# To import the xx and zz component of the dielectric constant
f=my_data[:,0]   # frequency #
xx=my_data[:,1]  # XX Dielectric values/ adjust to the format of file crystal =2, caste=1
yy=my_data2[:,2] # YY Dielectric values/ adjust to the format of file crystal =2, castMIRO101Ee=1
zz=my_data1[:,3] # ZZ Dielectric values/ adjust to the format of file crystal =2, castMIRO101Ee=1

f1=[] # frecuency now in nm
zz2=[] # Dielectric on the range
xx2=[] # Dielectric on the range
yy2=[] # Dielectric on the range

if len(zz)==len(xx):
    for i in range(0,len(f)):
        if bg>=f[i]>=1.12713: # This limit was due to the CASTEP file, but in Crystal one can have
            f1.append((round(1239.84193/f[i],2)))# Tranform frecuency in eV to nm wavelength
            a=round((xx[i])**2,4) # append the new values rounded
            b=round((yy[i])**2,4) #
            c=round((zz[i])**2,4) #
            zz2.append(c) #
            xx2.append(a) #
            yy2.append(b) #

X = np.linspace(x, y, z)

constantsSell, _ = sc.optimize.curve_fit(funcSell, f1, xx2, maxfev=9999990, xtol=1e-8)
Y3=funcSell(X,*constantsSell)

constantsSell1, _ = sc.optimize.curve_fit(funcSell, f1, zz2, maxfev=9999990, xtol=1e-8)
Y4=funcSell(X,*constantsSell1)

constantsSell2, _ = sc.optimize.curve_fit(funcSell, f1, yy2, maxfev=9999990, xtol=1e-8)
Y4=funcSell(X,*constantsSell2)

print(constantsSell[0],constantsSell[1],constantsSell[2],constantsSell[3],constantsSell[4])
print(constantsSell2[0],constantsSell2[1],constantsSell2[2],constantsSell2[3],constantsSell2[4])
print(constantsSell1[0],constantsSell1[1],constantsSell1[2],constantsSell1[3],constantsSell1[4])
l=1064
no=Sell(x1,constantsSell[0],constantsSell[1],constantsSell[2],constantsSell[3],constantsSell[4])
ne=Sell(x1,constantsSell1[0],constantsSell1[1],constantsSell1[2],constantsSell1[3],constantsSell1[4])
ny=Sell(x1,constantsSell2[0],constantsSell2[1],constantsSell2[2],constantsSell2[3],constantsSell2[4])


D1no=(sym.diff(no))
D1ne=(sym.diff(ne))
D1ny=(sym.diff(ny))
D2no=(sym.diff(D1no))
D2ne=(sym.diff(D1ne))
D2ny=(sym.diff(D1ny))
c=(3*(10**8)*(10**9))/(10**15)
pi=3.14
w=(2*pi*c)/l
print((((l**3)/(2*pi*c**2))*(D2no.subs(x1,l)))*(1/10**(-6)) , (((l**3)/(2*pi*c**2))*(D2ny.subs(x1,l)))*(1/10**(-6)), (((l**3)/(2*pi*c**2))*(D2ne.subs(x1,l)))*(1/10**(-6)))
print(math.sqrt((((l**3)/(2*pi*c**2))*(D2no.subs(x1,l)))*(1/10**(-6))*1.5*0.25)*2.0 , math.sqrt((((l**3)/(2*pi*c**2))*(D2ny.subs(x1,l)))*(1/10**(-6))*1.5*0.25)*2.0,math.sqrt((((l**3)/(2*pi*c**2))*(D2ne.subs(x1,l)))*(1/10**(-6))*1.5*0.25)*2.0 )


