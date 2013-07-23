
import networkx as nx
import matplotlib.pyplot as plt

from units import *


"""
You should really read about/make tests for this project!!
"""

class Simulator:

    def __init__(self):
        self.G    = nx.DiGraph()
        self.tags = {} # store label:uid mapping
        self.curr_uid = 0

    #def __setitem__(self, key, value):
    def __getitem__(self, key):
        uid = self.tags[key].copy()
        if len(uid) != 1:
            raise KeyError("non-unique identifier in __getitem__")
        return self.G.node[uid.pop()]['unit']

    def add_unit(self, unit=PrototypeUnit, uid=None, 
                 tags=set(), ports={}, **kwargs):
        """ Add a unit to the graph. Extra labeld args are treated as tags. """
        uid = uid if uid != None else self.get_uid()
        tags = set(tags) | set(kwargs.values())
        self.G.add_node(uid, unit=unit(self, uid=uid, tags=tags, ports=ports))

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
        for n in self.G:
            self.G.node[n]['unit'].step()

    def refresh_tags(self):
        """ Build dict of sets of uids from tags. Premature optimization! :( """
        d = {}
        for uid in self.G:
            # add so tags give identity for uid...laziness
            d[uid] = set([uid])
            # now build other tags
            for t in self.G.node[uid]['unit'].tags:
                d.setdefault(t,set()).add(uid) # or |= u
        self.tags = d

    def get_uid(self):
        self.curr_uid += 1
        return self.curr_uid-1

    def list_nodes(self):
        """ Print node data. """
        print 'NETWORK NODES:'
        data = []
        for n in self.G:
            nu = self.G.node[n]['unit']
            temp =  ['Node ' + str(n)]
            temp += ['Tags: ' + str(nu.tags)]
            temp += ['Ports: ' + str(nu.ports)]
            data.append(temp)
        self.print_with_columns(data)
        print

    def list_edges(self):
        """ Print edge data. """
        # TODO: sort edges?
        print 'NETWORK EDGES:'
        data = []
        for a,b in self.G.edges():
            edge = self.G[a][b]
            temp =  ['Edge ' + str(a) + ' -> ' + str(b)]
            temp += ['Maps: ' + str(edge['maps'])]
            data.append(temp)
        self.print_with_columns(data)
        print

    def print_with_columns(self, data):
        """ Print things nicely. """
        w = [max(map(len, col)) for col in zip(*data)]
        for row in data:
            print "    ".join((val.ljust(width) for val, width in zip(row, w)))

    def show_graph(self):
        """ Display a graphical representation of the graph. """
        nx.draw(S.G)
        plt.show()

if __name__ == '__main__':
    S = Simulator()
    S.add_unit(unit=IncrementUnit, label1='test1', group='g1')
    S.add_unit(unit=IncrementUnit, tags=['test2', 'g1'])
    S.add_unit(unit=IncrementUnit, tags=['test3', 'g1'])
    S.add_unit(unit=IncrementUnit, tags=set(['test4', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test5', 'g1']))
    S.add_unit(unit=SumUnit, tags=set(['adder', 'g1']))
    S.list_nodes()

    # TODO: verify one-to-many works
    # TODO: verify remove_port works

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
    
    for i in range(5):
        S.step_simulation()
        S.list_nodes()

    S.list_edges()

    #S.refresh_tags()
    #print S[1].__class__.__name__

