import sys
turn = 'X'

boardDict = {
            'A1': ' ', 'A2': ' ', 'A3': ' ',
            'B1': ' ', 'B2': ' ', 'B3': ' ',
            'C1': ' ', 'C2': ' ', 'C3': ' '
            }



def updateScanners():
    global columnOneScan
    global columnTwoScan
    global columnThreeScan
    global rowOneScan
    global rowTwoScan
    global rowThreeScan
    global diagonalOneScan
    global diagonalTwoScan
    columnOneScan = [boardDict['A1'], boardDict['B1'], boardDict['C1']]
    columnTwoScan = [boardDict['A2'], boardDict['B2'], boardDict['C2']]
    columnThreeScan = [boardDict['A3'], boardDict['B3'], boardDict['C3']]
    rowOneScan = [boardDict['A1'], boardDict['A2'], boardDict['A3']]
    rowTwoScan = [boardDict['B1'], boardDict['B2'], boardDict['B3']]
    rowThreeScan = [boardDict['C1'], boardDict['C2'], boardDict['C3']]
    diagonalOneScan = [boardDict['A1'], boardDict['B2'], boardDict['C3']]
    diagonalTwoScan = [boardDict['A3'], boardDict['B2'], boardDict['C1']]

def boardPrint(board):
    print('   1 2 3')
    print('A |' + board['A1'] + '|' + board['A2'] + '|' + board['A3'] + '|')
    print('  -------')
    print('B |' + board['B1'] + '|' + board['B2'] + '|' + board['B3'] + '|')
    print('  -------')
    print('C |' + board['C1'] + '|' + board['C2'] + '|' + board['C3'] + '|')

def checkRow(row): 
  
    win = True
    # Comparing each element with first item  
    for point in row: 
        if turn != point: 
            win = False
            break
    
    return win

def validPoint(pnt):
    valid = False
    valids = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    for val in valids:
        if pnt == val:
            if boardDict[pnt] == ' ':
                valid = True
                break
    return valid

boardPrint(boardDict)

while True:
    while True:
        point = str(input("Choose your point, " + turn + " | Format (A1,B2,C3): "))
        if validPoint(point):
            boardDict[point] = str(turn)
            boardPrint(boardDict)
            updateScanners()
        else:
            print("That point is already taken and/or is not valid.")
            continue

        if checkRow(columnOneScan):
            print(turn + ' wins!')
            break
        elif checkRow(columnTwoScan):
            print(turn + ' wins!')
            break
        elif checkRow(columnThreeScan):
            print(turn + ' wins!')
            break
        elif checkRow(rowOneScan):
            print(turn + ' wins!')
            break
        elif checkRow(rowTwoScan):
            print(turn + ' wins!')
            break
        elif checkRow(rowThreeScan):
            print(turn + ' wins!')
            break
        elif checkRow(diagonalOneScan):
            print(turn + ' wins!')
            break
        elif checkRow(diagonalTwoScan):
            print(turn + ' wins!')
            break
    
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    
    playAgain = input("Want to play again? | Respond with Y/N: ")
    if playAgain.lower() == 'y':
        boardDict = {
            'A1': ' ', 'A2': ' ', 'A3': ' ',
            'B1': ' ', 'B2': ' ', 'B3': ' ',
            'C1': ' ', 'C2': ' ', 'C3': ' '
            }

        continue
    else:
        sys.exit()
