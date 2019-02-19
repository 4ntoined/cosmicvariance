import matplotlib.pyplot as plt;
import numpy as np;
import math;
from scipy.integrate import quad;

def xE(z):
	return (omegaM*(1+z)**3+omegaK*(1+z)**2+omegaL)**.5;

def inverseE(z):
	return 1/xE(z);

def dV(z):
	entries = np.rint(z*100+1).astype(int)
	k = entries-1
	E=(omegaM*(1+z)**3+omegaK*(1+z)**2+omegaL)**.5;
	answerAndError=[quad(inverseE,0,c) for c in np.arange(0,z+.01,.01)]
	dC=[answerAndError[i][0] for i in range(0,entries)]
	dC[0]=0
	if omegaK>0:
		dM=math.sinh((omegaK**.5)*dC[k])/(omegaK**.5);
	if omegaK<0:
		dM=math.sin((abs(omegaK)**.5)*dC[k])/(abs(omegaK)**.5);
	if omegaK==0:
		dM=dC[k];
	dA=dM/(1+z);
	dVc=(((1+z)**2)*(dA**2))/E
	return dVc

run=0
x=np.arange(0,5.02,.01)
while run<3:
#(1,0,0) (.05,.95,0) (.2,0,.8)
	if run==0:
		omegaM,omegaK,omegaL=1,0,0
	if run==1:
		omegaM,omegaK,omegaL=.05,.95,0
	if run==2:
		omegaM,omegaK,omegaL=.2,0,.8

	if run==0:
		x1=[dV(a) for a in x]
	if run==1:
		x2=[dV(a) for a in x]
	if run==2:
		x3=[dV(a) for a in x]
	run+=1

plt.plot(x,x1)
plt.plot(x,x2)
plt.plot(x,x3)
plt.axis([0,5,0,1.2])
plt.savefig('comovingvolume.png',dpi=80)
plt.show();
