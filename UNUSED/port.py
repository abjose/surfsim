

class Port:
    
    def __init__(self, name, owner, message=None, multi_input=False):
        self.name = name
        self.owner = owner
        self.multi_input = multi_input
        self.message = message
        # need to know whether it's input or output?


    def update(self):
        pass

    def describe(self):
        pass
    
