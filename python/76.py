"""https://projecteuler.net/problem=76"""

num=10
nums=[0]*num
nums[0]=num
print(nums)
while(0 in nums):
	for n in range(len(nums),-1,-1):
		