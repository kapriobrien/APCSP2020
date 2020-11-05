# This program should draw a stop light

LIGHT_RADIUS = 25
STOPLIGHT_WIDTH = 100
STOPLIGHT_HEIGHT = 250
BUFFER = 75
middle = 200
# Implement a function that draws a single circle 
# with radius LIGHT_RADIUS.
# The circle should be in the center of the screen horizontally.
# Use the parameters for the y position and color
def draw_circle(y, color):
    circ = Circle(LIGHT_RADIUS)
    circ.set_color(color)
    circ.set_position(middle,y)
    add(circ)
    

def draw_rectangle(width,height,x,y):
    rect = Rectangle(width,height)
    rect.set_position(x,y)
    rect.set_color(Color.gray)
    add(rect)
    
draw_rectangle(STOPLIGHT_WIDTH,STOPLIGHT_HEIGHT,150,150)

draw_circle(200,Color.red)
draw_circle(275,Color.yellow)
draw_circle(350,Color.green)
