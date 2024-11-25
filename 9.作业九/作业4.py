a=int(input("请输入每次最多数的数字个数："))
b=int(input("请输入初始数字："))
"""c=30-(a+1)
d=c-(a+1)
e=d-(a+1)
f=e-(a+1)"""
print("只需要按照倒序依次输入下列数字即可取胜：")
for i in range(1,30):
    
    m=30-i*(a+1)
    
    print(f"{m}")
    if (m-b)>=0 and (m-b)<a or (m-b)<=0 and (m-a)<a:
        break
        
