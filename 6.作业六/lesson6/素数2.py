

def num(n):
    for j in range(2,n):
        if(n%j==0):
            return 0
    return 1

s=0
print('素数为:')
for i in range(2,1001):
    if(num(i)==1):
        #print('%d,'%i,end='')
        s+=1
print('共有%d个素数'%s)    
    
                
