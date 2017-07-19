"""Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%."""

def bouncy(n):
	if(n<100): return False
	inc=False
	dec=False
	for num in range(1,len(str(n))):
		if(int(str(n)[num-1])>int(str(n)[num])): dec=True
		elif(int(str(n)[num-1])<int(str(n)[num])): inc=True
	return(inc and dec)
perA=19602
perB=2178
num=perA+perB
while((perA/(perA+perB))<0.99):
	num+=1
	if(bouncy(num)): perA+=1
	else: perB+=1
print(num,(perA/(perA+perB)))
