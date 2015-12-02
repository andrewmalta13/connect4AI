import random
import gameHeuristic


def miniMax(gameState, depth, minim, maxim, areWeMaximizing):
    #base case
    if depth == 0 or gameState.checkTie() or abs(gameState.heuristicValue == gameHeuristic.WIN_VALUE):
        return gameState.heuristicValue
    
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
                temp = miniMax(newState, depth - 1, minim, result, (not areWeMaximizing))
                if temp < result:
                    result = temp
                if result < minim:
                    return minim
        return result

def breakTies(gameState, moveVals):
    maxVal = max(moveVals)
    possibleChoices = []
    for i in range(len(moveVals)):
        if (moveVals[i] == maxVal) and (gameState.heights[i] < gameState.boardHeight):
            #if this move results in a win. Take it
            newState = gameState.getState(i)
            if newState.heuristicValue == gameHeuristic.WIN_VALUE:
                return i

            for j in range(len(moveVals)):
                if (newState.heights[j] < newState.boardHeight 
                    and abs(newState.getState(j).heuristicValue) != gameHeuristic.WIN_VALUE):
                    possibleChoices.append(i)
  
    if possibleChoices == []:
        possibleChoices = [i for i in range(len(moveVals)) if moveVals[i] != float("-inf")]

    return possibleChoices[int(random.random() * len(possibleChoices))]


class AiPlayer(object):
    def __init__(self, depthToSearch, debug):
        self.depthToSearch = depthToSearch
        self.debug = debug

    def makeMove(self, gameState):
        moveVals = [float("-inf")] * gameState.boardWidth
        for i in range(gameState.boardWidth):
            if gameState.heights[i] < gameState.boardHeight:
                moveVals[i] = miniMax(gameState.getState(i), self.depthToSearch - 1, float("-inf"), float("inf"), False)
        
        choice = breakTies(gameState, moveVals)
        if self.debug:
            print moveVals
            print "Chose %d" % choice
        
        return choice
        
