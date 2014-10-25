import math, itertools

B = itertools.combinations([x for x in xrange(2,101)] + [x for x in xrange(2,101)], 2)

buff = set()
for b in B:
    base, p = b[0], b[1]
    buff.add(int(math.pow(base, p)))
print len(buff)
    
