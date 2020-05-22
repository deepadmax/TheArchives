K = 2
A, B = 1000000, 1
LENGTH = 1000000

fname = 'log'
log_k = 10
log_str = "[{:.3f}s] {:%id}/%i" % (len(str(LENGTH)), LENGTH)



# Load values for K, A, B
from read_kab import kab
K, A, B = kab(fname) or (K, A, B)

print('Values loaded!')
print('K = {:10d}'.format(K))
print('A = %s' % (str(A)[:10]+'..' if len(str(A))>6 else str(A)))
print('B = %s' % (str(B)[:10]+'..' if len(str(B))>6 else str(B)))



def sequence(a, b, k=2, length=100):
    while k < length:
        a, b = b, a-b
        k += 1

        yield k, a, b


import time

with open(fname, 'a') as f:
    t = time.time()

    for k, a, b in sequence(A, B, k=K, length=LENGTH):
        if k % log_k == 0:
            new_t = time.time()
            dt = new_t - t
            t = new_t
            print(log_str.format(dt, k))

        f.write("%i:%i,%i.\n" % (k, a, b))
