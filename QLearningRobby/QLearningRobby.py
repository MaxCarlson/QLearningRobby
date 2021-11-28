import numpy as np

NORTH = 1
SOUTH = 2
EAST = 3
WEST = 4

class State():
    WALL = 2

    def __init__(self):
        self.grid = np.random.randint(0,1, size=(10,10))
        self.pos = np.random.randint(0, 9, 2)
        self.reward = 0

    def current(self):
        return self.grid[self.pos[0]][self.pos[1]]

    def north(self):
        return self.grid[self.pos[0]][self.pos[1]+1] if self.pos[1] > 0 else State.WALL
    def south(self):
        return self.grid[self.pos[0]][self.pos[1]-1] if self.pos[1] < 10 else State.WALL
    def east(self):
        return self.grid[self.pos[0]+1][self.pos[1]] if self.pos[0] > 0 else State.WALL
    def west(self):
        return self.grid[self.pos[0]-1][self.pos[1]] if self.pos[0] < 10 else State.WALL

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
                self.pos[1] - 1
            elif dir == SOUTH:
                self.pos[1] + 1
            elif dir == EAST:
                self.pos[0] + 1
            elif dir == WEST:
                self.pos[0] - 1
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
        # Dim 6 are actions, N,S,E,W,Pickup
        self.q = np.zeros((2, 3, 3, 3, 3, 5))

    def action(self, state, eps, eta, gamma):
        d0, d1, d2, d3, d4 = state.getInfo()

        act = 0
        actions = self.q[d0][d1][d2][d3][d4]

        r = np.random.rand(0, 1)
        if r < eps:
            act = np.random.randint(0,5)
        else:
            act = actions.argmax()

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


        s0, s1, s2, s3, s4 = state.getInfo()
        stateP1 = self.q[s0][s1][s2][s3][s4]
        maxAP = stateP1[stateP1.argmax]

        self.q[d0][d1][d2][d3][d4][act] += eta * (reward + gamma * maxAP - q0)

        a=5





def run(episodes, actions, eta, gamma):
    robby = Robby()

    eps = 0.1
    for N in range(episodes):
        if N and N % 50 == 0 and eps:
            #eps -= 0.001
            eps -= 0.002
            eps = 0 if eps < 0 else eps

           
        state = State()
        for M in range(actions):
            robby.action(state, eps, eta, gamma)



run(5000, 200, 0.2, 0.9)

