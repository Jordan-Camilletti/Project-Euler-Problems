"""https://projecteuler.net/problem=76
"""

def twoToOne(nums):#Transforming 2,1 to 1,1,1
	rtnNum=nums
	for num in range(len(rtnNums)-1):
		if(rtnNum[num]==2 and rtnNum[num+1]==1):
			for n in range(len(nums)-1,num+2,-1):
				rtnNum[n]=rtnNum[n-1]
			for n in range(num,num+3):
				rtnNum[num]=1

n=5
ways=0
nums=[0]*n
nums[0]=n
move=False
while(0 in nums):
	ways+=1
	move=False
	for num in range(len(nums)):
		#print(str(num)+" X "+str(nums[num]))
		if(nums[num]==1 and n!=len(nums)-1):
			nums[num+1]=1
		elif(nums[num]!=0):
			nums[num+1]+=1
			nums[num]-=1
			break
	print(nums)
print(ways)