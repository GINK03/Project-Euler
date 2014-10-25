import math
import itertools
class Prime:
    List = [2, 3]
    @staticmethod
    def primeNum(n):
        for i in xrange(1, n+1):
            if n%i != 0 and not i in Prime.List:
                if [] == filter(lambda x:x==True, [i%l == 0 for l in Prime.List]):  
                    Prime.List.append(i)
        #print Prime. List
    @staticmethod
    def isPrime(n):
        if n != 0 and n != 1 and abs(n) in Prime.List:
            return True
        else:
            return None

for i in xrange(1, 3001):
    Prime.primeNum(i)
    pass
a, b = 0, 0
def fomula(n):
    return n * n +  a * n + b
def makeFomula(a_in,b_in):
    global a, b
    a,b = a_in, b_in
    c = 0
    while True:
        toEval = abs(fomula(c))
        if toEval > 3001:
            print 'abundant toEval,' , toEval
        if Prime.isPrime(toEval):
            c += 1
        else:
            return c

B = [a for a in xrange(-1000, 1001)]
RESULT = []
for e in itertools.combinations_with_replacement( B, 2 ):
    p_n = makeFomula(e[0], e[1])
    #p_n = makeFomula(-79, 1601)
    if p_n >= 3:
        print 'prime num,', p_n, 'a', e[0], 'b', e[1]
        RESULT.append( [p_n, e[0], e[1]] )
    #makeFomula(e[0], e[1])
ans = sorted( RESULT, key=lambda x:x[0]*(-1))[0]
print ans, ans[1]*ans[2]
