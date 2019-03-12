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
	dVc=dVc*(3000/.7)**2  #factor of 1 hubble distance
	return dVc

def V(a,b):  #integrates the volume element from redshift a to redshift b 
	return quad(dV,a,b)[0]

omegaM,omegaK,omegaL=.2,0,.8
'''
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
'''

z1=np.arange(0,2,.1)
z11=np.arange(0,2.1,.1)
z2=np.arange(0,2,.2)
z22=np.arange(0,2.2,.2)
z3=np.arange(0,2,.3)
z33=np.arange(0,2.3,.3)
volumeslices=[V(z11[i],z11[i+1]) for i in range(len(z11)-1)]
volumeslices2=[V(z22[i],z22[i+1]) for i in range(len(z22)-1)]
volumeslices3=[V(z33[i],z33[i+1]) for i in range(len(z33)-1)]
cv=[219.7 - 52.4 * math.log(volumeslices[i],10) + 3.21*math.log(volumeslices[i],10)**2 for i in range(len(volumeslices))]
cv2=[219.7 - 52.4 * math.log(volumeslices2[i],10) + 3.21*math.log(volumeslices2[i],10)**2 for i in range(len(volumeslices2))]
cv3=[219.7 - 52.4 * math.log(volumeslices3[i],10) + 3.21*math.log(volumeslices3[i],10)**2 for i in range(len(volumeslices3))]
#plt.plot(x,x1)
#plt.plot(x,x2)
#plt.plot(x,x3)
#plt.axis([0,5,0,1.2])
plt.scatter(z1,cv,c='blue')
plt.scatter(z2,cv2,c='red')
plt.scatter(z3,cv3,c='green')
plt.title("Cosmic Variance of Various Redshift Bins")
plt.xlabel("Redshift Bins BLUE=.1 RED=.2 GREEN=.3")
plt.ylabel("Cosmic Variance in %")
plt.savefig('cosmo6.png',dpi=80)
#plt.show();
