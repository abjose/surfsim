
from units import InputUnit
from assembler import Assembler
# need to do something like surfsim.units import InputUnit?

class InputAssembler(Assembler):

    def __init__(self, simulator, AR, tags=set(), ports={}):
        print 'input-tags', tags
        print 'input-ports', ports
        ports.update(dict(input_src=AR))
        super(InputAssembler, self).__init__(simulator, tags=tags, ports=ports)
        #ports.update(dict(input_src=AR))
        self.add_unit(unit  = InputUnit, 
                      tags  = tags | {'input_unit'}, 
                      ports = ports)
