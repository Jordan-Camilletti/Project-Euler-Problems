def num(starting):
	length=len(str(starting))
	place=[" "," "," hundred "," thousand "," "," hundred "," million "," "," hundred "," billion "]
	ones=["","one","two","three","four","five","six","seven","eight","nine"]
	tens=["","onety","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"]
	wrd=""
	i=length-1
	while(i>=0):
		i-=1
		if(length-i==1 or length-i==4 or length-i==7):
			wrd=tens[int(str(starting)[i])]+place[length-i-1]+wrd
		else:
			wrd=ones[int(str(starting)[i])]+place[length-i-1]+wrd
	print(wrd)

num(1)
num(2)
num(10)
num(12)
num(50)
num(100)
num(666)
