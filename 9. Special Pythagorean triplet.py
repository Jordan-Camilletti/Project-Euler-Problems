"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

def pythag(a,b,c):
  if((a*a)+(b*b)==c*c):
    return True
  return False

a=3;b=4;c=5
if(pythag(a,b,c)):
  print(a+b+c)
