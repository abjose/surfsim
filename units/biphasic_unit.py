
from irf_unit import IRFUnit
import numpy as np

class BiphasicUnit(IRFUnit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(BiphasicUnit, self).__init__(simulator, uid=uid, 
                                           tags=tags, ports=ports)
        # should definitely make other parameters available to modfiy
        # note: currently goes up and then dips down, might need to flip around
        super(BiphasicUnit, self).__init__(simulator, uid=uid, 
                                           tags=tags, ports=ports)
        self.history = np.array([]) # ensure history isn't None
        A = ports['A']
        t = np.arange(0,16,0.1)
        self.IRF = A*(2*(t**2)*np.exp(1.25*-t) - 0.005*(t**6)*np.exp(1*-t))
        self.IRF /= sum(self.IRF)

if __name__ == '__main__':
    bu = BiphasicUnit(None, uid=1, ports=dict(A=-1))
    bu.ports['input'] = np.random.randn(500)
    bu.show_irf()
    bu.show_signal()
    bu.show_convolution()

