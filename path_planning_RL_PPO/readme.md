# Here is the place where everything happend 
We worked using the reference from OpenIA and https://github.com/MorvanZhou

# Reinforcement Learning
The typical framing of a Reinforcement Learning (RL) scenario: an agent takes actions in an environment, which is interpreted into a reward and a representation of the state, which are fed back into the agent.
![alt text](https://github.com/DavidCastilloAlvarado/path_planning_self_driving/raw/master/path_planning_RL_PPO/images/RL.png)
Reinforcement learning is considered as one of three machine learning paradigms, alongside supervised learning and unsupervised learning. It differs from supervised learning in that correct input/output pairs[clarification needed] need not be presented, and sub-optimal actions need not be explicitly corrected. Instead the focus is on performance[clarification needed], which involves finding a balance between exploration (of uncharted territory) and exploitation (of current knowledge).
modeled as a Markov decision process:

a set of environment and agent states, S;
a set of actions, A, of the agent;
{\displaystyle P_{a}(s,s')=Pr(s_{t+1}=s'|s_{t}=s,a_{t}=a)} {\displaystyle P_{a}(s,s')=Pr(s_{t+1}=s'|s_{t}=s,a_{t}=a)} is the probability of transition from state {\displaystyle s} s to state {\displaystyle s'} s' under action {\displaystyle a} a.
{\displaystyle R_{a}(s,s')} R_a(s,s') is the immediate reward after transition from {\displaystyle s} s to {\displaystyle s'} s' with action {\displaystyle a} a.
rules that describe what the agent observes

# Proximal Policy Optimization



# Neural Network for both of them, Actor and Critic
They was built usign tensorflow-gpu 1.6, in python3.5

