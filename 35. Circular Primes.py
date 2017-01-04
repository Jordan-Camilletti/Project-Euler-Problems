"""
"""

def rotate(num):
	x=0
	strg=str(num)
	newStr=""
	while(newStr!=strg):
		x+=1
		newStr=strg[x:] + strg[:x]
		print (int(strg[x:] + strg[:x]))
	
rotate(197)
