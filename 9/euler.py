import itertools

A = range(1000)

for e in itertools.combinations(A, 3):
    if e[0] + e[1] + e[2] == 1000:
        if e[0] * e[0] + e[1] * e[1] == e[2] * e[2]:
            print e

