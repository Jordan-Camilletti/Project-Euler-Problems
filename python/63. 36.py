"""The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?"""

sum=0
power=1
for num in range(1,10):
	power=1
	while(len(str(pow(num,power)))>=power):
		if(len(str(pow(num,power)))==power):
			sum+=1
		power+=1
print(sum)
		