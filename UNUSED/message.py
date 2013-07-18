

class Message:
    
    def __init__(self, value):
        # hmm, is this too flexible?
        # would only be useful if you want more metadata... which I'm not sure
        # is necessary if you're going to use NetworkX
        # ...consider getting rid of this class
        self.value = value;
