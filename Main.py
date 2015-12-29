import numpy as np
from Policy import StagePolicy, Policy
from Actions import Up, Down, Left, Right
from State import State

start = np.matrix('4;5')
end = np.matrix('6;6')
init_state = State(start, end)
U = [Up(), Down(), Left(), Right()]

U[0].do(init_state)