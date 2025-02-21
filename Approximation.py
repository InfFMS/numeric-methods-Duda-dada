
#x3 – x +1 = 0
#x3 – x2 – 9x + 9 = 0
#x2 – ex = 0
#5x – 6ln(x) – 7 = 0
#cos(x) + 2x – 3 = 0
#C точностью до 0.01.

import numpy as np
import matplotlib.pyplot as mp
import math


#функция для поиска корней
delta=0.01
def solve(f,a,b):
     while (b-a)/2 >= delta:
         c = (a+b)/2
         if f(c)==0:
             return(c)
         elif f(a)*f(b)<0:
             b=c
         else:
             a=c
     return((a+b)/2)
#1)
def eq1(x):
    return x**3 - x + 1
x=np.linspace(-2,1 ,1000)
y= x**3 - x + 1
fig,ax=mp.subplots()
mp.plot(x,y ,label="1",color='black')
mp.grid(True)
mp.show()
print('Корни первого уравнения', solve(eq1,-1.5,1))
#2)
def eq2(x):
    return x**3 - x**2 - 9*x + 9
x=np.linspace(-5,5 ,1000)
y= x**3 - x**2 - 9*x + 9
fig,ax=mp.subplots()
mp.plot(x,y ,label="2",color='black')
mp.grid(True)
mp.show()
print('Корень второго уравнения(1)', solve(eq2,-4,-2))
print('Корень второго уравнения(2)', solve(eq2,-1,2))
print('Корни второго уравнения(3)', solve(eq2,2,4))
#3)
def eq3(x):
    return x**2- np.exp(x)
x=np.linspace(-5,5 ,1000)
y= x**2 - np.exp(x)
fig,ax=mp.subplots()
mp.plot(x,y ,label="3",color='black')
mp.grid(True)
mp.show()
print('Корень третьего уравнения', solve(eq3,-1,1))

#4)
def eq4(x):
    return 5*x - 6*np.log(x) - 7
x=np.linspace(0.1,5 ,1000)
y= 5*x - 6*np.log(x) - 7
fig,ax=mp.subplots()
mp.plot(x,y ,label="4",color='black')
mp.grid(True)
mp.show()
print('Корень четвертого уравнения(1)', solve(eq4,0.1,1))
print('Корень четвертого уравнения(1)', solve(eq4,2,5))

def eq5(x):
    return np.cos(x) + 2*x - 3
x=np.linspace(-5,5 ,1000)
y= np.cos(x) + 2*x - 3
fig,ax=mp.subplots()
mp.plot(x,y ,label="5",color='black')
mp.grid(True)
mp.show()
print('Корень пятого уравнения', solve(eq5,0,2))


