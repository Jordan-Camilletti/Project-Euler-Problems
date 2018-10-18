"""
"""

length=3
spiral=[[]]
for n1 in range(length):
	spiral.append([])
	for n2 in range(length):
		currNum=(length*length)-(2*(length-1))+n1
		spiral[n1].append(currNum-n2)
print(spiral)