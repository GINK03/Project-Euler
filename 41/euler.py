import sys, itertools, math

def isPrime(n):
    for i in xrange(2, math.sqrt(n)+1):
        if n%i == 0:
            return False
    return True
res = [0]
for l in xrange(1, len('123456789') + 1):
    for p in itertools.permutations('123456789'[:l]):
        p = ''.join(p)
        if isPrime(int(p)):
            res.append(int(p))

print sorted(res)[-1]
