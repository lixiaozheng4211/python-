mg=[]
sum=0
for i in range(1000,10000):
    a=i%10       #得到个位数
    b=i//10%10   #得到十位数
    c=i//100%10  #得到百位数
    d=i//1000    #得到千位数
    if(i==((a**4)+(b**4)+(c**4)+(d**4))):
       mg.append(i)  #将i添加到mg列表中
       sum=sum+1
#
print("玫瑰花数为：",",".join(map(str, mg)))  #line12
print("玫瑰花数有：",sum,"个")


#line12(注释)
#  ","代表了mg空列表中数据用，隔开
#  .join()",".join(...)：将上一步得到的字符串序列用逗号连接。
#  如果输入是空列表，则结果是一个空字符串。
#  map(str, mg)：将 mg 列表中的每个元素转换为字符串。
