n=27
h=0
for i in range(1000):
    n=2*(n-1)+1
    h+=1
    print("第{}小时的细胞总数为：{}.".format(h,n))
    if n>=100000:
        print("第{}小时的细胞总数为：{}.".format(h,n))
        print("要得到10w细胞最少需要{}小时。".format(h))
        break
