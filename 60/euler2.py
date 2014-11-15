import itertools,sys
sys.path.append('../pythonlib')
import basic

prims = basic.primeTable(10000)
primsSet = set(basic.primeTable(10000000))

def makeChain(chain):
    if len(chain) == 5:
        return chain
    for p in prims:
        if p > chain[-1]:
            new_chain = makeChain(chain+[p])
            if new_chain and allPrime(chain):
                return new_chain
    return False

def allPrime(chain):
    return all(int(''.join(map(str,[p[0],p[1]]))) in primsSet for p in itertools.permutations(chain, 2))

chain = 0
while not chain:
    chain = makeChain([prims.pop(0)])

print 'ans', chain
