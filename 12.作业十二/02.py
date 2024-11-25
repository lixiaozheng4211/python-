for x in range(0,21):
    for y in range(0,34):
        z=100-5*x-3*y
        if x+y+3*z==100 :
            print('公鸡个数{}，母鸡个数{}，小鸡个数{}'.format(x,y,3*z))
