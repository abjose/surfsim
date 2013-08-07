
import numpy as np

from unit import Unit


class ThreshUnit(Unit):
    # should probably do sigmoid

    def __init__(self, simulator, thresh, c, r0, rmax,
                 uid=None, tags=set(), ports={}):
        super(ThreshUnit, self).__init__(simulator, uid=uid, 
                                         tags=tags, ports=ports)
        self.set_port('input', 0)
        self.set_port('output', 0)

    def operation(self):
        # set rate to signal * c if signal > thresh, else r0.
        # could just do most recent...
        signal = np.array(self.ports['input'])
        signal[signal < thresh]  = r0
        signal[signal >= thresh] *= c
        self.set_port('output', signal)
        

if __name__ == '__main__':
    pass
