import gameState
gameOver = False

board = gameState.gameState()

if __name__ == "__main__":
	while(not gameOver):
		nextMove = -1
		retVal = -1
		while(nextMove < 0):
			print board
			nextMove = input("Player " + str(board.turn) + ": Which column would you like to play a token in? ")
			retVal = board.insert(nextMove)
		if retVal != 0:
			gameOver = retVal
			break
	print board
	print "Game Over! Code: " + str(gameOver)