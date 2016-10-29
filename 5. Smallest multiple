"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

def div20(num):
	for x in range(10):
		if(num%(x+11)!=0):
			return False
	return True

num=20
while(True):
	if(div20(num)):
		break
	num+=20
print(num)
