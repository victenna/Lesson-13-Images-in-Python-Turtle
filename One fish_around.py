import turtle
fish=turtle.Turtle()
wn=turtle.Screen()
wn.setup(1200,900)
wn.bgpic("Aquarium.gif") 
image1 ="fish1.gif"
image2="fish2.gif"
image3="fish3.gif"
image4="fish4.gif"
wn.addshape(image1)
wn.addshape(image2)
wn.addshape(image3)
wn.addshape(image4)
fish.showturtle()
fish.up()
fish.goto(-400,-200)

r=-1
while True:
    r=r+1
    if r>0:
        fish.left(90)
    fish.shape(image1)
    for i in range(400):
        fish.fd(2)
        
    fish.shape(image2)
    fish.left(90)
    for i in range(200):
        fish.fd(2)
        
    fish.shape(image3)
    fish.left(90)
    for i in range(400):
        fish.fd(2)
        #time.sleep(0.005)

    fish.shape(image4)
    fish.left(90)
    for i in range(200):
        fish.fd(2)
       




    
