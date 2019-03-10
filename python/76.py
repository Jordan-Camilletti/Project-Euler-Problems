"""https://projecteuler.net/problem=76"""

num=6
currNum=num
ways=1
inc=0
while(currNum>=num/2):
	ways+=inc
	inc+=1
	currNum-=1
inc-=1
while(currNum>1):
	ways+=inc
	currNum-=1
print(ways)