import sys

if len(sys.argv) != 3:
    raise ValueError('Log filename and end value required!')

fname = sys.argv[1]
E = int(sys.argv[2])


# Load values for K, A, B
from read_kab import kab
tmp = kab(fname)

if not tmp:
    raise ValueError('K, A, B could not be read from file.')

K, B, A = tmp
i, j = A, B-A

print('Deposit 1:', str(i)[:10]+'..' if len(str(i))>6 else str(i))
print('Deposit 2:', str(j)[:10]+'..' if len(str(j))>6 else str(j))
print('End value:', E)


k = 2
log_k = K // 10

while True:
    if B == E:
        print('\nEnd value reached for a %ik sequence.' % k)
        break

    if k % log_k == 0:
        print('.', end='', flush=True)

    A, B = B, A+B
    k += 1