#=====引入库
import turtle as t
import random as r
import time

t1=t.Pen()
t2=t.Pen()
t1.hideturtle()
t2.hideturtle()

#=====数据驱动
paimian=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
huase=['♥','♠','♣','♦']
Title=[0,400]
Time=[50,50]
hp=[[200,100],[-200,100],[-200,-100],[200,-100]]
jishi1,jishi2=10,4
#=====定义函数
def move1(x,y):
    t1.pu()
    t1.goto(x,y)
    t1.pd()
def move2(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()
def pk(x,y):
    move1(x,y)
    t1.color("black","white")
    t1.seth(0)
    for i in range(2):
        t1.fd(120)
        t1.circle(5,90)
        t1.fd(190)
        t1.circle(5,90)
    move1(x,y)
    r.shuffle(paimian)
    n=r.randint(0,3) #随机整数
    if n==0 or n==3:
        t1.pencolor('red')
    elif n==1 or n==2:
        t1.pencolor('black')
    move1(x+20,y+160)
    t1.write(paimian[0],align='center',font=('楷体',30,'bold'))     #扑克值的大小总是取首元素
    move1(x+20,y+145)
    t1.write(huase[n],align='center',font=('楷体',20,'bold'))
    move1(x+17,y)
    t1.write(huase[n],font=('楷体',90,'bold'))
def title(x,y):
    t.hideturtle()
    t.pu()
    t.goto(x+100,y)
    t.pd()
    t.pencolor("green")
    t.write('记忆力大比拼！！',align='center',font=('黑体',50,'bold'))
#=====主程序

title(Title[0],Title[1])

while True:
    t.tracer(0)
    title(Title[0], Title[1])
    for i in range(4):
        pk(hp[i][0],hp[i][1])
    for i in range(jishi1):
        move2(Time[0],Time[1])
        t2.hideturtle()
        t2.write(jishi1-i,align='center',font=('黑体',30,'bold'))
        time.sleep(1)
        t2.clear()
    t.tracer(1)
    t1.clear()
    t.tracer(0)
    for i in range(jishi2):

        move2(Time[0],Time[1])
        time.sleep(1)
        t2.write(jishi2 - i-1, align='center', font=('黑体', 30, 'bold'))
        t2.clear()
    t.tracer(1)
