

class TemplateCR(ConnectionRule):

    def __init__(self, simulator, connector, ):
        super(TemplateCR, self).__init__(simulator, connector)

    def update(self):
        """ Update values with which connections objects will be initialized """
        pass
   
    def should_connect(self, pre_group, post_group):
        """ Return True if groups should be connected, else False. """
        # TODO: consider using lazyarrays
        # TODO: after modifying connector so can add parameters to each edge
        #       should somehow have this so it can modify parameters for 
        #       each time connector connects things?
        raise NotImplementedError()

   
