"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

""If you have a compiler with no time limit, you can chance 'while(True)' to 'while(x<=600851475143)'. However if you don't then
you have to change and increase x each time to what the code puts out until you exceed time limit, then x is probably the right answer"""

def isPrime(num):
	for x in range(num-2):
		if(num%(x+2)==0):
			return False
	return True
	
x=1
top=1
while(True):
	x+=1
	if(600851475143%x==0 and isPrime(x)):
		if(x>=top):
			top=x
			break
print(top)
