

if __name__=='__main__':

    import numpy as np
    import matplotlib.pyplot as plt

    # TODO: make sure input is 100x100

    from simulator  import Simulator
    from assemblers import BCMAssembler, InputAssembler
    from connectors import Connector
    from assembly_rules   import GridAR, InputAR, SinusoidInput 
    from connection_rules import DistanceCR 

    # initialize simulator
    S = Simulator()

    # create stimulus layer
    size    = 100
    spacing = 0.1
    freq    = 5
    amp     = 1
    step    = .5
    sin = SinusoidInput(size, spacing, freq, amp, step)
    input_layer = InputAR(S, sin)
    input_layer.make_population('input_group', 1000) # should make 10000?
    # or make stimulus smaller...

    plt.ion()

    for i in range(20):
        plt.cla()
        plt.imshow(sin.output, cmap='Greys')
        plt.draw()
        sin.step()
        raw_input()
    plt.cla()
    plt.ioff()

    # initialize BCM assembler
    bcm = BCMAssembler(S, 0,0,10)
    bcm.show_graph()

    # make a layer of BCMs
    bcm_layer = GridAR(S, bcm, xl=100, yl=100, dx=5, dy=5)
    bcm_layer.make_population('bcm_group', 100)
    S.show_graph()

    # make connector for connecting input units and BCM temporal units
    input_bcm_connector = Connector(S)
    # are these tags right/sufficient?
    input_bcm_connector.add_connection({'input_unit'}, 'output', 
                                       {'bph_unit'},   'input')

    # make connections based on distance between input and BCMs
    # Want to connect individually, not based on group
    input_cr = DistanceCR(S, input_bcm_connector, 1)
    #print S.filter_units({'input_unit'})
    #print S.filter_units({'bph_unit'})
    input_cr.make_individual_connections(S.filter_units({'input_unit'}),
                                         S.filter_units({'bph_unit'}))
    
    # WARNING: this is wrong, will also delete their connections to other things
    # verify each bcm input is connected to <= 1 input
    # could maybe put this into its own function...somewhere? and
    # specify max allowable degree
    #bcm_uids = S.filter_units({'bph_unit'})
    #for uid in bcm_uids:
    #    preds = S.G.predecessors(uid)
    #    if len(preds) <= 1:
    #        continue
    #    for p in preds[1:]:
    #        S.G.remove_edge(p, uid)


    # TODO: positions seem to be being added to tags...
    # TODO: bph_unit is being kept in tags when you don't want it to be
    # TODO: kinda weird to be putting things that should be re-initialized
    #       every time in the __init__ method of assemblers....

    # step things, including visualization
    # also superimpose dots for BCM outputs
    
    print 'STARTING SIMULATION'
    for i in range(10):
        S.step_simulation()
        #S.list_nodes()
        print 'Completed simulation step', i

    """
    plt.ion()

    for i in range(30):
        plt.cla()
        plt.imshow(sin.output, cmap='Greys')
        plt.draw()
        sin.step()
        #raw_input()
    """
