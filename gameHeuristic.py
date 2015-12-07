# An object representing the heuristic value of a game state
class Heuristic():
    runOfTwoVal = 1
    runOfThreeVal = 2
    winVal = 100

    def __init__(self, state):
        # A run has a # of tokens, a direction, and an occurrence count
        def initRunArr():
            arr = []
            for i in [3, 2]: # We go backwards so that runs of three are listed out first when explaining
                for dir in ['horizontal', 'vertical', 'diagonal']:
                    arr.append({'tokens': i, 'dir': dir, 'count': 0})
            return arr

        self.playerOneRuns = initRunArr()
        self.playerTwoRuns = initRunArr()

        self.winCode = state.winCode
        self.playerOne = state.playerOne
        self.playerTwo = state.playerTwo

    # Add a run to the heuristic for a particular player
    def addRun(self, player, tokens, dir):
        runArr = self.playerOneRuns if player == self.playerOne else self.playerTwoRuns

        # Find run object in array and increase count
        for run in runArr:
            if run['tokens'] == tokens and run['dir'] == dir:
                run['count'] += 1

    # Computer the heuristic value, agnostic of player
    def value(self):
        # +/- winVal for winning state
        if self.winCode:
            return self.winVal * self.winCode

        def getRunValue(run):
            return run['count'] * (self.runOfTwoVal if run['tokens'] == 2 else self.runOfThreeVal)

        # Add up run values for each player multiplied by player number
        playerOneValue = self.playerOne * sum(map(getRunValue, self.playerOneRuns))
        playerTwoValue = self.playerTwo * sum(map(getRunValue, self.playerTwoRuns))

        return playerOneValue + playerTwoValue

    # Is this state good, bad, or neutral for a particular player
    def goodOrBad(self, player):
        sign = self.value() * player
        if sign > 0:
            return 'good'
        elif sign < 0:
            return 'bad'
        else:
            return 'neutral'

    # Return an explanation of this state's value to a particular player
    def explain(self, player, me = True, prefix = 'This is a'):

        # Function to write out a list of runs
        def writeRuns(runs):
            def getRunStr(run):
                if run['count'] == 1:
                    return 'a %s run of %d' % (run['dir'], run['tokens'])
                else:
                    return '%d %s runs of %d' % (run['count'], run['dir'], run['tokens'])

            runs = filter(lambda run: run['count'], runs) # Remove runs with 0 count
            runStrs = map(getRunStr, runs)

            if len(runStrs) < 2:
                return ''.join(runStrs)

            return ', '.join(runStrs[0:-1]) + ' and %s' % runStrs[-1]

        # Begin out message
        explanation = prefix + ' '

        goodOrBad = self.goodOrBad(player)

        # If it's a win or loss state, state that and return
        if self.winCode:
            explanation += 'win' if self.winCode * player > 0 else 'loss'
            explanation += ' state for %s' % 'me' if me else 'you'
            return explanation

        # Otherwise, say if it's good, bad, or neutral, and why
        explanation += self.goodOrBad(player)
        explanation += ' state for %s' % 'me' if me else 'you'

        if goodOrBad == 'neutral':
            return explanation

        # List runs
        if player == self.playerOne:
            myRuns = self.playerOneRuns
            yourRuns = self.playerTwoRuns
        else:
            myRuns = self.playerTwoRuns
            yourRuns = self.playerOneRuns
        explanation += ', because %s ' % 'I' if me else 'you'
        explanation += 'only have ' if goodOrBad == 'bad' and writeRuns(myRuns) else 'have '
        explanation += writeRuns(myRuns) or 'nothing'
        explanation += ' and %s ' % 'you' if me else 'I'
        explanation += 'only have ' if goodOrBad == 'good' and writeRuns(yourRuns) else 'have '
        explanation += writeRuns(yourRuns) or 'nothing'

        return explanation


# Given a group of four, calculate its value
# A cluster has value to a player if that player
# has two or three tokens in it and the other player has none
def evaluateCluster(heuristic, state, cluster, type):
    playerOneCount = cluster.count(state.playerOne)
    playerTwoCount = cluster.count(state.playerTwo)

    # If one player is the only one in the cluster, a win is possible
    if (playerOneCount == 0 or playerTwoCount == 0):
        count = playerOneCount + playerTwoCount # The count is whichever is not 0
        playerInCluster = state.playerOne if playerOneCount else state.playerTwo

        if count == 2 or count == 3:
            heuristic.addRun(playerInCluster, count, type)

def calculateHeuristic(state):
    heuristic = Heuristic(state)

    # Check for column runs, awarding value for runs of 2 or 3
    # that could eventually become wins
    for colNumber, col in enumerate(state.board):
        top = state.heights[colNumber] - 1

        # Ignore columns with fewer than 2 tokens
        if top < 1:
            continue

        topToken = col[top]

        # If we have a run of two
        if topToken == col[top - 1]:
            # If we have a run of three and at least one space above it
            if top > 1 and col[top - 2] == topToken and state.boardHeight - top > 1:
                heuristic.addRun(topToken, 3, 'vertical')
            # If we have a run of two and at least two spaces above it
            elif state.boardHeight - top > 2:
                heuristic.addRun(topToken, 2, 'vertical')

    # Check for row runs
    # For every cluster of 4 where a win is eventually possible
    # add its value to the heuristic
    for rowNumber in range(min(state.heights) - 1, max(state.heights)):
        row = map(lambda col: col[rowNumber], state.board)

        for i in range(state.boardWidth - 3):
            cluster = row[i:i+4]
            evaluateCluster(heuristic, state, cluster, 'horizontal')

    # Check for diagonal runs
    # For every cluster of 4 where a win is eventually possible
    # add its value to the heuristic
    for rowNumber in range(state.boardHeight - 3):
        # Check possible diagonals that go up to the right
        for colNumber in range(state.boardWidth - 3):
            cluster = [state.board[colNumber + i][rowNumber + i] for i in range(4)]
            evaluateCluster(heuristic, state, cluster, 'diagonal')

        # Check possible diagonals that go up to the left
        for colNumber in range(3, state.boardWidth):
            cluster = [state.board[colNumber - i][rowNumber + i] for i in range(4)]
            evaluateCluster(heuristic, state, cluster, 'diagonal')

    return heuristic
    