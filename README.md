# GridWorld-MDP
Implementation of Bellman update Value Iteration and Temporal Difference Q-Learning agent demonstrated with Grid World. 

The Q-Learning implementations addressed the following issues:

* To converge, a decreasing learning rate alpha is used in Q-Learning Agent
* To address the exploration/exploitation problem, a decreasing exploration rate epsilon is used in Epsilon Decreasing Agent

**Dependency**: `matplotlib`. Install with command `pip install matplotlib`. 

To run Value Iteration in Grid World, run command:

```shell
$ python TestValueIteration.py
```

To run Q-Learning agents in Grid World, run command:

```shell
$ python TestLearningAgent.py
```

![Class Diagram](doc.svg)
