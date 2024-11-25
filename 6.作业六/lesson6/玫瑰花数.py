s=0
for i in range(1000,10000):
    a=i%10
    b=i//10%10
    c=i//100%10
    d=i//1000
    if(i==a**4+b**4+c**4+d**4):
        s+=1
        print(i,'\t',end='')
print('\n玫瑰花数为:',s)
