import time

def fib_sequence():
    cur_number = 1
    past_number = 1
    print(cur_number)
    print(cur_number)
    while cur_number < max_num:
        fib_number = cur_number + past_number
        print(fib_number)
        past_number = cur_number
        cur_number = fib_number

def printing():
    print("Generating...")
    if max_num <= 1000:
        time.sleep(1)
        fib_sequence()
    elif max_num <= 10000:
        time.sleep(3)
        fib_sequence()
    else:
        time.sleep(5)
        fib_sequence()
    print("Completed!")

print("Completed!")
print("Welcome to the Fibonacci Sequence Generator!")
print("Let's begin: What number do you want to go up to?")
max_num = int(input())

printing()