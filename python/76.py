"""
"""

def ways(num1,num2=0):
	if(num1<=1 and num2<=1):
		return(1)
	if(num1<=num2):
		return(1+ways(num2))
	return(1+ways(num1-1,num2+1))

print(ways(5))
print(ways(100))
