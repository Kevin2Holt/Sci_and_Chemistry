import matplotlib.pyplot as plt
import numpy as np
from time import process_time


def getRand(mean, stdDev, numStdDev):
	output = np.random.normal(mean, stdDev)
	while output > mean+(stdDev*numStdDev) or output < mean-(stdDev*numStdDev):
		output = np.random.normal(mean, stdDev)
	# print(output)
	return output





mean_lower = 14778
mean_higher = 14922
stdDev = 69
num_stdDev = 4
step_size = 0.1

num_iterations = pow(10,7)
num_logs = pow(10,1)# The number of logged iterations (i.e. how often it logs)


# Data is offset for efficiency
offset = int(mean_lower - (stdDev*(num_stdDev+2)))

# Define a frequency axis
axis_len = int(mean_higher + (stdDev*(num_stdDev+2))) - offset
vaxis = np.arange(0, axis_len, step_size)+offset

# Resize axis_len to account for step_size
axis_len = int(axis_len/step_size)

# Initialize Arrays
pre_low = np.zeros(axis_len)
pre_high = np.zeros(axis_len)
post_low = np.zeros(axis_len)
post_high = np.zeros(axis_len)

startTime = process_time()
# Display Values
print("offset:",offset)
print("mean_lower:",mean_lower,"\tWith offset:",mean_lower-offset)
print("mean_higher:",mean_higher,"\tWith offset:",mean_higher-offset)
print()
print("Begin Random Generation: ("+str(num_iterations)+" iterations)")
offset = int(offset/step_size)

for i in range(num_iterations):
	num1 = int(getRand(mean_lower, stdDev, num_stdDev)/step_size)
	num2 = int(getRand(mean_lower, stdDev, num_stdDev)/step_size)

	if num1 <= num2:
		low = num1
		high = num2
	else:
		low = num2
		high = num1

	# print("offset:",offset)
	# print("low:",low,"\thigh:",high,"\t\tWith Offset:",low-offset,"\t",high-offset)

	pre_low[low-offset] += 1
	pre_high[high-offset] += 1

	num3 = int(getRand(low*step_size, stdDev, num_stdDev)//step_size)
	num4 = high

	if num3 <= num4:
		low2 = num3
		high2 = num4
	else:
		low2 = num4
		high2 = num3

	# print("low2:",low2,"\thigh2:",high2,"\t\tWith Offset:",low2-offset,"\t",high2-offset)

	post_low[low2-offset] += 1
	post_high[high2-offset] += 1


	# Print Progess
	if i%(num_iterations/num_logs) == 0 and i != 0:
		print(i,"\tElapsed Time (s):",round(process_time()-startTime,3),"\t("+str(round((process_time()-startTime)/(i/1000),3))+" / 1000)")
		# print(i,"\tThis Iteration =>\tPre_Low:",round(low*step_size,len(str(step_size).split(".")[1])),
		# 	"\tPre_High:",round(high*step_size,len(str(step_size).split(".")[1])),
		# 		"\tPost_Low:",round(low2*step_size,len(str(step_size).split(".")[1])),
		# 		"\tPost_High:",round(high2*step_size,len(str(step_size).split(".")[1])))


print("End Random Generation")

# Sum low and high arrays to get pre- and post- burn spectra and hole-burning
pre_sum = np.array(list(map(lambda x,y: x+y, pre_low, pre_high)))
post_sum = np.array(list(map(lambda x,y: x+y, post_low, post_high)))
result = np.array(list(map(lambda x,y: x-y, pre_sum, post_sum)))
# Create a np.array from a python-list
# That list is initialized (using map) with the result of an inline (lambda) function
# lambda <variables>: <function body>, <variable values>

plt.plot(vaxis,pre_low)
plt.plot(vaxis,pre_high)
plt.plot(vaxis,pre_sum)
plt.xlim(int(mean_lower - (stdDev*(num_stdDev))), int(mean_higher + (stdDev*num_stdDev)))
plt.legend(["Pre_Low","Pre_High","Pre_Sum"])
plt.show()


plt.plot(vaxis,post_low)
plt.plot(vaxis,post_high)
plt.plot(vaxis,post_sum)
plt.xlim(int(mean_lower - (stdDev*(num_stdDev))), int(mean_higher + (stdDev*num_stdDev)))
plt.legend(["Post_Low","Post_High","Post_Sum"])
plt.show()


plt.plot(vaxis,pre_sum)
plt.plot(vaxis,post_sum)
plt.plot(vaxis,result)
plt.xlim(int(mean_lower - (stdDev*(num_stdDev))), int(mean_higher + (stdDev*num_stdDev)))
plt.legend(["Pre_Sum","Post_Sum","Result"])
plt.show()