import sys, itertools

c = 0
for i in itertools.count(1):
    t = str(i)
    mini, maxi = map(int, [''.join(sorted(t)), ''.join(sorted(t,reverse=True))])
    if mini < i < maxi:
        c += 1
    if c/float(i) > 0.990:
        print 'ans', i-1
        break
#print 'ans ', c
