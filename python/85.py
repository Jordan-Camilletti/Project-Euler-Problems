def findWaysB(xLen,yLen,maxX,maxY):
	return(

def findWaysA(maxXLen,maxYLen):
	ways=0
	for xLen in range(1,maxXLen+1):
		for yLen in range(1,maxYLen+1):
			ways+=(maxXLen-xLen+1)*(maxYLen-yLen+1)
			#ways+=findWaysB(xLen,yLen,maxXLen,maxYLen)
			print("X: "+str(xLen)+"\nY: "+str(yLen)+"\n")
	return(ways)

tot=0
findWaysA(5,2)
