import operator
import os

PLAYERONE=1
PLAYERTWO=2
NUMPLAYERS=2
BOARDWIDTH=7
BOARDHEIGHT=6
WIDTHFlag=0
HEIGHTFLAG=1
CHECKARRAY=[[1,-1],[0,-1],[-1,-1],[-1,0]]

class gameState:

  def __init__(self):
    self.board = [['E' for i in range(BOARDHEIGHT)] for j in range(BOARDWIDTH)]
    self.heights = [0] * BOARDWIDTH
    self.numTokens = 0
    self.turn = PLAYERONE
    self.heuristicValue = 0 #PLACEHOLDER VALUE
    self.winCode = 0
  def __str__(self):
    retString = "\n\n\t"
    for i in range(0 , BOARDWIDTH):
      retString += " " + str(i) + " "
    retString += "\n\t"
    retString += "-" * BOARDWIDTH * 3
    retString += '\n\t'
    for i in range(0,BOARDHEIGHT)[::-1]:
      for j in range(0,BOARDWIDTH):
        retString += " " + str(self.board[j][i]) + " "
      retString += "\n\n\t"
    retString += '\n'
    os.system('cls' if os.name == 'nt' else 'clear')
    return retString
  # returns 0 for success, the playernum of the winner, or a negative for an error
  def insert(self,colNum):
    if not isinstance( colNum, int ) or colNum > BOARDWIDTH:
      print "Invalid column number"
      return -1
    if self.heights[colNum] == BOARDHEIGHT:
      print "That column is full"
      return -1
    rowNum = self.heights[colNum] 
    self.board[colNum][self.heights[colNum]] = self.turn
    self.heights[colNum] += 1
    self.numTokens += 1;
    
    if self.numTokens >= BOARDWIDTH * BOARDHEIGHT:
      return NUMPLAYERS + 1


    winVal = self.checkWin([colNum,rowNum])
    self.turn = PLAYERTWO if self.turn == PLAYERONE else PLAYERONE

    return winVal

  def checkWin(self,checkPosition):

    for adjustPair in CHECKARRAY:
      counter = 0
      currentPosition = map(operator.add,checkPosition,map(operator.mul,adjustPair,[-3,-3]))
      
      for val in range(7):
        if currentPosition[0] < 0 or currentPosition[0] >= BOARDWIDTH or currentPosition[1] < 0 or currentPosition[1] >= BOARDHEIGHT:
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

