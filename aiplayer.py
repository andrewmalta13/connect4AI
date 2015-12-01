import random



def miniMax(gameState, depth, minim, maxim, areWeMaximizing):
    #base case
    if depth == 0: #do we also need to check if this is a leaf
        return gameState.heuristicValue
        # return int(random.random() * 1000) - 500
    
    if areWeMaximizing:
        result = minim
        for i in range(gameState.boardWidth):
            if gameState.heights[i] < gameState.boardHeight:
                newState = gameState.getState(i)
                temp = miniMax(newState, depth - 1, result, maxim, (not areWeMaximizing))
                if temp > result:
                    result = temp
                if result > maxim:
                    return maxim
        return result
    else:
        result = maxim
        for i in range(gameState.boardWidth):
            if gameState.heights[i] < gameState.boardHeight:
                newState = gameState.getState(i)
                # print newState
                temp = miniMax(newState, depth - 1, minim, result, (not areWeMaximizing))
                if temp < result:
                    result = temp
                if result < minim:
                    return minim
        return result

class AiPlayer(object):
    def __init__(self, depthToSearch):
        self.depthToSearch = depthToSearch

    def makeMove(self, gameState):
        moveVals = [float("-inf")] * gameState.boardWidth
        for i in range(gameState.boardWidth):
            if gameState.heights[i] < gameState.boardHeight:
                moveVals[i] = miniMax(gameState.getState(i), self.depthToSearch - 1, float("-inf"), float("inf"), False)

        return moveVals.index(max(moveVals))
