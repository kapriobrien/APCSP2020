# Enter your code here

def min(x,y):
    if x < y:
        return x
    if y < x:
        return y
    if x == y:
        return x

test = min(14,14)
print(test)
test = min(13,18)
print(test)
test = min(25,12)
print(test)
