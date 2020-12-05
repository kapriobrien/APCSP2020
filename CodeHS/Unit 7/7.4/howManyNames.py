def nameSplitter():
    userNumber = int(input("How many names do you have?: "))
    #userName = str.split(userInput)
    nameList = []
    for name in range(userNumber):
        nameInput = input('Name: ')
        nameList.append(str(nameInput))
    reverseNames = nameList[::-1]
    lastName = reverseNames[0]
    middleNames = nameList[1:userNumber-1]

    print('First name: ' + str(nameList[0]))
    print('Middle names: ' + str(middleNames))
    print('Last name: ' + str(lastName))
       
nameSplitter()
