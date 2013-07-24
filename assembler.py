
import networkx as nx


class Assembler(UnitGraph):
    
    def __init__(self, simulator, tags=set()):
        super(Assembler, self).__init__()
        self.S    = simulator # simulator to insert instances in to
        self.tags = tags
        


    def set_graph(self, G):
        # add own tags for every node in graph
        for n in G:
            G.node[n]['unit'].tags |= self.tags
    
    def copy_graph(self):
        """ Make a deep copy of the graph. """
        # Are you sure this is enough of a copy?!
        # need to differentiate...so insert tags at copy-time?
        # can differentiate just by calling get_uid!
        return self.G.copy()
# also perhaps allow for adding special/specific names when inserting instances...
