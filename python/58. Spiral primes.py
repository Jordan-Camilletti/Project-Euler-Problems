"""
"""

def isPrime(num):
	if(num==1):
		return(False)
	for n in range(3,int(num/2),2):
		if(num%n==0):
			return(False)
	return(True)
	
length=5
while(True):
	length+=2
	cornerNums=[1]
	primeRatio=0
	for n in range(int((length-1)/2)):
		for corner in range(4):
			cornerNums.append(cornerNums[-1]+((n+1)*2))

	for num in cornerNums:
		if(isPrime(num)):
			primeRatio+=1
	if(float(primeRatio/len(cornerNums))<0.1):
		print(length)
		break