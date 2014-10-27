import os, sys, math, itertools

for l in sys.stdin:
    l = l.strip()
    l = l.replace('"','')
    li = l.split(',')

toEval = []
for e in map(lambda x:x.lower(), sorted(li)):
    length = 0
    for c in e:
        length += int(ord(c) - 96)
    toEval.append(length)

MAX = sorted(toEval).pop()

# make triangle number
triangles = []
def makeTriangle(n):
    return (n * (n + 1)) /2
for i in xrange(1, MAX+1):
    triangles.append(makeTriangle(i))
result = []
for evl in toEval:
    if evl in triangles:
        result.append(evl)
print len(result)
#print toEval
    
