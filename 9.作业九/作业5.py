m="y"
while (m=="y"):
    b=[]
    a=0
    def panduan(x):
        
        
        if x%4==0 and x%100!=0 or x%400==0:
            b.append(x)
            return 1
        else:
            return 0
    c=int(input("请输入比2024大的年份："))
    for i in range(2024,c+1):
        
        a+=int(panduan(i))
    
    for index, year in enumerate(b):#enumerate(b) 函数用于同时获取列表 b 中元素的索引和对应的值。
        if index > 0 and index % 10 == 0:
            
            print()  # 每10个换行
        print(year, end=", " if index < len(b) - 1 else "")
    print("从2024年到{}年中的闰年数为：{}".format(c,a))
    m=input("想再玩一次吗？y or n")
