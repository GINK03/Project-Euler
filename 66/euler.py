import math, sys, os, itertools, operator

# check out this url
# http://en.wikipedia.org/wiki/Diophantine_equation
# and, check out this url here
# http://techtipshoge.blogspot.jp/2014/10/blog-post.html
def isEqual(D, p, q):
    return p*p - D*q*q == 1

def ak_generator(D):
    p, q = 0, 1
    x = int(D**0.5)
    while True:
        a = (x + p)/q
        yield a
        p = a*q - p
        q = (D - p*p)/q
    pass

result = []
for D in xrange(3,1001):
    if int(math.sqrt(D))**2 == D:
        continue
    akgen = ak_generator(D)
    ps = [0, 1]
    qs = [1, 0]
    
    while True:
        ak = akgen.next()
        pnext = ak*ps[-1] + ps[-2]
        qnext = ak*qs[-1] + qs[-2]
        #qnext = (D - pnext ** 2)/qs[-1]
        
        if isEqual(D, pnext, qnext):
            result.append( (D, pnext, qnext) )
            break

        ps.append(pnext)
        qs.append(qnext)

print 'ans', sorted(result, key=lambda x:x[1]).pop()
