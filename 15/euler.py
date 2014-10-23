import itertools

head = reduce(lambda x,y:x*y, xrange(1,41))
foot = reduce(lambda x,y:x*y, xrange(1,21))
print head/(foot*foot)
