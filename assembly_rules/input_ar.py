
import cv2   as cv
import numpy as np  # perhaps this can be imported in base class?

from assembly_rule import AssemblyRule
from assemblers    import InputAssembler


class InputAR(GridAR):
    
    def __init__(self, sim, filepath):        
        # init input
        self.source = cv.VideoCapture(filepath)
        if not self.source.isOpened():
            raise Exception("Source wouldn't open in InputAR.")
        flag, self.input = self.source.read()
        self.h, self.w = np.size(self.input, 0), np.size(self.input, 1)
        # init assembler
        # should be able to just use a Unit?
        assembler = InputAssembler(simulator)
        # init superclass
        super(InputAR, self).__init__(sim, assembler, xl=self.h, yl=self.w)
        self.r, self.c = 0,0
        
        
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
