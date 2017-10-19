"""The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""

from itertools import permutations

def isPrime(num):
	if(num%2==0): return False
	for x in range(3,num,2):
		if(num%x==0): return False
	return True

for number in range(1001,9998,2):
	for increase in range(2,(10000-number)/2,2):
		perms=list(permutations(str(number)))
		if(isPrime(number) and isPrime(number+increase) and isPrime(number+increase+increase)):
			if((tuple(str(number+increase)) in perms) and (tuple(str(number+increase+increase)) in perms)):
				print(str(number)+str(number+increase)+str(number+increase+increase))
