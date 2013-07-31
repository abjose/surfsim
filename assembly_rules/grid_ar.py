
from assembly_rule import AssemblyRule

class GridAR(AssemblyRule):

    def __init__(self, simulator, assembler, 
                 x0=0, y0=0, xl=10, yl=10, dx=1, dy=1):
        # take steps in range [x0, xl) of size dx
        super(GridAR, self).__init__(simulator, assembler)
        self.x,  self.y  = x0, y0
        self.x0, self.y0 = x0, y0
        self.xl, self.yl = xl, yl
        self.dx, self.dy = dx, dy

    def step(self):
        """ Update values with which Assembler objects will be initialized """
        self.ports['pos'] = (self.x, self.y)
        if self.x+self.dx >= self.xl or self.dx == 0:
            # handle if too many instantiated?
            self.y = (self.y + self.dy) % self.yl
        self.x = (self.x + self.dx) % self.xl
        

if __name__ == '__main__':
    A = GridAR(0,0, x0=5, y0=0, xl=15, yl=20, dx=1, dy=0)

    for i in range(40):
        print A.x, A.y
        A.step()
