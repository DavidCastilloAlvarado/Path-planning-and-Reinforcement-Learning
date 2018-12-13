# Reinforcement Learning
The typical framing of a Reinforcement Learning (RL) scenario: an agent takes actions in an environment, which is interpreted into a reward and a representation of the state, which are fed back into the agent.
![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/RL.png)
Reinforcement learning is considered as one of three machine learning paradigms, alongside supervised learning and unsupervised learning. It differs from supervised learning in that correct input/output pairs[clarification needed] need not be presented, and sub-optimal actions need not be explicitly corrected. Instead the focus is on performance[clarification needed], which involves finding a balance between exploration (of uncharted territory) and exploitation (of current knowledge).

## Modeled as a Markov decision process:
A Markov decision process is a 4-tuple {S,A Pa,Ra}
1. S is a finite set of states, [sensor-2, sensor-1, sensor0, sensor1, sensor2, values]
2. A is a finite set of actions[Steering angle between -6|6 degrees]
3. Pa is the probability that action a in state s at time "t" t will lead to state s' at time t+1
4. Ra is the immediate reward (or expected immediate reward) received after transitioning from state s to state s', due to action  a

               Ra = 0.4 + (0.2 if s[0]<1 else 0.001) + (0.4 if m <1 else 0.001) or -1 if collides
               s[0] = global approach
               m = relative approach

![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/robot.jpg)

# Proximal Policy Optimization (PPO)
The Policy was optimizer using a method call PPO (2017) a new family of policy gradient methods for reinforcement learning.
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

