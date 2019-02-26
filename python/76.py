"""https://projecteuler.net/problem=76
"""

def ways(num1,num2=0,t=0):
	print(str(num1)+" X "+str(num2))
	if(num1<num2):
		return(0)
	if(num2<=0):
		return(ways(num1-1,num2+1))
	if(num1==num2+1):
		return(1+ways(num2)+ways(num1,num2-1))
	return(1+ways(num1-1,num2+1))

print(ways(5))
