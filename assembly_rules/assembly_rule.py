

class AssemblyRule(object):

    def __init__(self, simulator, assembler):
        # allow objects aside from assemblers?
        self.S = simulator
        self.A = assembler
        self.tags  = set()
        self.ports = {}

    def step(self):
        """ Update values with which Assembler objects will be initialized """
        raise NotImplementedError()
        # TODO: consider using lazyarrays
        pass

    def make_population(self, pop_name, N):
        """ Instantiate N versions of A. """
        for uid in range(N):
            # update init things
            self.step()
            # insert instance
            self.A.make_instance(tags=self.tags | {pop_name, pop_name+str(uid)},
                                 ports=self.ports)

        # SHOULD MAKE THIS AN ITERATOR INSTEAD?
