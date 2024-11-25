import turtle as t


data1=[[-300,150],[-50,-50],[-125,-125]]
data2=[[-85,-85],[-30,-125]]
data3=[[-30,-125],[0,0],[100,50]]
data4=[[[-80,-125],[120,-200]],[[10,-80],[100,-150]],[[50,-5],[250,-30]],[[75,25],[200,0]]]
data5=[[250,200]]
def m1(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def m2(x,y):
    t.goto(x,y)

def m3(x,y):
    t.seth(0)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(40)
    t.end_fill()
#左翼
t.color("black","blue")
t.pensize(5)
t.speed(20)
t.begin_fill()
m1(data1[0][0],data1[0][1])
m2(data1[1][0],data1[1][1])
m2(data1[2][0],data1[2][1])
m2(data1[0][0],data1[0][1])
t.end_fill()
#左下
m1(data1[1][0],data1[1][1])
t.begin_fill()
m2(data2[0][0],data2[0][1])
m2(data2[1][0],data2[1][1])
m2(data1[1][0],data1[1][1])
t.end_fill()
#中间
m2(data3[0][0],data3[0][1])
m2(data3[1][0],data3[1][1])
m2(data1[0][0],data1[0][1])
#右翼
t.begin_fill()
m2(data3[1][0],data3[1][1])
m2(data3[2][0],data3[2][1])
m2(data1[0][0],data1[0][1])
t.end_fill()
#风
m1(data4[0][0][0],data4[0][0][1])
m2(data4[0][1][0],data4[0][1][1])
m1(data4[1][0][0],data4[1][0][1])
m2(data4[1][1][0],data4[1][1][1])
m1(data4[2][0][0],data4[2][0][1])
m2(data4[2][1][0],data4[2][1][1])
m1(data4[3][0][0],data4[3][0][1])
m2(data4[3][1][0],data4[3][1][1])
#太阳
m3(data5[0][0],data5[0][1])
t.hideturtle()
t.done()
