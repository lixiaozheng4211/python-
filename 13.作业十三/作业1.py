#=====引入库
import time
import turtle as t

#=====数据驱动
Title=[0,200]
Time=[0,0]
#=====定义函数
def p(x,y):
    global k
    k=1

def move1 (x,y):
    t1.pu()
    t1.goto(x,y)
    t1.pd()

def move2(x, y):
    t2.pu()
    t2.goto(x, y)
    t2.pd()
t.tracer(0)
t1=t.Pen()
t2=t.Pen()
t1.hideturtle()
t2.hideturtle()
#=====标题
move1(Title[0],Title[1])
t1.write("抢10秒可以免单",align='center',font=('楷体',40,"bold"))
#=====数字显示
sum,add,k=0.01,0.01,0
t.onscreenclick(p)#多线程函数，用来记录点击屏幕的
while True:
    sum+=add
    move2(Time[0],Time[1])
    t2.write("{:.2f}".format(sum),align='center',font=('楷体',50,"bold"))    #抄的
    time.sleep(1/60)
    if k==1:
        sum-=add
        if abs(sum - 10.00) <= 0.5:
            move1(Title[0], Title[1] - 400)
            t1.write("恭喜您免单！！", align='center', font=('楷体', 40, "bold"))
        else:
            move1(Title[0], Title[1] - 400)
            t1.write("很遗憾您没有获得免单！！", align='center', font=('楷体', 40, "bold"))
    t2.clear()
