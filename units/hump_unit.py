
from unit import Unit


class TemplateUnit(Unit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(TemplateUnit, self).__init__(simulator, uid=uid, 
                                           tags=tags, ports=ports)
        # declare ports like: self.set_port('port_name', [initial value])
        # you can set these ports to 'listen' to other ports with
        # connect (a Simulator function)

    def operation(self):
        # using the ports you declared in __init__, do the necessary operations
        # using your input ports and update your output ports
        print "Template unit -- why are you using me??"
        # function like at**x * exp(-t)

if __name__ == '__main__':
    pass
