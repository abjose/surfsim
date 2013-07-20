
from unit import Unit

"""
Make this a unit that has lots of functionality to allow customization 
'on-the-fly' as in the pseudocode demo
"""


class PrototypeUnit(Unit):
    
    def __init__(self, simulator, uid=None):
        super(PrototypeUnit, self).__init__(simulator, uid=uid, 
                                            tags=tags, ports=ports)

    def operation(self):
        pass

"""
To add:
- stuff to allow storing/running operation code from command-line
- stuff to allow saving created units...as python files??? technically just a simple as writing to a text file??? Might want to use type(...) built-in
http://www.pythonexamples.org/2011/01/12/how-to-dynamically-create-a-class-at-runtime-in-python/

"""



if __name__ == '__main__':
    pass
