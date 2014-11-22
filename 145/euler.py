import math, itertools, fractions, operator

def makeReverseAndAdd(n):
    tgt = map(lambda x:x, str(n))
    tgt.reverse()
    if tgt[0] == '0':
        return False
    return all(map(lambda x:x%2 ==1, map(int, str(n + int(''.join(tgt))))))

MAX = 10**9
c = 0
for n in xrange(1,MAX):
    if n%100000 == 0:
        print 'iter,',n
    if makeReverseAndAdd(n):
        c += 1
print 'ans', c
