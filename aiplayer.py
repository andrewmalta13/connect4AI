import random

class AiPlayer(object):
    def __init__(self, depthToSearch):
        self.depthToSearch = depthToSearch

    def miniMax(self, gameState, depth, minim, maxim, areWeMaximizing):
        #base case
        if depth == 0: #do we also need to check if this is a leaf
            return gameState.heuristicValue
            # return int(random.random() * 1000) - 500
        
        if areWeMaximizing:
            result = minim
            for i in range(gameState.boardWidth):
                newState = gameState.getState(i)
                temp = self.miniMax(newState, depth - 1, result, maxim, (not areWeMaximizing))
                if temp > result:
                    result = temp
                if result > maxim:
                    return maxim
            return result
        else:
            result = maxim
            for i in range(gameState.boardWidth):
                newState = gameState.getState(i)
                temp = self.miniMax(newState, depth - 1, result, maxim, (not areWeMaximizing))
                if temp < result:
                    result = temp
                if result < minim:
                    return minim
            return result

    def makeMove(self, gameState):
        moveVals = [self.miniMax(gameState.getState(i), self.depthToSearch - 1, float("-inf"), float("inf"), False)
            for i in range(gameState.boardWidth)]     

        print moveVals    
        return moveVals.index(max(moveVals))
