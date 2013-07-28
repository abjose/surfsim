
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
    from assembler import Assembler
    from connector import Connector
    
    # TODO: verify one-to-many works
    # TODO: verify remove_port works

    # instantiate simulator
    S = Simulator()

    # add some units
    S.add_unit(unit=IncrementUnit, label1='test1', group='g1')
    S.add_unit(unit=IncrementUnit, tags=['test2', 'g1'])
    S.add_unit(unit=IncrementUnit, tags=set(['test3', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test4', 'g1']))
    S.add_unit(unit=IncrementUnit, tags=set(['test5', 'g1']))
    S.add_unit(unit=SumUnit,       tags=set(['adder', 'g1']))

    # print out current nodes
    # S.list_nodes()

    # connect increment units into a loop
    S.connect(0, 'output', 1, 'input')
    S.connect(1, 'output', 2, 'input')
    S.connect(2, 'output', 3, 'input')
    S.connect(3, 'output', 4, 'input')
    S.connect(4, 'output', 0, 'input')
    # connect all increment units to a sum unit
    S.connect(0, 'output', 5, 'input')
    S.connect(1, 'output', 5, 'input')
    S.connect(2, 'output', 5, 'input')
    S.connect(3, 'output', 5, 'input')
    S.connect(4, 'output', 5, 'input')
    # TODO: allow passing lists to connect, so this could be
    # S.connect([0,1,2,3,4], 'output', 5, 'input') or something
    
    # display current edges
    S.list_edges()

    # step the simulation
    for i in range(5):
        S.step_simulation()
        S.list_nodes()

    S.show_graph()

    #S.refresh_tags()
    #print S[1].__class__.__name__

    # Make an Assembler instance
    A = Assembler(S, tags={'test_group'})
    
    # Copy an example graph into the assembler
    A.G = S.G.copy()

    # Insert instances of the Assembler into the simulation
    A.make_instance(tags={'group_a'})
    A.make_instance(tags={'group_b'})
    A.make_instance(tags={'group_c'})
    A.make_instance(tags={'group_d'})

    S.show_graph()

    # Make a Connecor instance
    C = Connector(S)

    # Add a template connection to the Connector
    C.add_connection({'test1'}, 'output', {'test1'}, 'input')
    C.add_connection({'test3'}, 'output', {'test3'}, 'input')
    C.add_connection({'test5'}, 'output', {'test5'}, 'input')

    # Connect group_a and group_b in the way specified
    self.S.filter_units(pre_pop_tags)
    C.make_connection(self.S.filter_units({'test_group', 'group_a'}), 
                      self.S.filter_units({'test_group', 'group_b'}))

    S.show_graph()

    #S.step_simulation()
    #S.list_nodes()
