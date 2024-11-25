#导入数据库
import turtle as t
t.speed(100)
t.hideturtle()
def dl(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("orange","yellow")
    t.seth(0)
    t.begin_fill()
    t.circle(200)
    t.end_fill()
    
def yj(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red","white")
    t.seth(0)
    t.begin_fill()
    t.circle(32)
    t.end_fill()

def yq(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.seth(0)
    t.begin_fill()
    t.circle(23)
    t.end_fill()

def zzb(x,y,fx):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.seth(fx)
    t.circle(150,30)

    
def yzb(x,y,fx):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("black")
    t.seth(fx)
    t.circle(-150,30)





#笑脸
dl(-200,0)
yj(-300,250)
yj(-100,250)
yq(-300,250)
yq(-100,250)
zzb(-200,80,0)
yzb(-200,80,180)

#哭脸
dl(-200+500,0)
yj(-300+500,250)
yj(-100+500,250)
yq(-300+500,250)
yq(-100+500,250)
zzb(-200+500,80+60,180)
yzb(-200+500,80+60,0)



