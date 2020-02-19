"""A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length."""

def contains(main, value, size):
"""	-1: not found
	0 : value matches front of main
	1 : value matches back of main"""
	return(-1)
	
def combine(values):
"""This takes a list of values amd iterates through it once
It adds or combines these values into a 2nd array, which it then returns"""
	combinedValues=[values[0]]
	del(values[0])
	for val in values:
		

values=[]#individual 3-len codes
file=open("keylog.txt")
for n in file.read().split("\n"):
	values.append(n+"")
file.close()
while(len(values)>1):
	values=combine(values)
print(len(values[0]))