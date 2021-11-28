import numpy as np

class State():
    def __init__(self):
        self.grid = np.random.randint(0,1, size=(10,10))
        self.pos = np.random.randint(0, 9, 2)
        self.reward = 0




class Robby():
    def __init__(self):
        # Dim 1 is no can, or can - currrent square
        # Dim 2,3,4,5 (N,S,E,W) is empty,can,wall 
        # Dim 6 are actions, N,S,E,W,Pickup
        self.q = np.zeros((2, 3, 3, 3, 3, 5))





def run():
