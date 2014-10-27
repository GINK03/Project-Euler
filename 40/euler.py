import sys, itertools

#maxNum = int(raw_input().strip())
maxNum = 1000000
targetStr = '.'
for i in xrange(1, maxNum):
    targetStr += str(i)
    if len(targetStr) > maxNum:
        break
access = [1, 10, 100, 1000, 10000, 100000, 1000000]
r = 1
for acc in access:
    r *= int(targetStr[acc])

print 'result', r
