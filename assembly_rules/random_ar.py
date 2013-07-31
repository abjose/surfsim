
import numpy as np

from assembly_rule import AssemblyRule

class RandomAR(AssemblyRule):

    def __init__(self, simulator, assembler,
                 x0=0, y0=0, xl=10, yl=10):
        # distribution has mean of x0 and sd of xsd, scaled by xscale
        super(RandomAR, self).__init__(simulator, assembler)
        self.x0, self.y0 = x0, y0
        self.xl, self.yl = xl, yl

    def step(self):
        """ Update values with which Assembler objects will be initialized """
        x = (self.xl - self.x0) * np.random.rand() + self.x0
        y = (self.yl - self.y0) * np.random.rand() + self.y0
        self.ports['pos'] = (x,y)
        print x,y


if __name__ == '__main__':
    A = RandomAR(0,0, x0=5, y0=0, xl=15, yl=-20)

    for i in range(5):
        A.step()
