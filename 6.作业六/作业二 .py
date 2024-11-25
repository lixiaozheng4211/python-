sum=0
print("素数是")
for a in range(2,1001):
    flag=1
    for b in range(2,a):
        if(a%b==0):
            flag=0
            break
    if(flag==1):
        print("%d,"%a,end='')
        sum=sum+1
print("\n")
print("素数的个数：",sum,"个")
