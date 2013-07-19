
from unit import Unit



class SumUnit(Unit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(SumUnit, self).__init__(simulator, uid=uid, 
                                      tags=tags, ports=ports)
        self.set_port('input', 0)
        self.set_port('sum', 0)

    def operation(self):
        val = self.ports['input']
        self.set_port('sum', sum(val))



if __name__ == '__main__':
    pass
