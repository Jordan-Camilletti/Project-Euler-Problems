"""
"""

def prime(num):
	for x in range(2,int(num**0.5)+1):
		if(num%x==0):
			return False
	return True

top=0
topA=0
topB=0
for a in range(-999,1000):
	for b in range(-1000,1001):
		n=0
		while(prime(abs((n*n)+(a*n)+b))):
			n+=1
		if(n>top):
			top=n
			topA=a
			topB=b

print(topA*topB,"top a:",topA, "top b:",topB,top)
