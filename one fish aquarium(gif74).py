import turtle,time,random
wn=turtle.Screen()
wn.setup(850,600)

AQ=[]
for i in range(74):
    i1=str(i)
    AQ.append(i1+'.gif')
    
image11 = ("f11.gif")
image12 = ("f12.gif")
image31 = ("f31.gif")
image32 = ("f32.gif")
wn.addshape(image11)
wn.addshape(image12)
wn.addshape(image31)
wn.addshape(image32)

t=turtle.Turtle()
t.showturtle()
t.speed(10)
t.penup()

X=-90
Y=-90
dx=4
dy=2

k=0
while True:
    k=k+1
    k1=k%74
    wn.bgpic(AQ[k1])
    t.setposition(X+dx,Y+dy)
    X,Y=t.position()
    
    if dx>0:
        t.shape(image11)
        time.sleep(0.01)
        t.shape(image12)
        time.sleep(0.01)

    if dx<0:
        t.shape(image31)
        time.sleep(0.01)
        t.shape(image32)
        time.sleep(0.01)
     
    if X>250:
        dx=-dx
    if X<-260:
        dx=-dx
    if Y<-205:
        dy=-dy  
    if Y>210:
        dy=-dy
    
