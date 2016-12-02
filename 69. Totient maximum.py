"""Euler's Totient function, φ(n), is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum"""

def reletivPrime(a,b):
	top=1
	if(a>b):
	    for i in range(b-1):
	        if(a%(i+2)==0 and b%(i+2)==0):
	            return False
		return True
	else:
		for i in range(a-1):
		    if(a%(i+2)==0 and b%(i+2)==0):
		        return False
		return True

def phi(n):
    tot=0
    for x in range(n-1):
        if(reletivPrime(x+1,n)):
			tot=tot+1
    return(tot)
    
top=4
n=210
num=2
while(num<1000000):
    num+=2
    p=phi(num)
    if(num/p>top):
        top=num/p
        n=num

print("n",n)
print("top",top)
