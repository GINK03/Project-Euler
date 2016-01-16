import os, math, itertools, sys
sys.path.append('../pythonlib')
import basic

from itertools import ifilter

def head(a):
    for e in a:
        return e
def gen_solutions():
    a, b = 1, 1
    while True:
        a, b = a * 3 + b * 4, a * 2 + b * 3
        if a % 2 == 1 and b % 2 == 1:
            m, n = (b + 1) / 2, (a + 1) / 2
            yield m, n

N = 10 ** 12
print head(x[0] for x in ifilter(lambda x: x[1] > N, gen_solutions()))
