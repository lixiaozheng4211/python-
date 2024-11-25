sum=0
for x in range(0,6):
    for y in range(0,11):
        z=(5-x-0.5*y)
        if x+0.5*y+z==5 and x>=0 and y>=0 and z>=0  :
            print('一元数量{}，五角数量{}，一角数量{}'.format(x,2*y,int(10*z)))
            sum+=1
print('总方案个数为{}'.format(sum))