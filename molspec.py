import matplotlib.pyplot as plt
import numpy as np


def getRand(mean, stdDev, numStdDev):
	output = np.random.normal(mean, stdDev)
	while output > mean+(stdDev*numStdDev) or output < mean-(stdDev*numStdDev):
		output = np.random.normal(mean, stdDev)
	return output

# Test values
# mean_lower = 14800
# mean_higher = 15000

mean_lower = 14778
mean_higher = 14922
stdDev = 90
num_stdDev = 4

num_iterations = pow(10, 7)

# data is offset for efficiency
offset = int((mean_lower + mean_higher) / 2) - (stdDev * num_stdDev)

# Initialize arrays
Pre_Low		= np.zeros((stdDev*((num_stdDev+1)*2))+1, dtype=int)
Pre_High	= np.zeros((stdDev*((num_stdDev+1)*2))+1, dtype=int)
Post_Low	= np.zeros((stdDev*((num_stdDev+1)*2))+1, dtype=int)
Post_High	= np.zeros((stdDev*((num_stdDev+1)*2))+1, dtype=int)

# Display values
print("offset: ", offset)
print("mean_lower: ", mean_lower,"\t Wtih offset:", mean_lower-offset)
print("mean_higher: ", mean_higher,"\t Wtih offset:", mean_higher-offset)
print()
print("Begin Random Generation: ("+str(num_iterations)+")")

for i in range(num_iterations):
	# Gaussian random int centered on mean_lower
	num1 = np.random.normal(mean_lower, stdDev)
	# Ensure num1 is within <num_stdDev> standard deviations
	while num1 > mean_lower+(stdDev*num_stdDev) or num1 < mean_lower-(stdDev*num_stdDev):
		num1 = np.random.normal(mean_lower, stdDev)

	# Gaussian random int centered on mean_higher
	num2 = np.random.normal(mean_higher, stdDev)
	# Ensure num2 is within <num_stdDev> standard deviations
	while num2 > mean_higher+(stdDev*num_stdDev) or num2 < mean_higher-(stdDev*num_stdDev):
		num2 = np.random.normal(mean_higher, stdDev)
	
	# Sort low & high
	if num1 <= num2:
		low = num1
		high = num2
	else:
		low = num2
		high = num1

	# Increment Pre (offset for efficiency)
	Pre_Low[int(low)-offset] += 1
	Pre_High[int(high)-offset] += 1


	# Gaussian random int centered on pre-low
	num3 = np.random.normal(low, stdDev)
	# Ensure num3 is within <num_stdDev> standard deviations
	while num3 > low+(stdDev*num_stdDev) or num3 < low-(stdDev*num_stdDev):
		num3 = np.random.normal(low, stdDev)

	# Sort Post low & high
	if num3 <= high:
		low2 = num3
		high2 = high
	else:
		low2 = high
		high2 = num3

	# Increment Post (offset for efficiency)
	Post_Low[int(low2)-offset] += 1
	Post_High[int(high2)-offset] += 1

	# Print progress
	if i%pow(10, 6) == 0 and i != 0:
		print(i,"\t\tThis iteration =>\tPre-Low:", int(low)-offset, "\tPre-High:", int(high)-offset,"\tPost-Low:", int(low2)-offset, "\tPost-High:", int(high2)-offset)
		# print(i)

print("End Random Generation")
# print("Pre_Low:", Pre_Low)
# print("Pre_High:", Pre_High)

# Sum low & high
Pre_Sum = np.array(list(map(lambda x, y: x + y, Pre_Low, Pre_High)))
Post_Sum = np.array(list(map(lambda x, y: x + y, Post_Low, Post_High)))
result = np.array(list(map(lambda x, y: x - y, Pre_Sum, Post_Sum)))

# Plot & Show
plt.plot(Pre_Low)
# plt.show()
plt.plot(Pre_High)
# plt.show()
plt.plot(Pre_Sum)
plt.xlim(0, (stdDev*(num_stdDev+1)*2))
plt.legend(['Pre_Low', 'Pre_High', 'Pre_Sum'])
plt.show()


# Plot & Show
plt.plot(Post_Low)
# plt.show()
plt.plot(Post_High)
# plt.show()
plt.plot(Post_Sum)
plt.xlim(0, (stdDev*(num_stdDev+1)*2))
plt.legend(['Post_Low', 'Post_High', 'Post_Sum'])
plt.show()


# Plot & Show
plt.plot(Pre_Sum)
# plt.show()
plt.plot(Post_Sum)
# plt.show()
plt.plot(result)
plt.xlim(0, (stdDev*(num_stdDev)*2))
plt.legend(['Pre_Sum', 'Post_Sum', 'Result'])
plt.show()






