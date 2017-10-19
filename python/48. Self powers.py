/*The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.*/

tot=0
for n in range(1,1001):
	tot+=(n**n)
print(str(tot)[-10:])
