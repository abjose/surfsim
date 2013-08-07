
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

from unit import Unit

class IRFUnit(Unit):
    # would be pretty nice to have some kind of generic 'tune' function
    # that lets you control the parameters of the function...
    # ...could just move these things into unit.py?
    # should instead have one 'linear filter' unit with multiple 
    # filters to select from, another 'nonlinear filter'...
    # should IRF just be another port?!
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(IRFUnit, self).__init__(simulator, uid=uid, 
                                      tags=tags, ports=ports)
        # should probably initialize to a vector of 0s rather than just 0?
        self.set_port('input', 0)
        self.set_port('output', 0)
        self.IRF = None # impulse response function
        self.history = None # if not None, assume temporal filter

    def operation(self):
        signal = self.ports['input']
        if signal == []:
            signal = [0]
        print 'meow', signal
        if self.history != None: # temporal
            # convention: newest sample goes at end of history array
            #self.history = np.append(self.history, signal[-1]) # append last
            #HACK! TODO: fix
            self.history = np.append(self.history, signal[0]) # append first
            self.set_port('output', np.convolve(self.history, 
                                                self.IRF, mode='valid'))
        else:
            self.set_port('output', np.convolve(signal, self.IRF, mode='valid'))


    def show_irf(self):
        # plot kernel
        plt.plot(self.IRF)
        plt.show()
    
    def show_signal(self):
        # plot input
        plt.plot(self.ports['input'])
        plt.show()

    def show_convolution(self):
        plt.plot(np.convolve(self.ports['input'], self.IRF, mode='valid'))
        plt.show()

if __name__ == '__main__':
    pass
