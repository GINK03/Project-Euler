import itertools

L = [2 for x in xrange(1,1001)]
SL =  reduce(lambda x,y:x+y, map(lambda x:int(x), str(reduce(lambda x,y:x*y, L))))
print SL

      
