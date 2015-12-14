import gameState
import aiplayer
import sys
import argparse
import os
import signal
from math import *

# setup with command arguments
parser = argparse.ArgumentParser()

parser.add_argument("--debug", action="store_true", help="print additional information for debugging")
parser.add_argument("--explain", action="store_true", help="explain AI decisions")
args = parser.parse_args()

def sigIntHandler(signum,frame):
    print "\nThanks for playing!\n"
    sys.exit(1)

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    while(True):
        print "Welcome!"
        print "1: Start standard game"
        print "2: Start custom sized game"
        print "3: Load Game"
        print "4: Exit"
        selected = input("Which would you like? ")
        if selected is 1:
            playGame()
        elif selected is 2:
            width = None
            while not isinstance(width,int):
                width = input("How wide should the board be? (4-10) ")
                if width not in range(4,11):
                    print "Invalid width"
                    width = None
            height = None
            while not isinstance(height,int):
                height = input ("How tall should the board be? (4-10) ")
                if height not in range(4,11):
                    print "Invalid height"
                    height = None
            playGame(width,height)
        elif selected is 3:
            loadGame = gameState.gameState().importBoard(False);
            if loadGame is not None:
                if loadGame.winCode is 0:
                    playGame(loadGame.boardWidth,loadGame.boardHeight,loadGame)
                else:
                    print "That game has already ended!"
        elif selected is 4:
            print "Thanks for playing!"
            sys.exit(1)
        else:
            print "Invalid option"

def playGame(w=7,h=6,ourGame=None):
    gameOver = False
    if ourGame is None:
        ourGame = gameState.gameState(w, h)
    aiPlayer = aiplayer.AiPlayer(int(9 / log(w)), args.debug, args.explain, ourGame.playerTwo)
    aiLastMove = None
    while(not gameOver and not ourGame.checkTie()):
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
                if args.debug and nextMove is -2:
                    print "Game will be set to selected state"
                    testGame = ourGame.importBoard(True)
                    if testGame is None:
                        print "Import Failed"
                    else:
                        ourGame = testGame
                        continue
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
        if args.debug:
            ourGame.exportBoard(True)
        else:
            ourGame.exportBoard(False)
        if ourGame.winCode != 0:
            gameOver = ourGame.winCode
            if ".4sav" in ourGame.exportName:
                os.remove(ourGame.exportName)
            break
    print ourGame
    if gameOver == ourGame.playerOne:
        print "Nice work! You won!"
    elif gameOver == ourGame.playerTwo:
        print "The AI beat you! Try again"
    else:
        print "Game was a tie!"


if __name__ == "__main__":
    signal.signal(signal.SIGINT,sigIntHandler)
    menu()
