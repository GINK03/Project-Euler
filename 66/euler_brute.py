import itertools, math
#import numpy as np
MAX_RANGE = 100000000

global c
c = 0
def xp_generator():
    global c
    c = 2
    while True:
        yield c**2
        c += 1
if __name__ == '__main__':
    #global c
    D = [d for d in xrange(1,1001) if d != int(math.sqrt(d))**2]
    #powlist = set([p**2 for p in xrange(1,MAX_RANGE)])
    #np.dtype(np.int64)
    #immutable_xp = np.array([x**2 for x in xrange(2,MAX_RANGE)])
    #immutable_xp = [x**2 for x in xrange(2,MAX_RANGE)]
    result_list = []
    for d in D:
        #for xp in np.nditer(immutable_xp, flags=['refs_ok']):
        #for xp in immutable_xp:
        for i, xp in enumerate(xp_generator()):
            #if i%100000000 == 0:
            #    print 'iter', i
            yp = (xp - 1)/d
            if (xp - 1)%d != 0 or not int(math.sqrt(yp))**2 == yp:
                continue
                #print 'itery',xp, yp, d
            if xp - d*yp == 1:
                print 'xp=', xp, 'yp=', yp,'d=', d
                result_list.append( (xp, yp, d) )
                c = 2
                break
    print sorted(result_list, key=lambda x:x[0]*(-1))
