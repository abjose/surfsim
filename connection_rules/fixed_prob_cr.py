
import numpy as np

class TemplateCR(ConnectionRule):

    def __init__(self, simulator, connector, P):
        # P in [0, 1] is prob. to connect group i in pre to group j in post
        # 0 never connects, 1 always does (all to all)
        super(TemplateCR, self).__init__(simulator, connector)
        self.P = P

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass
   
    def should_connect(self, pre_group, post_group):
        """ Return True if groups should be connected, else False. """
        return np.random.rand() < self.P

   
