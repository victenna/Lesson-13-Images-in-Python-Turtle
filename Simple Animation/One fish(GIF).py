import turtle,time
turtle.tracer(2)
t=turtle.Turtle()
wn=turtle.Screen()
wn.setup(1200,900)
wn.bgpic("Aquarium.gif")

image11="f11.gif"
image21="f21.gif"
image31="f31.gif"
image41="f41.gif"
wn.addshape(image11)
wn.addshape(image21)
wn.addshape(image31)
wn.addshape(image41)

image12 ="f12.gif"
image22="f22.gif"
image32="f32.gif"
image42="f42.gif"
wn.addshape(image12)
wn.addshape(image22)
wn.addshape(image32)
wn.addshape(image42)


t.showturtle()
t.up()
t.goto(-400,-200)

r=-1
while True:
    r=r+1
    if r>0:
        t.left(90)
    
    for i in range(100):
        t.shape(image11)
        t.fd(4)
        time.sleep(0.1)
        t.shape(image12)
        t.fd(4)
        time.sleep(0.1)

    t.left(90)
    for i in range(50):
        t.shape(image21)
        t.fd(4)
        time.sleep(0.1)
        t.shape(image22)
        t.fd(4)
        time.sleep(0.1)

    t.left(90)
    for i in range(100):
        t.shape(image31)
        t.fd(4)
        time.sleep(0.1)
        t.shape(image32)
        t.fd(4)
        time.sleep(0.1)
        
    t.left(90)
    for i in range(50):
        t.shape(image41)
        t.fd(4)
        time.sleep(0.1)
        t.shape(image42)
        t.fd(4)
        time.sleep(0.1)
        
        
        


    
