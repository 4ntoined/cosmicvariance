import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import quad

def volumesphere(r):
	return (4/3)*math.pi*r**3

def v(side1,side2,r):
	return (1-math.cos(side1))*side2/(4*math.pi) *volumesphere(r)

def dv(r):
	return (1-math.cos(10*math.pi/180))*10*math.pi/180*r**2

def cat(r):
	return quad(dv,0,r)[0]

#s1 and s2 in degrees
s1=10
s2=10
radius=5
#--------------
s1=s1*math.pi/180
s2=s2*math.pi/180
#s1 and s2 are now in radians

x=np.arange(0,radius+.01,.01)
x1=[v(s1,s2,i) for i in x]
#y1=[dv(i,s1,s2) for i in x]
z1=[cat(i) for i in x]

plt.plot(x,z1)
plt.title("volume v. redshift")
plt.xlabel("radius")
#plt.ylabel("volume of sphere section")
plt.ylabel("volume")
plt.savefig('normalvolumeCHECK.png', dpi=80)
#plt.show()