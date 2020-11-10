# All you have to do in this exercise is write a good comment that explains
# what local variables are. You should also give an example of a function
# and what the local variables are, and what the scope is of the variable.

#This is a function
def Function():
    x = "Local" #This is a local variable
    print(x)
x = "Global" #This is a global variable

Function()
print(x)

#The local variable isn't equal to the gloval variable because of scope
