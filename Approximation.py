
#x3 – x +1 = 0
#x3 – x2 – 9x + 9 = 0
#x2 – ex = 0
#5x – 6ln(x) – 7 = 0
#cos(x) + 2x – 3 = 0
#C точностью до 0.01.

import numpy as np
import matplotlib.pyplot as mp
import random as rd
import math


#1
x=np.linspace(-10,10,100)
new_massiv_Y=[]
fig,ax=mp.subplots()
for el in x:
    value=el**3-el+1
    new_massiv_Y.append(value)
mp.plot(x,new_massiv_Y,label="1",color='black')
mp.grid(True)
mp.show()
eps=0.01
def f(x):
   y=x**3-x+1
   return(y)
z1=-3
z2=3
def solve(f):
    d=rd.uniform(z1,z2)
    g=rd.uniform(z1,z2)
    x=rd.uniform(z1,z2)
    d_correct=z1
    g_correct=z2
    while abs(f(x))>eps:
      if f(d) * f(g) < 0:
         x=rd.uniform(d,g)
         d_correct=d
         g_correct=g
         d = rd.uniform(d, g)
         g = rd.uniform(d, g)
      else:
          d = rd.uniform(d_correct, g_correct)
          g = rd.uniform(d_correct, g_correct)
    return(x,f(x))
print('Корни первого уравнения:', solve(f))

#########2) x3 – x2 – 9x + 9 = 0


a=np.linspace(-10,10,100)
new_massiv2=[]
for el in a:
    value2=el**3-el**2-el*9+9
    new_massiv2.append(value2)
fig,ax=mp.subplots()
mp.plot(a,new_massiv2,label="(x**3-x**2-9x+9)",color='black')
mp.grid(True)
mp.show()
#-3,5   -2,5
#0,5     2
#2       3,5

def f2(x):
    y = x**3-x**2-x*9 + 9
    return (y)

z1=-3.5
z2=-2.5
print('Корни второго уравнения:', solve(f2))
z1=0.5
z2=2
print(solve(f2))
z1=2
z2=3.5
print(solve(f2))
########### 3) x2 – ex = 0
x2 = np.linspace(-10,10, 100)
y2 = x2**2 - np.exp(x2)
fig, axs = mp.subplots()
mp.plot(x2, y2, label="x2 – ex = 0", color="black")
mp.grid(True)
mp.legend()
mp.show()

def f3(x):
    y = x**2-np.exp(x)
    return (y)

z1=-2
z2=2
print('Корни третьего уравнения:', solve(f3))

##########4) 5x – 6ln(x) – 7 = 0
# x3 = np.linspace(-10,10, 100)
# y3 =  5*x3 - 6*math.log(x3) - 7
# fig, axs = mp.subplots()
# mp.plot(x3, y3, label="5x – 6ln(x) – 7 = 0", color="black")
# mp.grid(True)
# mp.legend()
# mp.show()
#
#



a=np.linspace(-10,10,100)
new_massiv5=[]
for el in a:
    value5=math.cos(el) + 2*el - 3
    new_massiv5.append(value5)
fig,ax=mp.subplots()
mp.plot(a,new_massiv5,label="(5)",color='black')
mp.grid(True)
mp.show()
#1,  2
def f5(x):
    y = math.cos(x) + 2*x - 3
    return (y)

z1=1
z2=2
print('Корни пятого уравнения:', solve(f5))