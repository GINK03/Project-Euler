import sys, itertools
sys.path.append('../pythonlib')
import basic

class Prime:
    def __init__(self):
        self.source = 0
        self.primePerms = []

toEval = filter(lambda x:x>1000, basic.primeTable(10000))
primeList = []
for to_eval in toEval:
    to_perm = str(to_eval)
    prime = Prime()
    prime.source = to_eval
    primeList.append(prime)
    for perm in itertools.permutations(to_perm):
        int_perm = int(''.join(perm))
        if to_perm == ''.join(perm) or int_perm in prime.primePerms:
            continue
        if int_perm in toEval:
            prime.primePerms.append(int_perm)


for p in filter(lambda x:len(x.primePerms) >= 2, primeList):
    #print p.source, filter(lambda x:x > 0, sorted(map(lambda x: x - p.source, p.primePerms)))
    difference = filter(lambda x:x, sorted(map(lambda x: x - p.source, p.primePerms)))
    if len(difference) <= 2:
        continue
    # differenceは必ず等差数列のこう差を含むはず 
    # -> this means a entity has twiced number
    for diff in difference:
        if diff*2 in difference:
            print 'match ', p.source, 'diff=', diff, difference, ' p=', ''.join(map(lambda x:str(x), [p.source, p.source+diff, p.source+2*diff]))
