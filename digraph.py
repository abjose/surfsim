

class DiGraph:

    def __init__(self):
        self.graph = {} # {(start,end):value}
        self.IDs   = {} # {uid:object} ???
        self.curr_uid = 0 # fancier way? also, what if loading graph?

    def add_node(self, node_id):
        self.graph

    def get_connection(self, start, end):
        return self.graph.get((start,end), 0)

    def set_connection(self, start, end, value):
        self.graph[(start,end)] = value

    def predecessors(self, node_id):
        return [uid for uid in self.IDs.keys() 
                if self.get_connection(uid, node_id) != 0]

    def successors(self, node_id):
        return [uid for uid in self.IDs.keys() 
                if self.get_connection(node_id, uid) != 0]

    def get_uid(self):
        curr_uid += 1
        return self.curr_uid-1

"""
Have predecessors, successors
get_connection
this class could also take care of ensuring UID constraints
"""

    
