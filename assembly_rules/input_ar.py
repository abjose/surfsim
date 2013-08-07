

import numpy as np  # perhaps this can be imported in base class?

from grid_ar    import GridAR
from assemblers import InputAssembler


class InputAR(GridAR):
    # TODO: modify so that this takes an assembler as an argument and 
    # tesselates it over each 'pixel' of some input object (that can
    # have 'step' called on it) - dont' make specific to video
    # could make the input classes in here too...
    
    def __init__(self, sim, input_src): #assembler, input_src):        
        # input_src should be something with source matrix and step() function
        self.input_src = input_src
        # init assembler
        # should be able to just use a Unit?
        assembler = InputAssembler(sim, self)
        h, w = self.input_src.get_dims()
        # init superclass
        super(InputAR, self).__init__(sim, assembler, xl=h, yl=w)
        #self.r, self.c = 0,0
        
    def step_input(self):
        self.input_src.step()
        
    def get_pix(self, (x,y)):
        # don't do this? just have things access self.input
        return self.input_src.source[y][x] #??

    def reset_input(self):
        # reset input to first frame
        pass


class VideoInput(object):
    import cv2   as cv

    def __init__(self, filepath):
        # init input
        self.source = cv.VideoCapture(filepath)
        if not self.source.isOpened():
            raise Exception("Source wouldn't open in InputAR.")
        flag, self.input = self.source.read()
        self.h, self.w = np.size(self.input, 0), np.size(self.input, 1)
                
    def step(self):
        # how to step when components are told to step? could give one
        # the job of telling this when it steps? seems sorta hacky
        # TODO: make handle end-of-file (I think just check flag?)
        flag, self.input = self.source.read()
        #cv2.imwrite(str(c) + '.jpg',frame)
        #c = c + 1
        #cv2.waitKey(1)

    def get_dims(self):
        return (self.h, self.w)

    def release_input(self):
        self.input.release()


class SinusoidInput(object):
    #import numpy as np

    def __init__(self, side, spacing, f, amp, step_size):
        # On a sidexside size grid with each step spacing apart, insert
        # sin with freq f and amplitude amp. On step, increment by step_size.
        # TODO: add ability to change angle
        self.steps  = 0
        self.side   = side
        self.range  = np.arange(0,self.side*spacing, spacing)
        self.func   = lambda x: amp*np.sin(f*x + step_size*self.steps)
        self.output = None
        self.step()

    def step(self):
        sin = self.func(self.range)
        self.output = np.resize(sin, (self.side, self.side))
        self.steps += 1

    def get_dims(self):
        return (self.side, self.side)

if __name__ == '__main__':
    pass
