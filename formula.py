import numpy as np
import matplotlib.pyplot as plt
import math



def sspec(v,S):
	wZPL = 5.0
	vPSB = 50.0
	a = 3
	b = 1.0/vPSB
	ZPL = (1.0)/((math.pi*wZPL)*(1 + (v/wZPL)**2))
	PSB = (b**a)*(v**(a-1))*np.exp(-b*v)/math.gamma(a)*(v>0)
   
	return math.exp(-S)*ZPL + (1.0 - math.exp(-S))*PSB

vstep = 10.0
vaxis = np.arange(15000.0, 16500.0, vstep)


vo = 15500
sig = 150

pdf = np.exp(-(vaxis-vo)**2/(2.0*sig**2))
pdf /= np.sum(pdf)*vstep

# print(pdf)
# plt.plot(vaxis, pdf)
# plt.show()




vstop = 16000
nstop = np.argmin(np.abs(vstop-vaxis))

S = 1
SpTot = 0*vaxis
totline = 0*vaxis

for n in range(0,len(vaxis[0:nstop])):
	vZPL = vaxis[n]
	Spn = sspec(vaxis - vZPL,S)
	SpTot += Spn*pdf[n]*vstep

# totline[n] = SpTot

plt.plot(vaxis, pdf, color=[0.7,0.7,0.7])
plt.plot(vaxis, SpTot)
plt.show()