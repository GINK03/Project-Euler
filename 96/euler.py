
def distinct(v, h):
    if 0 <= v <= 2 and 0 <= h <= 2:
        return 1
    if 3 <= v <= 5 and 0 <= h <= 2:
        return 2
    if 6 <= v <= 8 and 0 <= h <= 2:
        return 3
    if 0 <= v <= 2 and 3 <= h <= 5:
        return 4
    if 3 <= v <= 5 and 3 <= h <= 5:
        return 5
    if 6 <= v <= 8 and 3 <= h <= 5:
        return 6
    if 0 <= v <= 2 and 6 <= h <= 8:
        return 7
    if 3 <= v <= 5 and 6 <= h <= 8:
        return 8
    if 6 <= v <= 8 and 6 <= h <= 8:
        return 9
class E:
    def __init__(self):
        self.v = 0
        self.h = 0
        self.p = 0
        self.g = None
# soleve
entry = [1,2,3,4,5,6,7,8,9]

import random
import sys
sys.setrecursionlimit(10**5)
tryregister = []
prb_num = 0
def callable(tryable = None):
    global tryregister
    global prb_num
    c = 0
    maylist = []
    for v in xrange(9):
        for h in xrange(9):
            eibuff = []
            for e in entry:
                vertical = filter(lambda x:x.v == v and x.p == e, toEval) 
                horizon  = filter(lambda x:x.h == h and x.p == e, toEval) 
                group    = filter(lambda x:x.g == distinct(v,h) and x.p == e, toEval) 
                param    = filter(lambda x:x.v == v and x.h == h, toEval).pop()
                if param.p != 0:
                    break
                if vertical == [] and horizon == [] and group == []:
                    ei = filter(lambda x:x.v == v and x.h == h, toEval).pop()
                    eibuff.append( (ei, e) )
            if len(eibuff) == 1:
                ei, e = eibuff.pop()
                ei.p = e
                c += 1
                if tryregister != []:
                    tryregister.append( (ei, e) )
                #print probnum, 'place,', ei.v, ei.h, e
            if len(eibuff) >= 2:
                maylist.append(eibuff)
    if filter(lambda x:x.p == 0, toEval) != []:
        if c == 0:
            if maylist != []:
                where = random.randint(0,len(maylist)-1)
                maylist = sorted(maylist, key=lambda x:len(x))
                where = 0
                which = random.randint(0,len(maylist[where])-1)
                #print prb_num,'it is not good...i will try...'
                #print maylist
                #print maylist[0]
                ei, e = maylist[where].pop(which)
                ei.p = e
                tryregister.append( (ei, e) )
                return None
            else:
                # dispose all
                for ti, te in tryregister:
                    ti.p = 0
                # dispose try register
                print prb_num,'i will dispose all try and restart'
                tryregister = []
                return None
        else:
            return None
    else:
        tryregister = []
        #print 'finished'
        return True
TEST = '''000003017
015009008
060000000
100007000
009000200
000500004
000000020
500600340
340200000'''
import sys,copy
if __name__ == '__main__':
    rawdata = []
    buff = ''
    for line in sys.stdin:
        line = line.strip()
        if line.isdigit():
            buff += line + '\n'
        if len(buff.split('\n')) == 10:
            rawdata.append(copy.copy(buff)[:-1])
            buff = ''
    #print rawdata
    print len(rawdata)
    print rawdata
    result = 0
    for probnum, raw in enumerate(rawdata):
    #for probnum, raw in enumerate([TEST]):
        prb_num = probnum+1
        toEval = []
        for v, l in enumerate(raw.split('\n')):
            for h, e in enumerate(l):
                ei = E()
                ei.v = v
                ei.h = h
                ei.p = int(e)
                ei.g = distinct(v,h)
                toEval.append(ei) 
        while callable() != True:
            pass

        for e in toEval:
            if e.v == 0 and e.h == 0:
                result += e.p*100
            if e.v == 0 and e.h == 1:
                result += e.p*10
            if e.v == 0 and e.h == 2:
                result += e.p*1

        print 'itr', prb_num, result
print 'ans', result
