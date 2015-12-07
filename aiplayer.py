import random
import gameHeuristic


def miniMax(gameState, depth, minim, maxim, areWeMaximizing):
    #base case
    if depth == 0 or gameState.checkTie() or abs(gameState.heuristicValue) == gameHeuristic.Heuristic.winVal:
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

class AiPlayer(object):
    def __init__(self, depthToSearch, debug, explain, playerNumber):
        self.depthToSearch = depthToSearch
        self.debug = debug
        self.explain = explain
        self.playerNumber = playerNumber

    def makeMove(self, gameState):
        moveVals = [float("-inf")] * gameState.boardWidth
        for i in range(gameState.boardWidth):
            if gameState.heights[i] < gameState.boardHeight:
                moveVals[i] = miniMax(gameState.getState(i), self.depthToSearch - 1, float("-inf"), float("inf"), False)

        choice = Choice(gameState, moveVals, self.explain, self.playerNumber)
        choice.breakTies()

        if self.debug:
            print moveVals
            print "Chose %d" % choice.decision

        if self.explain:
            print choice.explanation

        return choice.decision


class Choice(object):
    def __init__(self, gameState, miniMaxArray, explain, playerNumber):
        self.gameState = gameState
        self.miniMaxArray = miniMaxArray
        self.explain = explain
        self.playerNumber = playerNumber

    def breakTies(self):
        maxVal = max(self.miniMaxArray)
        possibleChoices = []

        for i in range(len(self.miniMaxArray)):
            if (self.miniMaxArray[i] == maxVal) and (self.gameState.heights[i] < self.gameState.boardHeight):
                #if this move results in a win. Take it
                newState = self.gameState.getState(i)
                if newState.heuristicValue == gameHeuristic.Heuristic.winVal:
                    if (self.explain):
                        self.explanation = newState.heuristic.explain(self.playerNumber, True, "I chose this state because it is a")
                    self.decision = i
                    return

                for j in range(len(self.miniMaxArray)):
                    if (newState.heights[j] < newState.boardHeight 
                        and abs(newState.getState(j).heuristicValue) != gameHeuristic.Heuristic.winVal):
                        possibleChoices.append(i)

        if possibleChoices == []:  #all of our best choices cant be made for some reason
            possibleChoices = [i for i in range(len(self.miniMaxArray)) if self.miniMaxArray[i] != float("-inf")]
        
        self.decision = possibleChoices[int(random.random() * len(possibleChoices))]

        if self.explain:
            decisionVal = self.gameState.getState(self.decision).heuristicValue
            prefix = "This is a"
            suffix = ""
            if (filter(lambda x: abs(x) != gameHeuristic.Heuristic.winVal,
             self.miniMaxArray[:self.decision] + self.miniMaxArray[self.decision + 1:]) == []):
                self.explanation =  "I chose this move because if I didn't you would win."
                return
            elif (decisionVal == gameHeuristic.Heuristic.winVal):
                self.explanation = "I chose this move because now there is no way for me to lose."
                return
            elif (decisionVal < 0):
                prefix = "Despite the fact that this state is"
                suffix = " However, all of my other options were worse and would either let you win or give you a better state." 
            elif (decisionVal == 0):
                prefix = "I chose this state even though it is"
                suffix = " However, I didn't have a better option to consider."

            self.explanation = self.gameState.getState(self.decision).heuristic.explain(self.playerNumber, True, prefix) + suffix


