import numpy as np
import matplotlib.pyplot as plt
NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

class State():
    WALL = 2

    def __init__(self):
        self.grid = np.random.randint(0, 2, size=(10,10))
        self.pos = np.random.randint(0, 10, 2)
        if self.pos[1] == 10:
            a=4
        self.reward = 0

    def current(self):
        return self.grid[self.pos[0]][self.pos[1]]

    def north(self):
        return self.grid[self.pos[0]-1][self.pos[1]] if self.pos[0] > 0 else State.WALL
    def south(self):
        return self.grid[self.pos[0]+1][self.pos[1]] if self.pos[0] < 9 else State.WALL
    def east(self):
        return self.grid[self.pos[0]][self.pos[1]+1] if self.pos[1] < 9 else State.WALL
    def west(self):
        return self.grid[self.pos[0]][self.pos[1]-1] if self.pos[1] > 0 else State.WALL

    def getInfo(self):
        return self.current(), self.north(), self.south(), self.east(), self.west()

    def move(self, at, dir):
        reward = 0
        if at == State.WALL:
            reward = -5
        else:
            # Wall checking has already been done for us by this point, 
            # no need to repeat it
            if dir == NORTH:
                self.pos[0] -= 1
            elif dir == SOUTH:
                self.pos[0] += 1
            elif dir == EAST:
                self.pos[1] += 1
            elif dir == WEST:
                self.pos[1] -= 1
            else:
                RuntimeError(f'Invalid movement direction {dir}')

        self.reward += reward
        return reward

    def pickup(self):
        val = self.grid[self.pos[0]][self.pos[1]]
        self.grid[self.pos[0]][self.pos[1]] = 0
        reward = 10 if val else -1
        self.reward += reward
        return reward




class Robby():
    def __init__(self):
        # Dim 1 is no can, or can - currrent square
        # Dim 2,3,4,5 (N,S,E,W) is empty,can,wall 
        # Dim 6 are actions: Pickup,N,S,E,W,
        self.q = np.zeros((2, 3, 3, 3, 3, 5))

    def action(self, state, eps, eta, gamma, training):
        d0, d1, d2, d3, d4 = state.getInfo()

        act = 0
        actions = self.q[d0][d1][d2][d3][d4]

        r = np.random.rand()
        if r < eps:
            act = np.random.randint(0,5)
        else:
            act = actions.argmax()

        # Current reward for this action at this state
        q0 = actions[act]

        reward = 0
        if act == 0:
            reward = state.pickup()
        elif act == 1:
            reward = state.move(d1, NORTH)
        elif act == 2:
            reward = state.move(d2, SOUTH)
        elif act == 3:
            reward = state.move(d3, EAST) 
        elif act == 4:
            reward = state.move(d4, WEST) 

        if not training:
            return

        s0, s1, s2, s3, s4 = state.getInfo()
        stateP1 = self.q[s0][s1][s2][s3][s4]
        maxAP = stateP1[stateP1.argmax()]

        self.q[d0][d1][d2][d3][d4][act] += eta * (reward + gamma * maxAP - q0)






def run(robby, episodes, actions, eta, gamma, training=True):
 

    plotPoints = 100

    eps = 0.1
    totalRewards = 0
    ttotalRewards = 0
    rewards = []
    allRewards = []
    for N in range(episodes):
        if training and N and N % 50 == 0 and eps:
            #eps -= 0.001
            eps -= 0.005
            eps = 0 if eps < 0 else eps

           
        state = State()
        for M in range(actions):
            robby.action(state, eps, eta, gamma, training)

        totalRewards += state.reward
        ttotalRewards += state.reward
        allRewards.append(state.reward)
        if not N % plotPoints:
            rewards.append(ttotalRewards / plotPoints)
            ttotalRewards = 0
        print(f'Epoch {N+1}, Reward: {state.reward}')

    if training:
        plt.title('Robby\'s score vs. Episode')
        plt.plot(range(0, len(rewards)*plotPoints, plotPoints), rewards)
        plt.xlabel('Episode')
        plt.ylabel(f'Average rewards over last {plotPoints} epochs')
        plt.show()
        
    else:
        print(f'Test-Average: {totalRewards/episodes}')
        print(f'Test-Standard-Deviation: {np.std(allRewards)}') 


robby = Robby()
run(robby, 5000, 200, 0.2, 0.9, training=True)
run(robby, 5000, 200, 0.2, 0.9, training=False)


