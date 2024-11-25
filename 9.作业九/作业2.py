n=26625
h=11
for i in range(11,0,-1):
    
    n=n*0.5+0.5# 每小时的巨噬细胞数量，通过逆推计算前一小时的细胞数量
    h-=1
    n=int(n)
    if h==0:
        print("基数为：{}个".format(n))
        break
    
    print("第{}小时巨噬细胞数量为{}个。".format(h,n))
    
    
