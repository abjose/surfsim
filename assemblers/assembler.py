
from unitgraph import UnitGraph
from units import *


class Assembler(UnitGraph):
    
    def __init__(self, simulator, tags=set(), ports={}):
        super(Assembler, self).__init__()
        self.S     = simulator # simulator to insert instances in to
        self.tags  = tags.copy()
        self.ports = ports.copy()

    def make_instance(self, tags=set(), ports={}):
        """ Instantiate an instance of G in S. """
        # abstract:instance uid mapping
        uid_map = {} 
        # add nodes
        for uid in self.G:
            uid_map[uid] = self.S.curr_uid # get the current uid
            u = self.G.node[uid]['unit']
            ports = dict(u.ports.items() + self.ports.items() + ports.items())
            self.S.add_unit(unit  = eval(u.__class__.__name__),
                            tags  = u.tags | self.tags | tags, 
                            ports = ports)
        # add edges
        for a,b in self.G.edges():
            pre,post = uid_map[a], uid_map[b]
            edge_map = self.G[a][b]['maps']
            self.S.connect_with_map(pre, post, edge_map)

        # SHOULD MAKE THIS AN ITERATOR INSTEAD?
