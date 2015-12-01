RUN_OF_TWO_VALUE = 1
RUN_OF_THREE_VALUE = 2
WIN_VALUE = 100

def calculateHeuristic(state):
    # We start off with a heuristic value of 0
    # And add/subtract points for open runs of 2 of 3
    heuristic = 0

    # +inf or -inf for winning state
    if state.winCode:
        return WIN_VALUE * state.winCode

    # Check for column runs
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
                heuristic += RUN_OF_THREE_VALUE * topToken
            # If we have a run of two and at least two spaces above it
            elif state.boardHeight - top > 2:
                heuristic += RUN_OF_TWO_VALUE * topToken

    # Check for row runs
    # For every cluster of 4 where a win is eventually possible
    # Add appropriate value if there are 2 or 3 tokens present
    for rowNumber in range(min(state.heights) - 1, max(state.heights)):
        row = map(lambda col: col[rowNumber], state.board)

        for i in range(state.boardWidth - 3):
            cluster = row[i:i+4]
            playerOneCount = cluster.count(state.playerOne)
            playerTwoCount = cluster.count(state.playerTwo)

            # If one player is the only one in the cluster, a win is possible
            if (playerOneCount == 0 or playerTwoCount == 0):
                count = playerOneCount + playerTwoCount # The count is whichever is not 0
                playerInCluster = state.playerOne if playerOneCount else state.playerTwo

                if count == 2:
                    heuristic += RUN_OF_TWO_VALUE * playerInCluster
                if count == 3:
                    heuristic += RUN_OF_THREE_VALUE * playerInCluster


    return heuristic