#Example: How to import images to the Python-turtle code
#You can import to the Python turtle library image-files with
#an extension .gif ONLY.
# All images have to be located in the directory with a main
#executable file 

import turtle
wn=turtle.Screen()
wn.screensize(1300,1000)
wn.bgcolor('navy')
wn.bgpic("aquarium.gif") # image for background

image1 = ("fish1.gif") #specify image for a turtle object
image2 = ("fish2.gif") #specify image for a turtle object

wn.addshape(image1) #add turtle shape as an image
wn.addshape(image2) #add turtle shape as an image

fish=turtle.Turtle()
fish.shape(image1) # name for turtle object
fish.up()
fish.hideturtle()
fish.goto(-400,-250)
fish.showturtle()
fish.speed(0)

for i in range(800):
    fish.fd(1)
    
fish.lt(90)
fish.shape(image2) # name for turtle object
for i in range(500):
    fish.fd(1)



        

