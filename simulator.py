
import networkx as nx


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

    def add_unit(self, unit=PrototypeUnit, uid=None, tags=set(), ports={}):
        """ Add a unit to the graph. """
        uid = uid if uid != None else self.get_uid()
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
        print '\nNETWORK NODES:'
        for n in self.G:
            nu = self.G.node[n]['unit']
            print 'Node ' + str(n) + '\tPorts:', nu.ports
        print

if __name__ == '__main__':
    S = Simulator()
    S.add_unit(unit=IncrementUnit, tags=set(['test1', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test2', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test3', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test4', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test5', 'g1']))
    S.add_unit(unit=SumUnit, tags=set(['adder', 'g1']))
    S.list_nodes()

    # verify one-to-many works
    # verify many-to-one works
    # should make a list_connections function (like list_nodes)

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

    S.refresh_tags()

    print S['test1'].ports
    print S[0].ports
