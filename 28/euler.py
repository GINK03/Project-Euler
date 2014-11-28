import sys,math,operator,itertools

result = 0
cup = 1
start = 1
for n in xrange(1,501):
    end = 0
    for c in xrange(1,5):
        cup += n*2
        end = n*2*c+start
        print n, n*2*c+start,start,end
        result += n*2*c+start
    start = end

print 'ans,',result+1
