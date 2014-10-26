import itertools, math


def isRound(num):
    toEval = str(num)
    is_round = True
    for i in xrange(0, len(toEval)/2 ):
        if not toEval[i] == toEval[(-1)*(i+1)]:
            is_round = False
    #print num, toEval, is_round
    return is_round

if __name__ == '__main__':
    s = 0
    for n in xrange(1, 1000000):
        bitset = format(n, 'b')
        if isRound(n) and isRound(bitset):
            print 'conved', n, bitset
            s += n
    print 'result', s
