thx -> https://www.youtube.com/watch?v=VnpRp7ZglfA
# Section 1
Intro
- agent = directly control; environment = not directly controlled, but interacted with agent
- influence on agent to environment = action {video game ability, action}
- influence of environment to agent = state {position, battery level, velocity}
- added signal from environment to agent = reward [good or bad outcome, more positive = good, less = bad}

Markov Decision Process (MDP)
- discrete repeating sequence of state after reward {s0, a0, r1, s1, a1, r2, s2, a3, r3 ... } s=state, a=action, r=reward
- Markov property: each state is only dependent on the immediate previous state
- goal: any given timestamp use input state to determine output action in order to maximize subsequent rewards
- now we need to find policy that maxes return
- Episodes: full sequences of interaction, from start to terminal state.
- Trajectories: recorded experiences from those episodes.

Equations
- policy (pi): s -> a --> policy pi(a | s)
- return G sbscript t = avg return = r sbcript t + Gamma * r sbscript t+1 ...
- discount factor: 0 <= Gamma <= 1

# Section 2
Grid example
- Policy gradient method --> gradient = roc
- For this we need to know whats considered good and bad
- Value functions keep track of avg return expected when following certain policy (pi) in certain state (s) or state + action (s,a)
- State-value = V sbscript pi (s)
- Action-value = Q sbscript pi(s, a)
- 
