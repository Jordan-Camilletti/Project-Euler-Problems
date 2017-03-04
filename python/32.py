def a(n):
    t=0
    for x in range(n-1):
        if(n%(x+1)==0):
            t+=x+1
            if(t>n): return True
    return False

def g(g):
    for n in range(g):
        if(a(n+1) and a(g-n-1)): return False
    return True
    
    
#print(g(24)==False and g(25)==True and g(36)==False and g(35)==True and g(40)==False and g(41)==True)
t=0
for n in range(20161):
    if(!g(n+1)): t+=n+1
print(t)
