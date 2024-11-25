#导入数据库
import turtle as t
#导入子函数
def y1(x,y,a):           #红圆
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(a)
    t.end_fill()

def y2(x,y,a):          #白圆
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(a)
    t.end_fill()


def y3(x,y,a):             #蓝圆
    t.penup()             
    t.goto(x,y)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.circle(a)
    t.end_fill()

def star(x,y):          #五角星
    t.setheading(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("white")
    for i in range(5):
        t.forward(145)
        t.right(144)
    t.end_fill()
#主程序
t.speed(100)
y1(0,0,200)
y2(0,30,170)
y1(0,60,140)
y2(0,90,110)
y3(0,120,80)
star(-72.5,220)
