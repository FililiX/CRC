from numpy.random import random
from numpy import sin,cos, true_divide
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation

def SieveOfEratosthenes(n):
     
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers
    primelist = list()
    for p in range(n + 1):
        if prime[p]:
            primelist.append(p)#Use print(p) for python 3
    return primelist
    
xdata = list()
ydata = list()
zdata = list()
xdata.append(0)
ydata.append(0)
zdata.append(0)

primes = SieveOfEratosthenes(10000)
primes.insert(0,0)
xprev = False
yprev = False
zprev = False

for i in range(0,len(primes)-1):
    if zprev == True or i == 0:
        xdata.append(xdata[i] + (  ((-1)**(i//3)) * (primes[i+1] - primes[i])))
        ydata.append(ydata[i])
        zdata.append(zdata[i])
        xprev = True
        zprev = False
    elif xprev == True:
        xdata.append(xdata[i])
        ydata.append(ydata[i] + (  ((-1)**(i//3)) * (primes[i+1] - primes[i]) ))
        zdata.append(zdata[i])
        xprev = False
        yprev = True
    elif yprev == True:
        xdata.append(xdata[i])
        ydata.append(ydata[i])
        zdata.append(zdata[i] + (  ((-1)**(i//3)) * (primes[i+1] - primes[i]) ))
        zprev = True
        yprev = False


fig = plt.figure(frameon=False,figsize=(16,9))
# Create 3D container
ax = plt.axes(projection = '3d')
ax.axis('off')
# Visualize 3D scatter plot
ax.plot3D(xdata, ydata, zdata)
# Give labels
plt.show()
