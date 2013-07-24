



class Connector:
    
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
        

"""
-so need to store connection set between two collections of units
-should have a way of verifying that the two collections are what the connector is expecting?
-guess this also needs an 'add connection' thing to describe pre,pre_port, post,post_port stuff...where pre/post are sufficient sets of tags to describe the unit within the population that will be connected
-then have an make_connection things that is passed two sets of tags that should uniquely define the populations to connect
-then basically just call connect a few times...
"""

