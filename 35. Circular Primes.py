"""
"""

def isPrime(num):
	for x in range(num-2):
		if(num%(x+2)==0):
			return False
	return True

def rotate(num):
	x=0
	strg=str(num)
	newStr=""
	while(newStr!=strg):
		x+=1
		newStr=strg[x:] + strg[:x]
		if isPrime(int(strg[x:] + strg[:x]))==False:
			return False
	return True
	
total=0
for x in range(99):
	if(rotate(x+2)): total+=1
print(total)
