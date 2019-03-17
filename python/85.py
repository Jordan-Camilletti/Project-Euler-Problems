def findWaysB(xLen,yLen)

def findWaysA(maxXLen,maxYLen):
	ways=0
	for xLen in range(1,maxXLen+1):
		for yLen in range(1,maxYLen+1):
			print("X: "+str(xLen)+"\nY: "+str(yLen)+"\n")

tot=0
findWaysA(5,2)
