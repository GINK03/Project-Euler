import itertools

def makeBaseBitset(length):
    buff = []
    for i in xrange(1, length):
        buff.append(format(int(format(i, 'b')), '0' + str(len(format(length, 'b')))) )
    return buff

if __name__ == '__main__':
    c = 0
    s = 0
    for p1 in xrange(0,201):
        s = p1
        for p2 in xrange(0, 101):
            s += p2 * 2
            for p5 in xrange(0, 41):
                s += p5 * 5
                for p10 in xrange(0, 21):
                    s += p10 * 10
                    for p20 in xrange(0, 11):
                        s += p20 * 20
                        for p50 in range(0, 5):
                            s += p50 * 50
                            for p100 in xrange(0, 3):
                                s += p100 * 100
                                if s == 200:
                                    #print 'result', (p1, p1 *1), (p2, p2 * 2), (p5, p5*5) , (p10, p10*10), (p20, p20*20), (p50, p50*50), (p100, p100*100)
                                    c += 1
                                # reset p100
                                s = p1 + p2 * 2 + p5 * 5 + p10 * 10 + p20 * 20 + p50*50
                            # reset p50
                            s = p1 + p2 * 2 + p5 * 5 + p10 * 10 + p20 * 20
                        # reset p20
                        s = p1 + p2 * 2 + p5 * 5 + p10 * 10
                    # reset s10
                    s = p1 + p2 * 2 + p5 * 5
                # reset p5
                s = p1 + p2 * 2
            # reset p2
            s = p1
    print 'total ', c+1 
