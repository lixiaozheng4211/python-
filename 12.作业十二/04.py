sum=0
for x in range(0,17): # 男人吃三元
    for y in range(0,26):# 女人吃两元
        z=50-3*x-2*y
        if 3*x+2*y+z==50 and x>=0 and y>=0 and z>=0 :
            print('男人数量{}，女人数量{}，小孩数量{}'.format(x,y,z))
            sum+=1
print('总方案数为{}'.format(sum))