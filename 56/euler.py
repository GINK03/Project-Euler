import math, itertools

ansList = []

for a in xrange(1,100+1):
    for b in xrange(1,100+1):
        ansList.append(sum(map(lambda x:int(x), str(a**b))))

print sorted(ansList)[-1]
