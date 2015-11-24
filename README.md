gameState Spec

The gamestate class has the following attributes:

	board
		The board is an array that represents the board. Possible values are E if the spot is empty, or the player number that     placed a token there
	heights
		A list of values representing the last played token in each column
	numTokens
		total number of tokens currently on the board
	turn
		the player number whose turn it is (1 or 2)
	heuristicValue
		the value assigned to this game state by the heuristic function. Currently will always be zero, not yet implemented

And the following methods:

	insert(colNum)
		Inserts a token in the specified column, and then checks if the game has ended. Returns 0 for a completion, negative       with an error, or postive if the game has ended.

	checkWin([colNum,rowNum])
		Checks if there is a winning pattern that uses the specified token.

	setValue(value)
		Sets the heuristic value of the game state


A game can be played by running "python gameMaster.py"

