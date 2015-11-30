import gameState
from copy import deepcopy
from gameHeuristic import calculateHeuristic


class gameTree:
  def __init__(self,w=7,h=6):
    self.position = 0
    self.boardWidth = int(w)
    self.tree = dict()
    self.tree[0] = gameState.gameState(int(w),int(h))


  def __str__(self):
    print self.tree[self.position]
    print "Currently at position: ", self.position

  def getState(self,colNum):
    childPos = self.getPositionNum(self.position,colNum)
    if childPos not in self.tree:
      # copy current position to new variable
      newBoard = deepcopy(self.tree[self.position])

      # peform an insert
      newBoard.insert(colNum)
      # check win
      winVal = newBoard.checkWin
      newBoard.heuristicValue = calculateHeuristic(newBoard)

      ##TEMPORARY TESTING CODE#
      self.tree[childPos] = newBoard
    return childPos

  def getPositionNum(self,curPos,colNum):
    # 0 has children 1 - boardwidth, etc...
    return self.boardWidth * curPos + colNum + 1