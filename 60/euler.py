import itertools, sys
sys.path.append('../pythonlib')
import basic
primeTable = basic.primeTable(30000)
primeLargeTable = set(basic.primeTable(10000000))
temp_result = []
for i, pt in enumerate(itertools.combinations(primeTable,2)):
    if i%1000000 == 0:
        print 'iter', i, pt
    if all([int(''.join(s)) in primeLargeTable for s in itertools.permutations(map(str, list(pt)),2)]):
        for p in primeTable:
            if p in pt:
                continue
            pte = list(pt)
            pte.append(p)
            if all([int(''.join(s)) in primeLargeTable for s in itertools.permutations(map(str, pte),2)]):
                for p in primeTable:
                    if p in pte:
                        continue
                    pte2 = list(pte)
                    pte2.append(p)
                    if all([int(''.join(s)) in primeLargeTable for s in itertools.permutations(map(str, pte2),2)]):
                        print 'maybe maybe result = ', pte2, sum(pte2)
                        for p in primeTable:
                            if p in pte2:
                                continue
                            pte3 = list(pte2)
                            pte3.append(p)
                            if all([int(''.join(s)) in primeLargeTable for s in itertools.permutations(map(str, pte3),2)]):
                                print 'result = ', pte3, sum(pte3)
                                sys.exit(0)
