import gameState
import aiplayer
import sys
#from stack OverFlow
def validateInputs(val):
    try: 
        int(val)
        return True
    except ValueError:
        return False

# setup with command arguments
gameOver = False
numArgs = len(sys.argv)
ourGame = 0
#specified height,width
if numArgs == 3:
    if not validateInputs(sys.argv[1]) or not sys.argv[2]:
        print "Invalid argument"
        sys.exit(1)
    ourGame = gameState.gameState(sys.argv[1],sys.argv[2])
#no arguments
elif numArgs == 1:
    ourGame = gameState.gameState()
else:
    print "Invalid number of arguments"
    sys.exit(1)

aiPlayer = aiplayer.AiPlayer(6)

if __name__ == "__main__":
    while(not gameOver):
        if ourGame.turn == ourGame.playerOne:
            nextMove = None
            print ourGame
            while (nextMove < 0):
                nextMove = input("Player: Which column would you like to play a token in? ")
                if ((nextMove < len(ourGame.heights)) and (nextMove >= 0)):
                    errCheck = ourGame.getState(nextMove)
                    if not isinstance(errCheck, gameState.gameState):
                        nextMove = -1
                        print "Invalid move"
                    else:
                        ourGame = errCheck
                else:
                    print "Invalid move, please try again"
        else:
            ourGame = ourGame.getState(aiPlayer.makeMove(ourGame))

        if ourGame.winCode != 0:
            gameOver = ourGame.winCode
            break
    print ourGame
    print "Game Over! Code: " + str(gameOver)

