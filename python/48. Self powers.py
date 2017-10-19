"""The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000."""

tot=0#Yep, this is it
for n in range(1,1001):#This is the entire solution
	tot+=(n**n)#Just four lines
print(str(tot)[-10:])#This is all there is to the problem
