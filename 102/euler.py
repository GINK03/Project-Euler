import sys,math,os,operator

print reduce(operator.add, [x for x in xrange(1,11)])
c = 0
for line in sys.stdin:
    line = line.strip()
    ax,ay,bx,by,cx,cy = map(int, line.split(','))
    S = abs(1/2.*(ax*(by-cy)+bx*(cy-ay)+cx*(ay-by)))
    S0 = abs(1/2.*(0*(by-cy)+bx*(cy-0)+cx*(0-by)))
    S1 = abs(1/2.*(ax*(0-cy)+0*(cy-ay)+cx*(ay-0)))
    S2 = abs(1/2.*(ax*(by-0)+bx*(0-ay)+0*(ay-by)))
    if S == sum([S0,S1,S2]):
        c += 1
print 'ans,',c

