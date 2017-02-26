"""The sum of the first ten squared numbers is 385(1^2 + 2^2 + 3^2... + 10^2)==385
The sum of the first ten numbers squared is 3025(1+2+3...+10)^2==55^2==3025
The difference of between the two is 2640
Find the difference between the first 100 numbers"""

tot1=0;tot2=0
for x1 in range(101):#1^2 + 2+^ ... 100^2
    tot1=tot1+(x1*x1)

for x2 in range(101):#(1+2+3...+100)^2
    tot2=tot2+x2
print((tot2*tot2)-tot1)#finding the difference
