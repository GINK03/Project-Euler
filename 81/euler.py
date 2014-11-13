import sys, os, operator, itertools

TEST = '''131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331'''
source = [ map(int, x.split(',')) for x in TEST.split('\n')]
source = []
for line in sys.stdin:
    line.strip()
    source.append(map(int, line.split(',')))
# make matrix 
for h in xrange(len(source[-1])):
    for v in xrange(len(source)):
            if v == 0 and h == 0:
                print source[v][h]
                continue
            left = source[v][(lambda x:x if x >= 0 else 0)(h-1)]
            head = source[(lambda x:x if x >= 0 else 0)(v-1)][h]
            if head == source[v][h]:
                update = left
            elif left == source[v][h]:
                update = head
            else:
                update = sorted([head, left], reverse=True).pop()
            source[v][h] += update
            #print v,h,source[v][h]
print source[-1][-1]
