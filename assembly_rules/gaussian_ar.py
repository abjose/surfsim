
import numpy as np

from assembly_rule import AssemblyRule

class GaussianAR(AssemblyRule):

    def __init__(self, simulator, assembler,
                 x0=0, y0=0, xscale=20, yscale=20, xsd=1, ysd=1):
        # distribution has mean of x0 and sd of xsd, scaled by xscale
        super(GaussianAR, self).__init__(simulator, assembler)
        self.x0, self.y0 = x0, y0
        self.xscale, self.yscale = xscale, yscale
        self.xsd, self.ysd = xsd, ysd

    def step(self):
        """ Update values with which Assembler objects will be initialized """
        x = np.random.normal(loc=0, scale=self.xsd) * self.xscale + self.x0
        y = np.random.normal(loc=0, scale=self.ysd) * self.yscale + self.y0
        self.ports['pos'] = (x,y)
        print x,y

if __name__ == '__main__':
    A = GaussianAR(0,0, x0=0, y0=0, xscale=50, yscale=1)

    for i in range(5):
        A.step()
