import numpy as np
import math
import matplotlib.pyplot as plt

def volumesphere(r):
	return (4/3)*math.pi*r**3

def v(side1,side2,r):
	return (1-math.cos(side1))*side2/(4*math.pi) *volumesphere(r)

def dv(side1,side2,r):
	return (1-math.cos(side1))*side2*r**2

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
y1=[dv(s1,s2,i) for i in x]

plt.plot(x,y1)
plt.title("volume element v. redshift")
plt.xlabel("radius")
#plt.ylabel("volume of sphere section")
plt.ylabel("dV (volume element)")
plt.savefig('normalvolumeelement.png', dpi=80)
#plt.show()