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
lp = 532
l1 = lp*2
deff = 3.7*1E-12
x2_eff = 2*deff
L = 1E-3



"RUVBAN"

nx = [1.890485989527627, 0.445934354674558, 51617.383906844494, 0.011347944387600846, 134111.93539515167]
ny = [2.1167613266381378, 1.0476944643598867, 60670.54013015806, 0.027403703050539584, 127971.86535946309]
nz = [2.169642433924311, 1.0863421247626117, 65076.08574104012, 0.030305414019025347, 129218.10091242459]
        
theta_m =  90.0 
phi_m =18.55 
deff_m =  2.57071981542305 


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
plt.plot(tau,G2,"-")
plt.xlabel("t [s]")
plt.ylabel("$G_2 (t / t_{0})$")
plt.show()
