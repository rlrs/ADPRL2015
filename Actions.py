from State import State
import numpy as np
import operator

class Action(object):
    def __init__(self):
        self.delta = (0, 0)
        
        
    def do(self, state):
        return State(tuple(map(operator.add, state.pos, self.delta)))


class Up(Action):
    def __init__(self):
        self.delta = (-1, 0)

        
class Down(Action):
    def __init__(self):
        self.delta = (1, 0)
        
        
class Left(Action):
    def __init__(self):
        self.delta = (0, -1)
        
        
class Right(Action):
    def __init__(self):
        self.delta = (0, 1)
        