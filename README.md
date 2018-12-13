# Path planning self driving
We will create a map from the reality and put a diferential robot in there with the aim to use an path planning algorith through reinforecement learning (PPO)

# We will need the following libraries in python3.5
1. Tensorflow 1.6 >=
2. OpenCV 3.4 >=
3. matplotlib
4. numpy
5. pandas 
6. skimage
7. os

# Reinforcement Learning
The typical framing of a Reinforcement Learning (RL) scenario: an agent takes actions in an environment, which is interpreted into a reward and a representation of the state, which are fed back into the agent.
![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/RL.png)
Reinforcement learning is considered as one of three machine learning paradigms, alongside supervised learning and unsupervised learning. It differs from supervised learning in that correct input/output pairs[clarification needed] need not be presented, and sub-optimal actions need not be explicitly corrected. Instead the focus is on performance[clarification needed], which involves finding a balance between exploration (of uncharted territory) and exploitation (of current knowledge).

## Modeled as a Markov decision process:
A Markov decision process is a 4-tuple {S,A Pa,Ra}
1. S is a finite set of states, [values, sensor-2, sensor-1, sensor0, sensor1, sensor2]
2. A is a finite set of actions[Steering angle between -6|6 degrees]
3. Pa is the probability that action a in state s at time "t" t will lead to state s' at time t+1
4. Ra is the immediate reward (or expected immediate reward) received after transitioning from state {\displaystyle s} s to state s', due to action  a
![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/robot.jpg)

# Proximal Policy Optimization
We use the following paper, about proximal policy optimization, the particular sub-method aplied in this proyect was the CLIP method whit epsilon = 0.2 
we choose a value for gamma for the discounter equal to 0.9 
https://arxiv.org/pdf/1707.06347.pdf

# Neural Network for both of them, Actor and Critic
They was built usign tensorflow-gpu 1.6, in python3.
The NN was improved using batch normalization in from the input of every layer. 
![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/PPO.png)

ACTOR:
1. batch_normalization
2. dense(200), Activation function=Relú
3. batch_normalization
4. dense(100), Activation function=Relú
5. batch_normalization
6. tf.distributions.Norma
![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/actor.png)

CRITIC:
1. batch_normalization
2. dense(200), Activation function=Relú
3. batch_normalization
4. dense(100), Activation function=Relú
5. batch_normalization
6. dense(1),
![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/critic.png)

# Reference

[1.] OpenIA    

[2.] https://github.com/MorvanZhou




