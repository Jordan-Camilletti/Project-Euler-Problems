"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

def pythag(a,b,c):
  if((a*a)+(b*b)==c*c):
    return True
  return False
  
a=4
b=3
c=2
while(a<=335):
	a+=1
	while(b<a):
		b+=1
		while(c<b):
			c+=1
			print("c:",c)
			print("b:",b)
			print("a:",a)
