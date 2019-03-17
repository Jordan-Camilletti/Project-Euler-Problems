def findWaysA(maxXLen,maxYLen):
	ways=0
	for xLen in range(1,maxXLen+1):
		for yLen in range(1,maxYLen+1):
			ways+=(maxXLen-xLen+1)*(maxYLen-yLen+1)#TODO: Test these
			#print("X: "+str(xLen)+"\nY: "+str(yLen)+"\n")
	return(ways)

areaX=1
areaY=1
print(findWaysA(3,2))