
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:08:47 2023

@author: burto
"""

import numpy as np
import math as mt
import sympy as sym 
import matplotlib.pyplot as plt

###############Estimating Sellmeier coefficient#######################
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
my_data =  genfromtxt('BIBO.txt1', delimiter='')
my_data1 = genfromtxt('BIBO.txt1', delimiter='')
my_data2 = genfromtxt('BIBO.txt1', delimiter='')
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

######################################################################
lp = 405
l1 = lp*2
deff = 3.7*1E-12
x2_eff = 2*deff
L = 1E-3

#"BIBO"
nx = [constantsSell[0],constantsSell[1],constantsSell[2],constantsSell[3],constantsSell[4]]
ny = [constantsSell2[0],constantsSell2[1],constantsSell2[2],constantsSell2[3],constantsSell2[4]]
nz = [constantsSell1[0],constantsSell1[1],constantsSell1[2],constantsSell1[3],constantsSell1[4]]

theta_m =  34.4
phi_m =    75.7
deff_m =   -3.81471299979618
#"RUVBAN"

#nx = [1.7959268836049889, 0.443192326176112, 45313.262990234456, 0.010826821073462918, 132012.61709595495]
#ny = [2.1962200502159575, 1.0694389261334873, 62530.17092882354, 0.024172484972597046, 130815.43900969811]
#nz = [2.169642433924311, 1.0863421247626117, 65076.08574104012, 0.030305414019025347, 129218.10091242459]
        
#theta_m =  89.85
#phi_m =  22.1
#deff_m = 2.52909487551813
 
x=sym.symbols('x')
    
def Sell(l, A, B1, C1, B2, C2):
    return mt.sqrt(((A)+(((l**2)*B1)/((l**2)-C1))+(((l**2)*B2)/((l**2)-C2))))


def Sell2(x, A, B1, C1, B2, C2):
        return sym.sqrt(((A)+(((x**2)*B1)/((x**2)-C1))+(((x**2)*B2)/((x**2)-C2))))

sigma_p = 0.875E-6
sigma_1 = 1.875E-6

P = 1E-3

pi = mt.pi

c=299792458



l = 532
lam_t = l
#print((Sell2(831.8601,*nx))**1)


Dx = sym.diff(Sell2(x,*nx))
Dy = sym.diff(Sell2(x,*ny))
Dz = sym.diff(Sell2(x,*nz))

ng1 = Sell(l1,*nx)-l1*Dx.subs(x,l1)
ng2 = Sell(l1,*ny)-l1*Dy.subs(x,l1)
ng3 = Sell(l1,*nz)-l1*Dz.subs(x,l1)

vg1 = c/ng1
vg2 = c/ng2
vg3 = c/ng3


nx_ = Sell2(l1,*nx)
ny_ = Sell2(l1,*ny)
nz_ = Sell2(l1,*nz)




if nz_-ny_>ny_-nx_:
    type_="positive"
elif ny_-nx_>nz_-ny_:
    type_="negative"




def f1 (x,theta,phi):
    

    
    Sell_xsi = Sell2(x, *nx)**2
    Sell_ysi = Sell2(x, *ny)**2
    Sell_zsi = Sell2(x, *nz)**2
    


    

    
    
    a1 = 1/Sell_xsi
    b1 = 1/Sell_ysi
    c1 = 1/Sell_zsi
    # 


    kx=np.sin(theta)*np.cos(phi)
    ky=np.sin(theta)*np.sin(phi)
    kz=np.cos(theta)


    
    
    b11 = -(kx**2)*(b1+c1)-(ky**2)*(a1+c1)-(kz**2)*(a1+b1)
    c11 = (kx**2)*b1*c1 + (ky**2)*a1*c1 + (kz**2)*a1*b1




    n1 = sym.sqrt(2)/(sym.sqrt(-b11-sym.sqrt((b11**2) - 4*c11)))
    

    return n1


def f2 (x,theta,phi):
    

    
    Sell_xsi = Sell2(x, *nx)**2
    Sell_ysi = Sell2(x, *ny)**2
    Sell_zsi = Sell2(x, *nz)**2
    


    

         
    
    a1 = 1/Sell_xsi
    b1 = 1/Sell_ysi
    c1 = 1/Sell_zsi
    # 


    kx=np.sin(theta)*np.cos(phi)
    ky=np.sin(theta)*np.sin(phi)
    kz=np.cos(theta)


    
    
    b11 = -(kx**2)*(b1+c1)-(ky**2)*(a1+c1)-(kz**2)*(a1+b1)
    c11 = (kx**2)*b1*c1 + (ky**2)*a1*c1 + (kz**2)*a1*b1




    n1 = sym.sqrt(2)/(sym.sqrt(-b11+sym.sqrt((b11**2) - 4*c11)))

    return n1




def ng1(l1,theta_m,phi_m):
    D = sym.diff(f1(x,theta_m,phi_m))
    a = f1(x,theta_m,phi_m)-l1*1E-3*(D)
    a = a.subs(x,l1)
    return a

def ng2(l1,theta_m,phi_m):
    D = sym.diff(f2(x,theta_m,phi_m))
    a = f2(x,theta_m,phi_m)-l1*1E-3*(D)
    a = a.subs(x,l1)
    return a



def vgd1(l1,theta_m,phi_m):
    
    a = ((l1*1E-9)**3)/(2*mt.pi*c*c)
    D2 = sym.diff(f1(x,theta_m,phi_m))
    
    D3 = sym.diff(D2)*1E18
    # print(D3.subs(x,l1))
    Dl = a*D3
    Dl = Dl.subs(x,l1)
    return Dl


def vgd2(l1,theta_m,phi_m):
    
    a = ((l1*1E-9)**3)/(2*mt.pi*c*c)
    D2 = sym.diff(f2(x,theta_m,phi_m))
    
    D3 = sym.diff(D2)*1E18
    # print(D3.subs(x,l1))
    Dl = a*D3
    Dl = Dl.subs(x,l1)
    return Dl






Vg2 = vgd2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)

def sinc (D,L):
        # print(v,D,L)
        s = np.sin(D*L/2)
    
        s = (s*2) / (D*L)
        
        return s

def sinc2 (x,L):
        # print(v,D,L)
        s = sym.sin(x*L/2)
    
        s = (s*2) / (x*L)
        
        return s


# vg1_ = []
# for a in range(len(phi_)):
#     vg1_.append(f2(405,theta_[a]*mt.pi/180,phi_[a]*mt.pi/180))
# plt.plot(vg1_,phi_,"-")


if type_=='positive':

    n_1 = f2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    ng_ = ng2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    n_p = f1(lp,theta_m*mt.pi/180,phi_m*mt.pi/180)
    
    wp = 2*mt.pi*c/  (lp*1E-9*n_p)
    w1 = 2*mt.pi*c/  (l1*1E-9*n_1)
    
    Vg = float(vgd2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180))
    
elif type_=='negative':
    
    Vg = float(vgd1(l1,theta_m*mt.pi/180,phi_m*mt.pi/180))
    n_1 = f1(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    n_p = f2(lp,theta_m*mt.pi/180,phi_m*mt.pi/180)
    ng_ = ng1(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    wp = 2*mt.pi*c/  (lp*1E-9*n_p)
    w1 = 2*mt.pi*c/  (l1*1E-9*n_1)

f= int(wp/2)
det = np.linspace(-f,f,100)
d_k = []

for a in range(len(det)):
    delta_k = (w1+det[a])*(wp-w1+det[a])*sinc(float(Vg*(w1+det[a] -wp/2)**2),0.001)**2
    d_k.append(delta_k)
#plt.plot(det,d_k,"-")


def In (x):
    s = sym.sin((Vg*(w1+x -wp/2)**2)*0.001/2)
    s = s*2/((Vg*(w1+x -wp/2)**2)*0.001) 
    I= (w1+x)*(wp-w1+x)*s
    return I
Io = In(x)
Io1 = float(sym.integrate(Io,(x,-f,f+1)))

deff_m = deff_m*1E-12

""" value of the review"""
# deff_m = 3.7*1E-12

eo = 8.8541878176E-12
P = 1E-3

Ep2 = P/(c*eo*mt.pi*n_1*sigma_p**2)
R1 = Ep2*(deff_m**2)*L*L/(2*mt.pi*c*c)
R2 = ng_*ng_/(n_1**4)
R3 = mt.sqrt(abs(sigma_p**2/(sigma_1**2 + 2*sigma_p**2)))

Rsm = float(R1*R2*R3*Io1)

print("GVD:")
print(Vg)
print("Rsm:")
print(Rsm)

###############G2
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 16:02:50 2023

@author: burto
"""


# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:08:47 2023

@author: burto
"""

import numpy as np
import math as mt
import sympy as sym 
import matplotlib.pyplot as plt
from scipy.integrate import quad
lp = 405
l1 = lp*2
deff = 3.7*1E-12
x2_eff = 2*deff
L = 1E-3
nx = [constantsSell[0],constantsSell[1],constantsSell[2],constantsSell[3],constantsSell[4]]
ny = [constantsSell2[0],constantsSell2[1],constantsSell2[2],constantsSell2[3],constantsSell2[4]]
nz = [constantsSell1[0],constantsSell1[1],constantsSell1[2],constantsSell1[3],constantsSell1[4]]

theta_m =  34.4
phi_m =    75.7
deff_m =   -3.81471299979618


"parameters"
P = 1E-3
pi = mt.pi
c=299792458
l = 405
lam_t = l
x=sym.symbols('x')
    
def Sell(l, A, B1, C1, B2, C2):
    return mt.sqrt(((A)+(((l**2)*B1)/((l**2)-C1))+(((l**2)*B2)/((l**2)-C2))))


def Sell2(x, A, B1, C1, B2, C2):
        return sym.sqrt(((A)+(((x**2)*B1)/((x**2)-C1))+(((x**2)*B2)/((x**2)-C2))))
Dx = sym.diff(Sell2(x,*nx))
Dy = sym.diff(Sell2(x,*ny))
Dz = sym.diff(Sell2(x,*nz))

ng1 = Sell(l1,*nx)-l1*Dx.subs(x,l1)
ng2 = Sell(l1,*ny)-l1*Dy.subs(x,l1)
ng3 = Sell(l1,*nz)-l1*Dz.subs(x,l1)

vg1 = c/ng1
vg2 = c/ng2
vg3 = c/ng3


nx_ = Sell2(l1,*nx)
ny_ = Sell2(l1,*ny)
nz_ = Sell2(l1,*nz)

if nz_-ny_>ny_-nx_:
    type_="positive"
elif ny_-nx_>nz_-ny_:
    type_="negative"

def f1 (x,theta,phi):
    Sell_xsi = Sell2(x, *nx)**2
    Sell_ysi = Sell2(x, *ny)**2
    Sell_zsi = Sell2(x, *nz)**2
    
    
    a1 = 1/Sell_xsi
    b1 = 1/Sell_ysi
    c1 = 1/Sell_zsi

    kx=np.sin(theta)*np.cos(phi)
    ky=np.sin(theta)*np.sin(phi)
    kz=np.cos(theta)

    b11 = -(kx**2)*(b1+c1)-(ky**2)*(a1+c1)-(kz**2)*(a1+b1)
    c11 = (kx**2)*b1*c1 + (ky**2)*a1*c1 + (kz**2)*a1*b1

    n1 = sym.sqrt(2)/(sym.sqrt(-b11-sym.sqrt((b11**2) - 4*c11)))
    
    return n1

def f2 (x,theta,phi):
    Sell_xsi = Sell2(x, *nx)**2
    Sell_ysi = Sell2(x, *ny)**2
    Sell_zsi = Sell2(x, *nz)**2
    a1 = 1/Sell_xsi
    b1 = 1/Sell_ysi
    c1 = 1/Sell_zsi
    kx=np.sin(theta)*np.cos(phi)
    ky=np.sin(theta)*np.sin(phi)
    kz=np.cos(theta)
    
    b11 = -(kx**2)*(b1+c1)-(ky**2)*(a1+c1)-(kz**2)*(a1+b1)
    c11 = (kx**2)*b1*c1 + (ky**2)*a1*c1 + (kz**2)*a1*b1

    n1 = sym.sqrt(2)/(sym.sqrt(-b11+sym.sqrt((b11**2) - 4*c11)))

    return n1

def ng1(l1,theta_m,phi_m):
    D = sym.diff(f1(x,theta_m,phi_m))
    a = f1(x,theta_m,phi_m)-l1*1E-3*(D)
    a = a.subs(x,l1)
    return a

def ng2(l1,theta_m,phi_m):
    D = sym.diff(f2(x,theta_m,phi_m))
    a = f2(x,theta_m,phi_m)-l1*1E-3*(D)
    a = a.subs(x,l1)
    return a



def vgd1(l1,theta_m,phi_m):
    
    a = ((l1*1E-9)**3)/(2*mt.pi*c*c)
    D2 = sym.diff(f1(x,theta_m,phi_m))
    
    D3 = sym.diff(D2)*1E18
    # print(D3.subs(x,l1))
    Dl = a*D3
    Dl = Dl.subs(x,l1)
    return Dl


def vgd2(l1,theta_m,phi_m):
    
    a = ((l1*1E-9)**3)/(2*mt.pi*c*c)
    D2 = sym.diff(f2(x,theta_m,phi_m))
    
    D3 = sym.diff(D2)*1E18
    # print(D3.subs(x,l1))
    Dl = a*D3
    Dl = Dl.subs(x,l1)
    return Dl

Vg2 = vgd2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)

def sinc (D,L):
        # print(v,D,L)
        s = np.sin(D*L/2)
    
        s = (s*2) / (D*L)
        
        return s

def sinc2 (x,L):
        # print(v,D,L)
        s = sym.sin(x*L/2)
    
        s = (s*2) / (x*L)
        
        return s


# vg1_ = []
# for a in range(len(phi_)):
#     vg1_.append(f2(405,theta_[a]*mt.pi/180,phi_[a]*mt.pi/180))
# plt.plot(vg1_,phi_,"-")


if type_=='positive':

    n_1 = f2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    ng_ = ng2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    n_p = f1(lp,theta_m*mt.pi/180,phi_m*mt.pi/180)
    
    wp = 2*mt.pi*c/  (lp*1E-9*n_p)
    w1 = 2*mt.pi*c/  (l1*1E-9*n_1)
    
    Vg = float(vgd2(l1,theta_m*mt.pi/180,phi_m*mt.pi/180))
    
elif type_=='negative':
    
    Vg = float(vgd1(l1,theta_m*mt.pi/180,phi_m*mt.pi/180))
    n_1 = f1(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    n_p = f2(lp,theta_m*mt.pi/180,phi_m*mt.pi/180)
    ng_ = ng1(l1,theta_m*mt.pi/180,phi_m*mt.pi/180)
    wp = 2*mt.pi*c/  (lp*1E-9*n_p)
    w1 = 2*mt.pi*c/  (l1*1E-9*n_1)

f= int(wp/2)
det = np.linspace(-f,f,100)
d_k = []

# for a in range(len(det)):
#     delta_k = sinc(float(Vg*(w1+det[a] -wp/2)**2),0.001)**2
#     d_k.append(delta_k)
# plt.plot(det,d_k,"-")

band = 10E-9
band =  c / (band)

def I(x,t):
    s = mt.sin((Vg*L/4)*x*x)
    s = s/((Vg*L/4)*x*x) 
    a = np.exp(-x**2/band**2)
    b = np.exp(1j*x*t)
    
    inte = s*a*b
    return inte.real


def Ii(x,t):
    s = mt.sin((Vg*L/4)*x*x)
    s = s/((Vg*L/4)*x*x) 
    a = np.exp(-x**2/band**2)
    b = np.exp(1j*x*t)
    
    inte = s*a*b
    return inte.imag


vo= mt.sqrt(4/(Vg*L))
tl = mt.sqrt(Vg*L/4)*10
tau = np.linspace(-tl,tl,100)
G2 = []

for a in range(len(tau)):
    I1 = quad(I,-vo-vo/100,vo,args = (tau[a]))[0]
    I2 = quad(Ii,-vo-vo/100,vo,args = (tau[a]))[0]
    i_t = np.sqrt(I1.real**2+I2.real**2)**2
    i_t = np.sqrt(i_t**2)
    G2.append(i_t)

for a in range(len(tau)):
    print(tau[a],"   ",G2[a])
#plt.plot(tau,G2,"-")
#plt.xlabel("t [s]")
#plt.ylabel("$G_2 (t / t_{0})$")
#plt.show()
