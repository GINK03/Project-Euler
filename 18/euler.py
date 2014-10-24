import re, itertools
import random
import json

A = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

C = A.split('\n')
D = [ x.split(' ') for x in C ]
class SelfPoint:
    def __init__(self, h, v, value):
        self.h = h
        self.v = v
        self.value = value
        self.buff = self.value
        self.chain = None
    def setBuff(self, prevBuff):
        self.buff += prevBuff
    def clear(self):
        self.buff = self.value
        return self.chain
    def search(self, which):
        targetH = 0
        targetV = self.v + 1
        if which == 0:
            targetH = self.h + 0
            pass
            #右探索
        if which == 1:
            targetH = self.h + 1
            pass
            #左探索
        aSpl = filter(lambda sp: sp.h == targetH and sp.v == targetV, selfPoints)
        # chainは必ず，探索される
        if aSpl != []:
            self.chain = aSpl.pop()
            self.chain.setBuff(self.buff)
            #print self.chain, self.chain.h, self.chain.v, self.chain.value, self.chain.buff
        else:
            self.chain = self
        return self.chain
    
selfPoints = []
for iv, he in enumerate(D):
    #print iv, he
    for ih, ve in enumerate(he):
        selfPoints.append( SelfPoint(ih, iv, int(ve) ) )
startPoint = selfPoints[0]

for bit in xrange(0,int('11111111111111',2) + 1):
    #print '{0:15d}'.format(int(format(bit, 'b')))
    bits = map(lambda x:int(x), format(int(format(bit, 'b')), '014'))
    #print bits
    res = startPoint.search(bits[0]).search(bits[1]).search(bits[2]).search(bits[3]).search(bits[4])\
            .search(bits[5]).search(bits[6]).search(bits[7]).search(bits[8]).search(bits[9]).search(bits[10])\
            .search(bits[11]).search(bits[12]).search(bits[13]).search(0).buff
    print res
    startPoint.clear().clear().clear().clear().clear()\
      .clear().clear().clear().clear().clear().clear()\
      .clear().clear().clear().clear().buff
