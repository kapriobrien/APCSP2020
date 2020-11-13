def getHighestNumber(one,two, three):
    if one > two and one > three:
        return one
    elif two > one and two > three:
        return two
    elif three > one and three > two:
        return three

def run():
    print('Choose Three Numbers')
    one = int(input())
    two = int(input())
    three = int(input())

    value = getHighestNumber(one, two, three)

    print('The highest number is ' + str(value))

run()
