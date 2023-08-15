
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 12:08:47 2023

@author: burto
"""

import numpy as np
import math as mt
import matplotlib.pyplot as plt
from scipy.optimize import fsolve




lp = 532
l1 = lp*2
L = 1E-3

"VURQEF"
# selle =[1.939257624156827 ,0.0046201733565161655 ,134742.8486912627,0.33491150572064055 ,58887.39779184338]
# sello =[2.1475021915246852,0.053489472771176425,123809.63532074595,1.0018224278971701,61503.94989289683]

"ONOCOL01"

# selle =[2.1334087182826034  ,0.020186114832955425 , 141599.75428975158 ,
#         0.623776906026098,74386.52334436034]

# sello =[2.0176250569716565,0.7576661886990735,74373.12169702443,
#         0.021079767099701188 , 140557.65756427593]

"DIXWAJ"

# selle =[1.7783232373198676, 0.5722653646923247, 33446.38215349205 
#         ,0.022346399310137197, 111995.3093201559]

# sello =[1.8947691941920024, 0.6359258224174567, 43593.62331052622 ,
#         0.019881239623018326, 115897.98846865435]


"EGIKUB02-positive"

# selle =[28.58361934928793, 4.678281989258097 ,38777.47397406969, -29.859470549741367, 3901.777720512696]
# sello =[2.1247034822538793, 1.3479529974292561, 64271.73803350773, -0.7838555650189348, 64271.44937753851]


"SAQFUM"

# selle =[1.7904651598466805, 0.05460624769454377, 91607.55007814994, 0.8105872457802059, 39695.810041926314]
# sello =[2.010363328440273, 0.017750282020272998, 103541.8012539858, 0.9268891080565168, 52126.34901563138]


"IMIDZB01"


# selle =[1.6409276310876717, 0.03223158698506867, 65442.877713637296, 0.8306185154607646, 30955.348304207553]
# sello =[1.626875367720352, 0.027472717394730794, 66000.34486210723, 0.7713644531266042, 31002.003558130426]



"JETVOW "

# selle =[1.6151557699503352, 6.797047775595605, 147256.52157161472, -6.599881633983939,  147256.54568566725]
# sello =[37.7792828639067, -28.04335554516492, -1398.2030108441538, -8.068648554586543, -1399.8726462146058]


"SAQFUM"

# selle =[1.7904651598466805, 0.05460624769454377, 91607.55007814994, 0.8105872457802059, 39695.810041926314]
# sello =[2.010363328440273, 0.017750282020272998, 103541.8012539858, 0.9268891080565168, 52126.34901563138]

"HUTZAX01"
# selle =[1.9506247077249423, 0.04715137705501194, 147125.72469734427, 0.736156281563366, 73069.18124700317]
# sello =[1.8316125123106444, 0.03563666377502507, 146407.9011037287, 0.5380899588668341, 72323.59799735252]

"QAMFUF01"

# selle =[2.3297071434970777, 0.7631669713632797, 111356.41996754002, 0.013660312816163625, 234959.3759941976]
# sello =[2.2616312803445866, 0.712052892644223, 99894.22143037003, 0.020050265286093865, 226021.8058987032]


"BEKVOD"

# sello =[1.7373525060510397 ,0.06638627242955507, 94306.0064712162, 0.8939868395752323, 34981.736334657595]
# selle =[1.6981678862394916, 0.9435479433377625, 39007.615296841956, 0.08072651809788102, 95789.49430925158]


"WUJFOW"

# selle =[1.4989126755382198, 0.051375768726868755, 52057.87427313697, 1.0679062576555514,     17915.35072299919]
# sello =[1.5063880234757272, 0.059630633594892554, 52080.607237671225, 1.1375069884991353, 18094.6677718929]

# "ECIWAO2"
# name = "ECIWAO2"
# nx = [2.244749370863437, 0.021210878841035327, 249271.630840839, 1.341788542915219, 103697.67847428357]
# ny = [2.2674359820805026, 0.7305737041835006, 93026.7459292061, 0.007188263486725759, 275317.1249668403]
# nz = [1.9356230815936633, 0.647391916399499, 92131.90208764428, 0.015243093049533935, 245775.80021589616]


# sello =[2.244749370863437, 0.021210878841035327, 249271.630840839, 1.341788542915219, 103697.67847428357]
# selle = [1.9356230815936633, 0.647391916399499, 92131.90208764428, 0.015243093049533935, 245775.80021589616]



# "RUVBAN"
# name="RUVBAN"
# nx = [1.890485989527627, 0.445934354674558, 51617.383906844494, 0.011347944387600846, 134111.93539515167]
# ny = [2.1167613266381378, 1.0476944643598867, 60670.54013015806, 0.027403703050539584, 127971.86535946309]
# nz = [2.169642433924311, 1.0863421247626117, 65076.08574104012, 0.030305414019025347, 129218.10091242459]


# sello = [2.169642433924311, 1.0863421247626117, 65076.08574104012, 0.030305414019025347, 129218.10091242459]
# selle = [1.890485989527627, 0.445934354674558, 51617.383906844494, 0.011347944387600846, 134111.93539515167]

"AQOROP2"
name = "AQOROP2"

nx = [2.802842361442532, 0.004111349599221632, 259263.48638758608, 1.6668444730363403, 119747.7488400518]
ny = [2.311600808110341, 0.6547201800991022, 99024.0849514373, 0.007641837600799524, 260078.63920492862]
nz = [2.2466349992326973, 0.5306358571265285, 86212.66806255151, 0.005643573472296574, 263802.34610423766]

sello = [2.802842361442532, 0.004111349599221632, 259263.48638758608, 1.6668444730363403, 119747.7488400518]
selle = [2.2466349992326973, 0.5306358571265285, 86212.66806255151, 0.005643573472296574, 263802.34610423766]


"MOFTIL2"
name = "MOFTIL2"
nx = [1.7989663052680425, 0.5604479801909195, 99824.63793504509, 1.3144374332355626, 37961.82879291918]
ny = [1.7399916301454426, 0.26285885704236384, 106041.41806049037, 0.9907409494670057, 36163.86127135452]
nz = [1.6482007420228795, 0.1728575560603238, 102104.2784739305, 0.9919406829003953, 27910.40849062094]     
 
# selle = [1.7989663052680425, 0.5604479801909195, 99824.63793504509, 1.3144374332355626, 37961.82879291918]
# sello = [1.6482007420228795, 0.1728575560603238, 102104.2784739305, 0.9919406829003953, 27910.40849062094]

"MIRO101"
# name = 'MIRO101'
# sello =[2.1078,2.5100E-2,1.41489044E5,1.0871,5.62150205E4]
# selle =[1.7833 ,8.9000E-3,1.44323712E5,3.6470E-1,4.96202890E4]


"""MIRO102"""
# name = 'MIRO102'
# sello =[2.1385,1.1527,4.77658824E4,7.6600E-2,1.16666067E5]
# selle =[1.7890 ,5.0300E-2,1.07012455E5,7.4320E-1,3.58417385E4]

"MIRO-103"
# name = 'MIRO103'
# sello =[1.9010,5.1430E-1,5.12308938E4,4.0800E-2,1.57385759E5]
# selle =[2.0731 ,1.2882,5.76235328E4,1.0700E-2,1.59071640E5]


# lam_p= np.linspace(600,1400,num=500)
# lam_t = float(532)


    
def Sell(l, A, B1, C1, B2, C2):
    return mt.sqrt(((A)+(((l**2)*B1)/((l**2)-C1))+(((l**2)*B2)/((l**2)-C2))))









no = Sell(lp,*sello)
ne = Sell(lp,*selle)

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
        kp = 2*mt.pi*neff(l_p,a_c)/(l_p)
        ko = 2*mt.pi*Sell(l_o,*sello)/(l_o)
        ke = 2*mt.pi*neff(l_e,a_c-x[1])/(l_e)
    if type_=='positive':
        kp = 2*mt.pi*Sell(l_p,*sello)/(l_p)
        ko = 2*mt.pi*Sell(l_o,*sello)/(l_o)
        ke = 2*mt.pi*neff(l_e,a_c-x[1])/(l_e)
        
    A = ke*np.cos(x[1])+ko*np.cos(x[0])-kp
    B = ke*np.sin(x[1])+ko*np.sin(x[0])
    return A,B


phi = np.linspace(0,mt.pi/2,10000)
val_1 = []
val_=[]
phi_ = []
for a in range(len(phi)):
    val = np.sum(np.abs(f([0,0],lp,l1,phi[a])))
    val_1.append(val)
    if val<10000:
        val_.append(val)
        phi_.append(phi[a])
plt.plot(phi_,val_)
plt.xlabel('$\Theta_c$')
plt.ylabel('$\Delta k$')

        
plt.show()
i = np.argmin(val_)
a_c = phi_[i]



lam=np.linspace(850, 1400, num=100)


anoo=[]
aneo=[]
lae=[]
lao=[]
k_=[]  
l=0

for a in range(len(lam)):
    l_o= lam[a] * lp / (lam[a] - lp)

    result=1
    b=-mt.pi
    ano_o=[]
    ane_o=[]
    la_e=[]
    la_o=[]
    results=[]
    cod=[]
    k_=[]
    while b<mt.pi:

        x= fsolve(f,[-b,b],args=(lp,lam[a],a_c),xtol=1E-8)
        result= f(x,lp,lam[a],a_c)
        b= b+mt.pi/(180)
        k=0
        # if b>-1*mt.pi/(250) and f==0:
        #     b=1*mt.pi/(250)
        #     f=1
        if np.linalg.norm(result)<1e-7 and abs(neff(lam[a],a_c-x[0]) * np.sin(x[0]))<=1 and abs((l_o/lam[a])*neff(lam[a],a_c-x[0])  * np.sin(x[1]))<=1:
            results.append(abs(sum(result)))
            ao_e = mt.asin(neff(lam[a],a_c-x[1]) * np.sin(x[1]))
            ao_e = ao_e * 180 / np.pi
                
            ao_o=mt.asin(Sell(l_o,*sello)*mt.sin(x[0]))
            ao_o = ao_o * 180 / np.pi
            ano_o.append(ao_o)
            ane_o.append(ao_e)
            la_e.append(lam[a])
            la_o.append(l_o)
            k=1
        k_.append(k)
        
        
                
    h=sorted(results)
    for a in range(len(results)):
        if h[0]==results[a] or h[1]==results[a]:
            anoo.append(ano_o[a])
            aneo.append(ane_o[a])
            lae.append(la_e[a])
            lao.append(la_o[a])
        
        
plt.plot(lae,aneo,".",label='$n_e$')
plt.plot(lao,anoo,".",label='$n_e$')
plt.xlabel('$\theta_c$')
plt.ylabel('outside angle')
plt.legend()
        