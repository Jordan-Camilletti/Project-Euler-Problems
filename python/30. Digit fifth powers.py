"""
"""

num=0
tot=0
while(score>=num):
	num+=1
	score=0
	for n in str(num):
		score+=(int(n)**5)
	if(score==num): tot+=score
print(tot)
