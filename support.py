from copy import deepcopy

def linearAddCheck(arr:list, n:tuple) -> bool:
    for colIndex,col in enumerate(arr):
        for rowIndex,row in enumerate(col):
            if colIndex == n[0] and rowIndex == n[1]:
                if row == 0:
                    return True
    return False

def linearCheck(arr: list, n) -> bool:
    for col in arr:
        for row in col:
            if row == n:
                return True
    return False

def linearCompressCheck(board:list, direction:str):
    invertedBoard = deepcopy(board)[::-1]
    for col in board:
        for row in col:
            if row != 0:
                
