"""
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
		

def findNewSquare(num, sol1, sol89):
	#-1=new number leads to 1
	#-2=old number leads to 1
	#-3=new number leads to 89
	#-4=old number leads to 89
	if(num==1):
		return(-1)
	if(num in sol1):#TODO: add binary search to these
		return(-2)
	if(num==89):
		return(-3)
	if(num in sol89):#TODO: add binary search to these
		return(-4)
	sum=0
	
	
currNum=0
sol1=[]#Numbers that lead to 1
sol89=[]#Numbers that lead to 89
while(currNum<10000000):
	currNum+=1
	
	