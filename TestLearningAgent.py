from GridWorld import GridWorld
from ValueIteration import ValueIteration
from QLearning import QLearning
from EpsilonDecreasing import EpsilonDecreasing
from GridEnv import GridEnv
import matplotlib.pyplot as plt

# Calculates RMSE between value iteration results and Q-Learning results
class QLearningAnalyzer:
    def getRMSError(self, expect, result):
        sumSE = 0
        for key in expect:
            sumSE += (expect[key] - result[key]) ** 2
        MSE = sumSE / len(expect)
        return MSE ** 0.5

# Epsilon Decreasing Agent exploits more, so scores higher than Q-Learning agent
class TestLearningAgent:
    def getQValues(self, env):
        vi = ValueIteration()
        values = vi.valueIteration(env)
        qvalues = vi.getQValues(env, values)
        return qvalues

    def testLearningAgent(self, agent, env, nEpisodes = 5000):
        qvalues = self.getQValues(env)
        qla = QLearningAnalyzer()
        rmse = []
        score = 0

        for i in range(nEpisodes):
            # Learn each episode
            while not env.isTerminal(env.curState):
                state = env.curState
                action = agent.getAction(env.curState)
                reward, nextState = env.doAction(action)
                agent.update(state, action, nextState, reward)
            score += reward
            env.reset()
            # Calculate RMSE for qvalues after this episode
            error = qla.getRMSError(qvalues, agent.qvalues)
            rmse.append(error)
        self.visualizeResult(env, agent, rmse, score)
        
    def visualizeResult(self, env, agent, rmse, score):
        # Output eventual Learning result
        env.printQValues(agent.qvalues)
        env.printCnt(agent.cnt)
        env.printPolicy(agent.getPolicy(env.getStates()))
        # Visualize RMSE trend
        print("Final RMSE: %f" % rmse[-1])
        print("Final score: %d\n" % score)
        plt.plot(rmse)
        plt.show()

# Run Q-Learning in Grid Environment and analyze results
# Epsilon Decreasing Agent exploits more, so scores higher than Q-Learning agent
if __name__ == "__main__":
    test = TestLearningAgent()
    env = GridEnv((3, 4), 0.8, [(1, 1)], {(0, 3): +1, (1, 3): -1}, (2, 0))
    print("Test Q-Learning Agent\n")
    test.testLearningAgent(QLearning(env.getLegalActions), env, 5000)
    print("Test Epsilon Decreasing Agent\n")
    test.testLearningAgent(EpsilonDecreasing(env.getLegalActions), env, 5000)
