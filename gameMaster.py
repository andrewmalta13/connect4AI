import gameState
gameOver = False

board = gameState.gameState()

if __name__ == "__main__":
  while(not gameOver):
    nextMove = None
    retVal = 0
    while(nextMove < 0):
      print board
      nextMove = input("Player " + str(board.turn) + ": Which column would you like to play a token in? ")
      if ((nextMove < len(board.heights)) and (nextMove >= 0)):
        retVal = board.insert(nextMove)
    if retVal != 0:
      gameOver = retVal
      break
  print board
  print "Game Over! Code: " + str(gameOver)