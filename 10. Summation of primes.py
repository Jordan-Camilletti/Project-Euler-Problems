"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million."""

def isPrime(num):
	for x in range(num-2):
		if(num%(x+2)==0):
			return False
	return True
		
tot=0
for x in range(8):
	if(isPrime(x+2)):
		print(x+2)
		tot=tot+(x+2)
print(tot)
