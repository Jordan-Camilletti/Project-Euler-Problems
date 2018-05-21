"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?"""

nums=[0]*999999
for n in range(2,len(nums)):
    if(nums[n]==0):
        for n2 in range(n,len(nums),n):
          nums[n2]+=1

    if(n>4 and nums[n]==4 and nums[n-1]==4 and nums[n-2]==4 and nums[n-3]==4):
      print(n-3)
      break
