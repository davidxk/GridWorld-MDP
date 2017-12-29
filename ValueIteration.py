from collections import defaultdict

# MDP Value Iteration with Bellman update
class ValueIteration:
    def getQValueFromValues(self, mdp, state, action, values, discount):
        avg = 0
        for landing, prob in mdp.getTransitionStatesAndProbs(state, action):
            avg += prob * (mdp.getReward(state, action, landing) + discount * values[landing])
        return avg

    def valueIteration(self, mdp, discount = 0.9, iterations = 100):
        values = defaultdict(lambda: 0)
        for i in range(iterations):
            vnext = defaultdict(lambda: 0)
            for state in mdp.getStates():
                if not mdp.isTerminal(state):
                    maximum = float("-inf")
                    for action in mdp.getLegalActions(state):
                        qvalue = self.getQValueFromValues(mdp, state, action, values, discount)
                        maximum = max(maximum, qvalue)
                    vnext[state] = maximum
            values = vnext
        return values

    def getQValues(self, mdp, values, discount = 0.9):
        qvalues = {}
        for state in mdp.getStates():
            if not mdp.isTerminal(state):
                for action in mdp.getLegalActions(state):
                    qvalues[state, action] = self.getQValueFromValues(mdp, state, action, values, discount)
        return qvalues

    def getPolicy(self, mdp, values, discount = 0.9):
        policy = {}
        for state in mdp.getStates():
            if not mdp.isTerminal(state):
                maximum = -float("inf")
                for action in mdp.getLegalActions(state):
                    qvalue = self.getQValueFromValues(mdp, state, action, values, discount)
                    if qvalue > maximum:
                        maximum = qvalue
                        bestact = action
                policy[state] = bestact
        return policy
