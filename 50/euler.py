import sys, math
sys.path.append('../pythonlib/')
import basic

resultSet = set()
pTable = basic.primeTable(1000000)
pLen   = len(pTable)
for i, p in enumerate(pTable):
    startIndex = i+1
    if startIndex >= pLen:
        break
    if startIndex%100 == 0:
        print 'iter', startIndex, pLen
    for endIndex in xrange(startIndex+21, 1000000):
        if sum(pTable[startIndex:endIndex]) >= 1000000:
            break
        if sum(pTable[startIndex:endIndex]) in pTable:
            #print startIndex, sum(pTable[startIndex:endIndex]), endIndex - startIndex
            resultSet.add( (len(pTable[startIndex:endIndex]), sum(pTable[startIndex:endIndex])) )

print sorted(list(resultSet), key=lambda x:x[0])[-1]
