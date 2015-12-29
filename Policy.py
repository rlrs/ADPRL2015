class StagePolicy(object):
    pass

class Policy(object):
    def __init__(self):
        self.cur_it = 0
        self.stages = []
    
    def __len__(self):
        return len(self.stages)
        
    def __iter__(self):
        return self
    
    def next(self):
        if(self.cur_it == len(self)):
            raise StopIteration
        else:
            self.cur_it += 1
            return self.stages[self.cur_it]
            
    def add(self, stage_pol):
        self.stages.append(stage_pol) 