"""
https://projecteuler.net/problem=85
By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
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
while(findWays(areaX,areaY)<=2000000):
	print(str(areaX)+" "+str(findWays(areaX,areaY)))
	areaY+=1
	if(areaY>areaX):
		areaX+=1
		areaY=1
		
print("\nX: "+str(areaX)+"\nY: "+str(areaY)+"\nArea: "+str(areaX*areaY)+"\n"+str(2000000-findWays(areaX,areaY))) 
areaY-=1
print("\nX: "+str(areaX)+"\nY: "+str(areaY)+"\nArea: "+str(areaX*areaY)+"\n"+str(2000000-findWays(areaX,areaY))) 
