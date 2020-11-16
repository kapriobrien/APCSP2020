def tower():
    for i in range(3):
        put_ball()
        move()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()

move()
turn_left()
tower()
turn_right()
move()
move()
turn_right()
for i in range(3):
    move()
turn_left()
turn_left()
tower()
turn_right()
