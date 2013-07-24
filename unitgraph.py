
import networkx as nx
import matplotlib.pyplot as plt

from units import *


"""
You should really read about/make tests for this project!!

"""

class UnitGraph(object):

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
    
    def filter_nodes(self, tags):
        """ Return a SET of uids matching all specified tags. """ 
        # Can do math with resultant sets!
        # also allow filtering on...uids, port names?
        # could also use self.tags, just union all relevant sets
        return {n for n in self.G if tags <= self.G.node[n]['unit'].tags}
        
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
        nx.draw(self.G)
        plt.show()


if __name__ == '__main__':
    pass

