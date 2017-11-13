"""We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum."""

def pan(num):
	for n in range(1,10):
		if(str(n) not in str(num)):
			return(False)
	return(True)
total=0
prevNums=[]
for n1 in range(1,9877):
	n2=1
	while(len(str(n1)+str(n2)+str(n1*n2))<=9):
		if(pan(str(n1)+str(n2)+str(n1*n2)) and str(n1*n2) not in prevNums):
			prevNums.append(str(n1*n2))
			total+=(n1*n2)
		n2+=1
print(total)
