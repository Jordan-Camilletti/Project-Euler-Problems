"""https://projecteuler.net/problem=79
https://projecteuler.net/project/resources/p079_keylog.txt"""

def addLog(code,log):
	return()

code=[]
with open("keylog.txt","r+") as lines:
    for line in lines.readline():
		print(line)
		code=addLog(code,line)
print(len(code))