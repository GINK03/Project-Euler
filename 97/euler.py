import decimal
import math
decimal.getcontext().prec = 1000
a, b, c, d = decimal.Decimal(28433), decimal.Decimal(2), 7830457, decimal.Decimal(1)
for i in xrange(7830456):
    b = (b*2)%10000000000
    if i%100000 == 0:
        print 'iter', i
print (a*b + d)

