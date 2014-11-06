import sys, math, os

class F:
    def __init__(self):
        self.tail = 0
        self.head = 0
        self.root = 0
        self.last = 0
def initial_fomula(N):
    each = int(math.sqrt(N))
    f = F()
    # first conversion
    f.tail = (-1)*each
    f.head = each
    f.root = N
    
    # second conversion
    f.tail = N - f.tail**2
    f.head = each
    f.root = N
    
    # third conversion
    # need re-check
    if len([x for x in xrange(0,100) if (x+f.head)%f.tail == 0]) > 1:
        print [x for x in xrange(0,100) if (x+f.head)%f.tail == 0]
        temp = (-1)*[x for x in xrange(0,100) if (x+f.head)%f.tail == 0][0]
        if temp != 0:
            f.head = temp
            f.last = (each+abs(temp))/f.tail
        else:
            f.last = 0
        print 'tempdata', each, f.head, f.tail, f.last, temp
    else:
        print N, [x for x in xrange(1,100) if (x+f.head)%f.tail == 0]
        sys.exit(0)
    return f
def iterative_fomula(f):
    # second conversion
    original_base = f.root - f.head**2
    f.tail = original_base/f.tail
    f.head = (-1)*f.head
    # third conversion
    oldhead = f.head
    if f.last != 0:
        buff = [x for x in xrange(0,100) if (x+f.head)%f.tail == 0 and x**2 < f.root]
        if buff != []:
            temp = [x for x in xrange(0,100) if (x+f.head)%f.tail == 0 and x**2 < f.root][-1]
        else:
            temp = [x for x in xrange(0,100) if (x+f.head)%f.tail == 0][0]
            #print [x for x in xrange(0,100) if (x+f.head)%f.tail == 0]
        #temp = [x for x in xrange(0,100) if (x+f.head)%f.tail == 0][-1]
        f.head = temp*(-1)
        f.last = (oldhead+temp)/f.tail
    else:
        temp = [x for x in xrange(0,100) if (x+f.head)%f.tail == 0 and x**2 < f.root][0]
        pass
    print 'iterable', f.root, f.tail, f.head, f.last
    return f
if __name__ == '__main__':
    for i in xrange(2,1000):#[23,26, 27]:
        if int(math.sqrt(i))**2 == i:
            continue
        f = initial_fomula(i)
        print 'iter1', f.root, f.tail, f.head, f.last
        for _ in xrange(20):
            f = iterative_fomula(f)
