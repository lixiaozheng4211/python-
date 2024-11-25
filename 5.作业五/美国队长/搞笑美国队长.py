#导入数据库
import turtle as t
#定义子函数
def y1(x,y,a):          #红色圆   
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(a)
    t.end_fill()

def y2(x,y,a):        #白色圆 
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.circle(a)
    t.end_fill()


def dl(x,y):             #大脸
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("orange","yellow")
    t.seth(0)
    t.begin_fill()
    t.circle(80)
    t.end_fill()
    
def yj(x,y):                 #眼睛
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red","white")
    t.seth(0)
    t.begin_fill()
    t.circle(12.8)
    t.end_fill()

def yq(x,y):                 #眼球
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.seth(0)
    t.begin_fill()
    t.circle(9.2)
    t.end_fill()

def zzb(x,y,fx,z):             #嘴角1
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("brown")
    t.seth(fx)
    t.circle(90,z)

    
def yzb(x,y,fx,z):              #嘴角2
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("brown")
    t.seth(fx)
    t.circle(-90,z)

#主程序
t.speed(100)
y1(0,0,200)
y2(0,30,170)
y1(0,60,140)
y2(0,90,110)
dl(0,120)
yj(-40,200)
yj(40,200)
yq(-40,200)
yq(40,200)
zzb(0,140,0,20)
yzb(0,140,180,20)
t.hideturtle()
