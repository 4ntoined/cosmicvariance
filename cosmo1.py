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
ofile=open("cosmovar_measures.txt","w")
ifile=open("cosmovaroutput.txt")
indata=np.loadtxt(ifile, delimiter='  ')
ifile.close()
sigmadm=[]
sigma85=[]
sigma90=[]
sigma95=[]
sigma100=[]
sigma105=[]
sigma110=[]
i=0
while i<10:
	sigmadm.append(indata[i][2])
	sigma85.append(indata[i][3])
	sigma90.append(indata[i][4])
	sigma95.append(indata[i][5])
	sigma100.append(indata[i][6])
	sigma105.append(indata[i][7])
	sigma110.append(indata[i][8])
	i+=1

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

normal=cv2[0]/sigma95[0]
sigmadm=[sigmadm[i]*normal for i in range(len(sigmadm))]
sigma85=[sigma85[i]*normal for i in range(len(sigma85))]
sigma90=[sigma90[i]*normal for i in range(len(sigma90))]
sigma95=[sigma95[i]*normal for i in range(len(sigma95))]
sigma100=[sigma100[i]*normal for i in range(len(sigma100))]
sigma105=[sigma105[i]*normal for i in range(len(sigma105))]
sigma110=[sigma110[i]*normal for i in range(len(sigma110))]

#for item in cv2:
#	ofile.write("%f\r\n" % item)

#ofile.close()

#plt.plot(x,x1)
#plt.plot(x,x2)
#plt.plot(x,x3)
#plt.axis([0,5,0,1.2])
#plt.scatter(z1,cv,c='blue')
plt.scatter(z2,cv2,c='red')
plt.scatter(z2,sigmadm,c='#dc4806')
plt.scatter(z2,sigma85,c='magenta')
plt.scatter(z2,sigma90,c='cyan')
plt.scatter(z2,sigma95,c='yellow')
plt.scatter(z2,sigma100,c='black')
plt.scatter(z2,sigma105,c='green')
plt.scatter(z2,sigma110,c='#6f0c4f')
#plt.scatter(z3,cv3,c='green')
plt.title("Comparing cosmic variance measures. 0<z<2, dz=.2")
plt.xlabel("Redshift Bins, red-Driver paper, orange-dm, magenta-85, cyan-90, yellow-95, black-100, green-105, purple-110")
plt.ylabel("Cosmic Variance")
plt.savefig('cosmocompare1.png',dpi=120)
#plt.show();
