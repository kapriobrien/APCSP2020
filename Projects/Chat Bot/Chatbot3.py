print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder3 = int(input("3:"))
remainder5 = int(input("5:"))
remainder7 = int(input("7:"))

# reading all remainders
age = int((remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105)

print("Your age is" + str(age) + "; that's a good time to start programming!")
