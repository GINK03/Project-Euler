import sys,os,math,itertools, operator, fractions
sys.path.append('../pythonlib')
import basic
MAX = 10**6
MAX = 1500000
result = 0
tgt = [x for x in xrange(1, MAX)]
#tgt.reverse()
for x in [120]:#tgt:
  res = 0
  if x%10000 == 0:
    print 'iter', x
  for m in xrange(2, x):#math.sqrt(x/2)):
    for n in xrange(1,m):
      #if (n+m)%2 == 1 and fractions.gcd(n,m)==1:
        a, b, c = map(int, [abs(m*m - n*n), 2*m*n, m*m + n*n])
        print x, map(int, [a, b, c, a+b+c, x, m, n])
        if a + b + c == x:
          print x, map(int, [a, b, c, m, n])
          res += 1
  if res == 1:
    result += 1
print 'result,', result 
