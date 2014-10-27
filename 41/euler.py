import sys, itertools

def primeTable(n):
    sieve = [1 for _ in xrange(n + 1)]
    sys.exit(0)
    i = 2
    while i * i <= n:
        if sieve[i]:
            j = i + i
            while j <= n:
                sieve[j] = False
                j += i
        if i%100 == 0:
            print i
        i += 1
    table = [i for i in xrange(n + 1) if sieve[i] and i >= 2]
    return table
#123456789
#999999999
primeList = primeTable(999999990)
