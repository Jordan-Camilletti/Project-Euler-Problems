"""https://projecteuler.net/problem=76
"""

n=5
ways=0
nums=[0]*n
nums[0]=n
while(0 in nums):
	print(nums)
	ways+=1
	for num in range(len(nums)-1,-1,-1):
		#print(str(num)+" X "+str(nums[num]))
		if(nums[num]==1 and n!=len(nums)-1):
			nums[num+1]=1
		elif(nums[num]!=0):
			nums[num+1]+=1
			nums[num]-=1
			break
print(ways)