import random

c = 0
for i in xrange(100000000):
    aall = sum([ random.randint(1,4) for _ in range(1,10)])
    ball = sum([ random.randint(1,6) for _ in range(1,7)])
    if aall > ball:
        c += 1
        if i%10000 == 0 and i != 0:
            print c/float(i), c, i
