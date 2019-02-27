"""https://projecteuler.net/problem=76
"""

def ways(num1,num2=0):
	print(str(num1)+" X "+str(num2))
	if(num1<=1 or num2>num1):
		return(0)
	return(1+ways(num1-1,num2+1))

print(ways(5))
