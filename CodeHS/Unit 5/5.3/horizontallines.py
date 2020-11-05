# Write a function to draw a horizontal
# line given a y position and a length


def horizontal_line(y,length):
    line = Line(0,y,length,y)
    add(line)

horizontal_line(100,400)

horizontal_line(200,400)

horizontal_line(300,400)
