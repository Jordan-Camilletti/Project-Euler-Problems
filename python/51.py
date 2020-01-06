"""By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family."""

def bSearch(num,primes):
	if(len(primes)<1 or (len(primes)==1 and primes[0]!=num)):
		return(False)
	center=int(len(primes)/2)
	if(num==primes[center]):
		return(True)
	elif(num>primes[center]):
		return(bSearch(num,primes[center:]))
	else:
		return(bSearch(num,primes[:center]))

def isPrime(n,primes):
	if(bSearch(n,primes)):
		return(True)
	if(n % 2 == 0 or n % 3 == 0): 
		return(False)
	i = 5
	while(i * i <= n): 
		if(n % i == 0 or n % (i + 2) == 0): 
			return(False)
		i = i + 6
	return(True)

"""n=234
rep=list(str(n))
rep[1]="4"
n=int("".join(rep))
print(n)"""
def primeSwitch(num):
	primeCount=0
	for n in range(2**len(str(num))):
		print(2)#n in binary)
	#TODO: use this to replace the digits and test for primes
	return(0)

primes=[2,3,5,7]
currNum=9
replacePrimes=0
while(replacePrimes<8):
	currNum+=1
	if(isprime(currNum,primes)):
		primes.append(currNum)
		replacePrimes=primeSwitch(currNum)
		
print(currNum)