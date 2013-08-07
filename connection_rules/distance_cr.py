
import numpy as np

from connection_rule import ConnectionRule

class DistanceCR(ConnectionRule):

    def __init__(self, simulator, connector, dist):
        # connect pre unit to post units with probability a function of distance
        super(DistanceCR, self).__init__(simulator, connector)
        self.thresh = dist

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass
   
    def should_connect(self, pre_group, post_group):
        """ Return True if groups should be connected, else False. """
        # get sample units
        pre_unit  = pre_group.pop()
        post_unit = post_group.pop()
        # get positions -- will raise an exception if no position found?
        #print self.S.G.node[pre_unit]['unit'].ports#['pos']
        pre_pos  = self.S.G.node[pre_unit]['unit'].ports['pos']
        post_pos = self.S.G.node[post_unit]['unit'].ports['pos']
        # get distance
        d = np.linalg.norm([pre_pos, post_pos])
        # return sample units :/
        pre_group.add(pre_unit)
        post_group.add(post_unit)
        # decide on connection
        diff = abs(self.thresh - d)/float(self.thresh + d) # is this good?
        return np.random.rand() < (1-diff)
