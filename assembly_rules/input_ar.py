
import cv2   as cv
import numpy as np  # perhaps this can be imported in base class?

from assembly_rules import AssemblyRule
from assemblers     import InputAssembler


class InputAR(AssemblyRule):
    
    def __init__(self, simulator, filepath):
        # know assembler will be wrapping an InputUnit...
        # need to make 'InputAssembler' or something? or just instantiate
        # with Unit?...
        assembler = InputAssembler(simulator)
        super(InputAR, self).__init__(simulator, assembler)
        self.r, self.c = 0,0
        self.input  = None
        self.source = cv.VideoCapture(filepath)
        if not self.source.isOpened():
            raise Exception("Source wouldn't open in InputAR!")
        flag, self.input = self.source.read()
        self.w, self.h = np.size(self.input, 1), np.size(self.input, 0)
        
    def update_init_vals(self):
        # Want to increment over size of source
        # could just use a grid assembly rule...
        # should totally use lazyarrays
        self.ports[pos] = (self.x, self.y)
        self.r += 1
        if self.r >= self.h:
            if self.c >= self.w:
                raise Exception("Too many units being instantiated for input!")
            self.r = 0
            self.c += 1

    def step_input(self):
        # how to step when components are told to step? could give one
        # the job of telling this when it steps? seems sorta hacky
        # TODO: make handle end-of-file (I think just check for flag?)
        flag, self.input = self.source.read()
        #cv2.imwrite(str(c) + '.jpg',frame)
        #c = c + 1
        #cv2.waitKey(1)
        
    def get_pixel(self, x, y):
        # don't do this? just have things access self.input
        pass

    def reset_input(self):
        # reset input to first frame
        pass

    def release_input(self):
        self.input.release()


if __name__ == '__main__':
    pass
