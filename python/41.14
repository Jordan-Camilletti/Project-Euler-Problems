"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?"""

def panPrime(n):
	for x in range(len(str(n))):
		if(str(x+1) not in str(n)):
			return False
	for x in range(3,n,2):
		if(n%x==0):
			return False
	return True
for n in range(987654321,2141,-2):
	if(panPrime(n)):
		print(n)
		break
