import matplotlib.pyplot as plt

# Implementace Eratosthenova sita pro generovani prvocisel
def SieveOfEratosthenes(n):
     
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
             
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    primelist = list()
    for p in range(n + 1):
        if prime[p]:
            primelist.append(p)
    return primelist

# Vytvori souradnice dalsiho bodu
# Cyklicky se souradnice pricita +i, +j, +k, -i, -j, -k 
def create_point(i):
    global xprev
    global yprev
    global zprev
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

# Deklarace souradnic a inicializace pocatecniho bodu [0,0,0]
xdata = list()
ydata = list()
zdata = list()
xdata.append(0)
ydata.append(0)
zdata.append(0)
xprev = False
yprev = False
zprev = False

print("Enter the range in which you would like to calculate and draw primes (recommended 10000): ",end='')
n = int(input())

# Nacteni prvocisel do listu primes
primes = SieveOfEratosthenes(n)
primes.insert(0,0)

# Je vytvoreno zobrazeni vsech bodu
for i in range(0,len(primes)-1):
    create_point(i)

# 3D Graf
ax = plt.axes(projection = '3d')
ax.axis('off')
ax.axis('auto')
ax.plot3D(xdata, ydata, zdata, color='C1')
plt.show()
