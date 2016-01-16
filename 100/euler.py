import os, math, itertools, sys
sys.path.append('../pythonlib')
import basic

for e, ps in enumerate(basic.drange(999999999999, 1000000000100)):
    for e2, red in enumerate(basic.drange(1, ps)):
        blue = ps - red
        red = red
        (ps, pblue, pred) = ps, blue/float(ps), red/float(ps)
        #print pblue, pred, ps, red
        if e2%10000 == 0:
            print e2, ps, (pblue) * (pred)
        if (pblue) * (pred) == 0.5:
            print ps, blue, red
            break
    print ps

if __name__ == '__main__':
    print 'hello, world'
