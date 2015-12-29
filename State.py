import numpy as np

class State(object):
    def __init__(self, pos, goal):
        # The map is defined as a (fixed) part of the state, for simplicity
        self.map = np.matrix('1 1 1 1 1 1 1 1; \
                              1 0 1 0 1 0 0 1; \
                              1 0 1 0 1 1 0 1; \
                              1 0 1 0 0 0 0 1; \
                              1 0 0 0 1 0 0 1; \
                              1 0 1 1 1 1 1 1; \
                              1 0 0 0 0 0 0 1; \
                              1 1 1 1 1 1 1 1')
        self.pos = pos
        self.goal = goal