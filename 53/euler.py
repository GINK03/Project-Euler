import sys, math, itertools
sys.path.append('../pythonlib')
import basic

c = 0
for n in xrange(23, 100 + 1):
    for r in xrange(1, n+1):
        to_eval = basic.getCombinationNum(n, r)
        if to_eval > 1000000:
            c += 1

print c
