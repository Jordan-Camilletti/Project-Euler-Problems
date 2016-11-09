"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""

def palindrome(num):
	wrd=str(num)
	if(len(wrd)%2==0):
		for x in range(len(wrd)):
			if(wrd[x]!=wrd[len(wrd)-(x+1)]):
				return False
		return True

top=0
for a in range(1000):
	for b in range(1000):
		if(palindrome(a*b) and a*b>=top):
			top=a*b
print(top)
