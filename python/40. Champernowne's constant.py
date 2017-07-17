"""An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""

wrd="."
for n in range(1,1000001):
	wrd=wrd+str(n)
#print(wrd)
tot=1
for n in range(len(wrd)):
	if(n==1 or n==10 or n==100 or n==1000 or n==10000 or n==100000 or n==1000000):
		tot*=int(wrd[n])
print(tot)
