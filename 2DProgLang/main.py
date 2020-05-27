import sys

fname = sys.argv[1]
inputs = tuple([eval(x) for x in sys.argv[2:]])

from load import load
from run import run


class Cell:
    def __init__(self, x, y, state, function):
        self.x = x
        self.y = y
        self.s = state
        self.f = function


with open(fname) as f:
    cells = load(f.read())
    
    width = max([c[0] for c in cells]) + 1
    height = max([c[1] for c in cells]) + 1
    
    cells_dict = {}
    
    for i, j, x, y, s, f in cells:
        cells_dict[(i, j)] = Cell(x, y, s, f)
    
    print(f'{fname} loaded with arguments {inputs}!')

    run(array)