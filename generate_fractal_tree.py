from turtle import *
from math import sqrt,cos
import numpy as np

# Initialize the singletons object of the TurtleScreen subclass
screen = Screen()
turtle = Turtle()
screen.tracer(False)
# Set the color palette to take rgb colors
screen.colormode(255)

#TODO: Background gradient colors

# The color of the top of the image
color_top = (154,0,254)
# color_top =(0,161,255)
# The color of the bottom of the image 
color_bottom = (255,228,122)
# color_bottom = (0,255,143)
# Get width and height of the windows
width_screen,height_screen = screen.window_width(), screen.window_height()
# For each value of primary color we compute the color in the middle of the screen
deltas = [(element-color_top[index])/height_screen for index,element in enumerate(color_bottom)]
# Set the color of the screen in color_top
turtle.color(color_top)
# Pull the pen up
turtle.penup()
# Move the turtle to the point (x,y)
turtle.goto(-width_screen/2,width_screen/2)
# Pull the pen down
turtle.pendown()
direction = 1

# Create an array between two values
array = np.arange(height_screen//2,-height_screen//2,-1,dtype=int)
# Create a color gradient
for distance,y in enumerate(array):
    turtle.forward(width_screen * direction)
    #print(tuple([int(color_top[i] + delta * distance) for i, delta in enumerate(deltas)]))
    turtle.color(tuple([int(color_top[i] + delta * distance) for i, delta in enumerate(deltas)]))
    turtle.sety(y)
    direction *= -1
# Pull the pen up
turtle.penup()

#TODO: Draw a pythagoras tree (fractal)

# Move the turtle to the center of the image
turtle.goto(0,0)
# Position the turtle at 90 degrees
turtle.left(90)
depthTree = 10
#COLOR SCHEME 1
tree_color_start = (0,255,143)
tree_color_end =  (0,161,255)

#tree_color_start =  (154,0,254)
#tree_color_end = (255,228,122)

# Create a reccrusive function allowing to generate the pythagoras tree
def reccursive_pythagoras_tree(turtle_sing,size,level,angle):
    
    if(level < 1):
        return
    else:
        r1 = tree_color_start[0]
        r2 = tree_color_end[0]
        g1 = tree_color_start[1]
        g2 = tree_color_end[1]
        b1 = tree_color_start[2]
        b2 = tree_color_end[2]
        if(r1 >= r2):
            new_red = abs(r1 - (depthTree - level) * abs((r1 - r2)) // depthTree)
        else:
            new_red = abs(r1 + (depthTree - level) * abs((r1 - r2)) // depthTree)
        if(b1 >= b2):
            new_blue = abs(b1 - (depthTree - level) * abs((b1 - b2)) // depthTree)
            
        else:
            new_blue = abs(b1 + (depthTree - level) * abs((b1 - b2)) // depthTree)
        if(g1 >= g2):
            new_green = abs(g1 - (depthTree - level) * abs((g1 - g2)) // depthTree)
        else:
            new_green = abs(g1 + (depthTree - level) * abs((g1 - g2)) // depthTree)

        if(level == depthTree):
            turtle.color(tree_color_start)
        else:
            turtle.color(new_red, new_green, new_blue)
        # # Draw a square where each side are equal to size
        

        turtle_sing.begin_fill()
        for i in range(4):
            turtle_sing.forward(size)
            turtle_sing.left(90)
        turtle_sing.end_fill()
        # Initialize the position of the turtle for the left branch
        turtle_sing.forward(size)
        X2,Y2 = (float(round(turtle_sing.pos()[0])) ,float(round(turtle_sing.pos()[1])))
        turtle_sing.left(90)
        turtle_sing.forward(size)
        X1,Y1 = (float(round(turtle_sing.pos()[0])) ,float(round(turtle_sing.pos()[1])))
        turtle_sing.right(180-angle)
        d = sqrt((X1-X2)**2+(Y1-Y2)**2)*cos(angle*np.pi/180)**2
        leftSize = d/cos(angle*np.pi/180)
        turtle_sing.forward(leftSize)
        turtle_sing.left(90)
        turtle_pos = turtle.pos()
        turtle_heading = turtle.heading()
        # Call the function to compute the left branch
        reccursive_pythagoras_tree(turtle_sing,leftSize,level-1,angle)
        turtle.goto(turtle_pos[0],turtle_pos[1])
        turtle.seth(turtle_heading)
        # Initialize the position of the turtle for the right branch
        turtle_sing.left(90)
        turtle_sing.forward(leftSize)
        turtle_sing.left(180-angle)
        turtle_sing.forward(size)
        rightSize = sqrt((turtle.pos()[0]-turtle_pos[0])**2 + (turtle.pos()[1]-turtle_pos[1])**2)
      
        turtle_sing.left(angle)
        # Call the function to compute the right branch
        reccursive_pythagoras_tree(turtle_sing,rightSize,level-1,angle)

# Choose the depth of the tree
depthTree = 10
# Choose the angle formed by the left square and the center square
angle = 50
# Call the reccursive function
reccursive_pythagoras_tree(turtle,70,depthTree,angle)
screen.tracer(True)
screen.exitonclick()
