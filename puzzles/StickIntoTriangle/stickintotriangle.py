from random import random

ITERATIONS = 1000000
k = 0

for i in range(ITERATIONS):
    a = random()
    b = random()

    if a > b:
        a, b = b, a

    if a < 0.5 and b-a < 0.5 and 1-b < 0.5:
        k += 1

percentage = k / ITERATIONS
print(percentage)