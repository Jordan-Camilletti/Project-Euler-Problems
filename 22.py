def alph(letter):
	if(letter=="A"):
		return 1;
	elif(letter=="B"):
		return 2;
	elif(letter=="C"):
		return 3;
	elif(letter=="D"):
		return 4;
	elif(letter=="E"):
		return 5
	elif(letter=="F"):
		return 6
	elif(letter=="G"):
		return 7
	elif(letter=="H"):
		return 8
	elif(letter=="I"):
		return 9
	elif(letter=="J"):
		return 10
	elif(letter=="K"):
		return 11
	elif(letter=="L"):
		return 12
	elif(letter=="M"):
		return 13
	elif(letter=="N"):
		return 14
	elif(letter=="O"):
		return 15
	elif(letter=="P"):
		return 16
	elif(letter=="Q"):
		return 17
	elif(letter=="R"):
		return 18
	elif(letter=="S"):
		return 19
	elif(letter=="T"):
		return 20
	elif(letter=="U"):
		return 21
	elif(letter=="V"):
		return 22
	elif(letter=="W"):
		return 23
	elif(letter=="X"):
		return 24
	elif(letter=="Y"):
		return 25
	elif(letter=="Z"):
		return 26
	elif(letter=='"' or letter==","):
		return 0

def nameScore(name):
	tot=0
	for x in name:
		tot+=alph(x)
	return tot
	
"""f=open("names.txt")
next=f.read(1)
wrd=""
place=1
total=0
while(next != "="):#I put '=' at the end of the file to mark the end
	if(next==","):
		total+=(nameScore(wrd)*place)
		wrd=""
		place+=1
	wrd+=next
	next=f.read(1)
print(total)"""
total=0
wrd=""
with open('text.txt','r') as r:
    for line in sorted(r):
        for n in line:
                if(n==","):
                        total+=(nameScore(wrd)*place)
                        wrd=""
                        place+=1
                wrd+=n
print(total)
