#导入数据库
import turtle as t

#定义子函数
def dl(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("orange","yellow")
    t.seth(0)
    t.begin_fill()
    t.circle(200)
    t.end_fill()
    
def yj(x,y):                 #眼睛
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red","white")
    t.seth(0)
    t.begin_fill()
    t.circle(32)
    t.end_fill()

def yq(x,y):                 #眼球
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.seth(0)
    t.begin_fill()
    t.circle(23)
    t.end_fill()

def zzb(x,y,fx,z):             #嘴角1
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("brown")
    t.seth(fx)
    t.circle(150,z)

    
def yzb(x,y,fx,z):              #嘴角2
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("brown")
    t.seth(fx)
    t.circle(-150,z)

def yjjx(x,y,z):                #圆角矩形
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("orange","white")
    t.seth(0)
    t.begin_fill()
    t.forward(100)
    t.circle(20,90)
    t.forward(z)
    t.circle(20,90)
    t.forward(100)
    t.circle(20,90)
    t.forward(z)
    t.circle(20,90)
    t.end_fill()
    
def byyq(x,y):                 #半圆眼球
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red","black")
    t.seth(0)
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.circle(-20,180)
    t.end_fill()
    
def hxz(x,y):                    #横嘴角
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("brown")
    t.seth(0)
    t.pensize(5)
    t.forward(80)

#主程序
t.speed(100)
t.hideturtle()
                                    #笑脸
dl(-200,0)
yj(-300,250)
yj(-100,250)
yq(-300,250)
yq(-100,250)
zzb(-200,80,0,30)
yzb(-200,80,180,30)

                                    #哭脸
dl(-200+500,0)
yj(-300+500,250)
yj(-100+500,250)
yq(-300+500,250)
yq(-100+500,250)
zzb(-200+500,80+60,180,30)
yzb(-200+500,80+60,0,30)


                                    #呆滞脸
dl(-200,-500)
yjjx(-350,-270,5)
yjjx(-150,-270,5)
byyq(-320,-225)
byyq(-120,-225)
hxz(-240,-330)

t.pensize(2)                                     #第四张脸                              
dl(-200+500,-500)                  
yjjx(-350+500,-270,20)
yjjx(-150+500,-270,20)
yq(-300+500,-260)
yq(-100+500,-260)
t.pensize(8)
zzb(300,-330,0,20)
yzb(300,-330,180,20)
