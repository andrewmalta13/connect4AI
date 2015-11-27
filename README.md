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


gameTree.py

A gameTree has the following attributes:

	position 
		the index in the dictionary where the current position is located

	boardwidth 
		currently constant, may change later if we implement that
	tree 
		the game tree. Contains all of the states accessed by getState. A state can be accessed by gameTree.tree[position]

And the following methods:

	getState(colNum)
		checks the existence of the state (or creates the state) that starts at the current position and then has an insert in the column colNum. Returns the postion in the tree where the newly created state can be found. DOES NOT UPDATE THE CURRENT POSITION OF THE TREE

	getPositionNum(curPos,colNum)
		Given a position and a column number, will generate the position for that state. Just returns the integer, does nothing else.
