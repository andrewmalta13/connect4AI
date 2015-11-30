import gameTree
import aiplayer
gameOver = False

ourGame = gameTree.gameTree()
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