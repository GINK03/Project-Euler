import sys, math, itertools, copy

class IndexHolder:
    def __init__(self):
        self.index = 0
        self.resultList = []

holderList = []
def check(toEval, p):
    e1, e2, e3 = map(lambda x:len(x), toEval.split('0'))
    if e1 < e2:
        return None
    if e1**2 + e2**2 == e3**2:
        print p, e1, e2, e3
        if filter(lambda x:x.index == p, holderList) == []:
            holder = IndexHolder()
            holder.index = p
            holderList.append(holder)
        holder = filter(lambda x:x.index == p, holderList).pop()
        holder.resultList.append([e1, e2, e3])

BASE = 1000
BASE = int(raw_input())
for i in xrange(5, BASE + 1 + 5):
    originalList = [1 for x in xrange(i) ]
    firstList = copy.copy(originalList)
    for firstindex in xrange(1, len(firstList) + 1 -2):
        for secondindex in xrange(firstindex + 2, len(firstList) + 1 -2):
            firstList[firstindex] = 0
            firstList[secondindex] = 0
            evalStr = ''.join(map(lambda x:str(x), firstList))
            check(evalStr, i - 2 )
            firstList = copy.copy(originalList)

print sorted(holderList, key=lambda x:len(x.resultList))[-1].index
