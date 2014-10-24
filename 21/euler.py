import math
def factors(n):
    buff = []
    for e in xrange(1,n):
        if n%e == 0:
            buff.append(e)
    return buff

def count(n):
    first = factors(n)
    if first != []:
         secondN = reduce(lambda x,y:x+y, first)
         second  = factors(secondN)
         if second == []: 
             return None
         thirdN  = reduce(lambda x,y:x+y, second)
         if n == thirdN:
             return [n, secondN, thirdN]
         return None

resL = []
for some in xrange(1,10001):
    res = count(some)
    if res:
        if res[0] != res[1]:
            print res
            resL.append(res)

print resL
print reduce(lambda x,y:x+y, map(lambda x:x[0], resL))
        
    
