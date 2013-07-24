

class Connector:

    # TODO: have a way of verifying that the populations are what the connector is expecting?
    
    def __init__(self, simulator):
        self.S = simulator
        self.connections = []

    def add_connection(self, pre_tags, pre_portID, post_tags, post_portID):
        # note that pre and post are not uids but sets of tags...
        self.connections.append((pre_tags, post_tags, pre_portID, post_portID))

    def make_connection(self, pre_pop_tags, post_pop_tags):
        """ Instantiate connections between populations described by 
        pre_tags and post_tags """
        pre_pop  = self.S.filter_units(pre_pop_tags)
        post_pop = self.S.filter_units(post_pop_tags)
        # iterate through connections
        for pre_tags, post_tags, pre_portID, post_portID in connections:
            # get acual node uids
            pre  = self.S.filter_units(pre_tags, subset=pre_pop)
            post = self.S.filter_units(post_tags, subset=post_pop)
            # assert unique identification
            assert len(pre) == 1 and len(post) == 1
            # if so, go ahead and connect
            self.S.connect(pre, pre_portID, post, post_portID)
        



