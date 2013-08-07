
import numpy as np

from connection_rule import ConnectionRule

class FixedNumRandCR(ConnectionRule):

    def __init__(self, simulator, connector, n, pre_size, post_size):
        # connect pre unit to n post units randomly
        assert n <= post_size
        super(FixedNumRandCR, self).__init__(simulator, connector)
        # need to know the size of both populations - really need as arg??
        # not sure how to know otherwise if don't have tags yet...
        # pre-generate connection array - i (pre) is row, j (post) is column
        # hard to make unique...this is ugly
        self.cm = []
        for i in range(pre_size):
            self.cm.append([True]*n + [False]*(post_size-n))
        for i in self.cm:
            np.random.shuffle(i)   
        

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass
   
    def should_connect(self, pre_group, post_group):
        """ Return True if groups should be connected, else False. """
        # this isn't quite right - need a mapping from group to number...
        # TODO: add this mapping
        return self.cm[pre_group][post_group]
