import numpy as np
#make square numpy matrix of given size
def makeSquareMatrix(size):
    matrix_k = np.zeros((size,size))
    return matrix_k

#make a list of all the possible moves
def makeMoveList(size):
    moveList = []
    for i in range(size):
        for j in range(size):
            moveList.append((i,j))
    return moveList


