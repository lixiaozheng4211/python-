sxh=[]
sum=0
def s(n):
    a=n%10
    b=n//10%10
    c=n//100
    if(n==(a**3)+(b**3)+(c**3)):
        return 1
    return 0
#
for i in range(100,1000):
    if(s(i)):
        sxh.append(i)
        sum=sum+1
#
print("水仙花数是",",".join(map(str,sxh)))
print("水仙花数有",sum,"个")
