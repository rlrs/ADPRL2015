import numpy as np
from State import State
from Actions import Action, Up, Down, Left, Right

class Agent(object):
    def __init__(self, maze, discount, goal, goalcost, movecost):
        self.maze = maze
        self.V = np.zeros_like(maze, dtype=np.float)
        self.policy = np.zeros_like(maze) # Policy is just a matrix of numbers corresponding to actions
        self.gamma = discount
        self.actions = [Action(), Up(), Down(), Left(), Right()] # Action() is no action
        self.goal = goal
        self.goalcost = goalcost
        self.movecost = movecost
        
    def free(self):
        """ Get all free (non-wall) positions in maze """
        res = []
        for pos, val in np.ndenumerate(self.maze):
            if val == 0:
                res.append(pos)
        return res
        
    def actionset(self, state):
        """ Returns set of actions possible in state, used for staying in goal state """
        if state.pos == self.goal:
            return [Action()]
        else:
            return self.actions
        
    def evaluate(self):
        """ One iteration of in-place policy evaluation """
        free = self.free()
        for pos in free:
            (y,x) = pos
            if pos == self.goal: # I know this is not the 'correct' way, but now no artificial state is needed :)
                self.V[y,x] = self.goalcost
                continue
            s = State((y,x)) 
            a = self.actions[self.policy[y,x]]
            ss = a.do(s)
            self.V[y,x] = self.cost(s, ss) + self.gamma*self.V[ss.pos[0], ss.pos[1]]
        return
        
    def improve(self):
        """ Policy improvement """
        free = self.free()
        for pos in free:
            (y,x) = pos
            s = State((y,x))
            best = np.finfo(dtype=np.float).max
            besta = None
            for na in range(len(self.actionset(s))):
                a = self.actions[na]
                ss = a.do(s)
                if self.is_wall(ss):
                    continue
                Vss = self.cost(s, ss) + self.gamma*self.V[ss.pos[0], ss.pos[1]]
                if Vss < best:
                    best = Vss
                    besta = na
            self.policy[y,x] = besta
        return
        
    def valueit(self):
        """ One iteration of value iteration: J = TJ """
        free = self.free()
        for pos in free:
            (y,x) = pos
            if pos == self.goal:
                self.V[y,x] = self.goalcost
                continue
            s = State((y,x)) 
            best = np.finfo(dtype=np.float).max
            for a in self.actionset(s):
                ss = a.do(s)
                if self.is_wall(ss):
                    continue
                Vss = self.cost(s, ss) + self.gamma*self.V[ss.pos[0], ss.pos[1]]
                if Vss < best:
                    best = Vss
            self.V[y,x] = best
        return
        
    def is_wall(self, state):
        return self.maze[state.pos[0], state.pos[1]]
        
    def cost(self, state, sstate):
        """ Cost for going from state to sstate (action implicit) """
        if state.pos == self.goal:
            return 0
        else:
            return self.movecost