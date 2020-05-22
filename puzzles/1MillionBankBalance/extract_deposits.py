# Get filename from argument.
import sys

if len(sys.argv) != 2:
    raise ValueError('Filename argument missing!')

fname = sys.argv[1]


# Load values for K, A, B from file.
from read_kab import kab
tmp = kab(fname)

if not tmp:
    raise ValueError('Could not read K, A, B from file.')

K, B, A = tmp


# Calculate deposits from A and B.
x, y = A, B-A

# Write deposits to file.
with open('x.deposit', 'w') as f:
    f.write(str(x))

with open('y.deposit', 'w') as f:
    f.write(str(y))