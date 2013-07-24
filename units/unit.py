
class Unit(object):

    def __init__(self, simulator, uid=None, tags=set(), ports={}):
        """ Initialize the unit. """
        self.S = simulator
        self.uid   = uid if uid != None else self.S.get_uid()
        self.tags  = tags.copy()  # caution!! must copy or just have reference
        self.ports = ports.copy() # includes input, output, parameters?

    def step(self):
        """ Step the Unit. """
        self.update_input()
        self.operation()
    
    def operation(self):
        # need to use inputs, set outputs
        raise NotImplementedError()

    def describe(self):
        pass

    def set_port(self, portID, value):
        """ Update specified output port's value; add port if nonexistent. """
        # Bad form!
        try:
            self.ports[portID] = list(value)
        except TypeError:
            self.ports[portID] = value

    def remove_port(self, portID):
        if key in self.ports:
            del self.ports[portID]
            for p,s in self.S.G.in_edges(self.uid):
                # for every incoming edge, remove port if found
                if portID in self.S.G.edge[p][s]['maps']:
                    del self.S.G.edge[p][s]['maps'][portID]

    def update_input(self):
        """ Update all ports with values of ports they connect to.  """
        edges = self.S.G.in_edges(self.uid)
        for postpid in self.ports:
            data = []
            for p,s in edges:
                maps = self.S.G.edge[p][s]['maps']
                if postpid in maps:
                    pre = self.S.G.node[p]['unit']
                    data += [pre.ports[prepid] for prepid in maps[postpid]]
            self.set_port(postpid, data)
            


if __name__=="__main__":
    pass
