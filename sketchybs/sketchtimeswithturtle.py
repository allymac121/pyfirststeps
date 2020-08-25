#import turtle
import turtle

#set the main variables
lineLength = 0
angle = 0
penColour = "black"

#ask the users inputs for thier imagined sketch
lineLength = int(input("How long would you like the lines? "))
angle = int(input("what angle would you like the sketch to take?(0-360) "))
penColour = input("what color would you like to sketch in ? ")

#make the drawing

while lineLength != 0:

    turtle.color(penColour)
    turtle.forward(lineLength)
    turtle.right(angle)
    
    lineLength = int(input("How long would you like to make the line? (specify 0 to stop drawing) " ))

    if lineLength != 0 :
        penColor = input("What pen color would you like to use? (black, blue, red, green): ")
        angle = int(input("What angle would you like? (0-360): "))

print("Maestro as always!")
