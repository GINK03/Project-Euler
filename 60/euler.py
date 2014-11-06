import itertools, sys
sys.path.append('../pythonlib')
import basic
p = ['A', 'B', 'C', 'D']
primeTable = basic.primeTable(100000)
iteratePrimeTable = basic.primeTable(9999)
result = []
for i, pt in enumerate(itertools.combinations(iteratePrimeTable,5)):
    if i%100000 == 0:
        print 'iter', i, pt
    #continue
    #print pt
    comb = True
    for p in itertools.permutations(pt, 2):
        to_eval = int(''.join(map(lambda x:str(x),p)))
        if to_eval > primeTable[-1]:
            comb = False
            continue
        if not to_eval in primeTable:
            comb = False

    if comb:
        print pt, 'sum=', sum(pt)
        result.append(pt)
print sorted(result)
