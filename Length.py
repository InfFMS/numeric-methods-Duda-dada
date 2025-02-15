#cos(x)
#cos(x) + 0.1*x2
#-tanh(x-π/2)
#-0.2*(x- π)3 + 0.5*(x- π)2 +1
#На отрезке от 0 до π.

import numpy as np
import matplotlib.pyplot as mp

x=np.linspace(0,5,100)
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
