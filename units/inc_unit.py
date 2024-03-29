
from unit import Unit


class IncrementUnit(Unit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(IncrementUnit, self).__init__(simulator, uid=uid, 
                                            tags=tags, ports=ports)
        self.set_port('input', 0)
        self.set_port('output', 0)

    def operation(self):
        val = self.ports['input'][0]
        self.set_port('output', val+1)


if __name__ == '__main__':
    u1 = IncrementUnit(None, 20)
    print u1.ports
    u1.operation()
    print u1.ports
