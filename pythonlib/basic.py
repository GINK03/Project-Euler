
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
