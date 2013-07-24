
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
    # TODO: allow passing lists to connect, so this could be
    # S.connect([0,1,2,3,4], 'output', 5, 'input') or something
    S.connect(0, 'output', 5, 'input')
    S.connect(1, 'output', 5, 'input')
    S.connect(2, 'output', 5, 'input')
    S.connect(3, 'output', 5, 'input')
    S.connect(4, 'output', 5, 'input')
    
    for i in range(5):
        S.step_simulation()
        S.list_nodes()

    #S.show_graph()

    S.list_edges()

    #S.refresh_tags()
    #print S[1].__class__.__name__


    A = Assembler(S, tags={'test_group'})
    
    # after testing, take subgraph...also show adding manually
    A.G = S.G.copy()
    #A.show_graph()

    A.make_instance({'group_a'})
    A.make_instance({'group_b'})
    A.make_instance({'group_c'})
    A.make_instance({'group_d'})

    S.list_nodes()

    #S.show_graph()


    C = Connector(S)

    C.add_connection({'test1'}, 'output', {'test1'}, 'input')
    C.add_connection({'test3'}, 'output', {'test3'}, 'input')
    C.add_connection({'test5'}, 'output', {'test5'}, 'input')

    C.make_connection({'test_group', 'group_a'}, 
                      {'test_group', 'group_b'})

    S.list_edges()
    S.show_graph()
