"""https://projecteuler.net/problem=76"""

def mainFindWays(mainNum,num=mainNum-1):
	if(num<1 or num>=mainNum):
		return(0)
	return(subFindWays(num)+mainFindWays(mainNum,num-1))
	
def subFindWays():
	return(0)
	
print(mainFindWays(5))