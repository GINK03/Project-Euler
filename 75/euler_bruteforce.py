import sys,os,math,itertools, operator
sys.path.append('../pythonlib')
import basic
MAX = 10**6
MAX = 1500000
result = 0
tgt = [x for x in xrange(1, MAX) if x%2 == 0]
tgt.reverse()
for x in tgt:#[120]:
    res = 0
    for c in xrange(1, x/2):
        ab = x*(x -2*c)/2
        if c**2 != (x - c)**2 - 2*ab:
            continue
        for a in xrange(1, ab):
            b = ab/a
            if a**2  + b**2 ==  c**2:
                #print 'match','x',x,'ab',ab,'c',c, '[ab]', ab, 'a', a, 'b', b
                res += 1
            if a > b:
                break
    print x, res
    if res == 1:
        result +=1

print 'ans = ', result
