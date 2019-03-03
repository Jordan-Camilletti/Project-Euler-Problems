"""https://projecteuler.net/problem=76
"""

def ways(num1,num2=0):
	if(num1<num2):
		return(0)
	if(num1==1 and num2==0):
		return(1)
	if(num2==0):
		return(1+ways(num2-1,1))
	print(str(num1)+" X "+str(num2))
	return(
	#return(ways(num2)+ways(num1-1,num2+1))
	
print(ways(5))
print(ways(5)-1)
