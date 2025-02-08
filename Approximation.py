
#x3 – x +1 = 0
#x3 – x2 – 9x + 9 = 0
#x2 – ex = 0
#5x – 6ln(x) – 7 = 0
#cos(x) + 2x – 3 = 0
#C точностью до 0.01.

import numpy as np
import matplotlib.pyplot as mp
import scipy as sp

massiv=[range(100)]
new_massiv=[]
for el in massiv:
    x=(el**3-el+1)

    new_massiv.append(x)
fig,ax=mp.subplots()
x=np.linspace(-10,10,100)
y=new_massiv
mp.plot(x,y,label="x^3-x+1",color='pink')
mp.show()


