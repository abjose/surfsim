
from unit import Unit


class BiphasicUnit(IRFUnit):
    
    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        super(TemplateUnit, self).__init__(simulator, uid=uid, 
                                           tags=tags, ports=ports)
        # declare ports like: self.set_port('port_name', [initial value])
        # you can set these ports to 'listen' to other ports with
        # connect (a Simulator function)

    # might have impulse response look something like
    # A*(2*(t**2)*np.exp(1.25*-t) - 0.005*(t**6)*np.exp(1*-t))
    # where A initially equals 1 and can be shifted towards 0 to 
    # get smaller and smaller curves
    # note that currently goes up and then dips down - might need to flip around
    # by making A negative...

    def operation(self):
        # using the ports you declared in __init__, do the necessary operations
        # using your input ports and update your output ports
        print "Template unit -- why are you using me??"
        # function like at**x * exp(-t)

if __name__ == '__main__':
    pass
