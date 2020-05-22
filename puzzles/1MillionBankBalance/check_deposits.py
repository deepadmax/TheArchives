# Read deposit A from file
with open('x.deposit', 'r') as f:
    X = int(f.read().strip())

# Read deposit B from file
with open('y.deposit', 'r') as f:
    Y = int(f.read().strip())


# Get the first two values in the sequence.
A = X
B = A+Y

# Because the sequence includes A and B to begin with, it starts at size 2.
k = 2

# E represents the end value, which, for this purpose, is a million.
E = 1000000

# How often to print a dot. I've selected every 10%.
k_log = E // 10



while True:
    if B == E:
        print('!')
        print("Goal of %i has been reached with size %i sequence." % (E, k))
        break

    if k % k_log == 0:
        print('.', end='', flush=True)

    A, B = B, A+B
    k += 1


    # Making sure the loop breaks if the numbers indicate
    # they won't reach the target.

    if (B > E and A > E-B) or (A < 0 and B < 0):
        print("Sequence will not reach the target.")
        break