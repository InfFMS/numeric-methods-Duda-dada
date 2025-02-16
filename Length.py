#cos(x)
#cos(x) + 0.1*x2
#-tanh(x-π/2)
#-0.2*(x- π)3 + 0.5*(x- π)2 +1
#На отрезке от 0 до π.

import numpy as np
import matplotlib.pyplot as mp
import math
#########
x=np.linspace(0,4 ,100)
y=np.cos(x)
fig,ax=mp.subplots()
mp.plot(x,y ,label="cos(x)",color='red')
mp.grid(True)
mp.show()
def f(a):
    f=np.cos(a)
    return(f)

m=3.14/99
len=0
for i in range(99):
    el=i+m*i
    le=(((f(el)-f(el+m))**2) + m**2)**0.5
    len+=le
print(len)
################

x2=np.linspace(0,4,100)
y2=np.cos(x2) + 0.1*(x2**2)
fig,ax=mp.subplots()
mp.plot(x2,y2 ,label="cos(x) + 0.1 * x^2",color='blue')
mp.grid(True)
mp.show()
def f2(a2):
    f2= np.cos(a2) + 0.1*(x2**2)
    return(a2)
m=3.14/99
len2=0
for i in range(99):
    el=i+m*i
    l=(((f2(el)-f2(el+m))**2) + m**2)**0.5
    len2+=l
print(len2)

################    -tanh(x-π/2)=-ctg(x)


# x3=np.linspace(0,4,99)
# y3= math.tanh(x3-math.pi/2)
# fig,ax=mp.subplots()
# mp.plot(x3,y3 ,label="-ctg(x)",color='black')
# mp.legend()
# mp.grid(True)
# mp.show()
# def f3(a3):
#     f3=math.tanh(x3-math.pi/2)
#     return(a3)
#
# m=3.14/99
# len3=0
# for i in range(99):
#     el=i+m*i
#     lee=(((f3(el)-f3(el+m))**2) + m**2)**0.5
#     len3+=lee
# print(len3)

#####-0.2*(x- π)3 + 0.5*(x- π)2 +1
x4=np.linspace(0,4,99)
y4= -0.2*(x4-3.14)**3 + 0.5*(x4-3.14)**2 +1
fig,ax=mp.subplots()
mp.plot(x4,y4 ,color='black')
mp.grid(True)
mp.show()
def f4(a4):
    f4= -0.2*(x4-3.14)**3 + 0.5*(x4-3.14)**2 +1
    return(a4)

m=3.14/99
len4=0
for i in range(99):
    z=i+m*i
    lll=(((f4(z)-f4(z+m))**2) + m**2)**0.5
    len4+=lll
print(len4)
