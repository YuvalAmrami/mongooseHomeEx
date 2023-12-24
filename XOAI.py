def isOpen(board,rowNum,lineNum):
    if(board[rowNum][lineNum] == 0):
        return True
    else:
        return False

def updateboardAIInfo(RowNum,LineNum,playerOrAi, rows, lines, diagonals): # player is -1 Ai is +1
    rows[RowNum] = rows[RowNum] + playerOrAi
    lines[LineNum] = lines[LineNum] + playerOrAi
    if (RowNum == LineNum): # left diagonal
        diagonals[0] = diagonals[0] + playerOrAi
    if(RowNum +LineNum ==2): # right diagonal
        diagonals[1] = diagonals[1] + playerOrAi


def calculateStep(board, rows, lines, diagonals): # return AIRow, AILine
    # wining next round or prevent player's Win:
    for idx, diagonal in enumerate(diagonals):
        if (diagonal >=2 or diagonal <=-2):
            return findEmptyPointOnDgnl(board,idx)
    for idx, row in enumerate(rows):
        if (row >=2 or row <=-2):
            return idx, findEmptyLine(board,idx)
    for idx, line in enumerate(lines):
        if (line >=2 or line <=-2):
            return findEmptyRow(board,idx) ,idx
    # normal play naive approach: center, corners, and finally sides
    return strategicPlay(board,diagonals)

def findEmptyPointOnDgnl(board, idx):
    if (idx ==0):
        if isOpen(board,0,0):
            return 0,0
        elif isOpen(board,1,1):
            return 1,1
        elif isOpen(board,2,2):
            return 2,2
        else:  # the board is already finished
            return -1,-1
    else:
        if isOpen(board,0,2):
            return 0,2
        elif isOpen(board,1,1):
            return 1,1
        elif isOpen(board,2,0):
            return 2,0
        else:  # the board is already finished
            return -1,-1

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
    # print ('findEmptyCorner')
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

def findEmptySide(board):
    if isOpen(board,0,1):
        return 0,1
    elif isOpen(board,1,0):
        return 1,0
    elif isOpen(board,1,2):
        return 1,2
    elif isOpen(board,2,1):
        return 2,1
    else:
        return -1,-1   

def normalPlay(board): #naive approach
    if isOpen(board,1,1):
        print("center")
        return 1,1
    else:
        print("Corner")
        row, line = findEmptyCorner(board)
        if (row<0 or line<0):
            print("Side")
            row, line = findEmptySide(board)
        return row, line

def strategicPlay(board,diagonals): #smarter approach - dealing with the specific strategy of 3 corners conquer
    if isOpen(board,1,1):
        print("center")
        return 1,1
    else:
        if (diagonals[0]<0 and board[0][0]==-1 and board[2][2]==-1): 
            # I want to deal with the first time only so theoretically, I should have more restrictions but because of the small board in this game,
            # the restrictions of winning and not losing will prevent the game from entering here again. 
           return findEmptySide(board)
        elif (diagonals[1]<0 and board[0][2]==-1 and board[2][0]==-1):
           return findEmptySide(board)
        else:
            return normalPlay(board)


def playRound(board, playerInput, rows, lines, diagonals):
    rowNum = int(playerInput[0])
    lineNum = int(playerInput[1])
    if isOpen(board, rowNum,lineNum):
        print(isOpen)
        board[rowNum][lineNum] = -1
        printBoard(board)
        updateboardAIInfo(rowNum,lineNum ,-1, rows, lines, diagonals) 
        AIRow, AILine = calculateStep(board, rows, lines, diagonals)
        print("AIRow, AILine ", AIRow, AILine)
        if (AIRow>=0 and AILine>=0):
            board[AIRow][AILine] = 1
            updateboardAIInfo(AIRow,AILine ,1, rows, lines, diagonals)
            printBoard(board)
            return 1
        else:
            printBoard(board)
            return 0
    else:
        print("input error")
        return -1
    
def printBoard(board):
    for row in board:
        print(row)

def gameEnded(rows, lines, diagonals):
    for diagonal in diagonals:
        if (diagonal >=3 or diagonal <=-3):
            return True
    for row in rows:
        if (row >=3 or row <=-3):
            return True
    for line in lines:
        if (line >=3 or line <=-3):
            return True
    else:
        return False


board = [[0,0,0],[0,0,0],[0,0,0]]
rows = [0,0,0]
lines = [0,0,0]
diagonals = [0,0]

printBoard(board)
playerMove = input("Enter your next move (row,line): ").split(",")

while (playRound(board, playerMove, rows, lines, diagonals)!=0 and not gameEnded(rows, lines, diagonals) ):
    playerMove = input("Enter your next move (row,line): ").split(",")
print("game ended")