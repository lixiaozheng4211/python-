print('素数为:')
m=0
for i in range(2,1001):
    a=1#flag
    n=i
    for j in range(2,n):
        if(n%j==0):
            a=0
            m=m+1
            break
    if(a==1):
        print('%d'%n,end='')
    else:
        print(end='')
m=999-m
print('共有%d个素数'%m)
