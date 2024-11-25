#载入库
import turtle as t
import time
pen1 = t.Turtle()
#驱动数据
C1=[1500,800]
r1=[[430,60],[430,20],[430,-20],[430,-60],[430,-100]]
r2=[[396,40],[396,0],[396,-40],[396,-80]]
r3=[[362,20],[362,-20],[362,-60]]
r4=[[328,0],[328,-40]]
r5=[[294,-20]]
zAD=[[-650,350],[-650,300]]
zBC=[[-650,-300],[-700,300],[-650,350],[650,300]]
zEF=[[-650,-320],[-650,280],[650,-320],[650,280],[-60,-300],[-10,300],[-350,300]]
H1=[[204,-20,"pink"],[0,-20,"blue"],[-350,-20,"orange"],[-350,80,"green"]]
H2=[[-350,-120,"yellow"],[-450,-20,"white"],[490,-20,"black"]]
#定义
#移动
def move(x,y):
    t.penup()
    t.seth(0)
    t.goto(x,y)
    t.pendown()
#桌角
def A(x,y):
    t.pensize(2)
    move(x,y)
    t.color("black","dark gray")
    t.begin_fill()
    t.seth(0)
    for i in range(2):
       t.forward(1300)
       t.circle(-50,90)
       t.forward(600)
       t.circle(-50,90)
    t.end_fill()
    
#桌边（横）
def B(x,y):
    move(x,y)
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.forward(1300)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
#桌边（竖）
def C(x,y):
    move(x,y)
    t.color("red")
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.right(90)
        t.forward(600)
        t.right(90)
    t.end_fill()
#桌面
def D(x,y):
    move(x,y)
    t.color("green","dark green")
    t.begin_fill()
    for i in range(2):
        t.forward(1300)
        t.right(90)
        t.forward(600)
        t.right(90)
    t.end_fill()
#球洞
def E(x,y):
    move(x,y)
    t.color("gray")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def E1(x,y):
    move(x,y)
    t.seth(90)
    t.color("gray")
    t.begin_fill()
    t.circle(20,180)
    t.end_fill()

def E2(x,y):
    move(x,y)
    t.seth(-90)
    t.color("gray")
    t.begin_fill()
    t.circle(20,180)
    t.end_fill()
#中场线
def F(x,y):
    move(x,y)
    t.pencolor("black")
    t.seth(-90)
    t.forward(200)
    t.right(90)
    t.circle(100,180)
    t.right(90)
    t.forward(200)
    t.seth(90)
    t.forward(600)
#红球
def G(x,y):
    move(x,y)
    t.color("green","red")
    t.begin_fill()
    t.circle(20)
    t.end_fill()
#彩球
def H(x,y,c):
    move(x,y)
    t.color("green",c)
    t.begin_fill()
    t.circle(20)
    t.end_fill()

#主程序
t.hideturtle()
t.speed(0)
t.setup(C1[0],C1[1])
A(zAD[0][0],zAD[0][1])
B(zBC[0][0],zBC[0][1])
B(zBC[2][0],zBC[2][1])
C(zBC[1][0],zBC[1][1])
C(zBC[3][0],zBC[3][1])
D(zAD[1][0],zAD[1][1])
E(zEF[0][0],zEF[0][1])
E(zEF[1][0],zEF[1][1])
E(zEF[2][0],zEF[2][1])
E(zEF[3][0],zEF[3][1])
E2(zEF[4][0],zEF[4][1])
E1(zEF[5][0],zEF[5][1])
F(zEF[6][0],zEF[6][1])
G(r1[0][0],r1[0][1])
G(r1[1][0],r1[1][1])
G(r1[2][0],r1[2][1])
G(r1[3][0],r1[3][1])
G(r1[4][0],r1[4][1])
G(r2[0][0],r2[0][1])
G(r2[1][0],r2[1][1])
G(r2[2][0],r2[2][1])
G(r2[3][0],r2[3][1])
G(r3[0][0],r3[0][1])
G(r3[1][0],r3[1][1])
G(r3[2][0],r3[2][1])
G(r4[0][0],r4[0][1])
G(r4[1][0],r4[1][1])
G(r5[0][0],r5[0][1])
H(H1[0][0],H1[0][1],H1[0][2])
H(H1[1][0],H1[1][1],H1[1][2])
H(H1[2][0],H1[2][1],H1[2][2])
H(H1[3][0],H1[3][1],H1[3][2])
H(H2[0][0],H2[0][1],H2[0][2])
H(H2[2][0],H2[2][1],H2[2][2])
p =0
i = 20
while(p<=5):
    time.sleep(0.3)
    pen1.clear()
    t.tracer(0)
    pen1.hideturtle()
    pen1.penup()
    pen1.seth(0)
    pen1.goto(-450+p*i,-20+p*(i+30))
    pen1.pendown()   
    pen1.color("green",'white')
    pen1.begin_fill()
    pen1.circle(20)
    pen1.end_fill()
    t.tracer(10)
    p+=1
    i -=4
t.done()