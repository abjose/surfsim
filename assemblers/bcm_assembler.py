
import numpy as np

#import sys
#sys.path.append()
#from ..units import *
#from surfsim.unitgraph import UnitGraph #test
from assembler import Assembler
from units import BiphasicUnit, SumUnit, ThreshUnit


class BCMAssembler(Assembler):
    
    def __init__(self, simulator, x, y, R, tags=set(), ports={}):
        super(BCMAssembler, self).__init__(simulator, tags, ports)
        self.x, self.y, self.R = x,y,R
        # AGAIN, R, etc. should be ports!! right?
        # construct BCM
        # add (10) biphasic filters in a square of side R centered on x,y
        # TODO: probably need to add unique tags to all this
        max_dist = np.linalg.norm([(0,0),(R,R)])
        for i in range(10):
            r1, r2 = 2*np.random.rand(2)-1
            cx, cy = x+R*r1, y+R*r2
            ports = dict(pos=(cx,cy), 
                         A= np.linalg.norm([np.array((x,y))
                                            -np.array((cx,cy))]) / max_dist)
            #ports = ports.copy()
            tags |= {'bph_unit'}
            #tags = tags.copy()
            self.add_unit(unit=BiphasicUnit, 
                          ports=ports.copy(), tags=tags.copy())
            
        # connect them all to a summation unit
        # TODO: should have an easier way to access UIDs of things you just made
        # TODO: SumUnit probably won't work with signals...need it to strip
        #       first thing off
        tags={}
        bph_uids = self.G.nodes()
        self.add_unit(unit=SumUnit, tags=['sum_unit'], pos=(x,y))
        sum_uid = self.filter_units({'sum_unit'}).pop()
        for n in bph_uids:
            self.connect(n, 'output', sum_uid, 'input')

        # connect the summation unit to a linear threshold
        thresh_ports = dict(theta=0, slope=1, pos=(x,y))
        self.add_unit(unit=ThreshUnit, tags=['thresh_unit'], 
                      ports=thresh_ports.copy())
        thresh_uid = self.filter_units({'thresh_unit'}).pop()
        self.connect(sum_uid, 'output', thresh_uid, 'input')


    def make_instance(self, tags=set(), ports={}):
        x, y = ports['pos']
        self.__init__(self.S, x, y, self.R, self.tags, self.ports)
        super(BCMAssembler, self).make_instance(tags=tags, ports=ports)
