

class Connector(object):

    # TODO: have a way of verifying that the populations are what the connector is expecting?
    # TODO: add something to add extra attributes (like weight) to an edges
    
    def __init__(self, simulator):
        self.S = simulator
        self.connections = []

    def add_connection(self, pre_tags, pre_portID, post_tags, post_portID):
        # note that pre and post are not uids but sets of tags...
        self.connections.append((pre_tags, post_tags, pre_portID, post_portID))

    def make_connection(self, pre_pop, post_pop):
        """ Instantiate connections between populations """
        #if pre_pop == None and post_pop == None:
        #    pre_pop  = self.S.filter_units(pre_pop_tags)
        #    post_pop = self.S.filter_units(post_pop_tags)
        # iterate through connections
        for pre_tags, post_tags, pre_portID, post_portID in self.connections:
            # get acual node uids
            pre  = self.S.filter_units(pre_tags, subset=pre_pop)
            post = self.S.filter_units(post_tags, subset=post_pop)
            # assert unique identification
            assert len(pre) == 1 and len(post) == 1
            # if so, go ahead and connect
            self.S.connect(pre.pop(), pre_portID, post.pop(), post_portID)
        



