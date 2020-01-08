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
    GAMEOVER = (-1, -1)
    def __init__(self, shape, prob, walls, terminals):
        self.rows, self.cols = shape
        accident = (1 - prob) / 2
        self.turns = {-1: accident, 0: prob, +1: accident}
        self.walls = set(walls)
        self.terms = terminals

    def getStates(self):
        return [(i, j) for i in range(self.rows)
                    for j in range(self.cols) if (i, j) not in self.walls]

    def getTransitionStatesAndProbs(self, state, action):
        if state in self.terms:
            return [(GridWorld.GAMEOVER, 1.0)]

        result = []
        for turn in self.turns:
            dirc = GridWorld.DIRCS[(GridWorld.index[action] + turn) %
                    len(GridWorld.DIRCS)]
            row = state[0] + dirc[0]
            col = state[1] + dirc[1]
            landing = (row if 0 <= row < self.rows else state[0],
                        col if 0 <= col < self.cols else state[1])
            if landing in self.walls:
                landing = state
            prob = self.turns[turn]
            result.append( (landing, prob) )
        return result

    def getReward(self, state, action, nextState):
        if state in self.terms:
            return self.terms[state]
        else:
            return 0

    def isTerminal(self, state):
        return state == GridWorld.GAMEOVER

    def getLegalActions(self, state):
        if state in self.terms:
            return [GridWorld.EXIT]
        else:
            return GridWorld.DIRCS

    def printValues(self, values):
        output = str()
        divide = "\n" + "----------- " * self.cols + "\n"
        for i in range(self.rows):
            for j in range(self.cols):
                output += "   %+.2f   |" % values[(i, j)]
            output += divide
        print(output)

    def printQValues(self, qvalues):
        output = str()
        divide = "----------- " * self.cols + "\n"
        for i in range(self.rows):
            lines = []
            #"   00001   |    00001   |"
            # ????? ?????| ????? ?????|
            #"   00003   |    00003   |"
            for action in [GridWorld.NORTH, GridWorld.SOUTH]:
                line = str()
                for j in range(self.cols):
                    if (i, j) in [(1, 1), (0, 3), (1, 3)]:
                        line += "           |"
                    else:
                        line += "   %+.2f   |" % qvalues[(i, j), action] 
                lines.append( line + "\n" )
            #    ?????   |    ?????   | 
            #"00002 00002| 00002 00002|"
            #    ?????   |    ?????   | 
            line = str()
            for j in range(self.cols):
                if (i, j) == (1, 1):
                    line += "           |"
                elif (i, j) in [(0, 3), (1, 3)]:
                    line += "   %+.2f   |" % qvalues[(i, j), GridWorld.EXIT] 
                else:
                    line += "%+.2f %+.2f|" % (qvalues[(i, j), GridWorld.WEST],
                                            qvalues[(i, j), GridWorld.EAST]) 
            line += "\n"
            output += lines[0] + line + lines[1] + divide
        print(output)

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
        print(output)


# Additive Grid Environment for MDP Value Iteration
class GridWorldAdditive(GridWorld):
    def __init__(self, shape, prob, walls, terminals, reward = -0.01):
        super(GridWorldAdditive, self).__init__(shape, prob, walls, terminals)
        self.reward = reward

    def getReward(self, state, action, nextState):
        if state in self.terms:
            return self.terms[state]
        else:
            return self.reward
