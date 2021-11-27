import numpy as np

ROBBY_SENSORS_DIR = 4
ROBBY_INPUTS_DIR = 3
ROBBY_INPUTS_LOC = 2
ROBBY_STATES = ROBBY_SENSORS_DIR * ROBBY_INPUTS_DIR * ROBBY_INPUTS_LOC

O = 0
N = 1
S = 2
E = 3
W = 4
HAS_CAN = 1

# Notes on states ordering
# R0: Nothing on any sensor
# R1: Can on center sensor
# R2: Can on center sensor, wall on North
# R3: Can on center sensor, wall on South
# R4: Can on center sensor, wall on East
# R5: Can on center sensor, wall on West
# R6: wall on North
# R7: wall on South
# R8: wall on East
# R9: wall on West
# R.: Can on Center, wall N & W
# R.: Can on Center, wall N & E
# R.: Can on Center, wall S & W
# R.: Can on Center, wall S & E
# R.: wall N & W
# R.: wall N & E
# R.: wall S & W
# R.: Can on Center, Can on N
# R.: Can on Center, Can on S
# R.: Can on Center, Can on E
# R.: Can on Center, Can on W
# R.: Can on Center, Can on N, Can on S
# R.: Can on Center, Can on N, Can on E
# R.: Can on Center, Can on N, Can on W
# R.: Can on Center, Can on S, Can on E
# R.: Can on Center, Can on S, Can on W
#.....



# R.: wall S & E
# R.: wall S & E
# R.: wall S & E
# R.: wall S & E






class State():
    def __init__(self):
        self.grid = np.random.randint(0,1, size=(10,10))
        self.pos = np.random.randint(0, 9, 2)
        self.reward = 0




class Robby():
    def __init__(self):
        self.q = np.zeros((ROBBY_STATES,5))





def run():
