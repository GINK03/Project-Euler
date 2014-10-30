import itertools, sys
c = 0
for powed in xrange(1, 31 +1):
    for base in xrange(1, 10):
        if len(str(base**powed)) > powed:
            break
        if len(str(base**powed)) == powed:
            c+=1
            print base, powed, base**powed, len(str(base**powed))
print 'result = ', c
