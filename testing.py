import gameTree
import gameState

# Takes a string of "move" codes and constructs the corresponding state
def makeStateFromCode(codeStr, width=7, height=6):
    codes = map(int, list(codeStr))
    state = gameState.gameState(width, height)

    for code in codes:
        state = state.getState(code)
    
    return state

def showStateFromCode(codeStr, width=7, height=6):
    state = makeStateFromCode(codeStr, width, height)
    print str(state)
    print "Heuristic value: %d" % state.heuristicValue