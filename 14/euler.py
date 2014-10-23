import sys, math, os, itertools


def collatzGenerator(n):
    buff = n
    res  = []
    while True:
        if buff % 2 == 0:
            buff = buff / 2
            res.append(buff)
        else:
            buff = 3 * buff + 1
            res.append(buff)
        if buff == 1:
            return res
class MaxHolder:
    def __init__(self):
        self.MAXLEN = 0
        self.INDEX  = 0
maxHolder = MaxHolder()
for i in xrange(1000000):
    l = collatzGenerator(i+1)
    if len(l)  > maxHolder.MAXLEN:
        maxHolder.MAXLEN = len(l)
        maxHolder.INDEX  = i + 1
    if (i + 1) % 10000 == 0:
        print 'iter', i+1, 'then', len(l)

print 'RESULT = ', maxHolder.MAXLEN, maxHolder.INDEX
    
