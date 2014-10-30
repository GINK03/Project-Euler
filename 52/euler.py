import sys, math, itertools

'''
# set operator test
setT = set([1,1,3])
setS = set([3,1])
if setT == setS:
    print 'some'
'''
def byWith(b, n):
    buff = b * n
    return set(str(buff))
ByNum = [2, 3, 4, 5, 6]
for i in itertools.count(1):
    to_eval = [byWith(x, i) for x in ByNum] 
    if to_eval[0] == to_eval[1] == to_eval[2] == to_eval[3] == to_eval[4]:
        print i, to_eval
        sys.exit(0)
