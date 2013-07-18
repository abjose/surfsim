

class Population:

    def __init__(self, size, unit_class, structure=None, label=None):
        # should have a size itself...think of as a 'canvas' on which
        # Units are being painted
        self.size = size
        self.unit_class = unit_class
        self.structure = structure
        self.label = label
        self.elements = [] # call units?

    """
    There should be some kind of 'get_ports' function in Unit (or just
    get them normally) so that you can specify connections over port types
    """

    def describe(self):
        pass

    def generate_units(self, n):
        pass
