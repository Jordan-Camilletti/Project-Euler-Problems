def findWays(maxXLen,maxYLen):
	ways=0
	for xLen in range(1,maxXLen+1):
		for yLen in range(1,maxYLen+1):
			ways+=(maxXLen-xLen+1)*(maxYLen-yLen+1)
			#print("X: "+str(xLen)+"\nY: "+str(yLen)+"\n")
	return(ways)

areaX=1
areaY=1
print(findWays(3,2))
#TODO: add main loops for areaX and areaY
while(findWays(areaX,areaY)):
	areaY=1
	while(areaY<areaX):
		areaY++
	areaX++
