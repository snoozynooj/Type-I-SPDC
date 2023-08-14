
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:08:47 2023

@author: burto
"""

import numpy as np
import math as mt
import sympy as sym 
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import quad



lp = 1546/2
l1 = lp*2
L = 1E-3


"ECIWAO2"
# name = "ECIWAO2_1546"
# nx = [2.244749370863437, 0.021210878841035327, 249271.630840839, 1.341788542915219, 103697.67847428357]
# ny = [2.2674359820805026, 0.7305737041835006, 93026.7459292061, 0.007188263486725759, 275317.1249668403]
# nz = [1.9356230815936633, 0.647391916399499, 92131.90208764428, 0.015243093049533935, 245775.80021589616]


# sello =[2.244749370863437, 0.021210878841035327, 249271.630840839, 1.341788542915219, 103697.67847428357]
# selle = [1.9356230815936633, 0.647391916399499, 92131.90208764428, 0.015243093049533935, 245775.80021589616]

# selle =[2.244749370863437, 0.021210878841035327, 249271.630840839, 1.341788542915219, 103697.67847428357]
# sello = [1.9356230815936633, 0.647391916399499, 92131.90208764428, 0.015243093049533935, 245775.80021589616]

"RUVBAN"
# name="RUVBAN"
# nx = [1.890485989527627, 0.445934354674558, 51617.383906844494, 0.011347944387600846, 134111.93539515167]
# ny = [2.1167613266381378, 1.0476944643598867, 60670.54013015806, 0.027403703050539584, 127971.86535946309]
# nz = [2.169642433924311, 1.0863421247626117, 65076.08574104012, 0.030305414019025347, 129218.10091242459]


# sello = [2.169642433924311, 1.0863421247626117, 65076.08574104012, 0.030305414019025347, 129218.10091242459]
# selle = [1.890485989527627, 0.445934354674558, 51617.383906844494, 0.011347944387600846, 134111.93539515167]
   
"AQOROP2"
# name = "AQOROP2_1546"

# nx = [2.802842361442532, 0.004111349599221632, 259263.48638758608, 1.6668444730363403, 119747.7488400518]
# ny = [2.311600808110341, 0.6547201800991022, 99024.0849514373, 0.007641837600799524, 260078.63920492862]
# nz = [2.2466349992326973, 0.5306358571265285, 86212.66806255151, 0.005643573472296574, 263802.34610423766]

# selle = [2.802842361442532, 0.004111349599221632, 259263.48638758608, 1.6668444730363403, 119747.7488400518]
# sello = [2.2466349992326973, 0.5306358571265285, 86212.66806255151, 0.005643573472296574, 263802.34610423766]



"MOFTIL2"
name = "MOFTIL2_1546"
nx = [1.7989663052680425, 0.5604479801909195, 99824.63793504509, 1.3144374332355626, 37961.82879291918]
ny = [1.7399916301454426, 0.26285885704236384, 106041.41806049037, 0.9907409494670057, 36163.86127135452]
nz = [1.6482007420228795, 0.1728575560603238, 102104.2784739305, 0.9919406829003953, 27910.40849062094]     
 

"switch e-o"
sello = [1.7989663052680425, 0.5604479801909195, 99824.63793504509, 1.3144374332355626, 37961.82879291918]
selle = [1.6482007420228795, 0.1728575560603238, 102104.2784739305, 0.9919406829003953, 27910.40849062094]










X2 = np.zeros((3,9))

"ECIWAO_1546"


# X2[0][0]= -3.03100001E-06
# X2[0][1]= 0.887099981 
# X2[0][2]=   0.802299976
# X2[0][3]=  0.887099981
# X2[0][4]=  8.03499972E-07 
# X2[0][5]= -7.95599988E-07
# X2[0][6]=  0.802299976  
# X2[0][7]= -7.95599988E-07
# X2[0][8]= -5.20299977E-07 


# X2[1][0]=   0.879400015 
# X2[1][1]= 1.83699996E-07
# X2[1][2]=  -6.55800022E-07 
# X2[1][3]= 1.83699996E-07 
# X2[1][4]= -1.00600004 
# X2[1][5]= 0.340499997
# X2[1][6]=   -6.55800022E-07 
# X2[1][7]= -  0.340499997 
# X2[1][8]=   1.42600000 

# X2[2][0]=  0.922900021
# X2[2][1]=  8.56700026E-08
# X2[2][2]=  -2.47099990E-07 
# X2[2][3]=  8.56700026E-08
# X2[2][4]=  0.273299992    
# X2[2][5]=  1.65100002  
# X2[2][6]=  -2.47099990E-07
# X2[2][7]=   1.65100002  
# X2[2][8]=  -2.99000001 

"AQOROP_1546"


# X2[0][0]=  0.774200022  
# X2[0][1]= 6.72299997E-04
# X2[0][2]= -3.60700004E-02 
# X2[0][3]= 6.72299997E-04
# X2[0][4]=  2.91799998  
# X2[0][5]= 1.99400005E-04
# X2[0][6]=  -3.60700004E-02
# X2[0][7]= 1.99400005E-04
# X2[0][8]=  0.210600004  


# X2[1][0]= 7.03500002E-04
# X2[1][1]= 3.06999993 
# X2[1][2]= 2.24200005E-04
# X2[1][3]= 3.06999993 
# X2[1][4]= 2.54100002E-03
# X2[1][5]=  -3.41100001
# X2[1][6]= 2.24200005E-04
# X2[1][7]= -3.41100001   
# X2[1][8]= 7.69099977E-04

# X2[2][0]= 1.96700003E-02  
# X2[2][1]= 1.97200003E-04
# X2[2][2]= 0.515399992    
# X2[2][3]= 1.97200003E-04 
# X2[2][4]=  -3.29600000 
# X2[2][5]=  7.29500025E-04  
# X2[2][6]= 0.515399992 
# X2[2][7]= 7.29500025E-04
# X2[2][8]= 2.36700010 


"MOFTIL_1546"


# X2[0][0]=   0.856000006 
# X2[0][1]=  -7.22900004E-05 
# X2[0][2]=  -0.204600006
# X2[0][3]= -7.22900004E-05
# X2[0][4]=    2.15199995 
# X2[0][5]=   -9.23500011E-06
# X2[0][6]=  -0.204600006  
# X2[0][7]=   -9.23500011E-06
# X2[0][8]=  0.206100002 


# X2[1][0]=  -7.39399984E-05 
# X2[1][1]=   2.14800000   
# X2[1][2]= -9.46599994E-06  
# X2[1][3]=   2.14800000 
# X2[1][4]=  -2.40599999E-04
# X2[1][5]=   -3.00500011  
# X2[1][6]= -9.46599994E-06 
# X2[1][7]= -3.00500011 
# X2[1][8]=   -8.78299979E-05

# X2[2][0]= -0.205799997 
# X2[2][1]= -9.54499956E-06
# X2[2][2]= 9.40999985E-02  
# X2[2][3]= -9.54499956E-06 
# X2[2][4]=  -3.03099990  
# X2[2][5]= -8.47199990E-05 
# X2[2][6]= 9.40999985E-02
# X2[2][7]=  -8.47199990E-05
# X2[2][8]=  -0.199599996





    
def Sell(l, A, B1, C1, B2, C2):
    return mt.sqrt(((A)+(((l**2)*B1)/((l**2)-C1))+(((l**2)*B2)/((l**2)-C2))))




sigma_p = 0.875E-6
sigma_1 = 1.875E-6

P = 1E-3

pi = mt.pi

c=299792458



l = 1546/2
lam_t = l
l1 = l*2




no = Sell(l,*sello)
ne = Sell(l,*selle)

if no > ne:
    type_ = 'negative' 
elif ne > no:
    type_ = 'positive'
     
    
def neff(lam,ang):
    no = Sell(lam,*sello)
    ne = Sell(lam,*selle)
    a = np.cos(ang)**2 / (no*no)
    b = np.sin(ang)**2 / (ne*ne)
    nef = np.sqrt(1/(a+b))
    return nef


def f(x,l_p,l_e,a_c):
    l_o = l_e*l_p/(l_e-l_p)
    if type_=='negative':
        kp = 2*mt.pi*neff(l_p,a_c)/(l_p*1E-9)
        ko = 2*mt.pi*Sell(l_o,*sello)/(l_o*1E-9)
        ke = 2*mt.pi*neff(l_e,a_c-x[1])/(l_e*1E-9)
    if type_=='positive':
        kp = 2*mt.pi*Sell(l_p,*sello)/(l_p*1E-9)
        ko = 2*mt.pi*Sell(l_o,*sello)/(l_o*1E-9)
        ke = 2*mt.pi*neff(l_e,a_c-x[1])/(l_e*1E-9)
        
    A = ke*np.cos(x[1])+ko*np.cos(x[0])-kp
    B = ke*np.sin(x[1])+ko*np.sin(x[0])
    return A,B


phi = np.linspace(0,mt.pi/2,10000)
val_1 = []
val_=[]
phi_ = []
for a in range(len(phi)):
    val = np.sum(np.abs(f([0,0],l,l1,phi[a])))
    val_1.append(val)
    if val<10000:
        val_.append(val)
        phi_.append(phi[a])
i = np.argmin(val_)
a_c = phi_[i]


phi_ = np.linspace(0,360,num=1000)

res__=[]

if no > ne:
    n_p = neff(l,a_c)
elif ne > no:
    n_p = Sell(l,*sello)
     


def d_eff(phi,a_c):  

   if type_=='negative':
        
        X3=np.reshape(X2, (3,3,3), order='C')
        
    
    
        def T2(phi):
            h2=0
            o = np.zeros((3,1))
            o[0] = np.sin(phi)
            o[1] = -np.cos(phi)
    
            e = np.zeros((3,1))
            e[0] = -np.cos(a_c)*np.cos(phi)
            e[1] = -np.cos(a_c)*np.sin(phi)
            e[2] = np.sin(a_c)
            def P(i,j,k):
                ei=e[i]
                ej=e[j]
                ok=o[k]
                dijk= X3[i,j,k]
                t = ei*dijk*ej*ok
                return t

            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        h = P(a,b,c)
                        
                        # print(h)
                        h2=h+h2
            return h2

        Deff = T2(phi)
    
    
   elif type_=='positive':
        X3=np.reshape(X2, (3,3,3), order='C')
        def T2(phi):
            h2=0
            # phi  = phi*mt.pi/180
            o = np.zeros((3,1))
            o[0] = -np.sin(phi)
            o[1] = np.cos(phi)

            e = np.zeros((3,1))
            e[0] = -np.cos(a_c)*np.cos(phi)
            e[1] = -np.cos(a_c)*np.sin(phi)
            e[2] = np.sin(a_c)
            def P(i,j,k):
                oi=o[i]
                ej=e[j]
                ok=o[k]
                dijk= X3[i,j,k]
            
                t = oi*dijk*ej*ok
                return t
            for a in range(3):
                for b in range(3):
                    for c in range(3):
                        h = P(a,b,c)
                        h2=h+h2
            # h2=abs(h2)
            return h2
        Deff = T2(phi)
    
   return Deff

deff = []

for a in range(len(phi_)):
    deff.append(d_eff(phi_[a]*mt.pi/180,a_c))
    
plt.plot(phi_,deff,"-")    
# np.savetxt('Deff_phi'+name+'.txt', phi_)
# np.savetxt('Deff_deff'+name+'.txt', deff)



plt.show()    
i = np.argmax(np.abs(deff))
phi_opt = phi_[i]
theta_opt = a_c * 180/mt.pi
deff_m = np.max(np.abs(deff))    

x=sym.symbols('x')
def Sell2(x, A, B1, C1, B2, C2):
        return sym.sqrt(((A)+(((x**2)*B1)/((x**2)-C1))+(((x**2)*B2)/((x**2)-C2))))

def neff2(x,ang):
    no = Sell2(x,*sello)
    ne = Sell2(x,*selle)
    a = np.cos(ang)**2 / (no*no)
    b = np.sin(ang)**2 / (ne*ne)
    nef = sym.sqrt(1/(a+b))
    return nef

def f_e(x,ang):
    a = neff2(x,ang)
    return a
def f_o(x):
    a = Sell2(x,*sello)
    return a


def nge(l1):
        D = sym.diff(f_e(x,a_c))
        a = f_e(x,a_c)-l1*1E-9*(D)
        a = a.subs(x,l1)
        return a

def ngo(l1):
        D = sym.diff(f_o(x))
        a = f_o(x)-l1*1E-9*(D)
        a = a.subs(x,l1)
        return a



ng_e = nge(l1)
ng_o = ngo(l1)


Dng= abs(ng_e-ng_o)
band = 1E-9
band =  c / (band)

def I(v,t):
    s = mt.sin((Dng*L/(c*2))*v)
    s = s/((Dng*L/(c*2)*v)) 
    a = np.exp(-v**2/band**2)
    b = np.exp(1j*v*t)
    inte = s*a*b.real
    
    return inte


def Ii(x,t):
    s = mt.sin((Dng*L/(c*2))*x)
    s =  s/((Dng*L/(c*2)*x)) 
    a = np.exp(-x**2/band**2)
    b = np.exp(1j*x*t)
    
    inte = s*a*b.imag
    return inte


vo= float(2*c/(Dng*L))
tl = float(Dng*L/(c*2))*20
tl = tl*vo
vo = vo/vo

tau = np.linspace(-tl,tl,2001)
G2 = []



for a in range(len(tau)):
    I1 = quad(I,-vo+1,vo,args = (tau[a]))[0]
    I2 = quad(Ii,-vo+1,vo,args = (tau[a]))[0]
    i_t = np.sqrt(I1.real**2+I2.real**2)**2
    # i_t = np.sqrt(i_t**2)
    G2.append(i_t)

f_max = np.max(G2)

# vmax= np.array(1.835563942397468E+26)
# G2 = G2/vmax
tau = tau*Dng*L/(c*4)
plt.plot(tau,G2,"-")
plt.xlabel('t / $t_c$')
plt.ylabel('$G^{(2)}$')
plt.show()

# np.savetxt('G2_t_'+name+'.txt', tau)
# np.savetxt('G2_'+name+'.txt', G2)


# G2 = G2*vmax
f_max = np.max(G2)

f_2 = f_max/2
val = []
num = []




i = np.argmin(np.abs(G2-f_2))
G2_fwhm= G2[i]
i_=[]
# tau = tau*Dng*L/(c*4)
for a in range(len(G2)):
    if abs(G2_fwhm-G2[a])<np.min(G2)/1000:
        i_.append(a)

fwhm = tau[i_[1]]-tau[i_[0]]


print('\n')
print('the value of the FWHM is:', fwhm)






n_e = neff(l1, a_c)
n_o = Sell(l1,*sello)

if n_e > n_o:
    n_1 =n_o
else:
    n_1 = n_e
    
wp = 2*mt.pi*c/  (lp*1E-9*n_p)
"sinc function"
f= float(wp/2)
w1 = 2*mt.pi*c/  (l1*1E-9*n_1)
Dng = float(Dng)

Io = lambda h : (w1+h)*(wp-(w1+h))*np.sin((w1+h-wp/2)*(Dng*L/(c*2)))**2/((w1+h-wp/2)*(Dng*L/(c*2)))**2
Io1 = quad(Io, -f, f+10)
error = Io1[1]
Io1 = Io1[0]

""" value of the review"""
deff_m = deff_m*1E-12*2

eo = 8.8541878176E-12
P = 1E-3

Ep2 = P/(c*eo*mt.pi*n_1*sigma_p**2)
R1 = Ep2*(deff_m**2)*L*L/(2*mt.pi*c*c)
R2 = ng_e*ng_o/(n_1**4)
R3 = (abs(sigma_p**2/(sigma_1**2 + 2*sigma_p**2)))**2

Rsm = float(R1*R2*R3*Io1)

print("Dng:")
print(Dng)
print("Rsm:")
print(Rsm)
print('optic axis angle:')
print(a_c*180/mt.pi)
print('deff:')
print(deff_m*1E12/2)
print('phi_max:')
print(phi_opt)
