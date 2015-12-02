import gameState
import aiplayer
import sys
import argparse
import os

# setup with command arguments
parser = argparse.ArgumentParser()
parser.add_argument("--width", type=int, choices=range(4,10), default=7, help="board width")
parser.add_argument("--height", type=int, choices=range(4,10), default=6, help="board height")
parser.add_argument("--debug", action="store_true", help="print additional information for debugging")
args = parser.parse_args()



def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    while(True):
        print "Welcome!"
        print "1: Start standard game"
        print "2: Start custom sized game"
        print "3: Exit"
        selected = input("Which would you like? ")
        if selected is 1:
            playGame()
        elif selected is 2:
            width = None
            while not isinstance(width,int):
                width = input("How wide should the board be? ")
            height = None
            while not isinstance(height,int):
                height = input ("How tall should the board be? ")
            playGame(width,height)
        elif selected is 3:
            print "Thanks for playing!"
            sys.exit(1)
        else:
            print "Invalid option"
def playGame(w=7,h=6):
    gameOver = False
    ourGame = gameState.gameState(w, h)
    aiPlayer = aiplayer.AiPlayer(4, args.debug)
    aiLastMove = None
    while(not gameOver):
        print ourGame
        if ourGame.turn == ourGame.playerOne:
            nextMove = None
            while (nextMove < 0):
                if aiLastMove is not None:
                    print "AI played", aiLastMove
                nextMove = input("Player: Which column would you like to play a token in? ")
                if args.debug and nextMove is -1:
                    print "Dev Exit"
                    return
                if ((nextMove < len(ourGame.heights)) and (nextMove >= 0)):
                    errCheck = ourGame.getState(nextMove)
                    if not isinstance(errCheck, gameState.gameState):
                        if errCheck == ourGame.numPlayers + 1:
                            print "Board is full. Draw!"
                            sys.exit(1)
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


if __name__ == "__main__":
    menu()