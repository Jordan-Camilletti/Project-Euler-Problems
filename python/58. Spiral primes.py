"""
"""

def isPrime(num):
	for n in range(3,int(num/2),2):
		if(num%n==0):
			return(False)
	return(True)

for test in range(20):
	print(test," ",isPrime(test))

length=7
cornerNums=[1]
for n in range(int((length-1)/2)):
	for corner in range(4):
		cornerNums.append(cornerNums[-1]+((n+1)*2))
print(cornerNums)