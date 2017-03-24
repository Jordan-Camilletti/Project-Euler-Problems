"""
"""

num=0
tot=0
for x in range(1,100):
	score=0
	for n in str(x): score+=(int(n)**5)
	if(score==x): tot+=x
print(tot)
