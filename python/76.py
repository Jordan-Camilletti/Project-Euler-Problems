"""https://projecteuler.net/problem=76"""

def mainFindWays(mainNum,num):
	if(num<=1):
		return(1)
	return(subFindWays(mainNum,num)+mainFindWays(mainNum,num-1))
	
def subFindWays(mainNum,numA):
	numB=mainNum-numA
	if(numB<=2):#If numB is 1 or 2, return that number
		return(numB)
	print(str(numA)+" : "+str(numB))
	return(0)
	
print(mainFindWays(5,4))