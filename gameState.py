import operator
import os
import copy
import pickle
import datetime
from gameHeuristic import calculateHeuristic
NUMPLAYERS=2
CHECKARRAY=[[1,-1],[0,-1],[-1,-1],[-1,0]]


class bcolors:
        PURPLE = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'


class gameState:

    def __init__(self,w=7,h=6):
        self.boardWidth = w
        self.boardHeight = h
        self.board = [[0 for i in range(self.boardHeight)] for j in range(self.boardWidth)]
        self.heights = [0] * self.boardWidth
        self.numTokens = 0
        self.playerOne=-1
        self.playerTwo=1
        self.numPlayers = NUMPLAYERS
        self.turn = self.playerOne
        self.winCode = 0
        self.heuristicValue = 0
        self.children = [None] * self.boardWidth
        self.exportName = None

    def __str__(self):
        retString = "\n\n\t"
        for i in range(0 , self.boardWidth):
            retString += " " + str(i) + " "
        retString += "\n\t"
        retString += "-" * self.boardWidth * 3
        retString += '\n\t'
        for i in range(0,self.boardHeight)[::-1]:
            for j in range(0,self.boardWidth):
                val = self.board[j][i]
                retString += " " + self.generateString(val) + " "
            retString += "\n\n\t"
        retString += '\n'
        os.system('cls' if os.name == 'nt' else 'clear')
        return retString

    def getState(self,colNum):
        if self.children[colNum] is None:
            newState = copy.copy(self)
            newState.board = copy.deepcopy(self.board)
            newState.heights = copy.copy(self.heights)
            newState.children = [None] * self.boardWidth
            err = newState.insert(colNum)
            if err is -2 or err is self.numPlayers + 1:
                return err
            self.children[colNum] = newState
        return self.children[colNum]

    # returns 0 for success, the playernum of the winner, or a negative for an error
    def insert(self, colNum):
        if not isinstance( colNum, int ) or colNum > self.boardWidth:
            #print "Invalid column number"
            return -2
        if self.heights[colNum] == self.boardHeight:
            #print "That column is full"
            return -2
        if self.numTokens >= self.boardWidth * self.boardHeight:
            return self.numPlayers + 1

        rowNum = self.heights[colNum] 
        self.board[colNum][self.heights[colNum]] = self.turn
        self.heights[colNum] += 1
        self.numTokens += 1;
        winVal = self.checkWin([colNum,rowNum])
        self.heuristic = calculateHeuristic(self)
        self.heuristicValue = self.heuristic.value()
        self.turn = self.playerTwo if self.turn == self.playerOne else self.playerOne
        return winVal

    def checkWin(self,checkPosition):
        for adjustPair in CHECKARRAY:
            counter = 0
            currentPosition = map(operator.add,checkPosition,map(operator.mul,adjustPair,[-3,-3]))
            for val in range(7):
                if currentPosition[0] < 0 or currentPosition[0] >= self.boardWidth or currentPosition[1] < 0 or currentPosition[1] >= self.boardHeight:
                    currentPosition = map(operator.add,currentPosition,adjustPair)
                    continue
                else:
                    if self.board[currentPosition[0]][currentPosition[1]] == self.board[checkPosition[0]][checkPosition[1]]:
                        counter += 1
                    else:
                        counter = 0;
                    if counter == 4:
                        self.winCode = self.turn
                        return self.turn
                    currentPosition = map(operator.add,currentPosition,adjustPair)
        return 0

    def checkTie(self):
        for height in self.heights:
            if height != self.boardHeight:
                return False
        return True

    def setValue(self,value):
        self.heuristicValue = value

    def generateString(self,value):
        if value == self.playerOne:
            return bcolors.BLUE + 'X' + bcolors.ENDC
        elif value == self.playerTwo:
            return bcolors.RED + 'O' + bcolors.ENDC
        return bcolors.GREEN + '-' + bcolors.ENDC

    def exportBoard(self,isLog):
        if self.exportName is None:
            fileName = raw_input("What would you like to name your save file?\n")
            fileName += ".4log" if isLog else ".4sav" 
            self.exportName =  fileName
        f = open(self.exportName, 'a' if isLog else 'w')
        pickle.dump(self,f)

    def importBoard(self):
        thisBoard = None
        correctState = 0
        fileName = raw_input("What is the name of the file?\n")
        f = open(fileName,'r')
        while correctState is 0:
            try:
                thisBoard = pickle.load(f)
            except EOFError:
                print "No more gameStates in this file"
                print "returning None"
                return None
            print thisBoard
            correctState = input("Is this the state you want?\n 1 for yes, 0 for no\n")
        thisBoard.children = [None] * thisBoard.boardWidth
        if ".4sav" not in thisBoard.exportName:
            thisBoard.exportName = None
        return thisBoard