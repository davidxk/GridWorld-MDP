from GridWorld import GridWorld
from random import random

# Grid Environment for Q-Learning
class GridEnv(GridWorld):
    def __init__(self):
        self.curState = self.getInitialState()

    def getInitialState(self):
        return (2, 0)

    def doAction(self, action):
        state = self.curState
        if action == GridWorld.EXIT:
            self.curState = GridWorld.GAMEOVER
            return self.getReward(state, action, self.curState), self.curState
        dice = random()
        dirc = action
        if 0.8 <= dice < 0.9:
            dirc = GridWorld.DIRCS[(GridWorld.index[action] - 1) %
                    len(GridWorld.DIRCS)]
        elif dice >= 0.9:
            dirc = GridWorld.DIRCS[(GridWorld.index[action] + 1) %
                    len(GridWorld.DIRCS)]
        row = state[0] + dirc[0]
        col = state[1] + dirc[1]
        landing = (row if 0 <= row < GridWorld.ROWS else state[0], 
                    col if 0 <= col < GridWorld.COLS else state[1])
        if landing == (1, 1):
            landing = state
        self.curState = landing
        return self.getReward(state, action, self.curState), self.curState

    def reset(self):
        self.curState = self.getInitialState()
    
    def printCnt(self, cnt):
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
                        line += "   %5d   |" % cnt[(i, j), action] 
                lines.append( line + "\n" )
            #    ?????   |    ?????   | 
            #"00002 00002| 00002 00002|"
            #    ?????   |    ?????   | 
            line = str()
            for j in range(GridWorld.COLS):
                if (i, j) == (1, 1):
                    line += "           |"
                elif (i, j) in [(0, 3), (1, 3)]:
                    line += "   %5d   |" % cnt[(i, j), GridWorld.EXIT] 
                else:
                    line += "%5d %5d|" % (cnt[(i, j), GridWorld.WEST],
                                            cnt[(i, j), GridWorld.EAST]) 
            line += "\n"
            output += lines[0] + line + lines[1] + divide
        print output

