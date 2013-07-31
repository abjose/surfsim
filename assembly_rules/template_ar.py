
from assembly_rule import AssemblyRule

class TemplateAR(AssemblyRule):

    def __init__(self, simulator, assembler):
        super(TemplateAR, self).__init__(simulator, assembler)

    def step(self):
        """ Update values with which Assembler objects will be initialized. """
        raise NotImplementedError()
        # TODO: consider using lazyarrays
        pass
