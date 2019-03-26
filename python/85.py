"""
https://projecteuler.net/problem=85
"""

def findWays(maxXLen,maxYLen):
	ways=0
	for xLen in range(1,maxXLen+1):
		for yLen in range(1,maxYLen+1):
			#print("X: "+str(xLen)+"\nY: "+str(yLen)+"\n")
			ways+=(maxXLen-xLen+1)*(maxYLen-yLen+1)
	return(ways)

areaX=1
areaY=1
while(findWays(areaX,areaY)<2000000):
	print(str(areaX)+" "+str(findWays(areaX,areaY)))
	areaY+=1
	if(areaY>areaX):
		areaX+=1
		areaY=1
		
print("\nX: "+str(areaX)+"\nY: "+str(areaY)+"\nArea: "+str(areaX*areaY)+"\n"+str(findWays(areaX,areaY))) 
areaY-=1
print("\nX: "+str(areaX)+"\nY: "+str(areaY)+"\nArea: "+str(areaX*areaY)+"\n"+str(findWays(areaX,areaY))) 
