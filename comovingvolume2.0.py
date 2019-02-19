import matplotlib.pyplot as plt;
import numpy as np;
import math;
from scipy.integrate import quad;

def xE(z):
	return (omegaM*(1+z)**3+omegaK*(1+z)**2+omegaL)**.5;
def 

run=0
while run<3:
#(1,0,0) (.05,.95,0) (.2,0,.8)
	if run==0:
		omegaM,omegaK,omegaL=1,0,0

	if run==1:
		omegaM,omegaK,omegaL=.05,.95,0


	run+=1