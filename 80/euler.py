import math, decimal, itertools
decimal.getcontext().prec = 200

cnt = 0
buff = 0
for i in  itertools.count(1):
    if int(math.sqrt(i))**2 == i:
        continue
    cnt += 1 
    head,tail = str(decimal.Decimal(i).sqrt()).split('.')
    buff += sum(map(lambda x:int(x), head + tail[:99]))
    print i, cnt, buff
    if i >= 100:
        break
    
