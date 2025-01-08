import matplotlib.pyplot as plt
import numpy as np
import math
from time import process_time


vstart = 10000
vstop  = 20000
vstep  = 0.1

vaxis = np.arange(vstart, vstop, vstep)
Npts = len(vaxis)

mean_lower = 14778
mean_higher = 14922
stdDev = 69
num_stdDev = 4

num_iterations = pow(10, 5)
num_logs = pow(10, 2)# The number of logged iterations (i.e. how often it logs)

# Initialize Arrays
pre_low = np.zeros(Npts)
pre_high = np.zeros(Npts)
post_low = np.zeros(Npts)
post_high = np.zeros(Npts)

startTime = process_time()
print("Begin Random Generation: ("+str(num_iterations)+" iterations)\tStart Time:",startTime)
for i in range(num_iterations):
	num1 = np.random.normal(mean_lower, stdDev)
	num2 = np.random.normal(mean_higher, stdDev)

	if num1 <= num2:
		low = num1
		high = num2
	else:
		low = num2
		high = num1

	# print("low:",low)
	# print("vaxis:",vaxis)
	# print("vaxis-low:",vaxis-low)
	ndx1 = np.argmin(np.abs(vaxis-low))
	ndx2 = np.argmin(np.abs(vaxis-high))

	pre_low[ndx1] += 1
	pre_high[ndx2] += 1


	num3 = np.random.normal(low, stdDev)

	if num3 <= high:
		low2 = num3
		high2 = high
	else:
		low2 = high
		high2 = num3

	ndx3 = np.argmin(np.abs(vaxis-low2))
	ndx4 = np.argmin(np.abs(vaxis-high2))
	
	post_low[ndx3] += 1
	post_high[ndx4] += 1

	if i%(num_iterations/num_logs) == 0 and i != 0:
		print(i,"\tElapsed Time (s):",round(process_time()-startTime,3),"\t("+str(round((process_time()-startTime)/(i/1000),3))+" / 1000)")
		# print(i,"\tThis Iteration =>\tPre_Low:",round(low,len(str(vstep).split(".")[1])),
		# 	"\tPre_High:",round(high,len(str(vstep).split(".")[1])),
		# 		"\tPost_Low:",round(low2,len(str(vstep).split(".")[1])),
		# 		"\tPost_High:",round(high2,len(str(vstep).split(".")[1])))

plt.plot(vaxis, pre_low)
plt.plot(vaxis, pre_high)
plt.plot(vaxis, post_low)
plt.plot(vaxis, post_high)
plt.legend(["pre_low", "pre_high", "post_low", "post_high"])
plt.xlim(int(mean_lower - (stdDev*(num_stdDev))), int(mean_higher + (stdDev*num_stdDev)))
plt.show()