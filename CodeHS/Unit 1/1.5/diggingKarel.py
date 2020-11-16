def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def move_twice():
    move()
    move()

def move_thrice():
    move()
    move()
    move()
    
def dig_in():
    turn_right()
    move()
    move()
    move()
    put_ball()
    turn_around()
    move()
    move()
    move()
    turn_right()
    
move_twice()
dig_in()

move_thrice()
dig_in()

move_thrice()
dig_in()

move()
