
from itertools import *

# describe 2,1,0 : 2:target, 1:base, 0:not use

def base10to(n, b):
    if (int(n/b)):
        return base10to(int(n/b), b) + str(n%b)
    return str(n%b)
#for p in itertools.permutations('ABCD', 4):
#    print p
sourceList = '123456789'
resultSet = set()
for x in xrange(1, int('222222222', 3) + 1):
    baseList = str(format(int(base10to(x,3)), '09'))

    zipped = zip(sourceList, baseList)

    base = map(lambda x:x[0], filter(lambda x:x[1] == '1', zipped))
    target = map(lambda x:x[0], filter(lambda x:x[1] == '2', zipped))
    if base == [] or target == []: 
        continue
    #print base, target
    for be in permutations(base, len(base)):
        for te in permutations(target, len(target)):
             b = int(''.join(be))
             t = int(''.join(te))
             r = b*t
             rs = str(r)
             if '0' in rs or len(rs) > len(set(rs)):
                #print 'miss', b, t, r
                continue
             if len(str(b)) + len(str(t)) + len(rs) == len(set( str(b) + str(t) + rs )) == 9:
                resultSet.add( (b, t, rs) )
print reduce(lambda x,y:x+y, set(map(lambda x:int(x[2]), resultSet)))

