import numpy as np
from Agent import Agent
import pylab
pylab.ion()
np.set_printoptions(precision=2)

maze = np.matrix('1 1 1 1 1 1 1 1; \
                  1 0 1 0 1 0 0 1; \
                  1 0 1 0 1 1 0 1; \
                  1 0 1 0 0 0 0 1; \
                  1 0 0 0 1 0 0 1; \
                  1 0 1 1 1 1 1 1; \
                  1 0 0 0 0 0 0 1; \
                  1 1 1 1 1 1 1 1')
goal = (6,6)

## Optimistic PI
agentpi = Agent(maze, 1.0, goal, 0, 1)

for i in range(13): # could run until policy stability
    for j in range(10): # 1 = could run until cost delta < d
        agentpi.evaluate()
    agentpi.improve()

## Value iteration
agentvi = Agent(maze, 1.0, goal, 0, 1)
for i in range(16):
    agentvi.valueit()
agentvi.improve()

pylab.matshow(agentpi.policy, cmap=pylab.cm.Spectral)
pylab.colorbar(fraction=0.05, ticks=[0,1,2,3,4])
pylab.draw()

pylab.matshow(agentvi.policy, cmap=pylab.cm.Spectral)
pylab.colorbar(fraction=0.05, ticks=[0,1,2,3,4])
pylab.draw()