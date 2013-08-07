
from unit import Unit


class InputUnit(Unit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(InputUnit, self).__init__(simulator, uid=uid, 
                                        tags=tags, ports=ports)
        # Look at input_src object in ports and read pixel associated with
        # unit's position; set that as output.
        self.set_port('output', 0)

    def operation(self):
        #print self.ports['pos']
        # HACK! TODO: FIX
        if self.ports['pos'] == []:
            self.set_port('output', 0)
        else:
            val = self.ports['input_src'].get_pix(self.ports['pos'])
            self.set_port('output', val)
        

if __name__ == '__main__':
    pass
