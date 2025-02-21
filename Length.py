#cos(x)
#cos(x) + 0.1*x2
#-tanh(x-π/2)
#-0.2*(x- π)3 + 0.5*(x- π)2 +1
#На отрезке от 0 до π.
#


import numpy as np
import matplotlib.pyplot as mp


def length(f,a,b,n=100):
    x=np.linspace(a,b,n)
    y=f(x)
    total_length=0
    for i in range(n-1):
        dx =x[i+1]-x[i]
        dy=y[i+1]-y[i]
        total_length+=np.sqrt(dx**2+dy**2)
    return total_length


a=0
b=np.pi
#1
x=np.linspace(0,4 ,100)
y=np.cos(x)
fig,ax=mp.subplots()
mp.plot(x,y ,label="cos(x)",color='red')
mp.grid(True)
mp.show()
def f1(x):
    return np.cos(x)
print(length(f1, a, b))
#2
x2=np.linspace(0,4,100)
y2=np.cos(x2) + 0.1*(x2**2)
fig,ax=mp.subplots()
mp.plot(x2,y2 ,label="cos(x) + 0.1 * x^2",color='blue')
mp.grid(True)
mp.show()
def f2(x):
    return np.cos(x)+0.1*(x**2)
print(length(f2, a, b))
#3
x3=np.linspace(0,4,99)
y3= -np.tanh(x3 - np.pi/2)
fig,ax=mp.subplots()
mp.plot(x3,y3 ,label="-tanh(x-pi/2)",color='black')
mp.legend()
mp.grid(True)
mp.show()
def f3(x):
    return -(np.tanh(x-np.pi/2))
print(length(f3, a, b))
#4
x4=np.linspace(0,4,99)
y4= -0.2*(x4-3.14)**3 + 0.5*(x4-3.14)**2 +1
fig,ax=mp.subplots()
mp.plot(x4,y4 ,color='black')
mp.grid(True)
mp.show()
def f4(x):
    return (-0.2)*(x -np.pi)**3 + 0.5*(x-np.pi)**2 + 1

print(length(f4, a, b))
