import sys, math, os, itertools, fractions, decimal

MAX = 10**6
MIN = 1
c = 0 
if __name__ == '__main__':
    for i in xrange(MIN, MAX+1):
        if i%10000 == 0:
            print 'iter', i
        evals = [i]
        next_i = sum([math.factorial(x) for x in itertools.imap(int, str(i))])
        evals.append(next_i)
        while True:
            next_i = sum([math.factorial(x) for x in itertools.imap(int, str(next_i))])
            if next_i in evals:
                break
            evals.append(next_i)

        if len(evals) == 60:
            c += 1
    print 'result ', c
    
