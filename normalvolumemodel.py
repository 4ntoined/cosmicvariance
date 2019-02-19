import numpy as np
import math
import matplotlib.pyplot as plt

def volumesphere(r):
	return (4/3)*math.pi*r**3

#s1 and s2 in degrees
s1=10
s2=10
radius=5
#--------------
s1=s1*math.pi/180
s2=s2*math.pi/180
#s1 and s2 are now in radians
v=(1-math.cos(s1))*s2/(4*math.pi) *volumesphere(radius)

