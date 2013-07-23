
from unitgraph import UnitGraph


class Simulator(UnitGraph):

    def __init__(self):
        super(Simulator, self).__init__()

    def step_simulation(self):
        """ Step the elements of the simulation. """
        for n in self.G:
            self.G.node[n]['unit'].step()

if __name__ == '__main__':
    from units import *

    S = Simulator()
    S.add_unit(unit=IncrementUnit, label1='test1', group='g1')
    S.add_unit(unit=IncrementUnit, tags=['test2', 'g1'])
    S.add_unit(unit=IncrementUnit, tags=['test3', 'g1'])
    S.add_unit(unit=IncrementUnit, tags=set(['test4', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test5', 'g1']))
    S.add_unit(unit=SumUnit, tags=set(['adder', 'g1']))
    S.list_nodes()

    # TODO: verify one-to-many works
    # TODO: verify remove_port works

    # increment loop
    S.connect(0, 'output', 1, 'input')
    S.connect(1, 'output', 2, 'input')
    S.connect(2, 'output', 3, 'input')
    S.connect(3, 'output', 4, 'input')
    S.connect(4, 'output', 0, 'input')
    # sum things
    S.connect(0, 'output', 5, 'input')
    S.connect(1, 'output', 5, 'input')
    S.connect(2, 'output', 5, 'input')
    S.connect(3, 'output', 5, 'input')
    S.connect(4, 'output', 5, 'input')
    
    for i in range(5):
        S.step_simulation()
        S.list_nodes()

    S.show_graph()

    S.list_edges()

    #S.refresh_tags()
    #print S[1].__class__.__name__

