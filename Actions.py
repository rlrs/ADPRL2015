class Action(object):
    def __init__(self):
        pass
        
    def is_wall(self, state, dy, dx):
        return state.map[state.pos[0]+dy, state.pos[1]+dx]
        
    def do(self, state):
        pass
        
class Up(Action):
    def do(self, state):
        if self.is_wall(state, -1, 0):
            return state
        else:
            state.pos[0] -= 1
            return state
        
class Down(Action):
    def do(self, state):
        if self.is_wall(state, 1, 0):
            return state
        else:
            state.pos[0] += 1
            return state
        
        
class Left(Action):
    def do(self, state):
        if self.is_wall(state, 0, -1):
            return state
        else:
            state.pos[1] -= 1
            return state
        
        
class Right(Action):
    def do(self, state):
        if self.is_wall(state, 0, 1):
            return state
        else:
            state.pos[1] += 1
            return state
        