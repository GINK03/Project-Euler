import  itertools
from decimal import *
getcontext().prec = 10001


def Parse(dList):
    n = 10
    while True:
        parsedList = dList[:n]
        nextList   = dList[n: n*2]
        nextNextList = dList[n*2: n*3]
        #print 'parsedOrignal', parsedList
        #print 'parsedNext', nextList
        n += 1
        if parsedList == nextList and parsedList == nextNextList:
            return (n, nextList)
        if n == 10000:
            return (None, None)

#print str(Decimal(1)/Decimal(987))
res = []
for i in xrange(1,1001):
    sList =  str(Decimal(1)/Decimal(i))
    dList = sList[3:-1]
    if len(dList) == 0 or len(sList) == 0:
        continue
    if len(sList) < 100:
        continue
    print 'base', i
    depth, ist =  Parse(dList)
    res.append((i, depth))
print sorted(res, key=lambda x:x[1])
