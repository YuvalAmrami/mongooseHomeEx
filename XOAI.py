def isOpen(board,rowNum,lineNum):
    if(board[rowNum][lineNum] == 0):
        return True
    else:
        return False

def updateboardAIInfo(RowNum,LineNum,playerOrAi, rows, lines, diagonals): # player is -1 Ai is +1
    print("updateboardAIInfo: ", playerOrAi)
    rows[RowNum] = rows[RowNum] + playerOrAi
    lines[LineNum] = lines[LineNum] + playerOrAi
    if (RowNum == LineNum): # left diagonal
        diagonals[0] = diagonals[0] + playerOrAi
    if(RowNum +LineNum ==2): # right diagonal
        diagonals[1] = diagonals[1] + playerOrAi

def calculateStep(board, rows, lines, diagonals): #    return AIRow, AILine
    print("calculateStep: ")
    # wining next round
    for idx, diagonal in enumerate(diagonals):
        if (diagonal >=2):
            return findEmptyPointOnDgnl(board,idx)
    for idx, row in enumerate(rows):
        if (row >=2):
            return idx, findEmptyLine(board,idx)
    for idx, line in enumerate(lines):
        if (line >=2):
            return findEmptyRow(board,idx) ,idx
    print("calculateStep no win")
    # prevent player's Win:
    for idx, diagonal in enumerate(diagonals):
        if (diagonal <=-2):
            return findEmptyPointOnDgnl(board,idx)
    for idx, row in enumerate(rows):
        if (row <=-2):
            return idx, findEmptyLine(board,idx)
    for idx, line in enumerate(lines):
        if (line <=-2):
            return findEmptyRow(board,idx) ,idx
        print("calculateStep no lose")
    # normal play naive approach: center, corners, and finally sides
    if isOpen(board,1,1):
        print("center")

        return 1,1
    else:
        row, line = findEmptyCorner(board)
        if (row<0 or line<0):
            row, line = findEmptySides(board)
        

def findEmptyPointOnDgnl(board, idx):
    if (idx ==0):
        if isOpen(board,0,0):
            return 0,0
        elif isOpen(board,1,1):
            return 1,1
        else: #if isOpen(board,2,2)  - unless the board is already a losing board.
            return 2,2
    else:
        if isOpen(board,0,2):
            return 0,2
        elif isOpen(board,1,1):
            return 1,1
        else: #if isOpen(board,2,0)  - unless the board is already a losing board.
            return 2,0

def findEmptyLine(board,idx):
    for i in range(len(board[0])):
        if isOpen(board,idx,i):
            return i
    return -1

def findEmptyRow(board,idx):
    for i in range(len(board)):
        if isOpen(board,i,idx):
            return i
    return -1

def findEmptyCorner(board):
    if isOpen(board,0,0):
        return 0,0
    elif isOpen(board,0,2):
        return 0,2
    elif isOpen(board,2,0):
        return 2,0
    elif isOpen(board,2,2):
        return 2,2
    else:
        return -1, -1

def findEmptySides(board):
    if isOpen(board,0,1):
        return 0,1
    elif isOpen(board,1,0):
        return 1,0
    elif isOpen(board,1,2):
        return 1,2
    elif isOpen(board,2,1):
        return 2,1
    else:
        return -1, -1   


def playRound(board, playerInput, rows, lines, diagonals):
    rowNum = int(playerInput[0])
    lineNum = int(playerInput[1])
    print(rowNum, lineNum)
    if isOpen(board, rowNum,lineNum):
        print(isOpen)
        board[rowNum][lineNum] = -1
        printBoard(board)
        updateboardAIInfo(rowNum,lineNum ,-1, rows, lines, diagonals) 
        AIRow, AILine = calculateStep(board, rows, lines, diagonals)
        if (AIRow>=0 and AILine>=0):
            board[AIRow][AILine] = 1
            updateboardAIInfo(rowNum,lineNum ,1, rows, lines, diagonals)
            printBoard(board)
            return 1
        else:
            print("no more steps to play")
            printBoard(board)
            return 0
    else:
        print("input error")
        return -1
    
def printBoard(board):
    for row in board:
        print(row)



board = [[0,0,0]]*3
rows = [0,0,0]
lines = [0,0,0]
diagonals = [0,0]

printBoard(board)
playerMove = input("Enter your next move (row,line): ").split(",")
# print("playerMove",playerMove)
# playerInput = map(lambda num : int(num),playerMove)
# print(playerMove,playerInput)
while (playRound(board, playerMove, rows, lines, diagonals)!=0):
    playerMove = input("Enter your next move (row,line): ").split(",")
