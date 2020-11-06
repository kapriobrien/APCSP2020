print("Welcome to the Factorial Calculator!")
user_num = int(input("What number would you like to create a factorial for?: "))

subtractor = 1

factorial_num = user_num
subtracted = user_num
#for n in range(1, user_num + 1):
#    subtractor = subtractor*n  
#print(str(subtractor))

for i in range(user_num + 1):
    factorial_num = factorial_num * (subtracted - 1)
    subtracted = subtracted - 1
print(factorial_num)
