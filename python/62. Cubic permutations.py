"""The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube."""

def translateNum(num):#Added this function just so that the main code wouldn't look so messy
	return(''.join(sorted(str(num))))

cubes=[]#I know I could have combined 'cubes' and 'used' into a 2D array
used=[]#but 2 arrays is easier to work with when searching in each of them
num=0
n=0
while(5 not in used):#Number of permutation cubes wanted
	if(translateNum(num**3) in cubes):
		used[cubes.index(translateNum(num**3))]+=1
	else:
		cubes.append(translateNum(num**3))
		used.append(1)
	num+=1#Finding the largest of the permutation cubes w/ sorted numbers
while(translateNum(n**3)!=translateNum((num-1)**3)):#Once the largest of the cubes is found, this loop will find the smallest
	n+=1
print(n**3)
