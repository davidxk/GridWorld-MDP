# GridWorld-ADP
Implementation of Bellman update Value Iteration and Temporal Difference Q-Learning agent demonstrated with Grid World.

The Q-Learning implementations addressed the following issues:

* To converge, a decreasing learning rate **α** is used in Q-Learning Agent
* To address the exploration/exploitation problem, a decreasing exploration rate **ε** is used in Epsilon Decreasing Agent

**Dependency**: `matplotlib`. Install with command `pip3 install matplotlib`.

To run Value Iteration in Grid World, run command:

```shell
$ python3 TestValueIteration.py
```

To run Q-Learning agents in Grid World, run command:

```shell
$ python3 TestLearningAgent.py
```

Sample output

```text
Grid world Value Iteration with discounted rewards gamma = 0.90

   +0.64   |   +0.74   |   +0.85   |   +1.00   |
----------- ----------- ----------- ----------- 
   +0.57   |   +0.00   |   +0.57   |   -1.00   |
----------- ----------- ----------- ----------- 
   +0.49   |   +0.43   |   +0.48   |   +0.28   |
----------- ----------- ----------- ----------- 

   +0.59   |   +0.67   |   +0.77   |           |
+0.57 +0.64|+0.60 +0.74|+0.66 +0.85|   +1.00   |
   +0.53   |   +0.67   |   +0.57   |           |
----------- ----------- ----------- ----------- 
   +0.57   |           |   +0.57   |           |
+0.51 +0.51|           |+0.53 -0.60|   -1.00   |
   +0.46   |           |   +0.30   |           |
----------- ----------- ----------- ----------- 
   +0.49   |   +0.40   |   +0.48   |   -0.65   |
+0.45 +0.41|+0.43 +0.42|+0.40 +0.29|+0.28 +0.13|
   +0.44   |   +0.40   |   +0.41   |   +0.27   |
----------- ----------- ----------- ----------- 

 _ _ _ _
|> > > $|
|^   ^ !|
|^ < ^ <|
 _ _ _ _
```

Class Diagram can be found at [doc.svg](doc.svg).
