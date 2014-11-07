import itertools, math
import threading
#import numpy as np
MAX_RANGE = 100000000
class SearchPell(threading.Thread):
    def __init__(self, d, result_list):
        super(SearchPell, self).__init__()
        self.d = d
        self.target = result_list
    def xp_generator(self):
        c = 2
        while True:
            yield c**2
            c += 1
    def run(self):
        for i, xp in enumerate(self.xp_generator()):
            #if i%100000000 == 0:
            #    print 'iter', i
            yp = (xp - 1)/self.d
            if (xp - 1)%self.d != 0 or not int(math.sqrt(yp))**2 == yp:
                continue
                #print 'itery',xp, yp, d
            if xp - self.d*yp == 1:
                print ','.join(map(lambda x:str(x), ['xp=', xp, 'yp=', yp,'d=', self.d]))
                result_list.append( (xp, yp, self.d) )
                c = 2
                break
         
if __name__ == '__main__':
    D = [d for d in xrange(1,1001) if d != int(math.sqrt(d))**2]
    result_list = []
    SPs = [SearchPell(d,0) for d in D]
    [searchpell.start() for searchpell in SPs] 
    [searchpell.join() for searchpell in SPs]
    print sorted(result_list, key=lambda x:x[0]*(-1))
