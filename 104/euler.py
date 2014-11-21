import fractions, operator, math, sys, itertools
def fibogenerator():
    pair = [1, 1]
    i = 2
    while True:
        i += 1
        pair[1], pair[0] = pair[1] + pair[0], pair[1]
        yield i, pair[1]

evalset = set([x for x in xrange(1,10)])
def isPandegital(n):
    string = str(n)
    head, tail = set(map(int, string[:9])), set(map(int, string[-9:]))
    if tail == evalset == head:
        return True

for i, f in fibogenerator():
    if i%1000 == 0:
        print 'iter', i
    if isPandegital(f):
        print i
        break
