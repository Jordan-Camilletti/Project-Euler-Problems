"""
"""

length=7
cornerNums=[1]
for n in range(int((length-1)/2)):
	for corner in range(4):
		cornerNums.append(cornerNums[-1]+((n+1)*2))
print(cornerNums)