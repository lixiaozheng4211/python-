import turtle as t

# 定义全局变量来存储狼、羊、菜的图形对象
wolf_turtle = None
sheep_turtle = None
vegetable_turtle = None



def approach1():
    global wolf_turtle, sheep_turtle, vegetable_turtle
    # 定义初始在河岸1的列表，用数字1、2、3分别代表狼、羊、菜
    a = [1, 2, 3]
    # 定义初始为空的河岸2的列表
    b = []

    # 第一步：将羊从河岸1送到河岸2
    step1 = a.pop(a.index(2))  # 通过元素值找到羊的索引并移除
    b.append(step1)
    print("第一步后：河岸1:", a, "河岸2:", b)
    move_turtle(sheep_turtle, 'right', True)  # 将羊的图形对象移动到对岸，抬笔移动

    # 第二步：将狼从河岸1送到河岸2，然后把羊带回河岸1
    step2 = a.pop(a.index(1))
    b.append(step2)
    step3 = b.pop(b.index(2))
    a.append(step3)
    print("第二步后：河岸1:", a, "河岸2:", b)
    move_turtle(wolf_turtle, 'right', True)  # 将狼的图形对象移动到对岸，抬笔移动
    move_turtle(sheep_turtle, 'left', True)  # 将羊的图形对象移回原岸，抬笔移动

    # 第三步：将菜从河岸1送到河岸2
    step4 = a.pop(a.index(3))
    b.append(step4)
    print("第三步后：河岸1:", a, "河岸2:", b)
    move_turtle(vegetable_turtle, 'right', True)  # 将菜的图形对象移动到对岸，抬笔移动

    # 第四步：将羊从河岸1送到河岸2
    step5 = a.pop(a.index(2))
    b.append(step5)
    print("第四步后：河岸1:", a, "河岸2:", b)
    move_turtle(sheep_turtle, 'right', True)  # 将羊的图形对象移动到对岸，抬笔移动


def approach2():
    global wolf_turtle, sheep_turtle, vegetable_turtle
    # 定义初始在河岸1的列表，用数字1、2、3分别代表狼、羊、菜
    a = [1, 2, 3]
    # 定义初始为空的河岸2的列表
    b = []

    # 第一步：将羊从河岸1送到河岸2
    step1 = a.pop(a.index(2))  # 通过元素值找到羊的索引并移除
    b.append(step1)
    print("第一步后：河岸1:", a, "河岸2:", b)
    move_turtle(sheep_turtle, 'right', True)  # 将羊的图形对象移动到对岸，抬笔移动

    # 第二步：将菜从河岸1送到河岸2，然后把羊带回河岸1
    step2 = a.pop(a.index(3))
    b.append(step2)
    step3 = b.pop(b.index(2))
    a.append(step3)
    print("第二步后：河岸1:", a, "河岸2:", b)
    move_turtle(vegetable_turtle, 'right', True)  # 将菜的图形对象移动到对岸，抬笔移动
    move_turtle(sheep_turtle, 'left', True)  # 将羊的图形对象移回原岸，抬笔移动

    # 第三步：将狼从河岸1送到河岸2
    step4 = a.pop(a.index(1))
    b.append(step4)
    print("第三步后：河岸1:", a, "河岸2:", b)
    move_turtle(wolf_turtle, 'right', True)  # 将狼的图形对象移动到对岸，抬笔移动

    # 第四步：将羊从河岸1送到河岸2
    step5 = a.pop(a.index(2))
    b.append(step5)
    print("第四步后：河岸1:", a, "河岸2:", b)
    move_turtle(sheep_turtle, 'right', True)  # 将羊的图形对象移动到对岸，抬笔移动


def set1(tex1):
    global wolf_turtle
    t.register_shape(tex1)  # 登记一下
    wolf_turtle = t.Turtle()
    wolf_turtle.color('white')
    wolf_turtle.shape(tex1)
    wolf_turtle.penup()  # 抬笔
    wolf_turtle.fd(-300)


def set2(tex2):
    global sheep_turtle
    t.register_shape(tex2)
    sheep_turtle = t.Turtle()
    sheep_turtle.color('white')
    sheep_turtle.shape(tex2)
    sheep_turtle.penup()  # 抬笔
    sheep_turtle.seth(-90)
    sheep_turtle.fd(-150)
    sheep_turtle.seth(0)
    sheep_turtle.fd(-300)


def set3(tex3):
    global vegetable_turtle
    t.register_shape(tex3)
    vegetable_turtle = t.Turtle()
    vegetable_turtle.color('white')
    vegetable_turtle.shape(tex3)
    vegetable_turtle.penup()  # 抬笔
    vegetable_turtle.seth(90)
    vegetable_turtle.fd(-150)
    vegetable_turtle.seth(0)
    vegetable_turtle.fd(-300)



def move_turtle(turtle_obj, direction, penup_flag):
    if penup_flag:
        turtle_obj.penup()
    if direction == 'right':
        turtle_obj.setx(turtle_obj.xcor() + 600)
    elif direction == 'left':
        turtle_obj.setx(turtle_obj.xcor() - 600)
    if penup_flag:
        turtle_obj.pendown()

def river():
    # 设置绘制速度为最快，并且关闭动画效果
    t.hideturtle()
    t.speed(100)
    t.color("lightblue")  # 设置填充颜色为蓝色
    t.goto(-100, -400)
    t.begin_fill()
    t.seth(0)
    t.fd(200)
    t.seth(90)
    t.fd(800)
    t.seth(180)
    t.fd(200)
    t.seth(270)
    t.fd(200)
    t.end_fill()

#先画河流
river()
# 选择执行哪种方法
approach=int(input('please choose a way 1 or 2\n'))
if approach == 1 :
    set1('狼.gif')
    set2('羊.gif')
    set3('菜.gif')
    approach1()
else:
    set1('狼.gif')
    set2('羊.gif')
    set3('菜.gif')
    approach2()
t.done()