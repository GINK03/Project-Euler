import sys,math
c = 0
for i in xrange(1,10000000):
    if i%100000 == 0:
        print 'iter', i
    some = sum(map(lambda x:int(x)**2, str(i)))
    while True:
        some = sum(map(lambda x:int(x)**2, str(some)))
        if some == 1:
            break
        if some == 89:
            c+=1
            break

print 'ans,',c
