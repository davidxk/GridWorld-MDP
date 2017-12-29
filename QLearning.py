from collections import defaultdict
from collections import Counter
import random

class ReinforcementLearningAgent(object):
    def getAction(self, state):
        pass

    def update(self, state, action, nextState, reward):
        pass

# Q-Learning Agent
class QLearning(ReinforcementLearningAgent):
    def __init__(self, actionFn, discount = 0.9, epsilon = 0.3):
        self.qvalues = defaultdict(lambda: 0)
        self.epsilon = epsilon
        self.discount = discount
        self.getLegalActions = actionFn
        self.cnt = Counter()

    def getAction(self, state):
        ''' Address exploration vs exploitation issue '''
        legalActions = self.getLegalActions(state)
        if random.random() < self.epsilon:
            return random.choice(legalActions)
        action = self.__getPolicy__(state)
        return action

    def __alpha__(self, state, action):
        return 60.0 / (59 + self.cnt[state, action])

    def update(self, state, action, nextState, reward):
        ''' Learn from experience '''
        self.cnt[state, action] += 1
        difference = (reward + self.discount * self.__getValue__(nextState) - 
                self.qvalues[state, action])
        self.qvalues[state, action] += self.__alpha__(state, action)* difference
        
    def __getPolicy__(self, state):
        ''' Get max q-value '''
        actions = self.getLegalActions(state)
        return max(actions, key=lambda action: self.qvalues[state, action])

    def __getValue__(self, state):
        ''' Get max q-value '''
        actions = self.getLegalActions(state)
        return max(self.qvalues[state, action] for action in actions)

    def getPolicy(self, states):
        policy = {}
        for state in states:
            actions = self.getLegalActions(state)
            best = max(actions, key=lambda action: self.qvalues[state, action])
            policy[state] = best
        return policy
