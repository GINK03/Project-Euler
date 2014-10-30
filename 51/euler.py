import sys, math, itertools
sys.path.append('../pythonlib/')
import basic

resultSet = set()
pTable = basic.primeTable(1000000)
pLen   = len(pTable)
for i, p in enumerate(pTable):
    primeStr = str(p)
    buffSet  = set()
    for primeTup in itertools.permutations(primeStr):
        toEval = int(''.join(primeTup))
        if toEval%3 == 0 or toEval%2 == 0:
            continue
        elif toEval in pTable:
            buffSet.add(toEval)
    print p, len(buffSet)
