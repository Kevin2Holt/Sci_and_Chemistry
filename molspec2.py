import matplotlib.pyplot as plt
import numpy as np

low_mean = 14778
high_mean = 14922
low_stdDev = 100
high_stdDev = 90
num_stdDev = 4

num_itterations = 1000000


diff = high_mean - low_mean

low_offset	= low_mean-(low_stdDev*num_stdDev)
high_offset = high_mean-(high_stdDev*num_stdDev)

Pre_Low		= np.zeros((low_stdDev*(num_stdDev*2))+1+diff, dtype=int)
Pre_High	= np.zeros((high_stdDev*(num_stdDev*2))+1+diff, dtype=int)


for i in range(num_itterations):
	low = np.random.normal(low_mean, low_stdDev)
	while low > low_mean+(low_stdDev*num_stdDev) or low < low_mean-(low_stdDev*num_stdDev):
		low = np.random.normal(low_mean, low_stdDev)
	high = np.random.normal(high_mean, high_stdDev)
	while high > high_mean+(high_stdDev*num_stdDev) or high < high_mean-(high_stdDev*num_stdDev):
		high = np.random.normal(high_mean, high_stdDev)

	Pre_Low[int(low)-low_offset] += 1
	Pre_High[int(high)-high_offset+diff] += 1

	if i%100000 == 0:
		print(i)


plt.plot(Pre_Low)
# plt.show()
plt.plot(Pre_High)
# plt.show()


post = np.array(list(map(lambda x, y: x + y, Pre_Low, Pre_High)))


plt.plot(post)
plt.xlim(0, (high_stdDev*num_stdDev*2)+diff)
plt.show()