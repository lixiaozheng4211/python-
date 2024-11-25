def num(n):
        a=n%10
        b=(n//10)%10
        c=n//100
        sum=a**3+b**3+c**3
        if(n==sum):
            return 0
        return 1

s=0
print('水仙花数为:')
for i in range(100,1000):
    if(num(i)==0):
        print('%d,'%i,end='')
        s+=1
print('\n共有%d个水仙花数'%s)    
    
