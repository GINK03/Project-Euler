import sys, math, os, itertools

if __name__ == '__main__':
    print str(reduce(lambda x,y:x+y, map(lambda x:x**x, [x for x in xrange(1,1000 + 1)])))[-10:]
