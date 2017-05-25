"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included."""

def fac(num):
	tot=0
	for n in range(len(str(num))):
		i=1
		for x in range(int(str(num)[n])):
			i=i*(x+1)
		tot=tot+i
	return(tot)
	
total=0
for x in range(3,1499999):
	if(x==fac(x)):
		total=total+x
print(total)
