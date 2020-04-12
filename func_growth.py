import matplotlib.pyplot as plt 
import math
import numpy as np 

def Fa(n): return n**0.5
def Fb(n): return 10**n
def Fc(n): return n**1.5
def Fd(n): return 2**( (math.log2(n))**0.5 )
def Fe(n): return n**(5/3)

def plot(f, x, label):
    y = [f(i) for i in x]
    plt.plot(x,y, label = label)

# setting the x - coordinates 
x = np.arange(.1, 10) 

plot(Fa, x, 'A')
plot(Fb, x, 'B')
plot(Fc, x, 'C')
plot(Fd, x, 'D')
plot(Fe, x, 'E')

# function to show the plot 
plt.legend()
plt.show() 
