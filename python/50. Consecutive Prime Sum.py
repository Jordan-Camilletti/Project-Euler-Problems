"""The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?"""

import math

def isPrime(num):
	if(num<2): return False
	for x in range(2,int(math.sqrt(num))+1):
		if(num%x==0): return False
	return True

def sectionTotal(length,spot,primes):
	tot=0
	for n in range(length):
		tot+=primes[n+spot]
	return tot

primes=[2]
topLen=0
topNum=0
consecLen=1
spot=0
for n in range(3,1000004,2):#1,000,003=prime
	if(isPrime(n)):
		primes.append(n)
while(sectionTotal(consecLen,spot,primes)<1000000 or spot!=0):
	if(sectionTotal(consecLen,spot,primes)>=1000000):
		consecLen+=1
		spot=-1
	if(consecLen>topLen and isPrime(sectionTotal(consecLen,spot,primes)) and sectionTotal(consecLen,spot,primes)<1000000):
		topLen=consecLen
		topNum=sectionTotal(consecLen,spot,primes)
	spot+=1
print("Biggest Prime:",topNum," Primes in it:",topLen)
