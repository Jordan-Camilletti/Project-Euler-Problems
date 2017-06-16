"""The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

def isPrime(num):
	if(num==1 or num==0):
		return False
	for x in range(num-2):
		if(num%(x+2)==0):
			return False
	return True

def trun(num):
	word=str(num)
	if("0" in word or "4" in word or "6" in word or "8" in word):
		return False
	for x in range(len(word)):
		if(isPrime(int(word[x:]))==False or isPrime(int(word[:x+1]))==False):
			return False
	return True
count=0
num=9
tot=0
while(count<11):
	num+=2
	if(trun(num)):
		count+=1
		tot+=num
print(tot)
