"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""

def haveSim(n, d):
	for w in str(n):
		if(w in str(d) and int(w)!=0):
			return True
	return False

def cancel(n,d):
	newN=""
	newD=""
	for w in str(n):
		if(w in str(d)):
			newN=str(n).replace(w,"")
			newD=str(d).replace(w,"")
	try:
		return(float(int(newN)/int(newD))==float(n/d))
	except ValueError:
		return(False)
	except ZeroDivisionError:
		return(False)

totX=1
totY=1
for y in range(10,100):
	for x in range(10,y):
		if(haveSim(x,y) and cancel(x,y)):
			totX=totX*x
			totY=totY*y
print(totX,totY)
#If you can't figure out totX/totY on your own then you have bigger problems than this one
