

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
        # like seriously, I think you can like chain them together
        # and then you wouldn't have to implement as many rules

    def make_population(self, pop_name, N):
        """ Instantiate N versions of A. """
        for uid in range(N):
            # update init things
            self.step()
            # insert instance
            # TODO: might not need to copy here...
            t = self.tags.copy()
            p = self.ports.copy()
            #print t | {pop_name, pop_name+str(uid)}
            #print p
            #self.A.make_instance(tags=self.tags| {pop_name, pop_name+str(uid)},
            #                     ports=self.ports)
            self.A.make_instance(tags=t | {pop_name, pop_name+str(uid)},
                                 ports=p)

        # SHOULD MAKE THIS AN ITERATOR INSTEAD?
