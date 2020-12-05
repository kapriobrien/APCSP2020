numList = []
for num in range(5):
    num = int(input('Number: '))
    numList.append(num)
    print(numList)
    
sumNum = sum(numList)
print('Sum: ' + str(sumNum))
