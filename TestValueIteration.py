from GridWorld import GridWorld
from GridWorld import GridWorldAdditive
from ValueIteration import ValueIteration

# Run Value Iteration in different Grid World environments
if __name__ == "__main__":
    gamma = 0.9
    print "Grid world Value Iteration with discounted rewards gamma = %.2f\n" % gamma
    terminals = {(0, 3): +1, (1, 3): -1}
    gw = GridWorld((3, 4), 0.8, [(1, 1)], terminals)
    vi = ValueIteration()
    values = vi.valueIteration(gw, gamma)
    gw.printValues(values)
    qvalues = vi.getQValues(gw, values, gamma)
    gw.printQValues(qvalues)
    policy = vi.getPolicy(gw, values, gamma)
    gw.printPolicy(policy)

    reward = -0.01
    print "Grid world Value Iteration with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive((3, 4), 0.8, [(1, 1)], terminals, reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
 
    reward = -0.04
    print "Grid World with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive((3, 4), 0.8, [(1, 1)], terminals, reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
  
    reward = -0.1
    print "Grid World with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive((3, 4), 0.8, [(1, 1)], terminals, reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
 
    reward = -2
    print "Grid World with additive rewards = %.2f\n" % reward
    gwa = GridWorldAdditive((3, 4), 0.8, [(1, 1)], terminals, reward)
    values = vi.valueIteration(gwa, 1, 100)
    gwa.printValues(values)
    qvalues = vi.getQValues(gwa, values, 1)
    gwa.printQValues(qvalues)
    policy = vi.getPolicy(gwa, values, 1)
    gwa.printPolicy(policy)
