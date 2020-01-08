from GridWorld import GridWorld
from random import random

# Grid Environment for Q-Learning
class GridEnv(GridWorld):
    def __init__(self, shape, prob, walls, terminals, initial):
        super(GridEnv, self).__init__(shape, prob, walls, terminals)
        self.initial = initial
        self.curState = self.getInitialState()

    def getInitialState(self):
        return self.initial

    def doAction(self, action):
        state = self.curState
        if action == GridWorld.EXIT:
            self.curState = GridWorld.GAMEOVER
            return self.getReward(state, action, self.curState), self.curState
        dice = random()
        dirc = action
        prob, accident = self.turns[0], self.turns[1]
        if prob <= dice < prob + accident:
            dirc = GridWorld.DIRCS[(GridWorld.index[action] - 1) %
                    len(GridWorld.DIRCS)]
        elif dice >= prob + accident:
            dirc = GridWorld.DIRCS[(GridWorld.index[action] + 1) %
                    len(GridWorld.DIRCS)]
        row = state[0] + dirc[0]
        col = state[1] + dirc[1]
        landing = (row if 0 <= row < self.rows else state[0],
                    col if 0 <= col < self.cols else state[1])
        if landing in self.walls:
            landing = state
        self.curState = landing
        return self.getReward(state, action, self.curState), self.curState

    def reset(self):
        self.curState = self.getInitialState()
    
    def printCnt(self, cnt):
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
                        line += "   %5d   |" % cnt[(i, j), action] 
                lines.append( line + "\n" )
            #    ?????   |    ?????   | 
            #"00002 00002| 00002 00002|"
            #    ?????   |    ?????   | 
            line = str()
            for j in range(self.cols):
                if (i, j) == (1, 1):
                    line += "           |"
                elif (i, j) in [(0, 3), (1, 3)]:
                    line += "   %5d   |" % cnt[(i, j), GridWorld.EXIT] 
                else:
                    line += "%5d %5d|" % (cnt[(i, j), GridWorld.WEST],
                                            cnt[(i, j), GridWorld.EAST]) 
            line += "\n"
            output += lines[0] + line + lines[1] + divide
        print(output)

