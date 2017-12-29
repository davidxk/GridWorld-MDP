from MDP import MDP

'''
 c 0 1 2 3
r  _ _ _ _
0 |  _   $|
1 | |_|  !|
2 |_ _ _ _|
'''

# Grid Environment for MDP Value Iteration
class GridWorld(MDP):
    EXIT = (float("inf"), float("inf"))
    NORTH = (-1,  0)
    EAST  = ( 0, +1)
    SOUTH = (+1,  0)
    WEST  = ( 0, -1)
    DIRCS = [NORTH, EAST, SOUTH, WEST]
    index = {NORTH: 0, EAST: 1, SOUTH: 2, WEST: 3}
    ROWS  = 3
    COLS  = 4
    GAMEOVER = (-1, -1)
    def getStates(self):
        return [(i, j) for i in range(GridWorld.ROWS) 
                    for j in range(GridWorld.COLS) if (i, j) != (1, 1)]

    def getTransitionStatesAndProbs(self, state, action):
        if state[1] == 3 and (state[0] == 0 or state[0] == 1):
            return [(GridWorld.GAMEOVER, 1.0)]

        turns = {-1: 0.1, 0: 0.8, +1: 0.1} 
        result = []
        for turn in turns:
            dirc = GridWorld.DIRCS[(GridWorld.index[action] + turn) %
                    len(GridWorld.DIRCS)]
            row = state[0] + dirc[0]
            col = state[1] + dirc[1]
            landing = (row if 0 <= row < GridWorld.ROWS else state[0], 
                        col if 0 <= col < GridWorld.COLS else state[1])
            if landing == (1, 1):
                landing = state
            prob = turns[turn]
            result.append( (landing, prob) )
        return result

    def getReward(self, state, action, nextState):
        if state == (0, 3):
            return +1
        elif state == (1, 3):
            return -1
        else:
            return 0

    def isTerminal(self, state):
        return state == GridWorld.GAMEOVER

    def getLegalActions(self, state):
        if state[1] == 3 and (state[0] == 0 or state[0] == 1):
            return [GridWorld.EXIT]
        else:
            return GridWorld.DIRCS

    def printValues(self, values):
        output = str()
        divide = "\n" + "----------- " * GridWorld.COLS + "\n"
        for i in range(GridWorld.ROWS):
            for j in range(GridWorld.COLS):
                output += "   %+.2f   |" % values[(i, j)]
            output += divide
        print output

    def printQValues(self, qvalues):
        output = str()
        divide = "----------- " * GridWorld.COLS + "\n"
        for i in range(GridWorld.ROWS):
            lines = []
            #"   00001   |    00001   |"
            # ????? ?????| ????? ?????|
            #"   00003   |    00003   |"
            for action in [GridWorld.NORTH, GridWorld.SOUTH]:
                line = str()
                for j in range(GridWorld.COLS):
                    if (i, j) in [(1, 1), (0, 3), (1, 3)]:
                        line += "           |"
                    else:
                        line += "   %+.2f   |" % qvalues[(i, j), action] 
                lines.append( line + "\n" )
            #    ?????   |    ?????   | 
            #"00002 00002| 00002 00002|"
            #    ?????   |    ?????   | 
            line = str()
            for j in range(GridWorld.COLS):
                if (i, j) == (1, 1):
                    line += "           |"
                elif (i, j) in [(0, 3), (1, 3)]:
                    line += "   %+.2f   |" % qvalues[(i, j), GridWorld.EXIT] 
                else:
                    line += "%+.2f %+.2f|" % (qvalues[(i, j), GridWorld.WEST],
                                            qvalues[(i, j), GridWorld.EAST]) 
            line += "\n"
            output += lines[0] + line + lines[1] + divide
        print output

    def printPolicy(self, policy):
        actmap = { GridWorld.NORTH: '^', GridWorld.EAST: '>',
                GridWorld.SOUTH: 'v', GridWorld.WEST: '<' }
        divide = " _ _ _ _\n"
        actstrs = [actmap[policy[(0, j)]] for j in range(3)]
        first = '|' + ' '.join(actstrs) + " $|\n"
        actstrs = [actmap[policy[(1, j)]] for j in (0, 2)]
        second = "|" + actstrs[0] + "   " + actstrs[1] + " !|\n"
        actstrs = [actmap[policy[(2, j)]] for j in range(4)]
        third = '|' + ' '.join(actstrs) + "|\n"
        output = divide + first + second + third + divide
        print output


# Additive Grid Environment for MDP Value Iteration
class GridWorldAdditive(GridWorld):
    def __init__(self, reward = -0.01):
        self.reward = reward

    def getReward(self, state, action, nextState):
        if state == (0, 3):
            return +1
        elif state == (1, 3):
            return -1
        else:
            return self.reward
