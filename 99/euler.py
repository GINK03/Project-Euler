import sys, math

evalist = []
for i, line  in enumerate(sys.stdin):
    b,e = map(int, line.strip().split(','))
    evalist.append((i+1,math.log(b)*e))

print 'ans', sorted(evalist, key=lambda x:x[1]).pop()
