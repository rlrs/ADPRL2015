import numpy as np

class State(object):
    def __init__(self, pos):
        """ Agent position is Markov state.
            No artificial end state because it's handled in the Agent code """
        self.pos = pos