
import sys,math,os, itertools

MAX = 100

alist = [1 for x in xrange(1, MAX+1)] + [0 for x in xrange(1, MAX+1)]

partition = {'1':1,
            '1,2':1,
            '2,2':1,
            }
def partitionNumber(n, r):
    #print 'firstin', n, r, n-r,r, n-1,r-1
    if r == 1 or r == n:
        newkey = ','.join(map(str, [n,r]))
        partition[newkey] = 1
        return 1
    bkey = ','.join(map(str, [n-1,r-1]))
    akey = ','.join(map(str, [n-r,r]))
    
    bresult = 0
    if n-1 < r-1: #or n-r < r:
        newkey = ','.join(map(str, [n-1,r-1]))
        partition[newkey] = 0
        bresult = 0
    else:
        bresult = partition.get(bkey)

    aresult = 0
    if n-r < r:
        newkey = ','.join(map(str, [n-r,r]))
        partition[newkey] = 0
        aresult = 0
    else:
        aresult = partition.get(akey)
    newparam = aresult + bresult
    
    newkey = ','.join(map(str, [n,r]))
    partition[newkey] = newparam
    return newparam

for i in xrange(2, MAX+1):
    setbuff = set()
    for k in xrange(1,i+1):
        setbuff.add(','.join(map(str,[i,k])))
    res = 0
    for s in setbuff:
        i, k = map(int, s.split(','))
        res += partitionNumber(i,k)
    print 'result', i, res-1
