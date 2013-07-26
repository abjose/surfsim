

class ConnectionRule:

    def __init__(self, simulator, connector, ):
        self.S = simulator
        self.C = connector
        #self.attrs = {}

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass
    def should_connect(self, i, j):
        """ Return true if elements should be connected, else false. """
        # TODO: consider using lazyarrays
        # should you pass unit objects or indices? note that they're not
        # actually units but collections of units...
        pass

    def make_connections(self, pre_pop_tags, post_pop_tags, 
                         pre_pop=None, post_pop=None):
        # pre and post populations must have incremental names like pop1, pop2..
        # iterate through every element in pre and post, connect if should_connect
        # just add a get_next function? make an iterator or whatever?
        # and it just keeps going until none left

        # should pre and post be sets of uids or sets of tags?
        # can do lots of interesting things with sets of uids using chains
        # of filter commands...
        # why not both?
        # if change this, should probably change connector too...
        for i,pre_uid in iterate(self.S.filter_units(pre))

        # so need to filter things with tags (unless pops given)
        # then need to...append numbers to pop tags? so pop tags have to be
        # given?
