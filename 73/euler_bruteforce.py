import sys, os, math, itertools, fractions

MAX = 10**6
MAX = 12000

class Obj:
    def __init__(self):
        self.head = 0.
        self.tail = 0.
        self.param = 0.
    def cal(self):
        self.param = self.head / float(self.tail)
        return self.param
        
if __name__ == '__main__':
    source_list = [x for x in xrange(1, MAX +1)]
    result_list = []
    for i, p in enumerate(itertools.combinations( source_list,2)):
        obj = Obj()
        obj.head, obj.tail = p
        if obj.head > obj.tail:
            continue
        if i%1000000 == 0:
            print 'iter', i
            pass
        if 1./3. < obj.cal() < 1./2.:
            if fractions.gcd(obj.head, obj.tail) == 1:
                result_list.append(obj)
    #print [(x.head,x.tail, x.param) for x in sorted(result_list, key=lambda x:x.param)]
    #result = itertools.takewhile(lambda x:not (x.head == 3 and x.tail == 7), sorted(result_list, key=lambda x:x.param)  ) 
    #expand = [(x.head,x.tail) for x in result]
    print len(result_list)
