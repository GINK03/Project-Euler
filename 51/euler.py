import sys, math, itertools
sys.path.append('../pythonlib')
import basic

resultSet = set()
pTable = set(basic.primeTable(1000000))
swap = map(str, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
candi = []
for i, p in enumerate(pTable):
    for s in set(map(str, str(p))):
        c = 0
        for t in swap:
            rep = int(str(p).replace(s,t))
            if rep == p or len(str(rep)) != len(str(p)):
                continue
            #print rep, s, t, p
            if rep in pTable:
                c += 1
                #print c
        if c >= 7:
            candi.append(p)        
print sorted(candi, reverse=True)
