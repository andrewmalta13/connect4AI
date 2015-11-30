RUN_OF_TWO_VALUE = 1
RUN_OF_THREE_VALUE = 5
WIN_VALUE = float('inf')

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
        if topToken == col[top - 1]:
            if top > 1 and col[top - 2] == topToken:
                heuristic += RUN_OF_THREE_VALUE * topToken
            else:
                heuristic += RUN_OF_TWO_VALUE * topToken

    return heuristic