import os,sys,math,itertools

class SankakuNum:
    def __init__(self, index, snumwa):
        self.index = index
        self.snumwa  = snumwa

def generator():
    x = 1
    while True:
        yield SankakuNum(x, sum(range(1,x+1)) )
        x += 1

def factorNums(n):
    l = [i for i in xrange(1, round(math.sqrt(n)+1)) if not n % i]
    return (len(l) * 2, l[-1])

for i,snum in enumerate(generator()):
    count = 0
    count, last = factorNums(snum.snumwa)
    if i % 100 == 0:
        print 'iter', i, snum.index, snum.snumwa, last, count
    if count >=500:
        print 'end ', i, snum.index, snum.snumwa, last, count
        break
