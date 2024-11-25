sanjiao=[]
"""s2=[1,1]
sanjiao.append(s2)
s3=[1,s2[0]+s2[1],1]
sanjiao.append(s3)
s4=[1,s3[0]+s3[1],s3[1]+s3[2],1]
sanjiao.append(s4)
s5=[1,s4[0]+s4[1],s4[1]+s4[2],s4[2]+s4[3],1]
sanjiao.append(s5)"""
s=[1]

s2=[1,1]
s3=[1,2,1]
sanjiao.append(s)
sanjiao.append(s2)
sanjiao.append(s3)
for i in range(3,10):
    s=[1]
    
    for j in range(2, i+1):
        
        
           

        
        
        s.append(sanjiao[i-1][j - 2] + sanjiao[i - 1][j-1])# 中间的元素等于上一行的相邻两个元素之和
    
    s.append(1)
    sanjiao.append(s)
for i in range(10):
    s = " ".join(f"{num:^5}" for num in sanjiao[i])  # 每个数字居中对齐
    print(s.center(60))  # 整体居中显示
