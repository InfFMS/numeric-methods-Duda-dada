import matplotlib.pyplot as mp
import numpy as np

#1)
x1 = np.linspace(0, np.pi, 100)
y1 = np.sin(2*x1) + 1
y2 = -0.2*x1**2 +0.5
fig, axs = mp.subplots()
mp.plot(x1, y1, label="y1 = sin(2x) +1", color="pink")
mp.plot(x1, y2, label="y2 = -0.2*x**2 +0.5", color="purple")
mp.grid(True)
mp.legend()
mp.show()
a = 3.14/99
def f(x):
    y = np.sin(2*x) + 1
    return y
def f1(x):
    y = -0.2*x**2 +0.5
    return y
#def find_square(f,f1):
S1 = 0
sum1 =0
for i in range(99):
    S1 = a * (f(i*a)+f((i+1)*a ))/2
    sum1= sum1 + S1
#print(sum)
S2 = 0
sum2 =0
for i in range(99):
    S2 = a * (f1(i*a) + f1((i+1)* a)) / 2
sum2= S2+sum2
        #return (sum2)
print('1)площадь под графиком', sum1-sum2)

#2)
x2 = np.linspace(np.pi*(-1)/2, np.pi*(1/2), 100)
y3=np.cos(x2)+1.2
y4=-0.5*(x2**2)+0.7
fig, axs = mp.subplots()
mp.plot(x2, y3, label="y1 = cos(x)+1.2", color="blue")
mp.plot(x2, y4, label="y2 = -0.5*(x^2)+0.7", color="red")
mp.grid(True)
mp.legend()
mp.show()
a = 3.14/99
def f2(x2):
    y = np.cos(x2)+1.2
    return y
def f3(x2):
    y = -0.5*(x2**2)+0.7
    return y
S3 = 0
sum3 =0
for i in range(99):
    S3 = a * (f2(i*a)+f2((i+1)*a ))/2
    sum3= sum3 + S3
#print(sum)
S4 = 0
sum4 =0
for i in range(99):
    S4 = a * (f3(i*a) + f3((i+1)* a)) / 2
sum4= S4+sum4
print('2) площадь под графиком', sum3-sum4)
#3
x3 = np.linspace(-2,2, 100)
y5 = np.exp(-1*(x3**2) +1)
y6 = -0.3*(x3**3)+0.5
fig, axs = mp.subplots()
mp.plot(x3, y5, label="3 график", color="black")
mp.plot(x3, y6, color="grey")
mp.grid(True)
mp.legend()
mp.show()
a = 3.14/99
def f4(x3):
    y = np.exp(-1*(x3**2)+1)
    return y
def f5(x3):
    y = -0.3*(x3**3)+0.5
    return y
S5 = 0
sum5 =0
for i in range(99):
    S5 = a * (f4(i*a)+f4((i+1)*a ))/2
    sum5= sum5 + S5
#print(sum)
S6 = 0
sum6 =0
for i in range(99):
    S6 = a * (f5(i*a) + f5((i+1)* a)) / 2
sum6= S6+sum6

print('3)площадь под графиком', sum5-sum6)

#4
x4 = np.linspace(-2,2, 100)
y7 = np.exp(-1*(x4**2)+0.5)
y8 = 0.2*(np.sin(3*x4))-0.5
fig, axs = mp.subplots()
mp.plot(x4, y7, label="exp(-1*(x**2)+0.5", color="black")
mp.plot(x4, y8, label='0.2*(sin(3x))-0.5', color="grey")
mp.grid(True)
mp.legend()
mp.show()
a = 3.14/99
def f6(x4):
    y = np.exp(-1*(x4**2)+0.5)
    return y
def f7(x4):
    y = 0.2*(np.sin(3*x4))-0.5
    return y
S7 = 0
sum7 =0
for i in range(99):
    S7 = a * (f6(i*a)+f7((i+1)*a ))/2
    sum7= sum7 + S7
#print(sum)
S8 = 0
sum8 =0
for i in range(99):
    S8 = a * (f7(i*a) + f7((i+1)* a)) / 2
sum8= S8+sum8

print('4)площадь под графиком', sum7-sum8)

#5

x5 = np.linspace(-2,2, 100)
y9 = np.exp(-1*((x5+1)**2)+np.exp(-1*((x5-1)**2)+0.5))
y10 = -0.3*(x5**2)
fig, axs = mp.subplots()
mp.plot(x5, y9, label="exp(-1*((x5+1)^2)+exp(-1*((x5-1)^2)+0.5))", color="black")
mp.plot(x5, y10, label='-0.3*(x5^2)', color="grey")
mp.grid(True)
mp.legend()
mp.show()
a = 3.14/99
def f8(x5):
    y = np.exp(-1*((x5+1)**2)+np.exp(-1*((x5-1)**2)+0.5))
    return y
def f9(x5):
    y = -0.3*(x5**2)
    return y
S9 = 0
sum9 =0
for i in range(99):
    S9 = a * (f8(i*a)+f8((i+1)*a ))/2
    sum9= sum9 + S9
#print(sum)
S10 = 0
sum10 =0
for i in range(99):
    S10 = a * (f9(i*a) + f9((i+1)* a)) / 2
sum10= S10+sum10

print('5)площадь под графиком', sum9-sum10)
