
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

from unit import Unit

class ConvolutionUnit(Unit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(ConvolutionUnit, self).__init__(simulator, uid=uid, 
                                              tags=tags, ports=ports)
        self.set_port('input', 0)
        self.set_port('output', 0)
        self.IRF = None # impulse response function

    def operation(self):
        signal = self.ports['input']
        self.set_port('output', np.convolve(signal, self.IRF))
        # might want to enable "valid only" mode, like:
        #self.set_port('output', np.convolve(signal, self.IRF, mode='valid'))

    def show_irf(self):
        # plot kernel
        plt.plot(self.IRF)
        plt.show()
    
    def show_signal(self):
        # plot input
        plt.plot(self.ports['input'])
        plt.show()

    def show_convolution(self):
        plt.plot(np.convolve(self.ports['input'], self.IRF)
        plt.show()

if __name__ == '__main__':
    pass
