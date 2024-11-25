import turtle
turtle.speed(0)

def flag(x,y) :
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color('red')
    turtle.begin_fill()
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.forward(600)
    turtle.left(90)
    turtle.forward(400)
    turtle.left(90)
    turtle.end_fill()

def star(l,x,y,an) :
    turtle.setheading(an)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("gold","gold")
    for i in range(5):
        turtle.forward(l)
        turtle.right(144)
    turtle.end_fill()


def chinese_flag(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,l1,l2,an1,an2,an3,an4,an5,):
    flag(x1,y1)
    star(l1,x2,y2,an1)
    star(l2,x3,y3,an2)
    star(l2,x4,y4,an3)
    star(l2,x5,y5,an4)
    star(l2,x6,y6,an5)


chinese_flag(-300,-200,-260,105,-120,160,-80,120,-80,75,-120,20,120,40,0,40,40,0,40)
turtle.hideturtle()
turtle.done()






