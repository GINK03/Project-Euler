import math, sys, os, itertools,fractions
sys.path.append('../pythonlib')
import basic

pTable = set(basic.primeTable(1000000))
def countPrime(n):
    if n in pTable:
        return n-1
    
    i = 2
    t = 1
    #while i*i <= n:
    while i <= n:
        #print n, i, fractions.gcd(n,i)
        if fractions.gcd(n,i) == 1:
            t +=1
        i+=1
    return t
class Top:
    def __init__(self):
        self.top = 0
        self.i   = 0
if __name__ == '__main__':
    top = Top()
    tgt = [x for x in range(1, 1000001)]
    tgt.reverse()
    for n in tgt:
        fi = countPrime(n)
        if top.top < n/float(fi):
            top.top = n/float(fi)
            top.i   = n 
        #print 'n = ', n, 'fi = ', fi, 'n/fi = ', n/float(fi)
        #print i, cp
        if n%10 == 0:
            print 'iter', n
print top.i, top.top
