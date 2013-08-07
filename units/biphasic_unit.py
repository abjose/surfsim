
from irf_unit import IRFUnit
import numpy as np

class BiphasicUnit(IRFUnit):
    
    def __init__(self, simulator, A, uid=None, tags=set(), ports={}):
        super(BiphasicUnit, self).__init__(simulator, uid=uid, 
                                           tags=tags, ports=ports)
        # should definitely make other parameters available to modfiy
        # note: currently goes up and then dips down, might need to flip around
        super(BiphasicUnit, self).__init__(simulator, uid=uid, 
                                           tags=tags, ports=ports)
        t = np.arange(0,16,0.1)
        self.IRF = A*(2*(t**2)*np.exp(1.25*-t) - 0.005*(t**6)*np.exp(1*-t))

if __name__ == '__main__':
    bu = BiphasicUnit(None, 1, uid=1)
    bu.show_irf()
