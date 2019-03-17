def findWays(maxXLen,maxYLen):
	ways=0
	for xLen in range(1,maxXLen+1):
		for yLen in range(1,maxYLen+1):
			print("X: "+str(xLen)+"\nY: "+str(yLen))

tot=0
findWays(5,0)
