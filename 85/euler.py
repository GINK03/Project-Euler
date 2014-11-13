import math

def target_fomula(x,y):
    return (x**2 + x)*(y**2 + y)/4
c = True
for x in xrange(1,100):
    for y in xrange(1,100):
        if 2000000 < target_fomula(x,y) and c:
            print x*(y), target_fomula(x,y)
            print x*(y-1), target_fomula(x,y-1)
            c = None
            break
