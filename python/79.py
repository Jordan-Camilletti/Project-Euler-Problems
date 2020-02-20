"""A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length."""

"""	0: not found
	>0: value is found at end of main
	<0: value is found at start of main
	Returns the length of character shared between main and value"""
def contains(main, value, size):
	if(size==0 and main==value):
		return(size)
	if(value[(size*-1):]==main[:size]):#Found at start of main
		return(size*-1)
	if(main[(size*-1):]==value[:size]):#Found at end of main
		return(size)
	return(0)#Not found
	
"""This takes a list of values amd iterates through it once
It adds or combines these values into a 2nd array, which it then returns
Returns an array of combined values"""
def combine(values):
	combinedValues=[values[0]]
	del(values[0])
	for val in range(len(values)):
		result=addOn(val,values,combinedValues)
		values=result[0]
		combinedValues=result[1]
	return(combinedValues)
	"""for l in range(len(values[val])):
		for cVal in range(len(combinedValues)):
			contain=contains(combinedValues[cVal],values[val],l)
			if(contain>0):#Add value on to the end
				combinedValues[cVal]=combinedValues[cVal][:(-1*contain)]+values[val]
				del(values[val])
			elif(contain<0):#Add value on to the start
				combinedValues[cVal]=values[val][:contain]+combinedValues[cVal]
				del(values[val])"""

"""This goes through the process of adding the 2
It was put into its own array to allow it to stop once they combined
Returns a 2D array, [0] is values, [1] is combinedValues"""
def addOn(val, values, combinedValues):
	for l in range(len(values[val])):
		for cVal in range(len(combinedValues)):
			contain=contains(combinedValues[cVal],values[val],l)
			if(contain>0):#Add value on to the end
				combinedValues[cVal]=combinedValues[cVal][:(-1*contain)]+values[val]
				del(values[val])
				rtn=[values,combinedValues]
				return(rtn)
			elif(contain<0):#Add value on to the start
				combinedValues[cVal]=values[val][:contain]+combinedValues[cVal]
				del(values[val])
				rtn=[values,combinedValues]
				return(rtn)

values=[]#individual 3-len codes
file=open("keylog.txt")
for n in file.read().split("\n"):
	if(n+"" not in values):
		values.append(n+"")
file.close()

while(len(values)>1):
	values=combine(values)
print(len(values[0]))