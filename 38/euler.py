import re, sys, math, itertools

def makeSieve(n):
    return [int(x) for x in format(int(format(n, 'b')), '09')]

BASE = [1, 2, 3, 4, 5, 6, 7, 8, 9]

maxNum = 0
for i in xrange(1, int('111111111', 2) + 1 ):
    sieve = makeSieve(i)
    sieved = zip(sieve, BASE)
    sieved = [ x for x in map(lambda x:x[0] * x[1], sieved) if x != 0]
    sieveList = []
    for sievePermutation in itertools.permutations(sieved):
        sieved = int(''.join(map(lambda x:str(x), sievePermutation)))
        sieveList.append(sieved)
    #sieved = int(''.join(map(lambda x:str(x), sieved)))
    for siever in sieveList:
        s = ''
        for i in xrange(1, sys.maxint):
            s += str(siever * i)
            if len(s) >= 9:
                break
        if i == 1:
            continue
        if '0' in s:
            continue
        if len(s) != 9:
            continue
        if len(s) == len(set(s)):
            if int(s) > maxNum:
                maxNum = int(s)
                print 'pandegital', s, 'siever', siever
