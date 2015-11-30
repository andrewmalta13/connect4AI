import gameTree
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
    ourGame = gameTree.gameTree(sys.argv[1],sys.argv[2])
#no arguments
elif numArgs == 1:
    ourGame = gameTree.gameTree()
else:
    print "Invalid number of arguments"
    sys.exit(1)
aiPlayer = aiplayer.AiPlayer(2, ourGame)

if __name__ == "__main__":
    while(not gameOver):
        if ourGame.tree[ourGame.position].turn == 1:
            nextMove = None
            while (nextMove < 0):
                print ourGame.tree[ourGame.position]
                nextMove = input("Player " + str(ourGame.tree[ourGame.position].turn) + ": Which column would you like to play a token in? ")
                if ((nextMove < len(ourGame.tree[0].heights)) and (nextMove >= 0)):
                    ourGame.position = ourGame.getState(nextMove)
                else:
                    print "Invalid move, please try again"
        else:
            ourGame.position = ourGame.getState(aiPlayer.makeMove())

        if ourGame.tree[ourGame.position].winCode != 0:
            gameOver = ourGame.tree[ourGame.position].winCode
            break
    print ourGame.tree[ourGame.position]
    print "Game Over! Code: " + str(gameOver)

