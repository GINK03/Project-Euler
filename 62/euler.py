import sys, math, itertools

class SQ:
    def __init__(self):
        self.index = 0
        self.key   = ''

keyHash = {}
sqList = []
if __name__ == '__main__':
    for i in itertools.count(1):
        sq = SQ()
        sq.index = i
        sq.key   = ''.join(sorted(str(i**3)))
        key = ''.join(sorted(str(i**3)))
        sqList.append(sq)
        if keyHash.get(key) == None:
            keyHash[key] = 0
        keyHash[key] += 1
        if i%10000 == 0:
            for k,v in filter(lambda x:x[1] == 5, sorted( keyHash.iteritems(), key=lambda x:int(x[0])*(-1))):
                for sq in sorted(filter(lambda x:x.key == k, sqList), key=lambda x:int(x.key)*(-1)):
                    print sq.index, sq.key, sq.index**3
            sys.exit(0)

