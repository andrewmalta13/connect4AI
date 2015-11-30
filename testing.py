import gameTree
import gameState

# Takes a string of "move" codes and constructs the corresponding state
def makeStateFromCode(codeStr):
    codes = map(int, list(codeStr))
    ourGame = gameTree.gameTree()

    for code in codes:
        ourGame.position = ourGame.getState(code)
    
    return ourGame.tree[ourGame.position]

def showStateFromCode(codeStr):
    state = makeStateFromCode(codeStr)
    print str(state)
    print "Heuristic value: %d" % state.heuristicValue