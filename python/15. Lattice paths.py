"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

there's supposed to be a image here of those six ways

How many such routes are there through a 20×20 grid?"""

lastRow=[1,1]
currRow=[]
sqrLength=20
sqrCurr=2
for t in range(3,(sqrLength*2)+2):
	for n in range(len(lastRow)+1):
		if(n==0 or n==len(lastRow)):
			currRow.append(1)
		else:
			currRow.append(lastRow[n]+lastRow[n-1])	if(t%2!=0):
		print(sqrCurr-1,currRow[int(len(currRow)/2)])
		sqrCurr+=1
	lastRow=currRow
	currRow=[]
