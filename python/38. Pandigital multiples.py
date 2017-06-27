"""Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""

def pand(n):
	wrd=str(n)
	if(len(wrd)!=9): return False
	for x in range(1,10):
		if(str(x) not in wrd): return False
	return True
pands=[]
for n in range(123456789,987654322):
	if(pand(n)):
		pands.append(n)
def thing(num,n,pands):
	wrd=""
	for i in range(n):
		wrd=wrd+str(num*(i+1))
	return(int(wrd) in pands)

topP=0
for num in range(1,9876+1):
	for n in range(2,10):
		if(thing(num,n,pands)):
			wrd=""
			for i in range(n):
				wrd=wrd+str(num*(i+1))
			if(int(wrd)>topP):
				topP=int(wrd)
print(topP)
