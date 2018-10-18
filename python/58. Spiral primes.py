"""
"""

length=7
cornerNums=[1]
currNum=1
for n in range(int((length-1)/2)):
	for corner in range(4):
		currNum+=((n+1)*2)
		cornerNums.append(currNum)
print(cornerNums)