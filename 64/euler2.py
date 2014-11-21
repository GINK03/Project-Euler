import math, sys, os, itertools, operator



def parseN(res):
    i = 1
    for _ in itertools.count(1):
        if res[:i] == res[i:2*i] == res[i*2:i*3] == res[i*3:i*4] == res[i*4:i*5] == res[i*5:i*6] == res[i*6:i*7] == res[i*7:i*8] == res[i*8:i*9] == res[i*9:i*10]:
            return i
        else:
            #print res[:i], res[i:2*i]
            pass
        i += 1
c = 0
for S in xrange(2,10001):
    if int(math.sqrt(S))**2 == S:
        continue
    m0 = 0
    d0 = 1
    a0 = int(math.sqrt(S))
    res = []
    for n in itertools.count(1):
        if n == 1:
            mn = d0*a0 - m0
            dn = (S - mn**2)/d0
            an = int((a0+mn)/dn)
        else:
            mn = dn*an - mn
            dn = (S - mn**2)/dn
            an = int((a0+mn)/dn)
        res.append(an)
        if n > 10000:
            break
    #print S, res
    if parseN(res)%2 == 1:
        print S, parseN(res)
        c += 1
print 'ans, ',  c
