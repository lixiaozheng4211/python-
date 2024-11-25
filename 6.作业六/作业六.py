hw=[]
sum=0
def h(n):
    a=n%10
    b=n//10%10
    c=n//100%10
    d=n//1000%10
    e=n//10000
    if(a==e and b==d):
        return 1
    return 0
#
for i in range(10000,100000):
    if(h(i)):
        hw.append(i)
        sum=sum+1
#
print("回文数是",",".join(map(str,hw)))
print("回文数有",sum,"个")
