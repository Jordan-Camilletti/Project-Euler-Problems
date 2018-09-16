"""It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?"""

#This can only go up to 990 without causing a RecursionError, giving an answer of 152. The last 10 possible answers can just be guessed.
from fractions import Fraction

def squareSum(n):
	if(n==0):
		return(2)
	return(2+Fraction(1/squareSum(n-1)))

num=0
for n in range(990):
	#print(squareSum(n+1)-1)
	x,y=str(Fraction(squareSum(n+1)-1)).split("/")
	if(len(x)>len(y)):
		num+=1
print(num)