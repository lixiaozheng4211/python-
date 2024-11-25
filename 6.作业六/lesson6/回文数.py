def n(j):
    j=str(j)
    # 比较字符串和其反转是否相同
    if(j==j[::-1]):
        return 1
    else:
        return 0
s=0 
for i in range(10000,100000):
    if n(i):
        print(i)
        s+=1
print("\n回文数的个数为：",s)
