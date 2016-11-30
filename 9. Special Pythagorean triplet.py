"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

def pythag(a,b,c):
  if((a*a)+(b*b)==c*c):
    return True
  return False
  
c=4
b=3
a=2
while(c<=335):
	c+=1
	while(b<c):
		b+=1
		while(a<b):
			a+=1
			if(a,b,c):
				print(a*b*c)
