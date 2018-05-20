"""It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""

def sameNums(num):
	s1=sorted(str(num[0]))
	for n in range(1,6):
		if(len(str(num[0]))!=len(str(num[n]))):
			return(False)
		s2=sorted(str(num[n]))
		if(s1!=s2):
			return(False)
	return(True)

num=1
while(not sameNums([num,num*2,num*3,num*4,num*5,num*6])):
	num+=1
	
print(num)
