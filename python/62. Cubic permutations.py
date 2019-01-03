"""The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube."""

def translateNum(num):
	return(''.join(sorted(str(num))))

cubes=[]
used=[]
num=0
n=0
while(5 not in used):#5 not in [i[1] for i in cubes]
	if(translateNum(num**3) in cubes):
		used[cubes.index(translateNum(num**3))]+=1
	else:
		cubes.append(translateNum(num**3))
		used.append(1)
	num+=1
while(translateNum(n**3)!=translateNum((num-1)**3)):
	n+=1
print(n**3)
