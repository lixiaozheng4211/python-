

a=1
b=1


print("斐波那契数列前十五项为：")
for i in range(1, 16):
    print("第 {} 项: {}".format(i,a))
    
    a, b = b, a + b#把b的值赋值给a，a加b的值赋值给b相当于ab从第1，2项变成了2，3项
