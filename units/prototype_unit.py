
from unit import Unit

"""
Make this a unit that has lots of functionality to allow customization 
'on-the-fly' as in the pseudocode demo
"""


class PrototypeUnit(Unit):
    
    def __init__(self, simulator, uid=None):
        super(PrototypeUnit, self).__init__(simulator, uid=uid, 
                                            tags=tags, ports=ports)
        self.set_port('input', [0])
        self.set_port('output', [0])

    def operation(self):
        val = self.ports['input'][0]
        self.set_port('output', [val+1])



if __name__ == '__main__':
    pass
