import sys

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
    point = turn
    # Comparing each element with first item  
    for point in row: 
        if turn != point: 
            win = False
            break
    
    return win

boardPrint(boardDict)

for playerTurn in range(10):
    if (playerTurn + 1)%2 == 0:
        turn = 'O'
    else:
        turn = 'X'
    point = str(input("Choose your point, " + turn + " | Format (A1,B2,C3): "))
    if boardDict[point] == ' ':
            boardDict[point] = str(turn)
            boardPrint(boardDict)
            updateScanners()
    else:
        print("That point is already taken. Turn Skipped")

    if checkRow(columnOneScan):
        print(turn + ' wins!')
        sys.exit()
    elif checkRow(columnTwoScan):
        print(turn + ' wins!')
        sys.exit()
    elif checkRow(columnThreeScan):
        print(turn + ' wins!')
        sys.exit()
    elif checkRow(rowOneScan):
        print(turn + ' wins!')
        sys.exit()
    elif checkRow(rowTwoScan):
        print(turn + ' wins!')
        sys.exit()
    elif checkRow(rowThreeScan):
        print(turn + ' wins!')
        sys.exit()
    elif checkRow(diagonalOneScan):
        print(turn + ' wins!')
        sys.exit()
    elif checkRow(diagonalTwoScan):
        print(turn + ' wins!')
        sys.exit()


    
