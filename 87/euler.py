import sys, math, itertools
sys.path.append('../pythonlib')
import basic
ptable = basic.primeTable(7071)
print 'maxprime', 50000000**0.5
c = set()
for t1, t2, t3 in itertools.product(ptable,repeat=3):
    r = t1**2 + t2**3 + t3**4 
    if r < 50000000:
        c.add(r)

print 'ans,',len(c)
