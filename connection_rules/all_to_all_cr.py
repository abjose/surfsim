
from connection_rule import ConnectionRule

class AllToAllCR(ConnectionRule):

    def __init__(self, simulator, connector, ):
        super(AllToAllCR, self).__init__(simulator, connector)

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass
   
    def should_connect(self, pre_group, post_group):
        """ Return True if groups should be connected, else False. """
        return True #lol
