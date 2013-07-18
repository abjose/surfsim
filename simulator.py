
import networkx as nx

#from inc_unit import IncrementUnit
from units import *


"""
You should really read about/make tests for this project!!
"""

class Simulator:

    def __init__(self):
        self.G = nx.DiGraph()
        self.labels   = {} # store label:uid mapping
        self.curr_uid = 0

    #def __setitem__(self, key, value):
    #def __getitem__(self, key):
        # TODO: handle improper keys with keyerror exceptions and stuff
        # TODO: allow to use uid instead of label too?

    def add_unit(self, unit=PrototypeUnit, uid=None, tags=set(), ports={}, 
                 label=None):
        """ Add a unit to the graph. """
        uid = uid if uid != None else self.get_uid()
        self.G.add_node(uid, unit=unit(self, uid=uid, tags=tags, ports=ports))
        if label != None:
            # TODO: should these be stored anywhere else? any way to keep them
            # solely in the graph?
            self.labels[label] = uid

    def connect(self, pre, pre_portID, post, post_portID):
        """ If connection doesn't exist, make it; otherwise just add map. """
        # verify both nodes exist...
        assert pre in self.G and post in self.G
        if post not in self.G.node[pre]:
            self.G.add_edge(pre, post, maps=dict())
            self.G.edge[pre][post]['maps'][post_portID] = [pre_portID]
        else:
            self.G.edge[pre][post]['maps'][post_portID].append(pre_portID)

    def step_simulation(self):
        """ Step the elements of the simulation. """
        for n in self.G.nodes():
            self.G.node[n]['unit'].step()

    def get_uid(self):
        self.curr_uid += 1
        return self.curr_uid-1

    def list_nodes(self):
        print '\nNETWORK NODES:'
        for n in self.G:
            nu = self.G.node[n]['unit']
            print 'Node ' + str(n) + '\tPorts:', nu.ports
        print

if __name__ == '__main__':
    S = Simulator()
    S.add_unit(unit=IncrementUnit)
    S.add_unit(unit=IncrementUnit)
    S.add_unit(unit=IncrementUnit)
    S.add_unit(unit=IncrementUnit)
    S.add_unit(unit=IncrementUnit)
    S.add_unit(unit=SumUnit)
    S.list_nodes()

    # verify one-to-many works
    # verify many-to-one works
    # REALLLLLLLLY need labeling....
    # should make a list_connections thing too

    # increment loop
    S.connect(0, 'output', 1, 'input')
    S.connect(1, 'output', 2, 'input')
    S.connect(2, 'output', 3, 'input')
    S.connect(3, 'output', 4, 'input')
    S.connect(4, 'output', 0, 'input')
    # sum things
    S.connect(0, 'output', 5, 'input')
    S.connect(1, 'output', 5, 'input')
    S.connect(2, 'output', 5, 'input')
    S.connect(3, 'output', 5, 'input')
    S.connect(4, 'output', 5, 'input')

    print S.G.edges()
    
    for i in range(5):
        S.step_simulation()
        S.list_nodes()


