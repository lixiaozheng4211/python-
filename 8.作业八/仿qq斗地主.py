import  random as r
import turtle as t
t.tracer(0)
t.hideturtle()
date=['\u2665A','\u26652','\u26653','\u26654','\u26655','\u26656','\u26657','\u26658','\u26659','\u266510','\u2665J','\u2665Q','\u2665K',
      '\u2660A','\u26602','\u26603','\u26604','\u26605','\u26606','\u26607','\u26608','\u26609','\u266010','\u2660J','\u2660Q','\u2660K',
      '\u2666A','\u26662','\u26663','\u26664','\u26665','\u26666','\u26667','\u26668','\u26669','\u266610','\u2666J','\u2666Q','\u2666K',
      '\u2663A','\u26632','\u26633','\u26634','\u26635','\u26636','\u26637','\u26638','\u26639','\u266310','\u2663J','\u2663Q','\u2663K',
      '小王','大王']
dz=[]
lm1=[]
lm2=[]
def shu(x,name):
    for j in range(x):
        an=r.randint(0,len(date)-1)
        name.append(date[an])
        del date[an]
shu(20,dz)
shu(17,lm1)
shu(17,lm2)
'''
print(dz)
print(lm1)
print(lm2)
'''
###位移-----------------------
def lc(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
#####方框-------------
def gezi(a,b,c):
    x=0
    while x<=c :
        t.penup()
        t.goto(a+x,b)
        t.pendown()
        t.seth(-90)
        t.begin_fill()
        t.color("grey","white")
        for i in range(2):
            t.forward(85)
            t.circle(-10,90)
            t.forward(55)
            t.circle(-10,90)
            x+=18
        t.end_fill()
gezi(-475,100,684)
gezi(-400,-50,576)
gezi(-400,-170,576)
t.tracer(10,0)
####规定颜色---------------
def color(name):
    if name[i][0:1]=='\u2665' or name[i][0:1]=='\u2666' or name[i][0:1]=="大" :
        t.pencolor("red")
    elif name[i][0:1]=='\u2660' or name[i][0:1]=='\u2663' or name[i][0:1]=="小" :
        t.pencolor("black")
####数字------------------
def zi(name,x,y):
    if name[i][1:]=="10" :
        lc(x+36*i,y)
        t.write(name[i][1:],font=("微软雅黑",15))
    elif name[i][1:]=="王" :
        lc(x+36*i,y)
        t.write("J",font=("华文琥珀",16))
        lc(x+36*i,y-15)
        t.write("O",font=("华文琥珀",16))
        lc(x+36*i,y-30)
        t.write("K",font=("华文琥珀",16))
        lc(x+36*i,y-45)
        t.write("E",font=("华文琥珀",16))
        lc(x+36*i,y-60)
        t.write("R",font=("华文琥珀",16))
        lc(x+36*i,y-75)
    else:
        lc(x+36*i,y)
        t.write(name[i][1:],font=("微软雅黑",15))
##图形--------------

    if name[i][1:]!="王" :
        lc(x+36*i,y-30)
        t.write(name[i][0:1],font=("微软雅黑",24))
######汇总-----------
for i in range(20):
    color(dz)
    zi(dz,-545,80)
for i in range(17):
    color(lm1)
    zi(lm1,-470,-70)
    color(lm2)
    zi(lm2,-470,-190)
t.tracer(10,0)
t.done()
                
    
        
    


    
