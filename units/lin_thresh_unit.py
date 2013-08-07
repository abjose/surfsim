
import numpy as np

from unit import Unit


class ThreshUnit(Unit):

    def __init__(self, simulator, uid=None,
                 tags=set(), ports={}):
        super(ThreshUnit, self).__init__(simulator, uid=uid, 
                                         tags=tags, ports=ports)
        self.set_port('input', 0)
        self.set_port('output', 0)

    def operation(self):
        theta = self.ports['theta']
        slope = self.ports['slope']
        signal = np.array(self.ports['input'])
        print signal, theta
        # TODO: HAX
        if theta == []:
            theta = 1
        signal[signal <= theta]  = theta
        signal[signal >  theta] *= slope
        self.set_port('output', signal)
        

if __name__ == '__main__':
    pass
