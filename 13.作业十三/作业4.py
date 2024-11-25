#======载入库
import turtle as t
import random as r

t1=t.Pen()
t2=t.Pen()
t1.hideturtle()
t2.hideturtle()
#设置背景颜色为绿色
ls = [
    # 1            2           3           4           5           6           7           8           9           10
    '\u264B', '\u2648', '\u2649', '\u264F', '\u264E', '\u264A', '\u264D', '\u2653', '\u264C', '\u264F',  # 1

    '\u2653', '\u264F', '\u264B', '\u2648', '\u2649', '\u264F', '\u264E', '\u264C', '\u264E', '\u264A',  # 2

    '\u2648', '\u2649', '\u264F', '\u2653', '\u264B', '\u264E', '\u264C', '\u264A', '\u2652', '\u264B',  # 3

    '\u264D', '\u2650', '\u2652', '\u264B', '\u2649', '\u264C', '\u2648', '\u264F', '\u264A', '\u264F',  # 4

    '\u264A', '\u2649', '\u264B', '\u2652', '\u264C', '\u264F', '\u2653', '\u2648', '\u2653', '\u2649',  # 5

    '\u2649', '\u264D', '\u264F', '\u264C', '\u2648', '\u2650', '\u264E', '\u2651', '\u264E', '\u264C',  # 6

    '\u2652', '\u2649', '\u264C', '\u2648', '\u264B', '\u264A', '\u2650', '\u264F', '\u264E', '\u264D',  # 7

    '\u264E', '\u264C', '\u2648', '\u2649', '\u264F', '\u264B', '\u264F', '\u2653', '\u264D', '\u264E',  # 8

    '\u264C', '\u264F', '\u264E', '\u264D', '\u2648', '\u2649', '\u264B', '\u2652', '\u264F', '\u264C',  # 9

    '\u264D', '\u2650', '\u2652', '\u264B', '\u2649', '\u264C', '\u2648', '\u264F', '\u2653', '\u264A'  # 10
]

#=====数据驱动
title1=[100,200]
kaungjia1=[-700,300]
ball1=[100,-200]
#=====函数定义
def move1(x,y):
    t1.pu()
    t1.goto(x,y)
    t1.pd()
def move2(x,y):
    t2.pu()
    t2.goto(x,y)
    t2.pd()
def ball(x,y,size):
    move1(x,y)
    t1.pensize(9)
    t1.color('purple3', 'purple1')
    t1.begin_fill()
    t1.circle(size)
    t1.end_fill()

def title(x,y):
    move1(x,y)
    t1.write("吉普赛读心术",font=('楷体',40,'normal' ))
    move1(x,y-50)
    t1.color("yellow")
    t1.write("别把心事都藏在心底", font=('楷体', 20, 'normal'))
def kuangjia(x,y):
    t1.color("black")
    for i in range (11):
        move1(x+50*i,y)
        t1.seth(270)
        t1.fd(500)
    for i in range (11):
        move1(x,y-50*i)
        t1.seth(0)
        t1.fd(500)
def xuhao(x,y):


    for j in range (10):
        for i in range (10):
            a=10*j+i
            move1(x-40+51*(i+1),y-45-50*j)
            t1.pencolor('red')
            t1.write(ls[a], font=('楷体', 25, 'normal'))  # 画图案
            t1.pencolor('black')
            t1.write(a + 1, font=('楷体', 10, 'normal'))  # 画图案
def p(x,y):
    t1.color("red")
    move1(ball1[0]-80,ball1[1]+80)
    t1.write(ls[8], font=('楷体', 120,'normal'))
def word(x,y):
    move1(x+200,y-160)
    t1.write('游戏规则：\n请想10-99中任意一个数：', font=('楷体', 10, 'bold'))
    move1(x+200, y-200)
    t1.write('将这个数减去个位，再减去十位,并且在列表中找到结果对应的符号', font=('楷体', 10, 'bold'))
    move1(x+200, y-240)
    t1.write('请把这个符号记在心中,准备好被看穿内心了吗？请点击水晶球！', font=('楷体', 10, 'bold'))

def draw():
    title(title1[0],title1[1])
    kuangjia(kaungjia1[0],kaungjia1[1])
    ball(ball1[0],ball1[1],150)
    word(title1[0],title1[1])
    xuhao(kaungjia1[0],kaungjia1[1])



#=====主程序
r.shuffle(ls)
for i in range(10):
    ls[i*9-1]=ls[8]
t.bgcolor("white")
t.tracer(0)
t.onscreenclick(p)
draw()
t.done()
t.tracer(1)