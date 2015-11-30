import random

class AiPlayer(object):
    def __init__(self, depthToSearch, gameTree):
        self.depthToSearch = depthToSearch
        self.miniMaxTree = gameTree

    def miniMax(self, state, depth, minim, maxim, areWeMaximizing):
        #base case
        if depth == 0: #do we also need to check if this is a leaf
          # return state.heuristicValue
          return int(random.random() * 1000) - 500
        
        if areWeMaximizing:
            result = minim
            for i in range(self.miniMaxTree.boardWidth):
                gamestate = self.miniMaxTree.tree[self.miniMaxTree.getState(i)]
                temp = self.miniMax(gamestate, depth - 1, result, maxim, (not areWeMaximizing))
                if temp > result:
                    result = temp
                if result > maxim:
                    return maxim
            return result
        else:
            result = maxim
            for i in range(self.miniMaxTree.boardWidth):
                gamestate = self.miniMaxTree.tree[self.miniMaxTree.getState(i)]
                temp = self.miniMax(gamestate, depth - 1, result, maxim, (not areWeMaximizing))
                if temp < result:
                    result = temp
                if result < minim:
                    return minim
            return result

    def makeMove(self):
        moveVals = [self.miniMax(self.miniMaxTree.tree[self.miniMaxTree.getState(i)],
         self.depthToSearch - 1, float("-inf"), float("inf"), False) for i in range(self.miniMaxTree.boardWidth)]     

        print moveVals    
        return moveVals.index(max(moveVals))
