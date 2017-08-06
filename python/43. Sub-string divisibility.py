"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property."""

from itertools import permutations
def pan(num):
	if(len(str(num))!=10): return False
	for x in range(10):
		if(str(x) not in str(num)):
			return False
	return True
def subDiv(num):
	divs=[2,3,5,7,11,13,17]
	for x in range(2,9):
		if(int(str(num)[x-1:x+2])%divs[x-2]!=0): return False
	return True
tot=0
for n in permutations(range(10)):
	num=""
	for x in n:
		num+=str(x)
	if(pan(int(num))):
		if(subDiv(int(num))): tot+=int(num)
print(tot)
