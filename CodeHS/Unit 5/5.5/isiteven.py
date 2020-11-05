SENTINEL = 0

def is_even(num):
    num = num%2 == 0
    if num == True:
        print('Even')
        return
    if num == False:
        print('Odd')
        return

while True:
    user = int(input("Enter a number"))
    if user == SENTINEL:
        print('Done!')
        break
    is_even(user)
