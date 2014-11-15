import itertools
import math
t = '1_2_3_4_5_6_7_8_9_0'.split('_')
some = [x for x in xrange(10)]
some.reverse()
for e1,e2,e3,e4,e5,e6,e7,e8,e9 in itertools.product( some, repeat=9 ):
    a = int(''.join(map(str, [t[0],e1,t[1],e2,t[2],e3,t[3],e4,t[4],e5,t[5],e6,t[6],e7,t[7],e8,t[8],e9,t[9]])))
    if int(math.sqrt(a))**2 == a:
        print math.sqrt(a)
        break
