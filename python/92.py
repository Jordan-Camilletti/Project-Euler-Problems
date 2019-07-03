"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

# Returns index of num in arr if present, else -1 
def binarySearch(arr, num, left, right): 
    if(right>=left):#Check base case 
        mid=int(left+(right-left)/2)
  
        if(arr[mid] == num):#Testing middle 
            return(True)
        elif(arr[mid]>num):#Testing left half
            return(binarySearch(arr, num, left, mid-1))
        else:#Testing right half
            return(binarySearch(arr, num, mid+1, right))
  
    else:
        return(False)
		
def findNewSquare(num, sol1, sol89):
	#-1=new number leads to 1
	#-2=old number leads to 1
	#-3=new number leads to 89
	#-4=old number leads to 89
	if(num==1):
		return(-1)
	if(binarySearch(sol1,num,0,len(sol1)-1)):#TODO: add binary search to these
		return(-2)
	if(num==89):
		return(-3)
	if(binarySearch(sol89,num,0,len(sol89)-1)):#TODO: add binary search to these
		return(-4)
	sum=0
	while(num>=1):
		sum+=((num%10)*(num%10))
		num=int(num/10)
	return(findNewSquare(sum,sol1,sol89))
	
currNum=0
sol1=[]#Numbers that lead to 1
sol89=[]#Numbers that lead to 89
total=0
while(currNum<10000000):
	currNum+=1
	currSum=findNewSquare(currNum,sol1,sol89)
	if(currSum==-1):#Leads to new 1
		sol1.append(currNum)
	elif(currSum==-3):#Leads to new 89
		sol89.append(currNum)
		total+=1
	elif(currSum==-4):#Leads to old 89
		total+=1
	if(currNum%100000==0):
		print(currNum/100000)
print(total)