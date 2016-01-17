
# this method return large prime list
# there is a memory restriction, you can insert by 1000000, 
# if you inserted 10000000, your machine will stop.because of memory overflow
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

# this method allow you to decompress specified number
def primeDecomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  return table
# this method allow you to use decimal type iterator or huge number iterator 
def drange(start, end):
    n = start
    while True:
        n += 1
        yield n
        if n >= end:
            break

def totientFunction(n, pSet):
    if n in pSet:
        return n-1
    
    res = primeDecomposition(n)
    resset = set(res)
    buff = 1.
    for r in resset:
        buff *= (1. - 1./r)
    #print n, buff, buff*n, round(buff*n)
    return int(round(buff*n))
