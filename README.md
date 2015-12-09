# connect4AI

A project for Yale University CPSC 458 - Automated Decision Systems by [Andrew Malta](https://github.com/andrewmalta13), [Julian Rosenblum](https://julianrosenblum.com), and [Ted Tuckman](https://github.com/TedTuckman).

## Introduction

Our goal was to create an AI for the popular board game [Connect Four](https://en.wikipedia.org/wiki/Connect_Four) that could beat most human players but also make and explain its decisions in a way that humans can understand.  We accomplished this by creating a goal-based system that employs a version of the [Minimax](https://en.wikipedia.org/wiki/Minimax) algorithm to make decisions.

## Running the Program
(TBD)

## The Minimax Algorithm
Someone playing a turn based game is often as good as how many moves the can look ahead, maximizing their postion in the game while
minimizing the oppenent's.  Connect 4 is a zero sum game, meaning a good state for player 1 is neccesarily a bad state for player 2. 
This fact makes minimax a fantastic algorithm for deciding which move is best, looking multiple moves beyond the current move.  That
being said, connect 4's branching factor of the game tree (on a regular board) makes it computationally infeasible to explore more than
5 to 7 moves ahead. While exploring 5 to 7 moves ahead is somewhat quick, we decided to implement Alpha-Beta pruning in our implemenation of Mini-Max to not explore moves that we would never take given our current options.  The Mini-Max algorithm is especially good at
trapping opponents in losing states, but it relies heavily on the heursitic function to get it into favorable states in the earlier
stages of the game.

## The Heuristic Function
If computing power were an unlimited resource, the Minimax algorithm would only need to know if a particular state is a win-state for some player to calculate the steps for optimal play by traversing the entire game tree.  However, in practice, traversing the entire game tree is too slow and less consistent with how humans make decisions.  Instead, we decided there needs to be a more mature way of calculating the value of a particular non-win state for a player.  Since the end goal of the system is to create a run of four, we decided to award value for reaching intermediate goals of runs of two or three.  We defined a run of `n` to be any column with `n` tokens of a particular player on top, or any horizontal or diagonal cluster of four spaces with `n` tokens of a particular player and the rest of the spaces empty.  In other words, a run of `n` is a unique group of four that could eventually become a win for a particular player and currently has `n` of that player's tokens.  If there are multiple groups of four for a particular `n` tokens where this is the case, they are counted as multiple runs.  This strategy takes into account the increased benefit of having "open" runs.  We assigned the value of a run of three to be twice that of a run of two.  The heuristic value for a particular player is then equal to the value of his/her runs minus the value of his/her opponent's runs.  This heuristic function allows us to make more explainable decisions and not have to traverse as much of the game tree.

## Human-like Considerations in Decision Making
Even with the human-like heuristic function, Minimax still wound up making decisions that did not correspond with an intelligent human player, even though they made mathematical sense.  It turned out that humans have additional goals when it comes to Connect Four.  For example, while Minimax was indifferent between a move that would result in an immediate win and a move that would result in a definite win in a greater number of turns, most rational human players would choose the immediate win.  Thus, we had to add additional goals to our system to achieve more human-like behavior.  For example, not only do I want to win, I also want to win as quickly as possible.  Similarly, not only do I want to not lose, I particularly don't want to lose this turn.

## Explaining the Decision
We decided to make the explanation functionality come from a combination of the heuristic and Minimax functions.  We adapted the heuristic function to explain why a state is good or bad based on the runs that it used to compute the heuristic value.  We adapted the Minimax function to explain which goal was the primary factor in its decision.  Did it pick a state to achieve a win?  To avoid a loss?  Did it pick a state because it had a good heuristic value?  Did it pick a state even though it had a bad heuristic value?  We split the Minimax's explanation component into these different cases and had it use the heuristic function's explanation component to substantiate its decisions when necessary.  Thus, we were able to create explanations that were simple enough to make sense to a human but complex enough to express what went into the AI's decision with a reasonable amount of accuracy.

## Division of Labor
Andrew implemented the Minimax function.  Julian implemented the heuristic function.  Ted implemented the gameplay infrastructure.  The explain feature was implemented as a group.

## API Information

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
