"""
"""

def prime(num):
	for x in range(2,(num/2)+1):
		if(num%x==0):
			return False
	return True

a=-79
b=1601
n=0
while(prime((n*n)+(a*n)+b)):
	n+=1
print(n)
