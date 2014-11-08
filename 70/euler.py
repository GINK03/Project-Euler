import math, sys, os, itertools,fractions
sys.path.append('../pythonlib')
import basic
from decimal import *
getcontext().prec = 20

MAX = 10**7
pTable = set(basic.primeTable(MAX))
def countPrime(n):
    if n in pTable:
        return n-1
    
    res = basic.primeDecomposition(n)
    resset = set(res)
    buff = Decimal(1.)
    for r in resset:
        buff *= (Decimal(1.) - Decimal(1.)/Decimal(r))
    #print n, buff*n
    return int(round(buff*n))
class Top:
    def __init__(self):
        self.top = 0
        self.bottom = Decimal(100000)
        self.i   = 0
def isSame(n, fi):
    #print n, fi
    if ''.join(sorted(str(n))) == ''.join(sorted(str(fi))):
        return True
    return False
if __name__ == '__main__':
    top = Top()
    tgt = [x for x in xrange(2, MAX)]
    #tgt.reverse()
    for n in tgt:#[9849293, 9708131,8319823]:#tgt:
        fi = countPrime(n)
        if n%10000 == 0:
            print 'iter', n
        if isSame(n, fi) == False:
            continue
        #print 'n = ', n, 'fi = ', fi, 'n/fi = ', n/float(fi)
        if top.bottom > Decimal(n)/Decimal(fi):
            top.bottom = n/float(fi)
            top.i   = n 
            #print 'n = ', n, 'fi = ', fi, 'n/fi = ', n/float(fi)
        #print i, cp
print top.i, top.bottom
