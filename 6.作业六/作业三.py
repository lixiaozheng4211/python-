import math as m
def is_prime(n):
    for i in range(2,int(m.sqrt(n))+1):  
        if(n%i==0):
            return 0  
    return 1  
#
sum=0
primes=[]
#
for a in range(2,1001):
    if(is_prime(a)):      
        primes.append(a)   
        sum=sum+1
#
print("素数是",",".join(map(str, primes)))
print("\n素数的个数:", sum, "个")
