"""The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""

def prime(i):
	for x in range(2,i):
		if(i%x==0):
			return False
	return True

def circ(num):
	wrd=str(num)
	for x in range(len(wrd)):
		currWrd=""
		currWrd=wrd[x:]+wrd[:x]
		#print(currWrd)
		if not(prime(int(currWrd))):
			return False
	return True

tot=0
for n in range(2,1000000):
	if(circ(n)):
		#print(n)
		tot+=1
print(tot)
