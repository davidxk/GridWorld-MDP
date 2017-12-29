from QLearning import QLearning
import math
import random

# Exploration rate decreasing agent that address exploration/exploitation issue
class EpsilonDecreasing(QLearning):
    def __init__(self, actionFn, discount = 0.9):
        super(EpsilonDecreasing, self).__init__(actionFn, discount)
        self.count = 0

    def getAction(self, state):
        ''' Address exploration vs exploitation issue '''
        legalActions = self.getLegalActions(state) # FIXM: self
        if random.random() < self.__epsilon__():
            return random.choice(legalActions)
        action = self.__getPolicy__(state)
        return action

    def __epsilon__(self):
        return 60.0 / (56 + self.count/20)

    def update(self, state, action, nextState, reward):
        self.count += 1
        super(EpsilonDecreasing, self).update(state, action, nextState, reward)
