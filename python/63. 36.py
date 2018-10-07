"""The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?"""

def isPow(num):
	pwr=1
	while(pow(pwr,len(str(num)))<num):
		pwr+=1
	if(pow(pwr,len(str(num)))!=num):
		return(0)
	return(pwr)

sum=0
digit=0
while(isPow(digit)!=1):
	if(isPow(digit)>1):
		sum+=1
	digit+=1
print(sum)