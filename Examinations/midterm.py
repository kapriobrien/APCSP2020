rowOne = ['|',' ', "|",' ','|',' ','|' ]
rowTwo = ['|',' ', "|",' ','|',' ','|' ]
rowThree = ['|',' ', "|",' ','|',' ','|' ]
columnOneScan = [rowOne[1],rowTwo[1],rowThree[1]]
columnTwoScan = [rowOne[3],rowTwo[3],rowThree[3]]
columnThreeScan = [rowOne[5],rowTwo[5],rowThree[5]]
rowOneScan = [rowOne[1],rowOne[3],rowOne[5]]
rowTwoScan = [rowTwo[1],rowTwo[3],rowTwo[5]]
rowThreeScan = [rowThree[1],rowThree[3],rowThree[5]]
diagonalOneScan = [rowOne[1],rowTwo[3],rowThree[5]]
diagonalTwoScan = [rowOne[5],rowTwo[3],rowThree[1]]



while True:
    if turn == O:
        if point == ('A',1) and rowOne[1] == ' ':
            rowOne[1] = 'X'
        elif point == ('A',2) and rowOne[3] == ' ':
            rowOne[3] = 'X'
        elif point == ('A',3) and rowOne[5] == ' ':
            rowOne[5] = 'X'
        elif point == ('B',1) and rowTwo[1] == ' ':
            rowTwo[1] = 'X'
        elif point == ('B',2) and rowTwo[3] == ' ':
            rowTwo[3] = 'X'
        elif point == ('B',3) and rowTwo[5] == ' ':
            rowTwo[5] = 'X'
        elif point == ('C',1) and rowThree[1] == ' ':
            rowThree[1] = 'X'
        elif point == ('C',2) and rowThree[3] == ' ':
            rowThree[3] = 'X'
        elif point == ('C',3) and rowThree[5] == ' ':
            rowThree[5] = 'X'
        else:
            print("Choose an unoccupied space")
            continue


    if turn == X:
        if point == ('A',1) and rowOne[1] == ' ':
            rowOne[1] = 'O'
            
        elif point == ('A',2) and rowOne[3] == ' ':
            rowOne[3] = 'O'
        elif point == ('A',3) and rowOne[5] == ' ':
            rowOne[5] = 'O'
        elif point == ('B',1) and rowTwo[1] == ' ':
            rowTwo[1] = 'O'
        elif point == ('B',2) and rowTwo[3] == ' ':
            rowTwo[3] = 'O'
        elif point == ('B',3) and rowTwo[5] == ' ':
            rowTwo[5] = 'O'
        elif point == ('C',1) and rowThree[1] == ' ':
            rowThree[1] = 'O'
        elif point == ('C',2) and rowThree[3] == ' ':
            rowThree[3] = 'O'
        elif point == ('C',3) and rowThree[5] == ' ':
            rowThree[5] = 'O'
        else:
            print("Choose an unoccupied space")
            continue

def playMove():
    global point
    global point
    point = tuple(input("Choose your point | Format ('A',2): "))



def updateGrid():
    global realGrid
    realGrid = str(rowOne) + '\n' + str(rowTwo) + '\n' + str(rowThree)

def main():
    print(grid)
    #while not checkWinner('X') or not checkWinner('O'):
    updateGrid()
    print(realGrid)

main()
