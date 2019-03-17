"""https://projecteuler.net/problem=79
https://projecteuler.net/project/resources/p079_keylog.txt"""

def addLog(code,log):
	n1=log[0]
	n2=log[1]
	n3=log[2]
	print("X"+log+"X")
	code+=log
	return()

code=[]
with open("keylog.txt","r+") as lines:
	for line in lines:
		addLog(code,line[:-1])
print(len(code))
