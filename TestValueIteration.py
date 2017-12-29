from GridWorld import GridWorld
from GridWorld import GridWorldAdditive
from ValueIteration import ValueIteration

# Run Value Iteration in different Grid World environments
if __name__ == "__main__":
    gamma = 0.9
    print "Grid World with discounted rewards gamma = %.2f\n" % gamma
    gw = GridWorld()
    vi = ValueIteration()
    values = vi.valueIteration(gw, gamma)
    gw.printValues(values)
    qvalues = vi.getQValues(gw, values, gamma)
    gw.printQValues(qvalues)
    policy = vi.getPolicy(gw, values, gamma)
    gw.printPolicy(policy)

    reward = -0.01
    print "Grid World with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive(reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
 
    reward = -0.04
    print "Grid World with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive(reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
  
    reward = -0.1
    print "Grid World with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive(reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
 
    reward = -2
    print "Grid World with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive(reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
