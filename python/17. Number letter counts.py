"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?"""

onesLen=[0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tensLen=[0,3,6,6,5,5,5,7,6,6]
total=0
for i in range(1,1000):
    ones=i%10 
    tens=int(((i%100)-ones)/10)
    hundreds=int(((i%1000)-(tens*10)-ones)/100)
    c=i%10
    b=((i%100)-c)/10
    if(hundreds!=0):
        total+=onesLen[hundreds]+7
        if(tens!=0 or ones!=0): 
        	total += 3 
    if(tens==0 or tens==1):
    	total+=onesLen[tens*10+ones]
    else:
    	total+=tensLen[tens]+onesLen[ones]
 
total+=onesLen[1]+8
print(total)
