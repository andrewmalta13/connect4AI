import gameState
import aiplayer
import sys
import argparse

# setup with command arguments
parser = argparse.ArgumentParser()
parser.add_argument("--width", type=int, choices=range(4,10), default=7, help="board width")
parser.add_argument("--height", type=int, choices=range(4,10), default=6, help="board height")
parser.add_argument("--debug", action="store_true", help="print additional information for debugging")
args = parser.parse_args()

gameOver = False
ourGame = gameState.gameState(args.width, args.height)
aiPlayer = aiplayer.AiPlayer(4, args.debug)
aiLastMove = None
if __name__ == "__main__":
    while(not gameOver):
        print ourGame
        if ourGame.turn == ourGame.playerOne:
            nextMove = None
            while (nextMove < 0):
                if aiLastMove is not None:
                    print "AI played", aiLastMove
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
            print "AI is thinking ..."
            aiLastMove = aiPlayer.makeMove(ourGame)
            ourGame = ourGame.getState(aiLastMove)

        if ourGame.winCode != 0:
            gameOver = ourGame.winCode
            break
    print ourGame
    if gameOver == ourGame.playerOne:
        print "Nice work! You won!"
    elif gameOver == ourGame.playerTwo:
        print "The AI beat you! Try again"
    else:
        print "Game Over! Code: " + str(gameOver)

