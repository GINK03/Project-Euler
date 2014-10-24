import itertools, math
import json
def factor(i):
    buff = []
    for e in xrange(1,int(math.sqrt(i) +1)):
        if i%e == 0:
            if not e in buff:
                buff.append(e)
            if e != 1 and not i/e in buff:
                buff.append(i/e)
    if buff == []:
        return (i, None)
    #print i, buff
    if reduce(lambda x,y:x+y, buff) > i:
        return (i, reduce(lambda x,y:x+y, buff))
    else:
        return (i, None)
abundantNums = []
resultList   = []
for i in xrange(1, 28123 + 1):
    res = factor(i)
    if res[1]:
        abundantNums.append(res[0])
print sorted(abundantNums)

abundantSet = set()
for i, e in enumerate(itertools.combinations_with_replacement(abundantNums, 2)):
    abundantSet.add(e[0] + e[1])
    if i % 10000 == 0:
        print i, e
result = 0
for i in xrange(1, 28123 + 1):
    if not i in abundantSet:
        print i
        result += i
print 'result', result
