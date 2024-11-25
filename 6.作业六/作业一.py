#正
for j in range(1,10):
    for i in range(1,j+1):
        print("%dx%d=%d\t"%(j,i,i*j),end='')
    print()
print("\n")
#反
for a in range(9,0,-1):     #range反向计数需要加,-1
    for b in range(1,a+1):
        print("%dx%d=%d\t"%(b,a,a*b),end='')
    print()
