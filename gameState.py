import operator
import os
PLAYERONE=1
PLAYERTWO=-1
NUMPLAYERS=2
CHECKARRAY=[[1,-1],[0,-1],[-1,-1],[-1,0]]

class gameState:

  def __init__(self,w,h):
    self.boardWidth = w
    self.boardHeight = h
    self.board = [['E' for i in range(self.boardHeight)] for j in range(self.boardWidth)]
    self.heights = [0] * self.boardWidth
    self.numTokens = 0
    self.turn = PLAYERONE
    self.winCode = 0
  def __str__(self):
    retString = "\n\n\t"
    for i in range(0 , self.boardWidth):
      retString += " " + str(i) + " "
    retString += "\n\t"
    retString += "-" * self.boardWidth * 3
    retString += '\n\t'
    for i in range(0,self.boardHeight)[::-1]:
      for j in range(0,self.boardWidth):
        val = self.board[j][i]
        val = val if val == 1 or val == 'E' else 2
        retString += " " + str(val) + " "
      retString += "\n\n\t"
    retString += '\n'
    os.system('cls' if os.name == 'nt' else 'clear')
    return retString
  # returns 0 for success, the playernum of the winner, or a negative for an error
  def insert(self,colNum):
    if not isinstance( colNum, int ) or colNum > self.boardWidth:
      print "Invalid column number"
      return -1
    if self.heights[colNum] == self.boardHeight:
      print "That column is full"
      return -1
    rowNum = self.heights[colNum] 
    self.board[colNum][self.heights[colNum]] = self.turn
    self.heights[colNum] += 1
    self.numTokens += 1;
    
    if self.numTokens >= self.boardWidth * self.boardHeight:
      return NUMPLAYERS + 1


    winVal = self.checkWin([colNum,rowNum])
    self.turn = PLAYERTWO if self.turn == PLAYERONE else PLAYERONE

    return winVal

  def checkWin(self,checkPosition):

    for adjustPair in CHECKARRAY:
      counter = 0
      currentPosition = map(operator.add,checkPosition,map(operator.mul,adjustPair,[-3,-3]))
      
      for val in range(7):
        if currentPosition[0] < 0 or currentPosition[0] >= self.boardWidth or currentPosition[1] < 0 or currentPosition[1] >= self.boardHeight:
          currentPosition = map(operator.add,currentPosition,adjustPair)
          continue
        else:
          if self.board[currentPosition[0]][currentPosition[1]] == self.board[checkPosition[0]][checkPosition[1]]:
            counter += 1
          else:
            counter = 0;
          if counter == 4:
            self.winCode = self.turn
            return self.turn
          currentPosition = map(operator.add,currentPosition,adjustPair)
    return 0
  def setValue(self,value):
    self.heuristicValue = value

