import itertools
# sieve algorithme for prime search
def primeTable(n):
    sieve = [True for _ in xrange(n + 1)]
    i = 2
    while i * i <= n:
        if sieve[i]:
            j = i + i
            while j <= n:
                sieve[j] = False
                j += i
        i += 1
    table = [str(i) for i in xrange(n + 1) if sieve[i] and i >= 2]
    return table

def makeRoundSet(x):
    res = set()
    temp = x
    while True:
        head = temp[0]
        tail = temp[1:]
        temp = tail + head
        if temp == x:
            break
        res.add(temp)
    return res

if __name__ == '__main__':
    c = 0
    primeL = primeTable(1000000)
    for x in primeL:
        #print x
        if len(x) == 1:
            c += 1
            continue
        isRound = True
        #print x, makeRoundSet(x)
        for roundNum in makeRoundSet(x):
            if not roundNum in primeL:
                #print int(roundNum), 'normal'
                isRound = False
        if isRound:
            c += 1
            print c, x, makeRoundSet(x)

    print 'result', c
