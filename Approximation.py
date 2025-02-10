
#x3 – x +1 = 0
#x3 – x2 – 9x + 9 = 0
#x2 – ex = 0
#5x – 6ln(x) – 7 = 0
#cos(x) + 2x – 3 = 0
#C точностью до 0.01.

import numpy as np
import matplotlib.pyplot as mp

x=np.linspace(-10,10,100)
new_massiv_Y=[]
for el in x:
    value=el**3-el+1
    new_massiv_Y.append(value)
fig,ax=mp.subplots()
mp.plot(x,new_massiv_Y,label="1",color='pink')
mp.grid(True)
mp.show()
eps=0.01
d=-5
f=d**3-d+1
g=5
def solve(d, g, f):
    m = (d + g) / 2
    while d-g>=2*eps:
        m = (d + g) / 2
        d, g = (a, m) if f(d) * f(m) < 0 else (m, g)
    return (d + g) / 2
print(solve(d,g,f))




#x3 – x2 – 9x + 9 = 0
a=np.linspace(-10,10,100)
new_massiv2=[]
for el in a:
    value2=el**3-el**2-el*9+9
    new_massiv2.append(value2)
fig,ax=mp.subplots()
mp.plot(a,new_massiv2,label="(x**3-x**2-9x+9)",color='black')
mp.grid(True)
mp.show()
eps=0.01
d=-5
g=-2.5
f=d**3-d**2-9*d + 9
def solve(d, g, f):
    m = (d + g) / 2
    while d-g>=2*eps:
        m = (d + g) / 2
        d, g = (a, m) if f(d) * f(m) < 0 else (m, g)
    return (d + g) / 2
print(solve(d,g,f))

d=0
g=5
f=d**3-d**2-9*d + 9
def solve(d, g, f):
    m = (d + g) / 2
    while d-g>=2*eps:
        m = (d + g) / 2
        d, g = (a, m) if f(d) * f(m) < 0 else (m, g)
    return (d + g) / 2
print(solve(d,g,f))



#x2 – ex = 0

l=np.linspace(-10,10,100)
new_massiv_3=[]
for el in x:
    value3=el**2-np.exp(el)
    new_massiv_3.append(value3)
fig,ax=mp.subplots()
mp.plot(l,new_massiv_3,label="3",color='purple')
mp.grid(True)
mp.show()
eps=0.01
d=-10
g=10
f=l**2-np.exp(l)

def solve(d, g, f):
    m = (d + g) / 2
    while d-g>=2*eps:
        m = (d + g) / 2
        d, g = (a, m) if f(d) * f(m) < 0 else (m, g)
    return (d + g) / 2
print(solve(d,g,f))

