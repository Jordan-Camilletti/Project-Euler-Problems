"""If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?"""

tris=[]
score=[]
for c in range(1001):
	for b in range(c):
		for a in range(b+1):
			if(a+b+c<=1000 and (a*a)+(b*b)==(c*c)):
				tris.append([a,b,c])

for n in range(1001):
	score.append(0)
for t in tris:
	score[t[0]+t[1]+t[2]]+=1

topN=0
top=0
for t in range(len(score)):
	if(score[t]>topN):
		topN=score[t]
		top=t
print(top)
