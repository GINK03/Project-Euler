import sys,os,math,itertools, operator, fractions
sys.path.append('../pythonlib')
import basic
MAX = 1500000
temp_res = 0
triangles = [0 for x in xrange(MAX+1)]
for m in xrange(2, int(math.sqrt(MAX/2)) + 1):
    for n in xrange(1, m+1):
        if (m+n)%2 == 1 and fractions.gcd(n,m) == 1:
            a, b, c = m**2 - n**2, 2*m*n, m**2 + n**2
            p = sum([a,b,c])
            while p <= MAX:
                triangles[p] += 1
                if triangles[p] == 1: temp_res += 1
                if triangles[p] == 2: temp_res -= 1
                p += a+b+c
print 'result', temp_res

