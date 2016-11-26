"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

def isPrime(n):
    for x in range(n-2):
        if(n%(x+2)==0):
            return False
    return True

tot=0
num=1
while(tot<10001):
    num+=1
    if(isPrime(num)):
        tot+=1
print(tot)
print(num)
