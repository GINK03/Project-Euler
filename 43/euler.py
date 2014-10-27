import sys, math, os, itertools

base = '1234567890'

sieve = [2, 3, 5, 7, 11, 13, 17]

trueList = [True, True, True, True, True, True, True]

res = 0
for p in itertools.permutations(base):
    eval_num = ''.join(p)
    e1, e2, e3, e4, e5, e6, e7 = map(lambda x:int(x), [eval_num[1:4],eval_num[2:5],eval_num[3:6],eval_num[4:7],eval_num[5:8],eval_num[6:9],eval_num[7:10]])
    target = [e1, e2, e3, e4, e5, e6, e7]
    if trueList == map(lambda x:x[0]%x[1] == 0, zip(target, sieve)):
        res += int(eval_num)
    if len(res) > 2:

print res
