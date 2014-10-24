import math

l = math.factorial(100)
l2 = map(lambda x:int(x), str(l))
print reduce(lambda x,y:x+y, l2)

