import itertools, operator, sys, math
# see;https://oeis.org/A000607
sys.path.append('../pythonlib')
import basic
ptable = basic.primeTable(10000)

target = 2
while True:
    ways = [0 for x in xrange(target+1)]
    ways[0] = 1

    for i in xrange(len(ptable)):
        for j in xrange(ptable[i], target+1):
            ways[j] += ways[j - ptable[i]]

    if ways[target] > 5000:
        break
    target += 1

print 'result', target
