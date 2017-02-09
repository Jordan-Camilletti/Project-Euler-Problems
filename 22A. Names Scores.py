/*Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?*/

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
	else:
		return 0

def nameScore(name):
	tot=0
	for x in name:
                tot=tot+alph(x)
	return tot
	
total=0
wrd=""
place=1
with open('names.txt','r') as r:
    for line in sorted(r):
        for n in line:
                wrd+=n
        total+=(nameScore(wrd)*place)
        #print(wrd+"has score of ",nameScore(wrd)," pos ",place," sco ",(nameScore(wrd)*place))
        place+=1
        wrd=""
print(total)
