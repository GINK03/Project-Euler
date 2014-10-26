import itertools

def accume(n):
    s = 1
    for e in xrange(1, n+1):
        s *= e
    return s

def isSame(baseNum):
    b = 0
    for s in map(lambda x:int(x), str(baseNum)):
        if s <= 1:
            b += 1
            continue
        b += accume(s)
    return b


if __name__ == '__main__':
    resultL = []
    n = 3
    while True:
        if n == isSame(n):
            resultL.append(n) 
        n += 1
        if n > 2540160: #this is maximum number, 9! * 8 = 2903040 < 1000000: 8digit is max
            break

    print sum(resultL)
