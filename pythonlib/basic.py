
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
    table = [i for i in xrange(n + 1) if sieve[i] and i >= 2]
    return table

def getFactrial(n):
    result = 1
    for i in xrange(1,n+1):
        result *= i
    return result

def getCombinationNum(n, r):
    return getFactrial(n)/( getFactrial(r)*getFactrial(n - r) )
 
def dxrange(start, end):
    n = start
    while True:
        n += 1
        yield n
        if n >= end:
            break
