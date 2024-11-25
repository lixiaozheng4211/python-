for j in range(1,10):
    for i in range(1,j+1):
        print('%dx%d=%d\t'%(i,j,i*j),end='')
    print()
print()    
for j in range(1,10):
    for i in range(1,11-j):
        print('%dx%d=%d\t'%(i,10-j,i*(10-j)),end='')
    print()       
        
