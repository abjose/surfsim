
from unit import Unit


class SigmoidUnit(Unit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(SigmoidUnit, self).__init__(simulator, uid=uid, 
                                          tags=tags, ports=ports)

    def operation(self):
        pass

if __name__ == '__main__':
    pass
