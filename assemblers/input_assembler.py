
from assembler import Assembler
# need to do something like surfsim.units import InputUnit?
from units import InputUnit

class InputAssembler(Assembler):

    def __init__(self, simulator, AR, tags=set(), ports={}):
        super(InputAssembler, self).__init__(simulator, tags=tags, ports=ports)
        self.add_unit(unit=InputUnit, ports=dict(input_src=AR))
