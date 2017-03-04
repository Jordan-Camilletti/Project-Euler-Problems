def abundant(n):
    t=0
    for x in range(n-1):
        if(n%(x+1)==0):
            t+=x+1
            if(t>n): return True
    return False
	 
total=0
for m in range(20162):
	total+=(m+1)
	print(m)
	for n in range(m+1):
		if(perf((m+1)-(n+1))==True and perf(n+1)==True):
			total-=(m+1)
			break
print(total)
