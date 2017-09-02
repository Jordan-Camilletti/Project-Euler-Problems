"""It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
Created by Jordan Camilletti"""

def isPrime(num):
	for x in range(2,num):
		if(num%x==0): return False
	return True

def conjecture(x,primes):
	for prime in primes:
		sqr=1
		while(prime+(2*(sqr*sqr))<=x):
			if(prime+(2*(sqr*sqr))==x): return True
			sqr+=1
	return False

primes=[3]
curr=9
lastPrime=3
while(True):
	curr+=2
	if(lastPrime<curr):
		for p in range(lastPrime,curr+1):
			if(isPrime(p)):
				primes.append(p)
				lastPrime=p
	if(not isPrime(curr) and not conjecture(curr,primes)):
		print(curr)
