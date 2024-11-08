# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:19:56 2021

@author: Alonso
"""


from math import e, log

Rg=10; Cgs= 1.55e-9; Vgs1=6.5; Vgm=15; Vth= 5.3
Vp=24; Cgd= 0.25e-9; Ip=12; 
#Vgs1p= 4.2; Vthp=3.5; no lo considero al final
Cds= 0.25e-9

t1= Rg*Cgs*( log(1/(1-Vgs1/Vgm)) -log(1/(1-Vth/Vgm )) )
t2= Rg*Cgd*(Vp/(Vgm-Vgs1))
ton= t1 + t2
Eon= 0.5*Vp*Ip*ton + 0.5*Cds*Vp**2

t3= Rg*Cgd*Vp/Vgs1
t4= Rg*Cgs*log(Vgs1/Vth)
toff= t3+t4
Eoff= 0.5*Vp*Ip*toff

Egon=  Cgs*Vgm**2 + Vgm*Vp*Cgd
Egoff= 0.5*Cgs*Vgm**2 + Vgs1*Vp*Cgd

print("t1= ", t1)
print("t2= ", t2)
print("ton =", ton)
print("Eon =", Eon)

print("t3= ", t3)
print("t4= ", t4)
print("toff =", toff)
print("Eoff =", Eoff)

print("Egon =", Egon)
print("Egoff =", Egoff)
