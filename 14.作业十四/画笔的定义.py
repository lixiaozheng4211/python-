import turtle as t
def set(tex1, tex2, tex3):
    t.register_shape(tex1)  # 登记一下
    t1 = t.Turtle()
    t1.color('white')
    t1.shape(tex1)
    t1.fd(150)

    t.register_shape(tex2)
    t2 = t.Turtle()
    t2.color('white')
    t2.shape(tex2)
    t2.seth(-90)
    t2.fd(150)

    t.register_shape(tex3)
    t3 = t.Turtle()
    t3.color('white')
    t3.shape(tex3)
    t3.seth(90)
    t3.fd(150)

set('狼.gif', '羊.gif', '菜.gif')
# -------------------
t.done()