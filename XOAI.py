
bord = [0,0,0]*3
rows = [0,0,0]
lines = [0,0,0]
diagonals = [0,0]


def isOpen(rowNum,lineNum):
    if(bord[rowNum][lineNum] == 0):
        return True
    else:
        return False

def updateBordAIInfo(rowNum,lineNum):
    rows[rowNum] = rows[rowNum] - 1
    lines[lineNum] = lines[lineNum] - 1
    if (rowNum == lineNum):
        diagonals[0] = diagonals[0]+1
    if(rowNum +lineNum ==2):
        diagonals[1] = diagonals[1]+1

def calculateStep():
    

def playRound(playerInput):
    rowNum = playerInput[0]
    lineNum = playerInput[1]
    if isOpen(rowNum,lineNum):
        bord[rowNum][lineNum] = -1
        updateBordAIInfo(rowNum,lineNum)
        calculateStep()
    # else throw
