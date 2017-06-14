"""The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""

def palindrome(num):
	wrd=str(num)
	if(len(wrd)%2==0):
		for x in range(int(len(wrd)/2)):
			if(wrd[x]!=wrd[-(x+1)]):
				return False
	else:
		for x in range(int(len(wrd)/2)+1):
			if(wrd[x]!=wrd[-(x+1)]):
				return False
	return True

sum=0
for x in range(1,1000000):
	if(palindrome(x) and palindrome("{0:b}".format(x))):
		sum+=x
print(sum)
