#第十天的桃子数
tao=1
day=10
for i in range(9,0,-1):
    tao=2*(tao+1)
    day-=1
    print("第{}天桃子数为{}个。".format(day,tao))
