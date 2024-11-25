import turtle as t
import random as r
date=['红心A','红心2','红心3','红心4','红心5','红心6','红心7','红心8', '红心9','红心10','红心J','红心Q','红心K',
'黑桃A','黑桃2','黑桃3', '黑桃4','黑桃5','黑桃6','黑桃7','黑桃8', '黑桃9','黑桃10','黑桃J', '黑桃Q','黑桃K',
'方块A','方块2','方块3','方块4','方块5','方块6','方块7','方块8', '方块9','方块10','方块J','方块Q','方块K','梅花A',
'梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8', '梅花9','梅花10','梅花J','梅花Q','梅花K','小王','大王']
t.tracer(0)
def gezi(a,b,c):
    x=0
    while x<=c :
        t.penup()
        t.goto(a+x,b)
        t.pendown()
        t.seth(-90)
        for i in range(2):
            t.left(90)
            t.forward(55)
            t.left(90)
            t.forward(100)
            x+=29.75
gezi(-475,100,1130.5)
gezi(-400,-50,952)
gezi(-400,-170,952)
def zi(a,b,c):
    x=0
    while x<=c :
        t.penup()
        t.goto(a+x,b)
        t.pendown()
        an=r.choice(date)
        t.write(an,font=("微软雅黑",12 ,"normal"))
        date.remove(an)
        x+=59.25
zi(-465,145,1125.75)
zi(-395,-5,948)
zi(-395,-125,948)
t.hideturtle()
t.tracer(10,0)
