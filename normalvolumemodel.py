import numpy as np
import math
import matplotlib.pyplot as plt

def volumesphere(r):
	return (4/3)*math.pi*r**3

def v(side1,side2,r):
	return (1-math.cos(side1))*side2/(4*math.pi) *volumesphere(r)
#s1 and s2 in degrees
s1=90
s2=180
radius=5
#--------------
s1=s1*math.pi/180
s2=s2*math.pi/180
#s1 and s2 are now in radians

x=np.arange(0,radius+.01,.01)
x1=[v(s1,s2,i) for i in x]
newv=[volumesphere(r) for r in x]
newv[0]=1
x2=[x1[i]/newv[i] for i in range(len(x))]

plt.plot(x,x2)
plt.xlabel("radius")
plt.ylabel("volume of sphere section (in full volume of sphere w. same radius)")
plt.savefig('normalvolumeB.png', dpi=80)
#plt.show()