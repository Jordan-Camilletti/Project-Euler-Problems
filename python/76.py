"""https://projecteuler.net/problem=76
"""

num=5
ways=0
nums=[0]*num
nums[0]=num
print(nums)
while(0 in nums):
	print(nums)
	ways+=1
	for n in range(len(nums)-1,-1,-1):
		if(num[n]==1 and n!=len(nums)-1):
			nums[n+1]=1
		elif(num[n]!=0):
			nums[n+1]+=1
			nums[n]-=1
			break
			